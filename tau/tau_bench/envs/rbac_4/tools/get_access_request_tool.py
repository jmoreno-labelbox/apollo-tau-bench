# Copyright Sierra Technologies

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAccessRequestTool(Tool):
    """Retrieve a single access request by ID (read-only, deterministic)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # Assume: data["access_requests"] contains a list of dictionaries sourced from /mnt/data/access_requests.json.
        access_requests = data.get("access_requests", [])
        if not isinstance(access_requests, list):
            return json.dumps({"error": "access_requests must be a list"}, indent=2)

        request_id = kwargs.get("request_id")
        if not isinstance(request_id, str) or not request_id.strip():
            return json.dumps({"error": "request_id must be a non-empty string"}, indent=2)

        # Immutable reference search
        for row in access_requests:
            if isinstance(row, dict) and row.get("request_id") == request_id:
                return json.dumps({"access_request": row}, indent=2)

        return json.dumps({"error": f"Access request {request_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_access_request",
                "description": "Retrieve a single access request by ID (read-only).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {
                            "type": "string",
                            "description": "Access request ID, e.g. AR-004"
                        }
                    },
                    "required": ["request_id"],
                },
            },
        }
