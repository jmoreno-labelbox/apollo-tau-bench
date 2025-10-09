from tau_bench.envs.tool import Tool
import json
import math
import re
from typing import Any

class CreateCalendarEventEntryTool(Tool):
    """Inserts a record into the calendar_events table."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        broker_id: int = None,
        client_id: int = None,
        title: str = None,
        location: str = None,
        source: str = None,
        date: str = None
    ) -> str:
        start_at = ""
        end_at = ""

        # Improvement: if a date is given, automatically fill full-day times when start/end are absent
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
        payload = rec
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateCalendarEventEntry",
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
