from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetUserSkillGap(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, target_role: str = None) -> str:
        gaps = data.get("skill_gap_analysis", {}).values()
        result = [
            g
            for g in gaps.values() if g["user_id"] == user_id and g["target_role"] == target_role
        ]

        if not result:
            payload = {
                    "error": "No skill gap found",
                    "user_id": user_id,
                    "target_role": target_role,
                    "available_analyses": [
                        f"{g['user_id']} -> {g['target_role']}" for g in gaps
                    ],
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = result[0]
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserSkillGap",
                "description": "Gets the skill gap for a user targeting a specific role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user.",
                        },
                        "target_role": {
                            "type": "string",
                            "description": "The role the user wants to target.",
                        },
                    },
                    "required": ["user_id", "target_role"],
                },
            },
        }
