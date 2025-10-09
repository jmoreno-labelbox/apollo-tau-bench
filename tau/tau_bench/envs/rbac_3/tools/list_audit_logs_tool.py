from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ListAuditLogsTool(Tool):
    """Display audit logs with optional filters: action_type, user_id (actor_id), target_id, date range.
    Backward-compatible alias: filter_by == action_type.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        action_type: str = None,
        user_id: str = None,
        target_id: str = None,
        date_from: str = None,
        date_to: str = None,
        filter_by: str = None,
        actor_id: str = None
    ) -> str:
        # Support filter_by as alias for action_type, actor_id as alias for user_id
        action_type = action_type or filter_by
        user_id = user_id or actor_id
        user_id = user_id
        target_id = target_id
        date_from = date_from
        date_to = date_to

        logs = data.get("audit_logs", [])
        out = []

        dt_from = _parse_iso(date_from)
        dt_to = _parse_iso(date_to)

        for log in logs:
            if action_type and not _eq(log.get("action_type"), action_type):
                continue
            if user_id and not _eq(log.get("actor_id"), user_id):
                continue
            if target_id and not _eq(log.get("target_id"), target_id):
                continue

            if dt_from or dt_to:
                ts = _parse_iso(log.get("timestamp"))
                if dt_from and (not ts or ts < dt_from):
                    continue
                if dt_to and (not ts or ts > dt_to):
                    continue

            out.append(log)
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListAuditLogs",
                "description": "List audit logs with optional filters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action_type": {
                            "type": "string",
                            "description": "e.g., ACCESS_GRANTED, ACCESS_REJECTED",
                        },
                        "filter_by": {
                            "type": "string",
                            "description": "(alias) same as action_type",
                        },
                        "user_id": {
                            "type": "string",
                            "description": "Actor ID (maps to audit_logs.actor_id)",
                        },
                        "target_id": {"type": "string"},
                        "date_from": {
                            "type": "string",
                            "description": "ISO 8601 inclusive lower bound",
                        },
                        "date_to": {
                            "type": "string",
                            "description": "ISO 8601 inclusive upper bound",
                        },
                    },
                    "required": [],
                },
            },
        }
