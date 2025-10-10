# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateCalendarEventEntryTool(Tool):
    """Creates entry in calendar_events table."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        broker_id = kwargs.get("broker_id")
        client_id = kwargs.get("client_id")
        title = kwargs.get("title")
        start_at = ""
        end_at = ""
        location = kwargs.get("location")
        source = kwargs.get("source")

        # Enhancement: if date provided, auto-fill full-day times when start/end missing
        date = kwargs.get("date")
        if date and (not start_at or not end_at):
            date_str = str(date)
            if not start_at:
                start_at = f"{date_str}T00:00:00Z"
            if not end_at:
                end_at = f"{date_str}T23:59:59Z"

        if (
            broker_id is None
            or client_id is None
            or not title
            or not start_at
            or not end_at
            or not location
            or not source
        ):
            return _err(
                "broker_id, client_id, title, start_at, end_at, location, source are required"
            )

        rows = data.setdefault("calendar_events", [])
        event_id = _next_int_id(rows, "event_id")
        rec = {
            "event_id": event_id,
            "broker_id": int(broker_id),
            "client_id": int(client_id),
            "title": str(title),
            "start_at": str(start_at),
            "end_at": str(end_at),
            "location": str(location),
            "source": str(source),
        }
        rows.append(rec)
        return json.dumps(rec, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_calendar_event_entry",
                "description": (
                    "Creates entry in calendar_events table (supports date-only input to auto-fill full-day)."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "broker_id": {"type": "integer"},
                        "client_id": {"type": "integer"},
                        "title": {"type": "string"},
                        "date": {
                            "type": ["string", "null"],
                            "description": (
                                "YYYY-MM-DD (auto-fills 00:00:00Z-23:59:59Z if start/end omitted)"
                            ),
                        },
                        "location": {"type": "string"},
                        "source": {
                            "type": "string",
                            "enum": ["client_meeting", "viewing", "follow_up"],
                        },
                    },
                    "required": [
                        "broker_id",
                        "client_id",
                        "title",
                        "location",
                        "source",
                    ],
                },
            },
        }
