# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAccessRequestDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], request_id) -> str:
        for req in data.get('access_requests', []):
            if req.get('request_id') == request_id:
                return json.dumps(req)
        return json.dumps({"error": "Access request not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_access_request_details",
                        "description": "Retrieves details for a specific access request.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "request_id": {"type": "string"}
                                },
                                "required": ["request_id"]
                        }
                }
        }
