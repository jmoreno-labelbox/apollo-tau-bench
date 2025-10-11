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

def _now_utc_iso() -> str:
    return _today_iso() + "T00:00:00Z"

def _next_id(rows: List[Dict[str, Any]], key: str) -> int:
    max_id = 0
    for r in rows:
        try:
            max_id = max(max_id, int(r.get(key, 0)))
        except Exception:
            pass
    return max_id + 1

def _check_required(kwargs: Dict[str, Any], required: List[str]) -> Optional[str]:
    missing = [k for k in required if kwargs.get(k) is None]
    if missing:
        return f"Missing required argument(s): {', '.join(missing)}"
    return None

class CreateManualAlertEvent(Tool):
    """Create a manual in-game alert (is_manual_alert=true)."""
    @staticmethod
    def invoke(data, game_pk, pitch_id, suggestion_text, draft_status = "draft", leverage_index = 0.0)->str:
        err = _require_tables(data, ["game_day_events"])
        if err:
            return json.dumps({"error": err}, indent=2)
        need = _check_required(kwargs, ["game_pk","suggestion_text"])
        if need:
            return json.dumps({"error": need}, indent=2)
        events = list(data.get("game_day_events", {}).values())
        new_id = _next_id(events, "event_id")
        row = {
            "event_id": new_id,
            "game_pk": game_pk,
            "pitch_id": pitch_id,
            "timestamp_utc": _now_utc_iso(),
            "leverage_index": leverage_index,
            "is_manual_alert": True,
            "suggestion_text": suggestion_text,
            "draft_status": draft_status
        }
        events.append(row)
        return json.dumps({"event_id": new_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"create_manual_alert_event","description":"Creates a manual alert event with draft_status default 'draft'.","parameters":{"type":"object","properties":{"game_pk":{"type":"integer"},"pitch_id":{"type":"integer"},"leverage_index":{"type":"number"},"suggestion_text":{"type":"string"},"draft_status":{"type":"string"}},"required":["game_pk","suggestion_text"]}}}