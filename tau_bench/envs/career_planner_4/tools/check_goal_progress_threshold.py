from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class CheckGoalProgressThreshold(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
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
            payload = {"meets_threshold": False, "error": "Goal not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        progress = goal.get("progress_percent", 0)
        meets_threshold = False

        if comparison == "below":
            meets_threshold = progress < threshold
        elif comparison == "above":
            meets_threshold = progress > threshold
        elif comparison == "equal":
            meets_threshold = progress == threshold
        payload = {
                "meets_threshold": meets_threshold,
                "current_progress": progress,
                "threshold": threshold,
                "comparison": comparison,
            }
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
                "name": "checkGoalProgressThreshold",
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
