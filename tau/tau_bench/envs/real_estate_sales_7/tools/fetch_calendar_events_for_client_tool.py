# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FetchCalendarEventsForClientTool(Tool):
    """Returns calendar events for a client, optionally within a date range."""

    @staticmethod
    def invoke(data: Dict[str, Any], client_id, end_at, start_at) -> str:
        client_id = _as_int(client_id)
        if client_id is None:
            return _err("client_id is required")

        events = [
            e
            for e in data.get("calendar_events", [])
            if _as_int(e.get("client_id")) == client_id
        ]
        if start_at:
            events = [
                e
                for e in events
                if (e.get("end_at") or e.get("start_at") or "") >= start_at
            ]
        if end_at:
            events = [
                e
                for e in events
                if (e.get("start_at") or e.get("end_at") or "") <= end_at
            ]

        events_sorted = sorted(
            events,
            key=lambda e: (e.get("start_at") or "", e.get("end_at") or ""),
            reverse=False,
        )
        out = {
            "client_id": client_id,
            "total": len(events_sorted),
            "events": events_sorted[:100],
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_calendar_events_for_client",
                "description": (
                    "Fetch calendar events for a client with optional date range."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "start_at": {"type": ["string", "null"]},
                        "end_at": {"type": ["string", "null"]},
                    },
                    "required": ["client_id"],
                },
            },
        }
