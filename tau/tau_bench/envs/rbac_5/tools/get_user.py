# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _find_by_id(items: List[Dict[str, Any]], key: str, value: str) -> Optional[Dict[str, Any]]:
    for it in items or []:
        if it.get(key) == value:
            return it
    return None

class GetUser(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], department, first_name, last_name, mfa_enabled, role_id, status, user_id, username, allow_missing = False) -> str:

        def _not_found(msg: str) -> str:
            if allow_missing:
                return json.dumps({"ok": True, "message": "User not found"})
            return json.dumps({"error": msg})

        # If user_id exists, perform a search using user_id.
        if user_id:
            user = _find_by_id(list(data.get("users", {}).values()), "user_id", user_id)
            return json.dumps(user) if user else _not_found(f"user_id {user_id} not found")

        # Search using the username if one is supplied.
        if username:
            username_lower = username.strip().lower()
            for u in list(data.get("users", {}).values()):
                if u.get("username", "").lower() == username_lower:
                    return json.dumps(u)
            return _not_found(f"username {username} not found")

        # If first_name and last_name are supplied, create a username and perform a search.
        if first_name and last_name:
            first_name_clean = first_name.strip().lower()
            last_name_clean = last_name.strip().lower()
            username_to_search = first_name_clean[0] + last_name_clean
            for u in list(data.get("users", {}).values()):
                if u.get("username", "").lower() == username_to_search:
                    return json.dumps(u)
            return _not_found("User not found")


        # Return a filtered list if a department or status is specified without a specific identifier.
        if department or status or mfa_enabled is not None:
            users = list(data.get("users", {}).values())
            filtered: List[Dict[str, Any]] = []
            for u in users:
                if department and u.get("department") != department:
                    continue
                if status and u.get("status") != status:
                    continue
                if mfa_enabled is not None and u.get("mfa_enabled") != mfa_enabled:
                    continue
                filtered.append(u)
            if role_id:
                user_roles = data.get("user_roles", [])
                user_ids_with_role = {ur.get("user_id") for ur in user_roles if ur.get("role_id") == role_id}
                filtered = [u for u in filtered if u.get("user_id") in user_ids_with_role]
            return json.dumps({"ok": True, "users": filtered})
        if role_id:
            user_roles = data.get("user_roles", [])
            user_ids_with_role = {ur.get("user_id") for ur in user_roles if ur.get("role_id") == role_id}
            users = [u for u in list(data.get("users", {}).values()) if u.get("user_id") in user_ids_with_role]
            return json.dumps({"ok": True, "users": users})
        return json.dumps({"error": "Must provide user_id, username, both first_name and last_name, role_id, or department/status filter"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user",
                "description": "Fetch a single user by id/username/full name, or list users filtered by department, status, MFA, or role_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "User identifier (e.g., U-001)."},
                        "username": {"type": "string", "description": "Username to search for."},
                        "first_name": {"type": "string", "description": "User first name (used with last_name)."},
                        "last_name": {"type": "string", "description": "User last name (used with first_name)."},
                        "department": {"type": "string", "description": "Filter by department (exact match)."},
                        "status": {"type": "string", "description": "Filter by status (e.g., ACTIVE, SUSPENDED)."},
                        "mfa_enabled": {"type": "boolean", "description": "Filter by MFA status (enabled/disabled)."},
                        "role_id": {"type": "string", "description": "Filter users by having this role_id."},
                        "allow_missing": {"type": "boolean", "description": "If true, return {ok: True, message: 'User not found'} instead of an error when the user is not found.", "default": False}
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }