# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListAccessRequestsByUserTool(Tool):
    """list_access_requests_by_user"""

    @staticmethod
    def invoke(data: Dict[str, Any], user_id) -> str:
        out = [
            r for r in data.get("access_requests", []) if r.get("user_id") == user_id
        ]
        out = sorted(
            out, key=lambda r: (r.get("submitted_at") or "", r.get("request_id") or "")
        )
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_access_requests_by_user",
                "description": "Filter access_requests by user_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
