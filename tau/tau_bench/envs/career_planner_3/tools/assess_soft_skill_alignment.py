# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AssessSoftSkillAlignment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        target_role = kwargs.get("target_role")
        soft_skills = data.get("soft_skills", [])

        # Find soft skills that are applicable to the target role
        applicable_skills = []
        for s in soft_skills:
            if target_role in s.get("applicable_roles", []):
                applicable_skills.append(s["skill"])

        if applicable_skills:
            aligned = {
                "user_id": user_id,
                "role": target_role,
                "required_soft_skills": applicable_skills,
            }
            return json.dumps(aligned, indent=2)

        return json.dumps({"error": "No soft skills found for role."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assess_soft_skill_alignment",
                "description": "Gets soft skill expectations for a role and compares them to user development plans.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user being evaluated.",
                        },
                        "target_role": {
                            "type": "string",
                            "description": "The target role for soft skill comparison.",
                        },
                    },
                    "required": ["user_id", "target_role"],
                },
            },
        }
