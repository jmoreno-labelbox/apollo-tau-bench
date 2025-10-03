from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class UpdateEventStatus(Tool):
    """Modify draft_status for a game_day_event to either: draft|published|archived, and log the transition."""

    @staticmethod
    def invoke(data, event_id: str = None, draft_status: str = None, changed_at_utc: str = None) -> str:
        err = _require_tables(data, ["game_day_events"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        if event_id is None or draft_status is None:
            payload = {"error": "event_id and draft_status are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        if draft_status not in ("draft", "published", "archived"):
            payload = {"error": "draft_status must be one of draft|published|archived."}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        row = next(
            (e for e in data["game_day_events"] if e.get("event_id") == event_id), None
        )
        if not row:
            payload = {"error": f"Event '{event_id}' not found."}
            out = json.dumps(payload, indent=2)
            return out
        previous = row.get("draft_status")
        row["draft_status"] = draft_status
        audits = data.setdefault("event_status_audits", [])
        audits.append(
            {
                "event_id": event_id,
                "previous_status": previous,
                "new_status": draft_status,
                "changed_at_utc": changed_at_utc if changed_at_utc is not None else _now_utc_iso(),
            }
        )
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "UpdateEventStatus",
                "description": "Sets draft_status on a game_day_event and audits the transition.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "event_id": {"type": "integer"},
                        "draft_status": {"type": "string"},
                    },
                    "required": ["event_id", "draft_status"],
                },
            },
        }
