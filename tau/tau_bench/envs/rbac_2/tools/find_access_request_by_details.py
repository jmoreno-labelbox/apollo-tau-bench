# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindAccessRequestByDetails(Tool):
    """ Find an access request based on its content details. """

    @staticmethod
    def invoke(data: Dict[str, Any], resource_id, role_id, user_id) -> str:

        try:
            access_requests = data.get('access_requests', [])
        except:
            access_requests = []

        for request in access_requests:
            if (request.get("user_id") == user_id and
                request.get("requested_role_id") == role_id and
                request.get("resource_id") == resource_id):
                # 3. If a match is identified, return the complete request object.
                return json.dumps(request)

        return json.dumps({"error": "No matching access request found for the provided details."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_access_request_by_details",
                "description": "Finds a specific access request by searching for a combination of the user who requested it, the role they requested, and the resource they requested it for.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user ID of the requester."
                        },
                        "role_id": {
                            "type": "string",
                            "description": "The role ID that was requested."
                        },
                        "resource_id": {
                            "type": "string",
                            "description": "The resource ID that was requested."
                        }
                    },
                    "required": ["user_id", "role_id", "resource_id"]
                }
            }
        }
