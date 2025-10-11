# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require_tables




def _require_tables(data: Dict[str, Any], required: List[str]) -> Optional[str]:
    missing = [t for t in required if t not in data or data.get(t) is None]
    if missing:
        return f"Missing required table(s): {', '.join(missing)}"
    return None

class ListGameDayEvents(Tool):
    """Lists events for a game with optional filters. Note: min_leverage is a generic ≥ filter; 'high leverage' per policy uses strict > 1.5."""
    @staticmethod
    def invoke(data, draft_status, game_pk, is_manual_alert, min_leverage)->str:
        err = _require_tables(data, ["game_day_events"])
        if err:
            return json.dumps({"error": err}, indent=2)
        if game_pk is None:
            return json.dumps({"error":"game_pk is required."}, indent=2)
        min_lev = min_leverage
        is_manual = is_manual_alert
        status = draft_status
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