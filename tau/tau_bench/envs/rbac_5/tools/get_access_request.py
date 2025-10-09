from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetAccessRequest(Tool):
    """
    Retrieve access requests based on ID, user, status, resource, or role.

    kwargs:
      request_id: str (optional) - Specific access request ID to retrieve
      user_id: str (optional) - Filter by the user making the request
      status: str (optional) - Filter by status (PENDING, APPROVED, REJECTED)
      resource_id: str (optional) - Filter by the requested resource
      requested_role_id: str (optional) - Filter by the requested role
      include_user: bool = False - Include user details in the response
      include_role: bool = False - Include role details in the response
      include_resource: bool = False - Include resource details in the response
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        request_id: str = None,
        user_id: str = None,
        status: str = None,
        resource_id: str = None,
        requested_role_id: str = None,
        include_user: bool = False,
        include_role: bool = False,
        include_resource: bool = False
    ) -> str:
        access_requests = data.get("access_requests", [])

        # If request_id is supplied, return the specific access request
        if request_id:
            ar = _find_by_id(access_requests, "request_id", request_id)
            if not ar:
                payload = {"error": f"request_id {request_id} not found"}
                out = json.dumps(payload)
                return out

            # Construct a response with optional extensions
            out = {"access_request": ar}
            if include_user:
                uid = ar.get("user_id") or ""
                user = _find_by_id(data.get("users", []), "user_id", uid)
                if user is not None:
                    out["user"] = user
            if include_role:
                rid = ar.get("requested_role_id") or ""
                role = _find_by_id(data.get("roles", []), "role_id", rid)
                if role is not None:
                    out["role"] = role
            if include_resource:
                res_id = ar.get("resource_id") or ""
                resource = _find_by_id(data.get("resources", []), "resource_id", res_id)
                if resource is not None:
                    out["resource"] = resource
            payload = out
            out = json.dumps(payload)
            return out

        # Narrow down access requests according to the supplied criteria
        filtered_requests = []
        for request in access_requests:
            if user_id and request.get("user_id") != user_id:
                continue
            if status and request.get("status") != status:
                continue
            if resource_id and request.get("resource_id") != resource_id:
                continue
            if (
                requested_role_id
                and request.get("requested_role_id") != requested_role_id
            ):
                continue
            filtered_requests.append(request)
        payload = {"ok": True, "access_requests": filtered_requests}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAccessRequest",
                "description": "Retrieve access requests by ID, user, status, resource, or role with optional expansions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {
                            "type": "string",
                            "description": "Specific access request ID to retrieve.",
                        },
                        "user_id": {
                            "type": "string",
                            "description": "Filter by requesting user ID.",
                        },
                        "status": {
                            "type": "string",
                            "description": "Filter by status (PENDING, APPROVED, REJECTED).",
                        },
                        "resource_id": {
                            "type": "string",
                            "description": "Filter by requested resource ID.",
                        },
                        "requested_role_id": {
                            "type": "string",
                            "description": "Filter by requested role ID.",
                        },
                        "include_user": {
                            "type": "boolean",
                            "description": "Include user details in response.",
                            "default": False,
                        },
                        "include_role": {
                            "type": "boolean",
                            "description": "Include role details in response.",
                            "default": False,
                        },
                        "include_resource": {
                            "type": "boolean",
                            "description": "Include resource details in response.",
                            "default": False,
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }
