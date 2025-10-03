from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class AddUserGoal(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, goal: dict) -> str:
        goals_data = data.get("goals", [])
        user_goals = next((g for g in goals_data if g.get("user_id") == user_id), None)

        if user_goals:
            user_goals["goals"].append(goal)
        else:
            goals_data.append({"user_id": user_id, "goals": [goal]})
        payload = {"success": f"Goal {goal.get('goal_type')} added for user {user_id}"}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "addUserGoal",
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
