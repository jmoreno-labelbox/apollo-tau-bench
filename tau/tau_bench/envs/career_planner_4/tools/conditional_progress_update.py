# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class conditional_progress_update(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        user_id: str,
        goal_id: str,
        increment: int,
        threshold: int,
        update_date: str,
    ) -> str:
        # Retrieve the progress of the current goal.
        goals_data = data.get("goals", [])
        user_goals = next((g for g in goals_data if g.get("user_id") == user_id), {})
        goals = user_goals.get("goals", [])
        goal = next((g for g in goals if g.get("goal_id") == goal_id), None)

        if goal:
            current_progress = goal.get("progress_percent", 0)
            if current_progress < threshold:
                new_progress = current_progress + increment
                goal.update(
                    {"progress_percent": new_progress, "last_updated": update_date}
                )
                return json.dumps(
                    {
                        "success": f"Goal {goal_id} progress updated from {current_progress}% to {new_progress}%"
                    },
                    indent=2,
                )
            else:
                return json.dumps(
                    {
                        "result": f"Goal {goal_id} progress ({current_progress}%) already meets threshold"
                    },
                    indent=2,
                )
        return json.dumps({"error": "Goal not found"}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "conditional_progress_update",
                "description": "Conditionally update goal progress if below threshold",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "goal_id": {"type": "string"},
                        "increment": {"type": "integer"},
                        "threshold": {"type": "integer"},
                        "update_date": {"type": "string"},
                    },
                    "required": [
                        "user_id",
                        "goal_id",
                        "increment",
                        "threshold",
                        "update_date",
                    ],
                },
            },
        }
