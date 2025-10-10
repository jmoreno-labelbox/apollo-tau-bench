# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require_tables


class ApprovePlayerDevGoal(Tool):
    """Approve a goal (goal_status='Approved')."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["player_dev_goals"])
        if err:
            return json.dumps({"error": err}, indent=2)
        goal_id = kwargs.get("goal_id")
        if goal_id is None:
            return json.dumps({"error":"goal_id is required."}, indent=2)
        row = next((g for g in data["player_dev_goals"] if g.get("goal_id")==goal_id), None)
        if not row:
            return json.dumps({"error": f"Goal '{goal_id}' not found."}, indent=2)
        row["goal_status"] = "Approved"
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"approve_player_dev_goal","description":"Sets goal_status='Approved' for a goal.","parameters":{"type":"object","properties":{"goal_id":{"type":"integer"}},"required":["goal_id"]}}}
