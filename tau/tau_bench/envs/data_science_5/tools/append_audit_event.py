from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AppendAuditEvent(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], event_type: str = None, message: str = None, details: str = None) -> str:
        # Accept either message or details
        if details is not None:
            message = details
        logs = data.get("terminal_log", {}).values()
        max_id = 0
        for l in logs.values():
            try:
                lid = int(l.get("log_id", 0))
                if lid > max_id:
                    max_id = lid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "log_id": new_id,
            "event_type": event_type,
            "message": message,
            "created_at": _now_iso_fixed(),
        }
        data["terminal_log"][row["terminal_log_id"]] = row
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AppendAuditEvent",
                "description": "Append an audit/terminal log entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "event_type": {"type": "string"},
                        "message": {"type": "string"},
                    },
                    "required": ["event_type", "message"],
                },
            },
        }
