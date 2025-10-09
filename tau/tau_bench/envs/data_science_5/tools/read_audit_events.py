from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ReadAuditEvents(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], event_type: str = None) -> str:
        logs = data.get("terminal_log", {}).values() or []
        rows = [
            l for l in logs.values() if (not event_type or l.get("event_type") == event_type)
        ]
        payload = {"logs": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReadAuditEvents",
                "description": "List audit/terminal log entries (filter by event).",
                "parameters": {
                    "type": "object",
                    "properties": {"event_type": {"type": "string"}},
                    "required": [],
                },
            },
        }
