from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class AuditIamAccessTool(Tool):
    """Display IAM access audit logs within specified timestamps."""

    @staticmethod
    def invoke(data: dict[str, Any], start_time: str = None, end_time: str = None) -> str:
        logs = data.get("audit_logs", [])
        results = [
            l
            for l in logs
            if start_time <= l["timestamp"] <= end_time and "IAM" in l.get("details", "")
        ]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AuditIamAccess",
                "description": "Return IAM-specific audit logs in the provided time range",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "start_time": {"type": "string"},
                        "end_time": {"type": "string"},
                    },
                    "required": ["start_time", "end_time"],
                },
            },
        }
