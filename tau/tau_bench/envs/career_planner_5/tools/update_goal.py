# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class update_goal(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, goal_id: str, updates: dict) -> str:
        goals_data = data.get("goals", [])
        user_goals = next((g for g in goals_data if g.get("user_id") == user_id), None)
        if user_goals:
            goals = user_goals.get("goals", [])
            goal = next((g for g in goals if g.get("goal_id") == goal_id), None)
            if goal:
                if "notes_append" in updates:
                    goal["notes"] = (
                        goal.get("notes", "") + " " + updates.pop("notes_append")
                    )
                goal.update(updates)
                return json.dumps(
                    {"success": f"Goal {goal_id} updated for user {user_id}"}, indent=2
                )
        return json.dumps({"error": "Goal not found"}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "update_goal",
                "description": "Update goal details for a user",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "goal_id": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["user_id", "goal_id", "updates"],
                },
            },
        }
