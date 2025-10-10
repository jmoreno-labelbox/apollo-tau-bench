# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAccessRequest(Tool):
    """Updates an existing access request, used for rerouting or corrections."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        request_id = kwargs.get("request_id")
        new_reviewer_id = kwargs.get("new_reviewer_id")
        new_status = kwargs.get("new_status")

        for req in data.get('access_requests', []):
            if req.get("request_id") == request_id:
                if new_reviewer_id:
                    req["reviewer_id"] = new_reviewer_id
                if new_status:
                    req["status"] = new_status
                req["decision_at"] = kwargs.get("timestamp") 
                return json.dumps({"status": "success", "updated_request_id": request_id})
        
        return json.dumps({"status": "error", "message": "Request not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_access_request",
                "description": "Updates an existing access request. Primarily used to reroute a request to a new approver by changing the reviewer_id and resetting the status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string", "description": "The ID of the access request to update."},
                        "new_reviewer_id": {"type": "string", "description": "The user_id of the new approver to assign the request to."},
                        "new_status": {"type": "string", "description": "The new status for the request, e.g., 'PENDING'."},
                        "timestamp": {"type": "string", "description": "The timestamp of the update action."}
                    },
                    "required": ["request_id"]
                }
            }
        }
