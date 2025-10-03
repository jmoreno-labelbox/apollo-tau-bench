from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any

class GetAccessRequestById(Tool):
    """Retrieve complete details of a specific access request by its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], request_id: str = None) -> str:
        try:
            access_requests = data.get("access_requests", [])
        except:
            access_requests = []

        for request in access_requests:
            if request.get("request_id") == request_id:
                payload = request
                out = json.dumps(payload)
                return out
        payload = {"error": f"Access request with ID '{request_id}' not found."}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAccessRequestById",
                "description": "Retrieves the full details of a specific access request using its unique ID (e.g., 'AR-007').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {
                            "type": "string",
                            "description": "The unique ID of the access request to retrieve.",
                        }
                    },
                    "required": ["request_id"],
                },
            },
        }
