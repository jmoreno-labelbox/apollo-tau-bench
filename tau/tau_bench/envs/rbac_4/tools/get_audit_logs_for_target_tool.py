# Sierra copyright notice.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAuditLogsForTargetTool(Tool):
    """Get audit logs filtered by target_id (read-only, deterministic)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        target_id = kwargs.get("target_id")
        audit_logs = data.get("audit_logs", [])
        if not isinstance(audit_logs, list):
            return json.dumps({"error": "audit_logs must be a list"}, indent=2)

        if not isinstance(target_id, str) or not target_id.strip():
            return json.dumps({"error": "target_id must be a non-empty string"}, indent=2)

        results = [log for log in audit_logs if log.get("target_id") == target_id]
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_audit_logs_for_target",
                "description": "Retrieve audit logs filtered by target_id (user, resource, role, alert, etc.).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "target_id": {"type": "string", "description": "The target entity ID (e.g., U-001, RES-021, ALRT-003)"}
                    },
                    "required": ["target_id"]
                }
            }
        }
