from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class AnalyzeApplicantSkillFit(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], applicant_id: str = None, role: str = None) -> str:
        # Retrieve user skills - manage the actual data structure
        user_skill_names = set()

        # Locate the user within the users data
        user = next((u for u in data.get("users", []) if u.get("user_id") == applicant_id), {})
        if user:
            # Examine the skills_current field (actual data structure)
            user_skills = user.get("skills_current", [])
            if isinstance(user_skills, list):
                for skill_obj in user_skills:
                    if isinstance(skill_obj, dict) and skill_obj.get("skill"):
                        user_skill_names.add(skill_obj.get("skill"))

            # Additionally verify if a legacy "skills" field exists
            if not user_skill_names:
                user_skills = user.get("skills", [])
                if isinstance(user_skills, list):
                    for skill in user_skills:
                        if isinstance(skill, str):
                            user_skill_names.add(skill)
                        elif isinstance(skill, dict) and skill.get("skill"):
                            user_skill_names.add(skill.get("skill"))

        # Attempt to use the user_skills table as a backup
        if not user_skill_names:
            user_skills_entry = next(
                (u for u in data.get("user_skills", []) if u.get("user_id") == applicant_id), {}
            )
            if user_skills_entry:
                skills = user_skills_entry.get("skills", [])
                if isinstance(skills, list):
                    for skill in skills:
                        if isinstance(skill, str):
                            user_skill_names.add(skill)
                        elif isinstance(skill, dict) and skill.get("skill"):
                            user_skill_names.add(skill.get("skill"))

        # Debug: Verify if the user was located
        if not user_skill_names:
            return f"Error: No skills found for user {applicant_id}"

        # Retrieve role skills with mapping assistance
        role_mapping = {
            "AI Researcher": "Senior Data Scientist",
            "Security Analyst": "Cloud Security Specialist",
            "Marketing Specialist": "Product Marketing Specialist",
            "Senior Data Scientist": "Senior Data Scientist",
            "UX Design Lead": "UX Designer",
            "Cloud Security Compliance Specialist": "Cloud Security Specialist",
            "Product Marketing Specialist": "Product Marketing Specialist",
            "DevOps Engineer": "DevOps Engineer",
            "Data Scientist": "Data Scientist",
            "Data Analyst": "Senior Data Scientist",
        }

        target_role = role_mapping.get(role, role)
        role_rec = next(
            (
                r
                for r in data.get("role_skill_catalog", [])
                if r.get("role") == target_role
            ),
            {},
        )
        role_skills_raw = role_rec.get("required_skills", [])

        # Carefully extract skill names from possibly mixed data
        role_skill_names = set()
        for skill_item in role_skills_raw:
            if isinstance(skill_item, str):
                role_skill_names.add(skill_item)
            elif isinstance(skill_item, dict) and skill_item.get("skill"):
                role_skill_names.add(skill_item.get("skill"))

        # Identify matches - manage both direct matches and hierarchical skills
        matched = []
        missing = []

        # Examine each skill requirement for the role
        for role_skill in role_skill_names:
            # Verify for a direct match initially
            if role_skill in user_skill_names:
                matched.append(role_skill)
            else:
                # Determine if any user skill aligns with this role requirement
                skill_matched = False

                # Retrieve the specific skills for this role requirement from the catalog
                role_rec = next(
                    (
                        r
                        for r in data.get("role_skill_catalog", [])
                        if r.get("role") == target_role
                    ),
                    {},
                )
                for skill_category in role_rec.get("required_skills", []):
                    if (
                        isinstance(skill_category, dict)
                        and skill_category.get("skill") == role_skill
                    ):
                        specific_skills = skill_category.get("specific_skills", [])
                        # Verify if the user possesses any of the specific skills in this category
                        for user_skill in user_skill_names:
                            if user_skill in specific_skills:
                                matched.append(role_skill)
                                skill_matched = True
                                break
                        if skill_matched:
                            break

                if not skill_matched:
                    missing.append(role_skill)

        # Structure the response
        match_count = len(matched)
        skill_percentage = (
            round((match_count / len(role_skill_names)) * 100)
            if role_skill_names
            else 0
        )

        return f"Skills match: {match_count}/{len(role_skill_names)} ({skill_percentage}%)\nMatched: {matched}\nMissing: {missing}"
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AnalyzeApplicantSkillFit",
                "description": "Analyze how well an internal applicant's skills match a target role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "applicant_id": {
                            "type": "string",
                            "description": "User ID of applicant",
                        },
                        "role": {"type": "string", "description": "Target role title"},
                    },
                    "required": ["applicant_id", "role"],
                },
            },
        }
