# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindAccessRequestsByUserId(Tool):
    """Finds all access requests submitted by a specific user."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id_to_find = kwargs.get("user_id")
        try:
            all_requests = data.get('access_requests', [])
        except (KeyError, json.JSONDecodeError):
            all_requests = []

        user_requests = [
            request for request in all_requests
            if request.get("user_id") == user_id_to_find
        ]
        return json.dumps(user_requests)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_access_requests_by_user_id",
                "description": "Retrieves a list of all historical access requests submitted by a specific user, which can then be reviewed for patterns.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user whose access requests are to be retrieved."
                        }
                    },
                    "required": ["user_id"]
                }
            }
        }
