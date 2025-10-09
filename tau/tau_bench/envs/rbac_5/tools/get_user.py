from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetUser(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str = None,
        username: str = None,
        first_name: str = None,
        last_name: str = None,
        department: str = None,
        status: str = None,
        mfa_enabled: bool = None,
        role_id: str = None,
        allow_missing: bool = False
    ) -> str:
        pass

        def _not_found(msg: str) -> str:
            pass
            if allow_missing:
                payload = {"ok": True, "message": "User not found"}
                out = json.dumps(payload)
                return out
            payload = {"error": msg}
            out = json.dumps(payload)
            return out

        # If user_id is given, perform a search using user_id
        if user_id:
            user = _find_by_id(data.get("users", {}).values(), "user_id", user_id)
            return (
                json.dumps(user) if user else _not_found(f"user_id {user_id} not found")
            )

        # If a username is supplied, conduct a search using the username
        if username:
            username_lower = username.strip().lower()
            for u in data.get("users", {}).values():
                if u.get("username", "").lower() == username_lower:
                    payload = u
                    out = json.dumps(payload)
                    return out
            return _not_found(f"username {username} not found")

        # If both first_name and last_name are given, create a username and search
        if first_name and last_name:
            first_name_clean = first_name.strip().lower()
            last_name_clean = last_name.strip().lower()
            username_to_search = first_name_clean[0] + last_name_clean
            for u in data.get("users", {}).values():
                if u.get("username", "").lower() == username_to_search:
                    payload = u
                    out = json.dumps(payload)
                    return out
            return _not_found("User not found")

        # If department or status is supplied (without a specific identifier), return a filtered list
        if department or status or mfa_enabled is not None:
            users = data.get("users", {}).values()
            filtered: list[dict[str, Any]] = []
            for u in users.values():
                if department and u.get("department") != department:
                    continue
                if status and u.get("status") != status:
                    continue
                if mfa_enabled is not None and u.get("mfa_enabled") != mfa_enabled:
                    continue
                filtered.append(u)
            if role_id:
                user_roles = data.get("user_roles", {}).values()
                user_ids_with_role = {
                    ur.get("user_id")
                    for ur in user_roles.values() if ur.get("role_id") == role_id
                }
                filtered = [
                    u for u in filtered if u.get("user_id") in user_ids_with_role
                ]
            payload = {"ok": True, "users": filtered}
            out = json.dumps(payload)
            return out
        if role_id:
            user_roles = data.get("user_roles", {}).values()
            user_ids_with_role = {
                ur.get("user_id") for ur in user_roles.values() if ur.get("role_id") == role_id
            }
            users = [
                u
                for u in data.get("users", {}).values()
                if u.get("user_id") in user_ids_with_role
            ]
            payload = {"ok": True, "users": users}
            out = json.dumps(payload)
            return out
        payload = {
            "error": "Must provide user_id, username, both first_name and last_name, role_id, or department/status filter"
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUser",
                "description": "Fetch a single user by id/username/full name, or list users filtered by department, status, MFA, or role_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "User identifier (e.g., U-001).",
                        },
                        "username": {
                            "type": "string",
                            "description": "Username to search for.",
                        },
                        "first_name": {
                            "type": "string",
                            "description": "User first name (used with last_name).",
                        },
                        "last_name": {
                            "type": "string",
                            "description": "User last name (used with first_name).",
                        },
                        "department": {
                            "type": "string",
                            "description": "Filter by department (exact match).",
                        },
                        "status": {
                            "type": "string",
                            "description": "Filter by status (e.g., ACTIVE, SUSPENDED).",
                        },
                        "mfa_enabled": {
                            "type": "boolean",
                            "description": "Filter by MFA status (enabled/disabled).",
                        },
                        "role_id": {
                            "type": "string",
                            "description": "Filter users by having this role_id.",
                        },
                        "allow_missing": {
                            "type": "boolean",
                            "description": "If true, return {ok: True, message: 'User not found'} instead of an error when the user is not found.",
                            "default": False,
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }
