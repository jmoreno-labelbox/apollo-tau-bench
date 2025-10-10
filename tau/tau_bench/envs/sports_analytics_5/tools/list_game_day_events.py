# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListGameDayEvents(Tool):
    """Lists events for a game with optional filters. Note: min_leverage is a generic ≥ filter; 'high leverage' per policy uses strict > 1.5."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["game_day_events"])
        if err:
            return json.dumps({"error": err}, indent=2)
        game_pk = kwargs.get("game_pk")
        if game_pk is None:
            return json.dumps({"error":"game_pk is required."}, indent=2)
        min_lev = kwargs.get("min_leverage")
        is_manual = kwargs.get("is_manual_alert")
        status = kwargs.get("draft_status")
        rows = [e for e in data["game_day_events"] if e.get("game_pk")==game_pk]
        if min_lev is not None:
            rows = [e for e in rows if (e.get("leverage_index") or 0) >= float(min_lev)]
        if is_manual is not None:
            rows = [e for e in rows if bool(e.get("is_manual_alert")) == bool(is_manual)]
        if status:
            rows = [e for e in rows if e.get("draft_status")==status]
        return json.dumps(rows, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"list_game_day_events","description":"Lists game_day_events for a game with optional filters.","parameters":{"type":"object","properties":{"game_pk":{"type":"integer"},"min_leverage":{"type":"number"},"is_manual_alert":{"type":"boolean"},"draft_status":{"type":"string"}},"required":["game_pk"]}}}
