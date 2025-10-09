from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any

class GetAccessRequestDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], request_id: str = None) -> str:
        for req in data.get("access_requests", []):
            if req.get("request_id") == request_id:
                payload = req
                out = json.dumps(payload)
                return out
        payload = {"error": "Access request not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAccessRequestDetails",
                "description": "Retrieves details for a specific access request.",
                "parameters": {
                    "type": "object",
                    "properties": {"request_id": {"type": "string"}},
                    "required": ["request_id"],
                },
            },
        }
