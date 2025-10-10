# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class InsertCalendarEvent(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        events = data.get("calendar_events", [])
        new_id = _next_auto_id(events, "event_id")
        row = {
            "event_id": new_id,
            "broker_id": kwargs.get("broker_id"),
            "client_id": kwargs.get("client_id"),
            "title": kwargs.get("title"),
            "start_at": kwargs.get("start_at"),
            "end_at": kwargs.get("end_at"),
            "location": kwargs.get("location"),
            "notes": kwargs.get("notes"),
            "source": kwargs.get("source"),
        }
        events.append(row)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "insert_calendar_event",
                "description": "Create a calendar event.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "broker_id": {"type": "integer"},
                        "client_id": {"type": "integer"},
                        "title": {"type": "string"},
                        "start_at": {"type": "string"},
                        "end_at": {"type": "string"},
                        "location": {"type": "string"},
                        "notes": {"type": "string"},
                        "source": {"type": "string"},
                    },
                    "required": ["broker_id", "client_id", "title", "start_at", "end_at", "location", "source"],
                },
            },
        }
