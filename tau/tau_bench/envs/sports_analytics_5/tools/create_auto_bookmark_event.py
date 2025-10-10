# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require_tables


class CreateAutoBookmarkEvent(Tool):
    """Create an automatic high-leverage bookmark (is_manual_alert=false). Enforces leverage_index > 1.5."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["game_day_events"])
        if err:
            return json.dumps({"error": err}, indent=2)
        need = _check_required(kwargs, ["game_pk","pitch_id","leverage_index","narration"])
        if need:
            return json.dumps({"error": need}, indent=2)
        if float(kwargs["leverage_index"]) <= 1.5:
            return json.dumps({"error":"auto-bookmarks require leverage_index > 1.5"}, indent=2)
        events = list(data.get("game_day_events", {}).values())
        new_id = _next_id(events, "event_id")
        row = {
            "event_id": new_id,
            "game_pk": kwargs["game_pk"],
            "pitch_id": kwargs["pitch_id"],
            "timestamp_utc": _now_utc_iso(),
            "leverage_index": kwargs["leverage_index"],
            "is_manual_alert": False,
            "suggestion_text": kwargs["narration"],
            "draft_status": "draft"
        }
        events.append(row)
        return json.dumps({"event_id": new_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{
            "name":"create_auto_bookmark_event",
            "description":"Creates an automatic high-leverage bookmark (is_manual_alert=false).",
            "parameters":{"type":"object","properties":{
                "game_pk":{"type":"integer"},
                "pitch_id":{"type":"integer"},
                "leverage_index":{"type":"number"},
                "narration":{"type":"string"}}, "required":["game_pk","pitch_id","leverage_index","narration"]}
        }}
