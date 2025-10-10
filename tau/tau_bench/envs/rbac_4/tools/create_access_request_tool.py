# Copyright Sierra Technologies

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateAccessRequestTool(Tool):
    """Submit a new access request for a user."""
    @staticmethod
    def invoke(data: Dict[str, Any], justification, resource_id, role_id, user_id) -> str:
        access_requests = data.get("access_requests", [])
        audit_logs = data.get("audit_logs", [])

        # Eliminate redundant PENDING requests.
        for ar in access_requests:
            if ar["user_id"] == user_id and ar["resource_id"] == resource_id and ar["requested_role_id"] == role_id and ar["status"] == "PENDING":
                return json.dumps({"error": "Duplicate pending access request"}, indent=2)

        # Fixed request identifier
        new_id = f"AR-{len(access_requests) + 1:03d}"
        access_requests.append({
            "request_id": new_id,
            "user_id": user_id,
            "resource_id": resource_id,
            "requested_role_id": role_id,
            "justification": justification,
            "status": "PENDING",
            "submitted_at": "2025-08-11 11:00:00+00:00",
            "reviewed_by": None,
            "decision_at": None
        })

        # Logging for audit purposes
        new_log_id = f"L-{len(audit_logs) + 1:03d}"
        audit_logs.append({
            "log_id": new_log_id,
            "actor_id": user_id,
            "action_type": "ACCESS_REQUEST_CREATED",
            "target_id": new_id,
            "timestamp": "2025-08-11 11:00:00+00:00",
            "details": f"User {user_id} submitted a request for {role_id} on {resource_id}"
        })

        return json.dumps({"success": f"Access request {new_id} created"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_access_request",
                "description": "Submit a new access request for a given resource and role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "resource_id": {"type": "string"},
                        "role_id": {"type": "string"},
                        "justification": {"type": "string"}
                    },
                    "required": ["user_id", "resource_id", "role_id", "justification"]
                }
            }
        }
