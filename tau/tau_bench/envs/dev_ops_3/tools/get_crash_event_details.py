from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class get_crash_event_details(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], crash_id: str) -> str:
        pass
        crash_events = data.get("crash_events", [])
        for event in crash_events:
            if event.get("id") == crash_id:
                payload = event
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Crash event with id '{crash_id}' not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCrashEventDetails",
                "description": "Retrieves the full details for a given crash event.",
                "parameters": {
                    "type": "object",
                    "properties": {"crash_id": {"type": "string"}},
                    "required": ["crash_id"],
                },
            },
        }
