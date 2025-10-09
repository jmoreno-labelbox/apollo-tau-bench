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
        rows = [e for e in data.get("calendar_events", {}).values() if e.get("client_id") == client_id]
        payload = {"client_id": client_id, "events": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCalendarEventsForClient",
                "description": "List calendar events for a client.",
                "parameters": {
                    "type": "object",
                    "properties": {"client_id": {"type": "integer"}},
                    "required": ["client_id"],
                },
            },
        }
