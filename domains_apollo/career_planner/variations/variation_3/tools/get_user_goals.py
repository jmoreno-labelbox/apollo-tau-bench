from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetUserGoals(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        goals = data.get("goals", [])
        result = [g for g in goals if g["user_id"] == user_id]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserGoals",
                "description": "Retrieves the active career goals for a given user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user.",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }
