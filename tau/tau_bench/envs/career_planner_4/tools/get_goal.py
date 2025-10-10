# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_goal(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, goal_id: str) -> str:
        goals_data = data.get("goals", [])
        user_goals = next((g for g in goals_data if g.get("user_id") == user_id), {})
        goals = user_goals.get("goals", [])
        goal = next((g for g in goals if g.get("goal_id") == goal_id), None)
        return (
            json.dumps(goal, indent=2)
            if goal
            else json.dumps({"error": "Goal not found"}, indent=2)
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_goal",
                "description": "Get goal details for a user",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "goal_id": {"type": "string"},
                    },
                    "required": ["user_id", "goal_id"],
                },
            },
        }
