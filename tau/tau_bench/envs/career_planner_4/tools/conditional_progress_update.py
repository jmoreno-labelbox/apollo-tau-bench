from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class ConditionalProgressUpdate(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str,
        goal_id: str,
        increment: int,
        threshold: int,
        update_date: str,
    ) -> str:
        # Retrieve the current progress of the goal
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
                payload = {
                    "success": f"Goal {goal_id} progress updated from {current_progress}% to {new_progress}%"
                }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            else:
                payload = {
                    "result": f"Goal {goal_id} progress ({current_progress}%) already meets threshold"
                }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        payload = {"error": "Goal not found"}
        out = json.dumps(payload, indent=2)
        return out
            

    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "conditionalProgressUpdate",
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
