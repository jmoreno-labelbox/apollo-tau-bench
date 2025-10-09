from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateCalendarEvent(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        broker_id: str = None,
        client_id: str = None,
        title: str = None,
        start_at: str = None,
        end_at: str = None,
        location: str = None,
        notes: str = None,
        source: str = None
    ) -> str:
        if not all([broker_id, client_id, title, start_at, end_at]):
            payload = {
                "error": "broker_id, client_id, title, start_at, and end_at are required"
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        import time

        timestamp = str(int(time.time() * 1000))
        event_id = f"EVENT-{client_id}-{timestamp}"
        event = {
            "event_id": event_id,
            "broker_id": broker_id,
            "client_id": client_id,
            "title": title,
            "start_at": start_at,
            "end_at": end_at,
            "location": location,
            "notes": notes,
            "source": source,
            "status": "scheduled",
            "created_at": "2024-08-21T00:00:00Z",
        }
        payload = {
            "success": True,
            "event_id": event_id,
            "message": f"Calendar event created for client {client_id}",
            "event": event,
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateCalendarEvent",
                "description": "Create a calendar event for client meetings WA appointments",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "broker_id": {
                            "type": "integer",
                            "description": "Broker ID creating the event",
                        },
                        "client_id": {
                            "type": "integer",
                            "description": "Client ID for the event",
                        },
                        "title": {"type": "string", "description": "Event title"},
                        "start_at": {
                            "type": "string",
                            "description": "Start time in ISO format",
                        },
                        "end_at": {
                            "type": "string",
                            "description": "End time in ISO format",
                        },
                        "location": {"type": "string", "description": "Event location"},
                        "notes": {"type": "string", "description": "Event notes"},
                        "source": {
                            "type": "string",
                            "description": "Event source (client_meeting, follow_up, viewing, etc.)",
                        },
                    },
                    "required": [
                        "broker_id",
                        "client_id",
                        "title",
                        "start_at",
                        "end_at",
                    ],
                },
            },
        }
