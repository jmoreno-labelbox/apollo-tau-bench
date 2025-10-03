from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta

class ListAccessRequestsByStatusTool(Tool):
    """ListAccessRequestsByStatus"""

    @staticmethod
    def invoke(data: dict[str, Any], status: str) -> str:
        out = [r for r in data.get("access_requests", []) if r.get("status") == status]
        out = sorted(
            out, key=lambda r: (r.get("submitted_at") or "", r.get("request_id") or "")
        )
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListAccessRequestsByStatus",
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
