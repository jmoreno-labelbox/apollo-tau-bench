# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListAccessRequestsByStatusTool(Tool):
    """list_access_requests_by_status"""

    @staticmethod
    def invoke(data: Dict[str, Any], status) -> str:
        out = [r for r in data.get("access_requests", []) if r.get("status") == status]
        out = sorted(
            out, key=lambda r: (r.get("submitted_at") or "", r.get("request_id") or "")
        )
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_access_requests_by_status",
                "description": "Filter access_requests by status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "enum": ["PENDING", "APPROVED", "REJECTED"],
                        }
                    },
                    "required": ["status"],
                },
            },
        }
