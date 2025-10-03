from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class ApprovePlayerDevGoal(Tool):
    """Authorize a goal (goal_status='Approved')."""

    @staticmethod
    def invoke(data, goal_id: str = None) -> str:
        err = _require_tables(data, ["player_dev_goals"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        if goal_id is None:
            payload = {"error": "goal_id is required."}
            out = json.dumps(payload, indent=2)
            return out
        row = next(
            (g for g in data["player_dev_goals"] if g.get("goal_id") == goal_id), None
        )
        if not row:
            payload = {"error": f"Goal '{goal_id}' not found."}
            out = json.dumps(payload, indent=2)
            return out
        row["goal_status"] = "Approved"
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ApprovePlayerDevGoal",
                "description": "Sets goal_status='Approved' for a goal.",
                "parameters": {
                    "type": "object",
                    "properties": {"goal_id": {"type": "integer"}},
                    "required": ["goal_id"],
                },
            },
        }
