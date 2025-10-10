# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AuditIamAccessTool(Tool):
    """List IAM access audit logs between timestamps."""

    @staticmethod
    def invoke(data: Dict[str, Any], end_time, start_time) -> str:
        start = start_time
        end = end_time
        logs = data.get("audit_logs", [])
        results = [l for l in logs if start <= l["timestamp"] <= end and "IAM" in l.get("details", "")]
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "audit_iam_access",
                "description": "Return IAM-specific audit logs in the provided time range",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "start_time": {"type": "string"},
                        "end_time": {"type": "string"}
                    },
                    "required": ["start_time", "end_time"]
                }
            }
        }
