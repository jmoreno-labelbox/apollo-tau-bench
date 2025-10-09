from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetRoleSkills(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], role: str = None) -> str:
        catalog = data.get("role_skill_catalog", {}).values()

        # Debug: Verify if the catalog is loaded
        if not catalog:
            payload = {"error": "Role catalog not loaded"}
            out = json.dumps(payload, indent=2)
            return out

        # Attempt an exact match initially
        for entry in catalog:
            if entry.get("role") == role:
                skills = entry.get("required_skills", [])
                if not skills:
                    payload = {"error": f"No skills found for role '{role}'"}
                    out = json.dumps(payload, indent=2)
                    return out

                # Make sure to return a list of strings instead of dictionaries
                skill_names = []
                for skill in skills:
                    if isinstance(skill, str):
                        skill_names.append(skill)
                    elif isinstance(skill, dict) and skill.get("skill"):
                        skill_names.append(skill.get("skill"))
                payload = skill_names
                out = json.dumps(payload, indent=2)
                return out

        # Attempt a partial match for typical role variations
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

        mapped_role = role_mapping.get(role)
        if mapped_role:
            for entry in catalog:
                if entry.get("role") == mapped_role:
                    skills = entry.get("required_skills", [])
                    if not skills:
                        payload = {
                            "error": f"No skills found for mapped role '{mapped_role}'"
                        }
                        out = json.dumps(payload, indent=2)
                        return out

                    # Confirm that we return a list of strings rather than dictionaries
                    skill_names = []
                    for skill in skills:
                        if isinstance(skill, str):
                            skill_names.append(skill)
                        elif isinstance(skill, dict) and skill.get("skill"):
                            skill_names.append(skill.get("skill"))
                    payload = skill_names
                    out = json.dumps(payload, indent=2)
                    return out

        # Display available roles for debugging purposes
        available_roles = [entry.get("role") for entry in catalog.values()]
        payload = {"error": f"Role '{role}' not found", "available_roles": available_roles}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRoleSkills",
                "description": "Get required skills for a specific role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role": {
                            "type": "string",
                            "description": "Role title to lookup skills for.",
                        }
                    },
                    "required": ["role"],
                },
            },
        }
