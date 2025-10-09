from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetAuditLog(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], audit_log: list = None) -> str:
        payload = audit_log if audit_log is not None else []
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAuditLog",
                "description": "Return the audit log.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
