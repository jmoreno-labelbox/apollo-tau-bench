# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _find_by_id(items: List[Dict[str, Any]], key: str, value: str) -> Optional[Dict[str, Any]]:
    for it in items or []:
        if it.get(key) == value:
            return it
    return None

class GetAccessRequest(Tool):
    """
    Retrieve access requests by ID, user, status, resource, or role.

    kwargs:
      request_id: str (optional) - Specific access request ID to retrieve
      user_id: str (optional) - Filter by requesting user
      status: str (optional) - Filter by status (PENDING, APPROVED, REJECTED)
      resource_id: str (optional) - Filter by requested resource
      requested_role_id: str (optional) - Filter by requested role
      include_user: bool = False - Include user details in response
      include_role: bool = False - Include role details in response
      include_resource: bool = False - Include resource details in response
    """
    @staticmethod
    def invoke(data: Dict[str, Any], request_id, requested_role_id, resource_id, status, user_id, include_resource = False, include_role = False, include_user = False) -> str:

        access_requests = data.get("access_requests", [])

        # Return the single access request if request_id is specified.
        if request_id:
            ar = _find_by_id(access_requests, "request_id", request_id)
            if not ar:
                return json.dumps({"error": f"request_id {request_id} not found"})

            # Construct a response that allows for optional enhancements.
            out = {"access_request": ar}
            if include_user:
                uid = ar.get("user_id") or ""
                user = _find_by_id(list(data.get("users", {}).values()), "user_id", uid)
                if user is not None:
                    out["user"] = user
            if include_role:
                rid = ar.get("requested_role_id") or ""
                role = _find_by_id(list(data.get("roles", {}).values()), "role_id", rid)
                if role is not None:
                    out["role"] = role
            if include_resource:
                res_id = ar.get("resource_id") or ""
                resource = _find_by_id(data.get("resources", []), "resource_id", res_id)
                if resource is not None:
                    out["resource"] = resource

            return json.dumps(out)

        # Screen access requests according to specified parameters.
        filtered_requests = []
        for request in access_requests:
            if user_id and request.get("user_id") != user_id:
                continue
            if status and request.get("status") != status:
                continue
            if resource_id and request.get("resource_id") != resource_id:
                continue
            if requested_role_id and request.get("requested_role_id") != requested_role_id:
                continue
            filtered_requests.append(request)

        return json.dumps({"ok": True, "access_requests": filtered_requests})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_access_request",
                "description": "Retrieve access requests by ID, user, status, resource, or role with optional expansions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string", "description": "Specific access request ID to retrieve."},
                        "user_id": {"type": "string", "description": "Filter by requesting user ID."},
                        "status": {"type": "string", "description": "Filter by status (PENDING, APPROVED, REJECTED)."},
                        "resource_id": {"type": "string", "description": "Filter by requested resource ID."},
                        "requested_role_id": {"type": "string", "description": "Filter by requested role ID."},
                        "include_user": {"type": "boolean", "description": "Include user details in response.", "default": False},
                        "include_role": {"type": "boolean", "description": "Include role details in response.", "default": False},
                        "include_resource": {"type": "boolean", "description": "Include resource details in response.", "default": False}
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }