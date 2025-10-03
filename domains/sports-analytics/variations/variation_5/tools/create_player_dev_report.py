from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class CreatePlayerDevReport(Tool):
    """Generate a player_dev_reports entry with a consistent s3 path if one is not given."""

    @staticmethod
    def invoke(data, player_id: str, week_of_date: str, s3_pdf_path: str = None) -> str:
        err = _require_tables(data, ["player_dev_reports"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        need = _check_required({"player_id": player_id, "week_of_date": week_of_date}, ["player_id", "week_of_date"])
        if need:
            payload = {"error": need}
            out = json.dumps(payload, indent=2)
            return out
        rows = data["player_dev_reports"]
        new_id = _next_id(rows, "dev_report_id")
        path = s3_pdf_path or f"s3://reports/player_dev/{player_id}/{week_of_date}.pdf"
        row = {
            "dev_report_id": new_id,
            "player_id": player_id,
            "week_of_date": week_of_date,
            "created_at": _now_utc_iso(),
            "s3_pdf_path": path,
        }
        rows.append(row)
        payload = {"dev_report_id": new_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreatePlayerDevReport",
                "description": "Creates a player_dev_reports row.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "player_id": {"type": "integer"},
                        "week_of_date": {"type": "string"},
                        "s3_pdf_path": {"type": "string"},
                    },
                    "required": ["player_id", "week_of_date"],
                },
            },
        }
