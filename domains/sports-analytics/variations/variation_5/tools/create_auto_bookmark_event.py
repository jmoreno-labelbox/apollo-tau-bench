from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class CreateAutoBookmarkEvent(Tool):
    """Establish an automatic high-leverage bookmark (is_manual_alert=false). Requires leverage_index > 1.5."""

    @staticmethod
    def invoke(data, game_pk, pitch_id, leverage_index, narration, timestamp_utc: Any = None, is_manual_alert: Any = None, coach_visible: Any = None, draft_status: str = None) -> str:
        err = _require_tables(data, ["game_day_events"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        need = _check_required(
            {"game_pk": game_pk, "pitch_id": pitch_id, "leverage_index": leverage_index, "narration": narration},
            ["game_pk", "pitch_id", "leverage_index", "narration"]
        )
        if need:
            payload = {"error": need}
            out = json.dumps(payload, indent=2)
            return out
        if float(leverage_index) <= 1.5:
            payload = {"error": "auto-bookmarks require leverage_index > 1.5"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        events = data["game_day_events"]
        new_id = _next_id(events, "event_id")
        row = {
            "event_id": new_id,
            "game_pk": game_pk,
            "pitch_id": pitch_id,
            "timestamp_utc": _now_utc_iso(),
            "leverage_index": leverage_index,
            "is_manual_alert": False,
            "suggestion_text": narration,
            "draft_status": "draft",
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
                "name": "CreateAutoBookmarkEvent",
                "description": "Creates an automatic high-leverage bookmark (is_manual_alert=false).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {"type": "integer"},
                        "pitch_id": {"type": "integer"},
                        "leverage_index": {"type": "number"},
                        "narration": {"type": "string"},
                    },
                    "required": ["game_pk", "pitch_id", "leverage_index", "narration"],
                },
            },
        }
