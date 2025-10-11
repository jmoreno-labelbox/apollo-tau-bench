# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class list_user_goals(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        goals_data = data.get("goals", [])
        user_goals = next((g for g in goals_data if g.get("user_id") == user_id), {})
        goals = user_goals.get("goals", [])
        return json.dumps({"user_id": user_id, "goals": goals}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "list_user_goals",
                "description": "List all goals for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
