from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateCalendarEvent(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], broker_id: str = None, client_id: str = None, title: str = None, start_at: str = None, end_at: str = None, location: str = None, notes: str = None, source: str = None) -> str:
        events = data.get("calendar_events", {}).values()
        new_id = _next_int_id(events, "event_id")
        row = {
            "event_id": new_id,
            "broker_id": broker_id,
            "client_id": client_id,
            "title": title,
            "start_at": start_at,
            "end_at": end_at,
            "location": location,
            "notes": notes,
            "source": source,
        }
        data["calendar_events"][row["calendar_event_id"]] = row
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateCalendarEvent",
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
                    "required": [
                        "broker_id",
                        "client_id",
                        "title",
                        "start_at",
                        "end_at",
                        "location",
                        "source",
                    ],
                },
            },
        }
