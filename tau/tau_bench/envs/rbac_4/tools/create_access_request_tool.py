from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateAccessRequestTool(Tool):
    """File a new access request on behalf of a user."""

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        user_id: str = None, 
        resource_id: str = None, 
        role_id: str = None, 
        justification: str = None,
    submitted_at: Any = None,
    request_id: str = None,
    requester_id: str = None,
    subject_id: str = None
    ) -> str:
        # Support requester_id and subject_id as aliases for user_id
        user_id = user_id or requester_id or subject_id
        pass
        access_requests = data.get("access_requests", [])
        audit_logs = data.get("audit_logs", [])

        # Avoid duplicate PENDING requests
        for ar in access_requests:
            if (
                ar["user_id"] == user_id
                and ar["resource_id"] == resource_id
                and ar["requested_role_id"] == role_id
                and ar["status"] == "PENDING"
            ):
                payload = {"error": "Duplicate pending access request"}
                out = json.dumps(
                    payload, indent=2
                )
                return out

        # Predictable request ID
        new_id = f"AR-{len(access_requests) + 1:03d}"
        access_requests.append(
            {
                "request_id": new_id,
                "user_id": user_id,
                "resource_id": resource_id,
                "requested_role_id": role_id,
                "justification": justification,
                "status": "PENDING",
                "submitted_at": "2025-08-11 11:00:00+00:00",
                "reviewed_by": None,
                "decision_at": None,
            }
        )

        # Logging for audit
        new_log_id = f"L-{len(audit_logs) + 1:03d}"
        audit_logs.append(
            {
                "log_id": new_log_id,
                "actor_id": user_id,
                "action_type": "ACCESS_REQUEST_CREATED",
                "target_id": new_id,
                "timestamp": "2025-08-11 11:00:00+00:00",
                "details": f"User {user_id} submitted a request for {role_id} on {resource_id}",
            }
        )
        payload = {"success": f"Access request {new_id} created"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAccessRequest",
                "description": "Submit a new access request for a given resource and role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "resource_id": {"type": "string"},
                        "role_id": {"type": "string"},
                        "justification": {"type": "string"},
                    },
                    "required": ["user_id", "resource_id", "role_id", "justification"],
                },
            },
        }
