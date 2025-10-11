# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RejectAccessRequest(Tool):
    """ Reject an access request and record the reason. """

    @staticmethod
    def invoke(data: Dict[str, Any], rejection_reason, request_id, reviewer_id, timestamp) -> str:
        request_id_to_find = request_id

        try:
            access_requests = data.get('access_requests', [])
        except:
            access_requests = []

        request_found = False
        for request in access_requests:
            if request.get("request_id") == request_id_to_find:
                request["status"] = "REJECTED"
                request["reviewed_by"] = reviewer_id
                request["decision_at"] = timestamp
                request["rejection_reason"] = rejection_reason
                request_found = True
                break

        if not request_found:
            return json.dumps({"error": f"Access request with ID '{request_id_to_find}' not found."})

        data['access_requests'] = access_requests

        return json.dumps({
            "message": "Access request rejected successfully.",
            "request_id": request_id_to_find,
            "new_status": "REJECTED"
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "reject_access_request",
                "description": "Rejects a pending access request and records the reason for the rejection.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {
                            "type": "string",
                            "description": "The unique ID of the access request to be rejected."
                        },
                        "reviewer_id": {
                            "type": "string",
                            "description": "The user ID of the manager who is rejecting the request."
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp for the decision record."
                        },
                        "rejection_reason": {
                            "type": "string",
                            "description": "A brief, clear reason for why the request is being rejected."
                        }
                    },
                    "required": ["request_id", "reviewer_id", "timestamp", "rejection_reason"]
                }
            }
        }
