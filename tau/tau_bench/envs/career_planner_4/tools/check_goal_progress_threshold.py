# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class check_goal_progress_threshold(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        user_id: str,
        goal_id: str,
        threshold: int,
        comparison: str,
    ) -> str:
        goals_data = data.get("goals", [])
        user_goals = next((g for g in goals_data if g.get("user_id") == user_id), {})
        goals = user_goals.get("goals", [])
        goal = next((g for g in goals if g.get("goal_id") == goal_id), None)

        if not goal:
            return json.dumps(
                {"meets_threshold": False, "error": "Goal not found"}, indent=2
            )

        progress = goal.get("progress_percent", 0)
        meets_threshold = False

        if comparison == "below":
            meets_threshold = progress < threshold
        elif comparison == "above":
            meets_threshold = progress > threshold
        elif comparison == "equal":
            meets_threshold = progress == threshold

        return json.dumps(
            {
                "meets_threshold": meets_threshold,
                "current_progress": progress,
                "threshold": threshold,
                "comparison": comparison,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "check_goal_progress_threshold",
                "description": "Check if a goal's progress meets a threshold condition",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "goal_id": {"type": "string"},
                        "threshold": {"type": "integer"},
                        "comparison": {
                            "type": "string",
                            "enum": ["below", "above", "equal"],
                        },
                    },
                    "required": ["user_id", "goal_id", "threshold", "comparison"],
                },
            },
        }
