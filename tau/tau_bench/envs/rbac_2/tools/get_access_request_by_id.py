# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAccessRequestById(Tool):
    """ Get the full details of a specific access request using its ID. """

    @staticmethod
    def invoke(data: Dict[str, Any], request_id) -> str:
        try:
            access_requests = data.get('access_requests', [])
        except:
            access_requests = []

        for request in access_requests:
            if request.get("request_id") == request_id:
                return json.dumps(request)

        return json.dumps({"error": f"Access request with ID '{request_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_access_request_by_id",
                "description": "Retrieves the full details of a specific access request using its unique ID (e.g., 'AR-007').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {
                            "type": "string",
                            "description": "The unique ID of the access request to retrieve."
                        }
                    },
                    "required": ["request_id"]
                }
            }
        }
