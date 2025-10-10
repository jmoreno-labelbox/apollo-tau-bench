# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_goal_id_by_description(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, keyword: str) -> str:
        goals_data = data.get("goals", [])
        user_goals_obj = next(
            (g for g in goals_data if g.get("user_id") == user_id), None
        )
        if user_goals_obj:
            # Locate a goal whose description includes the specified keyword, regardless of case.
            goal = next(
                (
                    g
                    for g in user_goals_obj.get("goals", [])
                    if keyword.lower() in g.get("goal_description", "").lower()
                ),
                None,
            )
            if goal:
                return json.dumps({"goal_id": goal["goal_id"]}, indent=2)
        return json.dumps(
            {
                "error": f"Goal for user {user_id} containing keyword '{keyword}' not found"
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_goal_id_by_description",
                "description": "Find a user's goal ID by searching for a keyword in the goal's description.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "keyword": {
                            "type": "string",
                            "description": "A keyword to search for in the goal descriptions.",
                        },
                    },
                    "required": ["user_id", "keyword"],
                },
            },
        }
