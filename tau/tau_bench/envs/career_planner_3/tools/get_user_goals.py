# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserGoals(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id) -> str:
        goals = data.get("goals", [])
        result = [g for g in goals if g["user_id"] == user_id]
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_goals",
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
