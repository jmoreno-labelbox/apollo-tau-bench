from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetAuditLogsForTargetTool(Tool):
    """Retrieve audit logs filtered by target_id (read-only, predictable)."""

    @staticmethod
    def invoke(data: dict[str, Any], target_id: str = None) -> str:
        audit_logs = data.get("audit_logs", {}).values()
        if not isinstance(audit_logs, list):
            payload = {"error": "audit_logs must be a list"}
            out = json.dumps(payload, indent=2)
            return out

        if not isinstance(target_id, str) or not target_id.strip():
            payload = {"error": "target_id must be a non-empty string"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        results = [log for log in audit_logs.values() if log.get("target_id") == target_id]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetAuditLogsForTarget",
                "description": "Retrieve audit logs filtered by target_id (user, resource, role, alert, etc.).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "target_id": {
                            "type": "string",
                            "description": "The target entity ID (e.g., U-001, RES-021, ALRT-003)",
                        }
                    },
                    "required": ["target_id"],
                },
            },
        }
