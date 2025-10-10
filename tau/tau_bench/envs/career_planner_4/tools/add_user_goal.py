# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class add_user_goal(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, goal: dict) -> str:
        goals_data = data.get("goals", [])
        user_goals = next((g for g in goals_data if g.get("user_id") == user_id), None)

        if user_goals:
            user_goals["goals"].append(goal)
        else:
            goals_data.append({"user_id": user_id, "goals": [goal]})

        return json.dumps(
            {"success": f"Goal {goal.get('goal_type')} added for user {user_id}"},
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "add_user_goal",
                "description": "Add a new goal for a user",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "goal": {"type": "object"},
                    },
                    "required": ["user_id", "goal"],
                },
            },
        }
