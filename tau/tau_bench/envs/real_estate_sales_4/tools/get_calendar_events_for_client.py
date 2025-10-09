from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetCalendarEventsForClient(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], client_id: str = None) -> str:
        if not client_id:
            payload = {"error": "client_id is required"}
            out = json.dumps(payload, indent=2)
            return out

        events = data.get("calendar_events", {}).values()
        client_events = [e for e in events.values() if e.get("client_id") == client_id]
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
