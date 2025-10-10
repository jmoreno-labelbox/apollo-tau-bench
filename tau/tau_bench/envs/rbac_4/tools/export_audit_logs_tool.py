# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ExportAuditLogsTool(Tool):
    """Export audit logs with optional filters."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        actor_id = kwargs.get("actor_id")
        action_type = kwargs.get("action_type")
        target_id = kwargs.get("target_id")
        start_time = kwargs.get("start_time")
        end_time = kwargs.get("end_time")

        logs = data.get("audit_logs", [])
        results = []

        for log in logs:
            if actor_id and log.get("actor_id") != actor_id:
                continue
            if action_type and log.get("action_type") != action_type:
                continue
            if target_id and log.get("target_id") != target_id:
                continue
            if start_time and log.get("timestamp") < start_time:
                continue
            if end_time and log.get("timestamp") > end_time:
                continue
            results.append(log)

        # Deterministic export format (JSON string list of logs)
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "export_audit_logs",
                "description": "Export audit logs with optional filters for actor, action, target, and time range",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "actor_id": {"type": "string"},
                        "action_type": {"type": "string"},
                        "target_id": {"type": "string"},
                        "start_time": {"type": "string", "description": "ISO8601 lower bound"},
                        "end_time": {"type": "string", "description": "ISO8601 upper bound"}
                    }
                }
            }
        }
