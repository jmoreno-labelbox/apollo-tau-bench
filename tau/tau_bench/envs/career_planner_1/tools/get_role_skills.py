# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetRoleSkills(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        role = kwargs.get("role")
        catalog = data.get("role_skill_catalog", [])

        # Debug: Check if catalog is loaded
        if not catalog:
            return json.dumps({"error": "Role catalog not loaded"}, indent=2)

        # Try exact match first
        for entry in catalog:
            if entry.get("role") == role:
                skills = entry.get("required_skills", [])
                if not skills:
                    return json.dumps(
                        {"error": f"No skills found for role '{role}'"}, indent=2
                    )

                # Ensure we return a list of strings, not dictionaries
                skill_names = []
                for skill in skills:
                    if isinstance(skill, str):
                        skill_names.append(skill)
                    elif isinstance(skill, dict) and skill.get("skill"):
                        skill_names.append(skill.get("skill"))

                return json.dumps(skill_names, indent=2)

                # Try partial match for common role variations
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
                        return json.dumps(
                            {
                                "error": f"No skills found for mapped role '{mapped_role}'"
                            },
                            indent=2,
                        )

                    # Ensure we return a list of strings, not dictionaries
                    skill_names = []
                    for skill in skills:
                        if isinstance(skill, str):
                            skill_names.append(skill)
                        elif isinstance(skill, dict) and skill.get("skill"):
                            skill_names.append(skill.get("skill"))

                    return json.dumps(skill_names, indent=2)

        # List available roles for debugging
        available_roles = [entry.get("role") for entry in catalog]
        return json.dumps(
            {"error": f"Role '{role}' not found", "available_roles": available_roles},
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_role_skills",
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
