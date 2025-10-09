from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ExportAuditLogsTool(Tool):
    """Export audit logs with optional filtering."""

    @staticmethod
    def invoke(data: dict[str, Any], actor_id: str = None, action_type: str = None, 
               target_id: str = None, start_time: str = None, end_time: str = None) -> str:
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
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ExportAuditLogs",
                "description": "Export audit logs with optional filters for actor, action, target, and time range",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "actor_id": {"type": "string"},
                        "action_type": {"type": "string"},
                        "target_id": {"type": "string"},
                        "start_time": {
                            "type": "string",
                            "description": "ISO8601 lower bound",
                        },
                        "end_time": {
                            "type": "string",
                            "description": "ISO8601 upper bound",
                        },
                    },
                },
            },
        }
