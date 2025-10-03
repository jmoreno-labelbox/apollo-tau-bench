from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class CreateManualAlertEvent(Tool):
    """Generate a manual in-game alert (is_manual_alert=true)."""

    @staticmethod
    def invoke(data, game_pk, suggestion_text, pitch_id=None, leverage_index=0.0, draft_status="draft", is_manual_alert: Any = None, timestamp_utc: str = None, title: str = None, message: str = None, operator_note: str = None, coach_visible: Any = None) -> str:
        pass
        err = _require_tables(data, ["game_day_events"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        need = _check_required({"game_pk": game_pk, "suggestion_text": suggestion_text}, ["game_pk", "suggestion_text"])
        if need:
            payload = {"error": need}
            out = json.dumps(payload, indent=2)
            return out
        events = data["game_day_events"]
        new_id = _next_id(events, "event_id")
        row = {
            "event_id": new_id,
            "game_pk": game_pk,
            "pitch_id": pitch_id,
            "timestamp_utc": _now_utc_iso(),
            "leverage_index": leverage_index,
            "is_manual_alert": True,
            "suggestion_text": suggestion_text,
            "draft_status": draft_status,
        }
        events.append(row)
        payload = {"event_id": new_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateManualAlertEvent",
                "description": "Creates a manual alert event with draft_status default 'draft'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {"type": "integer"},
                        "pitch_id": {"type": "integer"},
                        "leverage_index": {"type": "number"},
                        "suggestion_text": {"type": "string"},
                        "draft_status": {"type": "string"},
                    },
                    "required": ["game_pk", "suggestion_text"],
                },
            },
        }
