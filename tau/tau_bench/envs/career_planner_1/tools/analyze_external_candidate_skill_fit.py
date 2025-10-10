# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AnalyzeExternalCandidateSkillFit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        role = kwargs.get("role")

        # gather candidate skills - handle both formats
        cand = next(
            (
                c
                for c in data.get("talent_network", [])
                if c.get("candidate_id") == candidate_id
            ),
            {},
        )
        cand_skill_names = set()

        if cand:
            cand_skills = cand.get("skills", [])
            if isinstance(cand_skills, list):
                for skill in cand_skills:
                    if isinstance(skill, str):
                        cand_skill_names.add(skill)
                    elif isinstance(skill, dict) and skill.get("skill"):
                        cand_skill_names.add(skill.get("skill"))

        # Debug: Check if candidate was found
        if not cand_skill_names:
            return f"Error: No skills found for candidate {candidate_id}"

        # gather role skills with mapping support
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

        # Safely extract skill names from potentially mixed data
        role_skill_names = set()
        for skill_item in role_skills_raw:
            if isinstance(skill_item, str):
                role_skill_names.add(skill_item)
            elif isinstance(skill_item, dict) and skill_item.get("skill"):
                role_skill_names.add(skill_item.get("skill"))

        # compute matches - handle both direct matches and hierarchical skills
        matched = []
        missing = []

        # Check each role skill requirement
        for role_skill in role_skill_names:
            # Check for direct match first
            if role_skill in cand_skill_names:
                matched.append(role_skill)
            else:
                # Check if any candidate skill matches this role requirement
                skill_matched = False

                # Get the specific skills for this role requirement from catalog
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
                        # Check if candidate has any of the specific skills in this category
                        for cand_skill in cand_skill_names:
                            if cand_skill in specific_skills:
                                matched.append(role_skill)
                                skill_matched = True
                                break
                        if skill_matched:
                            break

                if not skill_matched:
                    missing.append(role_skill)

        # format response
        match_count = len(matched)
        skill_percentage = (
            round((match_count / len(role_skill_names)) * 100)
            if role_skill_names
            else 0
        )

        return f"Skills match: {match_count}/{len(role_skill_names)} ({skill_percentage}%)\nMatched: {matched}\nMissing: {missing}"

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "analyze_external_candidate_skill_fit",
                "description": "Compare external candidate skills to target role requirements.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {
                            "type": "string",
                            "description": "ID of candidate in talent_network.json",
                        },
                        "role": {
                            "type": "string",
                            "description": "Target role title (must exist in role_skill_catalog.json)",
                        },
                    },
                    "required": ["candidate_id", "role"],
                },
            },
        }
