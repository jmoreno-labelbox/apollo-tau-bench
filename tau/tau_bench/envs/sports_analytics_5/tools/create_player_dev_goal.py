# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreatePlayerDevGoal(Tool):
    """Insert player_dev_goals row (status defaults to 'Proposed')."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["player_dev_goals"])
        if err:
            return json.dumps({"error": err}, indent=2)
        need = _check_required(kwargs, ["dev_report_id","player_id","goal_text","coach_id","target_review_date"])
        if need:
            return json.dumps({"error": need}, indent=2)
        rows = data["player_dev_goals"]
        new_id = _next_id(rows, "goal_id")
        row = {
            "goal_id": new_id,
            "dev_report_id": kwargs.get("dev_report_id"),
            "player_id": kwargs.get("player_id"),
            "goal_text": kwargs.get("goal_text"),
            "goal_status": "Proposed",
            "coach_id": kwargs.get("coach_id"),
            "target_review_date": kwargs.get("target_review_date")
        }
        rows.append(row)
        return json.dumps({"goal_id": new_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"create_player_dev_goal","description":"Creates a 'Proposed' goal linked to a dev report.","parameters":{"type":"object","properties":{"dev_report_id":{"type":"integer"},"player_id":{"type":"integer"},"goal_text":{"type":"string"},"coach_id":{"type":"integer"},"target_review_date":{"type":"string"}},"required":["dev_report_id","player_id","goal_text","coach_id","target_review_date"]}}}
