# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ApproveAccessRequest(Tool):
    """ Approve access requests and change their status from 'PENDING' to 'APPROVED' and create the required user-role assignment to grant the access."""

    @staticmethod
    def invoke(data: Dict[str, Any], expires_on, request_id, reviewer_id, timestamp) -> str:

        try:
            access_requests = data.get('access_requests', [])
            user_roles = data.get('user_roles', [])
        except Exception as e:
            return json.dumps({"error": f"Failed to load data lists: {e}"})

        request = None
        for req in access_requests:
            if req.get("request_id") == request_id and req.get("status") == "PENDING":
                request = req
                break

        if not request:
            return json.dumps({"error": f"Pending access request with ID '{request_id}' not found."})

        request["status"] = "APPROVED"
        request["reviewed_by"] = reviewer_id
        request["decision_at"] = timestamp

        ur_existing_ids = [int(ur["user_role_id"].replace("UR-", "")) for ur in user_roles if ur.get("user_role_id", "").startswith("UR-")]
        next_ur_id = max(ur_existing_ids) + 1 if ur_existing_ids else 1

        new_role_assignment = {
            "user_role_id": f"UR-{next_ur_id:03d}",
            "user_id": request["user_id"],
            "role_id": request["requested_role_id"],
            "assigned_by": reviewer_id,
            "assigned_on": timestamp,
            "expires_on": expires_on
        }
        user_roles.append(new_role_assignment)

        data['access_requests'] = access_requests
        data['user_roles'] = user_roles

        return json.dumps({
            "message": "Access request approved and role granted successfully.",
            "request_id": request_id,
            "new_assignment_id": new_role_assignment["user_role_id"]
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "approve_access_request",
                "description": "Approves a pending access request. This updates the request status and grants the specified role to the user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {
                            "type": "string",
                            "description": "The unique ID of the access request to approve."
                        },
                        "reviewer_id": {
                            "type": "string",
                            "description": "The user ID of the person approving the request."
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp of the approval decision."
                        },
                        "expires_on": {
                            "type": "string",
                            "description": "Optional: The timestamp when the role assignment expires. Use null for permanent roles."
                        }
                    },
                    "required": ["request_id", "reviewer_id", "timestamp"]
                }
            }
        }
