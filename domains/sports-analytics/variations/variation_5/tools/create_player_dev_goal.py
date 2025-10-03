from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class CreatePlayerDevGoal(Tool):
    """Add a player_dev_goals entry (status defaults to 'Proposed')."""

    @staticmethod
    def invoke(
        data, 
        dev_report_id: int, 
        player_id: int, 
        goal_text: str, 
        coach_id: int, 
        target_review_date: str,
        goal_status: str = None
    ) -> str:
        err = _require_tables(data, ["player_dev_goals"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        need = _check_required(
            {
                "dev_report_id": dev_report_id,
                "player_id": player_id,
                "goal_text": goal_text,
                "coach_id": coach_id,
                "target_review_date": target_review_date,
            },
            [
                "dev_report_id",
                "player_id",
                "goal_text",
                "coach_id",
                "target_review_date",
            ],
        )
        if need:
            payload = {"error": need}
            out = json.dumps(payload, indent=2)
            return out
        rows = data["player_dev_goals"]
        new_id = _next_id(rows, "goal_id")
        row = {
            "goal_id": new_id,
            "dev_report_id": dev_report_id,
            "player_id": player_id,
            "goal_text": goal_text,
            "goal_status": goal_status if goal_status is not None else "Proposed",
            "coach_id": coach_id,
            "target_review_date": target_review_date,
        }
        rows.append(row)
        payload = {"goal_id": new_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreatePlayerDevGoal",
                "description": "Creates a 'Proposed' goal linked to a dev report.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "dev_report_id": {"type": "integer"},
                        "player_id": {"type": "integer"},
                        "goal_text": {"type": "string"},
                        "coach_id": {"type": "integer"},
                        "target_review_date": {"type": "string"},
                    },
                    "required": [
                        "dev_report_id",
                        "player_id",
                        "goal_text",
                        "coach_id",
                        "target_review_date",
                    ],
                },
            },
        }
