from tau_bench.envs.tool import Tool
import json
from itertools import islice
from typing import Any

class ListClientCalendarEvents(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], client_id: str = None) -> str:
        rows = [e for e in data.get("calendar_events", []) if e.get("client_id") == client_id]
        payload = {"client_id": client_id, "events": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListClientCalendarEvents",
                "description": "List calendar events for a client.",
                "parameters": {
                    "type": "object",
                    "properties": {"client_id": {"type": "integer"}},
                    "required": ["client_id"],
                },
            },
        }
