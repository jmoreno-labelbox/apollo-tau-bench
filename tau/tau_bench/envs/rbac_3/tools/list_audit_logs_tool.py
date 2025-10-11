# Copyright Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _parse_iso(ts: Optional[str]) -> Optional[datetime]:
    """Robust ISO8601 parse: supports 'Z' and offsets; returns None if missing."""
    if not ts:
        return None
    ts = ts.replace("Z", "+00:00")
    return datetime.fromisoformat(ts)

def _eq(a: Optional[str], b: Optional[str]) -> bool:
    return (a or "") == (b or "")

class ListAuditLogsTool(Tool):
    """List audit logs with optional filters: action_type, user_id (actor_id), target_id, date range.
    Backward-compatible alias: filter_by == action_type.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], action_type, date_from, date_to, filter_by, target_id, user_id) -> str:
        action_type = action_type or filter_by

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

        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_audit_logs",
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