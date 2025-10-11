# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require_tables


class CreatePlayerDevReport(Tool):
    """Create a player_dev_reports row with deterministic s3 path if not provided."""
    @staticmethod
    def invoke(data, player_id, week_of_date, s3_pdf_path = f"s3://reports/player_dev/{kwargs.get('player_id')}/{kwargs.get('week_of_date')}.pdf")->str:
        err = _require_tables(data, ["player_dev_reports"])
        if err:
            return json.dumps({"error": err}, indent=2)
        need = _check_required(kwargs, ["player_id","week_of_date"])
        if need:
            return json.dumps({"error": need}, indent=2)
        rows = data["player_dev_reports"]
        new_id = _next_id(rows, "dev_report_id")
        path = s3_pdf_path
        row = {
            "dev_report_id": new_id,
            "player_id": player_id,
            "week_of_date": week_of_date,
            "created_at": _now_utc_iso(),
            "s3_pdf_path": path
        }
        rows.append(row)
        return json.dumps({"dev_report_id": new_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"create_player_dev_report","description":"Creates a player_dev_reports row.","parameters":{"type":"object","properties":{"player_id":{"type":"integer"},"week_of_date":{"type":"string"},"s3_pdf_path":{"type":"string"}},"required":["player_id","week_of_date"]}}}
