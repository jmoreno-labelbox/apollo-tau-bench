from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetAuditLog(Tool):
    """Access the audit log for compliance and monitoring needs."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        action_type: str = None,
        resource_id: str = None,
        time_range: str = None
    ) -> str:
        action_type = f"{action_type}" if action_type is not None else None
        resource_id = f"{resource_id}" if resource_id is not None else None
        time_range = f"{time_range}" if time_range is not None else None

        audit_log = data.get("audit_log", {}).values()
        filtered = audit_log
        if action_type:
            filtered = [e for e in filtered.values() if e.get("event_type") == action_type]
        if resource_id:
            filtered = [
                e for e in filtered if f"{e.get('subject_id')}" == f"{resource_id}"
            ]
        payload = {
            "audit_entries": filtered,
            "time_range": (time_range or "all_time"),
            "total_entries": len(filtered),
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        pass
        action_type = f"{action_type}" if action_type is not None else None
        resource_id = f"{resource_id}" if resource_id is not None else None
        time_range = f"{time_range}" if time_range is not None else None

        audit_log = data.get("audit_log", {}).values()
        filtered = audit_log
        if action_type:
            filtered = [e for e in filtered.values() if e.get("event_type") == action_type]
        if resource_id:
            filtered = [
                e for e in filtered if f"{e.get('subject_id')}" == f"{resource_id}"
            ]
        payload = {
                "audit_entries": filtered,
                "time_range": (time_range or "all_time"),
                "total_entries": len(filtered),
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
                "name": "GetAuditLog",
                "description": "Retrieve the audit log with optional filtering by action type, resource ID, or time range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action_type": {"type": "string"},
                        "resource_id": {"type": "string"},
                        "time_range": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
