# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require_tables


class FindNextScheduledGame(Tool):
    """Find the next scheduled game on/after current_date; tie-break on smallest game_pk."""
    @staticmethod
    def invoke(data, current_date)->str:
        err = _require_tables(data, ["games"])
        if err:
            return json.dumps({"error": err}, indent=2)
        if "current_date" not in kwargs or not current_date:
            return json.dumps({"error":"current_date is required (YYYY-MM-DD)."}, indent=2)
        candidates = [g for g in data["games"] if g.get("game_status")=="Scheduled" and str(g.get("game_date")) >= str(current_date)]
        if not candidates:
            return json.dumps({"error":"No scheduled games on or after current_date."}, indent=2)
        earliest = min(candidates, key=lambda g: (str(g.get("game_date")), int(g.get("game_pk") or 0)))
        return json.dumps({"next_game_pk":earliest.get("game_pk"),"home_team_id":earliest.get("home_team_id"),"away_team_id":earliest.get("away_team_id"),"game_date":earliest.get("game_date")}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"find_next_scheduled_game","description":"Returns earliest Scheduled game on/after a date.","parameters":{"type":"object","properties":{"current_date":{"type":"string"}},"required":["current_date"]}}}
