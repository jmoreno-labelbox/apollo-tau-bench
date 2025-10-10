# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAuditLog(Tool):
    """Retrieve the audit log for compliance and tracking purposes."""

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        action_type: str = None,
        resource_id: str = None,
        time_range: str = None,
    ) -> str:
        action_type = f"{action_type}" if action_type is not None else None
        resource_id = f"{resource_id}" if resource_id is not None else None
        time_range = f"{time_range}" if time_range is not None else None

        audit_log = data.get("audit_log", [])
        filtered = audit_log
        if action_type:
            filtered = [e for e in filtered if e.get("event_type") == action_type]
        if resource_id:
            filtered = [e for e in filtered if f"{e.get('subject_id')}" == f"{resource_id}"]

        return json.dumps(
            {
                "audit_entries": filtered,
                "time_range": (time_range or "all_time"),
                "total_entries": len(filtered),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_audit_log",
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
