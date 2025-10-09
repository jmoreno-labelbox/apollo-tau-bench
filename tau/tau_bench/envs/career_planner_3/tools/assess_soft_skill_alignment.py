from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class AssessSoftSkillAlignment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, target_role: str = None) -> str:
        soft_skills = data.get("soft_skills", [])

        # Identify relevant soft skills for the desired position
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
            payload = aligned
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": "No soft skills found for role."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssessSoftSkillAlignment",
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
