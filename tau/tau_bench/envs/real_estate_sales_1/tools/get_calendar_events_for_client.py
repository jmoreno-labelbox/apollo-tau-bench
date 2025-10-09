from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetCalendarEventsForClient(Tool):
    """Fetch calendar events associated with a specific client."""

    @staticmethod
    def invoke(data: dict[str, Any], client_id: str = None) -> str:
        if not client_id:
            payload = {"error": "client_id is required"}
            out = json.dumps(payload, indent=2)
            return out

        # Fetch calendar events for the client
        events = data.get("calendar_events", [])
        client_events = [e for e in events if e.get("client_id") == client_id]
        payload = {
            "client_id": client_id,
            "event_count": len(client_events),
            "events": client_events,
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
                "name": "getCalendarEventsForClient",
                "description": "Retrieve calendar events for a specific client",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {
                            "type": "integer",
                            "description": "Client ID to get events for",
                        }
                    },
                    "required": ["client_id"],
                },
            },
        }
