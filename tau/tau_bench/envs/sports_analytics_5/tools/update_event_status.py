# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateEventStatus(Tool):
    """Update draft_status for a game_day_event to one of: draft|published|archived, and audit the transition."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["game_day_events"])
        if err:
            return json.dumps({"error": err}, indent=2)
        event_id = kwargs.get("event_id")
        new_status = kwargs.get("draft_status")
        if event_id is None or new_status is None:
            return json.dumps({"error":"event_id and draft_status are required."}, indent=2)
        if new_status not in ("draft","published","archived"):
            return json.dumps({"error":"draft_status must be one of draft|published|archived."}, indent=2)
        row = next((e for e in data["game_day_events"] if e.get("event_id")==event_id), None)
        if not row:
            return json.dumps({"error": f"Event '{event_id}' not found."}, indent=2)
        previous = row.get("draft_status")
        row["draft_status"]=new_status
        audits = data.setdefault("event_status_audits", [])
        audits.append({
            "event_id": event_id,
            "previous_status": previous,
            "new_status": new_status,
            "changed_at_utc": _now_utc_iso()
        })
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"update_event_status","description":"Sets draft_status on a game_day_event and audits the transition.","parameters":{"type":"object","properties":{"event_id":{"type":"integer"},"draft_status":{"type":"string"}},"required":["event_id","draft_status"]}}}
