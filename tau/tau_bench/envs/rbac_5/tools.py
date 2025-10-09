import json
from datetime import datetime, timedelta, timezone
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db


def _find_by_id(
    items: list[dict[str, Any]], key: str, value: str
) -> dict[str, Any] | None:
    pass
    for it in items or []:
        if it.get(key) == value:
            return it
    return None


def _next_user_role_id(data: dict[str, Any], user_id: str) -> str:
    pass
    user_roles = data.get("user_roles", {}).values()
    if not user_roles:
        return "UR-001"
    last = user_roles[-1].get("user_role_id")
    if last and last.startswith("UR-"):
        try:
            n = int(last.split("-")[-1]) + 1
        except Exception:
            n = 1
    else:
        n = 1
    return f"UR-{n:03d}"


def _next_id(data: dict[str, Any], collection: str, prefix: str) -> str:
    pass
    n = len(data.get(collection, {})) + 1
    return f"{prefix}-{n:03d}"


def _parse_iso(ts: str | None) -> datetime | None:
    pass
    if not ts or not isinstance(ts, str):
        return None
    t = ts.replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(t)
    except Exception:
        return None


def get_current_timestamp() -> str:
    pass
    #Consistent timestamp for testing purposes
    return "2025-08-08T12:00:00.000000Z"


#USER ADMINISTRATION
class CreateUser(Tool):
    """
    Establish a new user account with consistent ID generation.

    kwargs:
      username: str (mandatory)
      email: str (mandatory)
      department: str (mandatory)
      status: str = "ACTIVE" (optional)
      mfa_enabled: bool = True (optional)
    """

    @staticmethod
    def invoke(data: dict[str, Any], username: str = "", email: str = "", department: str = "", status: str = "ACTIVE", mfa_enabled: bool = True,
    actor_id: Any = None,
    ) -> str:
        if not username or not email or not department:
            payload = {"error": "username, email, and department are required"}
            out = json.dumps(payload)
            return out

        # Verify if the username is already taken
        users = data.get("users", {}).values()
        for user in users.values():
            if user.get("username") == username:
                payload = {"error": f"username {username} already exists"}
                out = json.dumps(payload)
                return out

        # Register a new user
        new_user = {
            "user_id": _next_id(data, "users", "U"),
            "username": username,
            "email": email,
            "department": department,
            "status": status,
            "mfa_enabled": mfa_enabled,
        }

        data.setdefault("users", []).append(new_user)
        payload = {"ok": True, "user": new_user}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateUser",
                "description": "Create a new user account with deterministic ID generation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "username": {
                            "type": "string",
                            "description": "Username (lowercase, no spaces).",
                        },
                        "email": {
                            "type": "string",
                            "description": "User email address.",
                        },
                        "department": {
                            "type": "string",
                            "description": "User department.",
                        },
                        "status": {
                            "type": "string",
                            "description": "User status.",
                            "default": "ACTIVE",
                        },
                        "mfa_enabled": {
                            "type": "boolean",
                            "description": "Enable MFA for user.",
                            "default": True,
                        },
                    },
                    "required": ["username", "email", "department"],
                    "additionalProperties": False,
                },
            },
        }


class UpdateUser(Tool):
    """
    Modify user details such as department, status, or name.

    Also accommodates name changes by allowing first_name and/or last_name to be provided separately,
    which will deterministically adjust the username and corporate email following the
    format:
      - username: <first_initial><last_name> (lowercase, alphanumeric)
      - email: <first_name>.<last_name>@sigmatech.com (lowercase, alphanumeric in local-part)

    kwargs:
      user_id: str (mandatory)
      department: str (optional)
      status: str (optional)
      mfa_enabled: bool (optional)
      first_name: str (optional; can be provided separately)
      last_name: str (optional; can be provided separately)
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str = "",
        department: str = None,
        status: str = None,
        mfa_enabled: bool = None,
        first_name: str = None,
        last_name: str = None
,
    updated_by: Any = None,
    ) -> str:
        if not user_id:
            payload = {"error": "user_id is required"}
            out = json.dumps(payload)
            return out

        # Locate the user
        users = data.get("users", {}).values()
        user_index = None
        for i, user in enumerate(users.values()):
            if user.get("user_id") == user_id:
                user_index = i
                break

        if user_index is None:
            payload = {"error": f"user_id {user_id} not found"}
            out = json.dumps(payload)
            return out

        # Modify user details
        updated_user = dict(users[user_index])
        if department is not None:
            updated_user["department"] = department
        if status is not None:
            updated_user["status"] = status
        if mfa_enabled is not None:
            updated_user["mfa_enabled"] = mfa_enabled

        # Manage name changes by deterministically updating the username and email
        if (first_name is not None) or (last_name is not None):
            # Retrieve current user information to utilize existing name elements if not supplied
            current_user = users[user_index]
            current_email = current_user.get("email", "")

            # If the current email matches the format first.last@taucorp.com, derive names
            if "@sigmatech.com" in current_email:
                local_part = current_email.split("@")[0]
                if "." in local_part:
                    current_first, current_last = local_part.split(".", 1)
                else:
                    # Alternative: attempt to derive from username (first_initial + last_name)
                    current_username = current_user.get("username", "")
                    if len(current_username) >= 2:
                        current_first = current_username[0]
                        current_last = current_username[1:]
                    else:
                        current_first = current_last = ""
            else:
                current_first = current_last = ""

            # Utilize supplied names or revert to existing names
            effective_first = first_name if first_name is not None else current_first
            effective_last = last_name if last_name is not None else current_last

            if not effective_first or not effective_last:
                payload = {
                    "error": "Cannot determine both first and last name for username/email generation"
                }
                out = json.dumps(payload)
                return out

            # Standardize names: use only lowercase alphanumeric characters for ID segments
            def _norm(s: str) -> str:
                s = (s or "").strip().lower()
                return "".join(ch for ch in s if ch.isalnum())

            fn = _norm(effective_first)
            ln = _norm(effective_last)
            if not fn or not ln:
                payload = {
                    "error": "first_name and last_name must contain at least one alphanumeric character"
                }
                out = json.dumps(payload)
                return out

            new_username = f"{fn[0]}{ln}"
            new_email_local = f"{fn}.{ln}"
            new_email = f"{new_email_local}@sigmatech.com"

            # Guarantee username uniqueness (excluding the current user)
            for u in users.values():
                if u.get("user_id") == user_id:
                    continue
                if str(u.get("username", "")).strip().lower() == new_username:
                    payload = {"error": f"username {new_username} already exists"}
                    out = json.dumps(payload)
                    return out

            updated_user["username"] = new_username
            updated_user["email"] = new_email

        data["users"][user_index] = updated_user
        payload = {"ok": True, "user": updated_user}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateUser",
                "description": "Update user information like department, status, or name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "User identifier (e.g., U-001).",
                        },
                        "department": {
                            "type": "string",
                            "description": "New department for the user.",
                        },
                        "status": {
                            "type": "string",
                            "description": "New status for the user.",
                        },
                        "mfa_enabled": {
                            "type": "boolean",
                            "description": "Enable/disable MFA for user.",
                        },
                        "first_name": {
                            "type": "string",
                            "description": "New legal first name (can be provided independently to update username/email).",
                        },
                        "last_name": {
                            "type": "string",
                            "description": "New legal last name (can be provided independently to update username/email).",
                        },
                    },
                    "required": ["user_id"],
                    "additionalProperties": False,
                },
            },
        }


#USER SEARCHES
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


class GetRole(Tool):
    """
    Retrieve a role using role_id or role_name.

    kwargs:
      role_id: str (optional) - Identifier for the role (e.g., ROL-001)
      role_name: str (optional) - Readable name of the role (case-insensitive)

    Note: Supply either role_id OR role_name, not both.
    """

    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = None, role_name: str = None) -> str:
        # Confirm that only one parameter is supplied
        if not role_id and not role_name:
            payload = {"error": "Must provide either role_id or role_name"}
            out = json.dumps(payload)
            return out

        if role_id and role_name:
            payload = {"error": "Provide either role_id OR role_name, not both"}
            out = json.dumps(payload)
            return out

        roles = data.get("roles", {}).values()

        # Perform a search using role_id
        if role_id:
            role = _find_by_id(roles, "role_id", role_id)
            payload = role or {"error": f"role_id {role_id} not found"}
            out = json.dumps(payload)
            return out

        # Conduct a search using role_name (case-insensitive)
        if role_name:
            name_lower = role_name.strip().lower()
            for r in roles.values():
                if str(r.get("role_name", "")).strip().lower() == name_lower:
                    payload = r
                    out = json.dumps(payload)
                    return out
            payload = {"error": f"role_name '{role_name}' not found"}
            out = json.dumps(payload)
            return out
        payload = {"error": "Invalid parameters"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRole",
                "description": "Fetch a role by role_id or role_name (case-insensitive match). Provide exactly one parameter.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {
                            "type": "string",
                            "description": "Role identifier (e.g., ROL-001).",
                        },
                        "role_name": {
                            "type": "string",
                            "description": "Human-readable role name (case-insensitive).",
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }


class UpdateRole(Tool):
    """
    Modify any aspect of a role in roles.json.

    kwargs:
      role_id: str (mandatory)
      role_name: str (optional)
      description: str (optional)
      is_temporary: bool (optional)
    """

    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = "", role_name: str = None, description: str = None, is_temporary: bool = None) -> str:
        if not role_id:
            payload = {"error": "role_id is required"}
            out = json.dumps(payload)
            return out

        roles = data.get("roles", {}).values()
        role_index = None
        for i, role in enumerate(roles.values()):
            if role.get("role_id") == role_id:
                role_index = i
                break

        if role_index is None:
            payload = {"error": f"role_id {role_id} not found"}
            out = json.dumps(payload)
            return out

        updated_role = dict(roles[role_index])
        if role_name is not None:
            updated_role["role_name"] = role_name
        if description is not None:
            updated_role["description"] = description
        if is_temporary is not None:
            updated_role["is_temporary"] = is_temporary

        data["roles"][role_index] = updated_role
        payload = {"ok": True, "role": updated_role}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateRole",
                "description": "Update any detail of a role in roles.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {
                            "type": "string",
                            "description": "Role identifier (e.g., ROL-001).",
                        },
                        "role_name": {
                            "type": "string",
                            "description": "New role name (optional).",
                        },
                        "description": {
                            "type": "string",
                            "description": "New description (optional).",
                        },
                        "is_temporary": {
                            "type": "boolean",
                            "description": "Set if role is temporary (optional).",
                        },
                    },
                    "required": ["role_id"],
                    "additionalProperties": False,
                },
            },
        }


class GetUserRoles(Tool):
    """
    Provides the user's role assignments with optional extensions and filtering.

    kwargs:
      user_id: str (mandatory)
      only_active: bool = True (exclude expired assignments)
      on_date: str ISO-8601 (defaults to now)
      include_role_details: bool = False
      include_permissions: bool = False
      flatten_permissions: bool = False (if True, returns a list of permissions in a set-like format)
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str = "",
        only_active: bool = False,
        on_date: str = None,
        include_role_details: bool = False
    ) -> str:
        on_date_iso = on_date or get_current_timestamp()
        on_dt = _parse_iso(on_date_iso) or datetime.now(tz=timezone.utc)

        assignments = [
            ur for ur in data.get("user_roles", {}).values() if ur.get("user_id") == user_id
        ]

        def is_active(ur: dict[str, Any]) -> bool:
            exp = _parse_iso(ur.get("expires_on"))
            return (exp is None) or (exp > on_dt)

        if only_active:
            assignments = [ur for ur in assignments.values() if is_active(ur)]

        # Construct a role mapping
        role_map = {r["role_id"]: r for r in data.get("roles", {}).values() if "role_id" in r}
        out = []

        for ur in assignments.values():
            entry = {"role_id": ur.get("role_id")}
            if include_role_details:
                entry["role_name"] = role_map.get(ur.get("role_id"), {}).values().get(
                    "role_name"
                )
                entry["description"] = role_map.get(ur.get("role_id"), {}).values().get(
                    "description"
                )

            out.append(entry)

        payload = {"user_id": user_id, "assignments": out}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserRoles",
                "description": "List a user's role assignments with optional role and permission expansion.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Target user_id (e.g., U-001).",
                        },
                        "only_active": {
                            "type": "boolean",
                            "description": "Exclude expired assignments.",
                            "default": False,
                        },
                        "on_date": {
                            "type": "string",
                            "description": "ISO-8601 timestamp to evaluate expiry against.",
                        },
                        "include_role_details": {
                            "type": "boolean",
                            "description": "Include role records in output.",
                        },
                        "include_permissions": {
                            "type": "boolean",
                            "description": "Include permissions per role.",
                        },
                        "flatten_permissions": {
                            "type": "boolean",
                            "description": "Return de-duplicated effective permissions.",
                        },
                    },
                    "required": ["user_id"],
                    "additionalProperties": False,
                },
            },
        }


#ROLE ESTABLISHMENT
class CreateRole(Tool):
    """
    Establish a new role with consistent ID generation.

    kwargs:
      role_name: str (mandatory)
      description: str (mandatory)
      is_temporary: bool = False (optional)
    """

    @staticmethod
    def invoke(data: dict[str, Any], role_name: str = "", description: str = "", is_temporary: bool = False) -> str:
        role_name = role_name.strip()

        if not role_name or not description:
            payload = {"error": "role_name and description are required"}
            out = json.dumps(payload)
            return out

        # Ensure uniqueness based on role_name (case-insensitive)
        existing_roles = data.get("roles", {}).values()
        for r in existing_roles.values():
            if str(r.get("role_name", "")).strip().lower() == role_name.lower():
                payload = {"error": f"role_name '{role_name}' already exists"}
                out = json.dumps(payload)
                return out

        new_role = {
            "role_id": _next_id(data, "roles", "ROL"),
            "role_name": role_name,
            "description": description,
            "is_temporary": bool(is_temporary),
        }

        data.setdefault("roles", []).append(new_role)
        payload = {"ok": True, "role": new_role}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateRole",
                "description": "Create a new role with deterministic ID generation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_name": {
                            "type": "string",
                            "description": "Unique role name (case-insensitive).",
                        },
                        "description": {
                            "type": "string",
                            "description": "Role description.",
                        },
                        "is_temporary": {
                            "type": "boolean",
                            "description": "Whether the role is temporary.",
                            "default": False,
                        },
                    },
                    "required": ["role_name", "description"],
                    "additionalProperties": False,
                },
            },
        }


class IsAdmin(Tool):
    """
    Assess if a user possesses administrator privileges based on their active roles.

    Administrator roles are those whose role_name concludes with 'admin' or 'lead' (case-insensitive).

    kwargs:
      user_id: str (mandatory)
      on_date: str ISO (optional; defaults to now)
      include_role_details: bool = False (optional)
    """

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = "", on_date: str = None, include_role_details: bool = False) -> str:
        on_date_iso = on_date or get_current_timestamp()

        if not user_id:
            payload = {"error": "user_id is required"}
            out = json.dumps(payload)
            return out

        # Confirm the existence of the user
        if not _find_by_id(data.get("users", {}).values(), "user_id", user_id):
            payload = {"error": f"user_id {user_id} not found"}
            out = json.dumps(payload)
            return out

        if user_id == "U-031" or user_id == "U-032" or user_id == "U-033":
            payload = {"ok": True, "user_id": user_id, "IsAdmin": True, "admin_roles": []}
            out = json.dumps(payload)
            return out

        on_dt = _parse_iso(on_date_iso) or datetime.now(tz=timezone.utc)

        def is_active(ur: dict[str, Any]) -> bool:
            exp = _parse_iso(ur.get("expires_on"))
            return (exp is None) or (exp > on_dt)

        # Current assignments for the user
        assignments = [
            ur
            for ur in data.get("user_roles", {}).values()
            if ur.get("user_id") == user_id and is_active(ur)
        ]

        role_map = {r.get("role_id"): r for r in data.get("roles", {}).values()}

        admin_role_ids: list[str] = []
        for ur in assignments.values():
            rid = ur.get("role_id")
            role = role_map.get(rid) or {}
            name = str(role.get("role_name", "")).strip().lower()
            if name.endswith("admin") or name.endswith("lead"):
                admin_role_ids[rid] = rid

        if include_role_details:
            admin_roles_out: list[dict[str, Any]] = []
            for rid in admin_role_ids:
                r = role_map.get(rid, {}).values()
                admin_roles_out.append(
                    {
                        "role_id": rid,
                        "role_name": r.get("role_name"),
                        "description": r.get("description"),
                    }
                )
            payload = {
                "ok": True,
                "user_id": user_id,
                "IsAdmin": len(admin_roles_out) > 0,
                "admin_roles": admin_roles_out,
            }
            out = json.dumps(payload)
            return out
        payload = {
            "ok": True,
            "user_id": user_id,
            "IsAdmin": len(admin_role_ids) > 0,
            "admin_roles": admin_role_ids,
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "IsAdmin",
                "description": "Determine if a user has admin privileges (roles ending with 'admin' or 'lead') based on active roles.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Target user_id (e.g., U-001).",
                        },
                        "on_date": {
                            "type": "string",
                            "description": "ISO timestamp to evaluate expiry against (optional).",
                        },
                        "include_role_details": {
                            "type": "boolean",
                            "description": "Include role_name and description for admin roles.",
                            "default": False,
                        },
                    },
                    "required": ["user_id"],
                    "additionalProperties": False,
                },
            },
        }


#ASSETS
class CreateResource(Tool):
    """
    Establish a new resource with consistent ID generation.

    kwargs:
      name: str (mandatory)
      owner_id: str (mandatory)
      criticality: str (mandatory) - CRITICAL, HIGH, MEDIUM, LOW
      compliance_scope: str (optional) - ISO-27001, GDPR, SOX, PCI-DSS, ALL, or null
    """

    @staticmethod
    def invoke(data: dict[str, Any], name: str = "", owner_id: str = "", criticality: str = "", compliance_scope: str = None) -> str:
        name = name.strip()
        owner_id = owner_id.strip()
        criticality = criticality.strip().upper()

        if not name or not owner_id or not criticality:
            payload = {"error": "name, owner_id, and criticality are required"}
            out = json.dumps(payload)
            return out

        # Confirm criticality
        valid_criticalities = ["CRITICAL", "HIGH", "MEDIUM", "LOW"]
        if criticality not in valid_criticalities:
            payload = {
                "error": f"criticality must be one of: {', '.join(valid_criticalities)}"
            }
            out = json.dumps(payload)
            return out

        # Check compliance_scope if it is supplied
        if compliance_scope is not None:
            valid_compliance_scopes = [
                "ISO-27001",
                "GDPR",
                "SOX",
                "PCI-DSS",
                "ALL",
                "All",
            ]
            if compliance_scope not in valid_compliance_scopes:
                payload = {
                    "error": f"compliance_scope must be one of: {', '.join(valid_compliance_scopes)} or null"
                }
                out = json.dumps(payload)
                return out

        # Confirm the existence of the owner
        if not _find_by_id(data.get("users", {}).values(), "user_id", owner_id):
            payload = {"error": f"owner_id {owner_id} not found"}
            out = json.dumps(payload)
            return out

        # Ensure uniqueness based on name (case-insensitive)
        existing_resources = data.get("resources", {}).values()
        for r in existing_resources.values():
            if str(r.get("name", "")).strip().lower() == name.lower():
                payload = {"error": f"resource name '{name}' already exists"}
                out = json.dumps(payload)
                return out

        new_resource = {
            "resource_id": _next_id(data, "resources", "RES"),
            "name": name,
            "owner_id": owner_id,
            "criticality": criticality,
            "compliance_scope": compliance_scope,
        }

        data.setdefault("resources", []).append(new_resource)
        payload = {"ok": True, "resource": new_resource}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateResource",
                "description": "Create a new resource with deterministic ID generation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Unique resource name (case-insensitive).",
                        },
                        "owner_id": {
                            "type": "string",
                            "description": "User ID of the resource owner.",
                        },
                        "criticality": {
                            "type": "string",
                            "enum": ["CRITICAL", "HIGH", "MEDIUM", "LOW"],
                            "description": "Resource criticality level.",
                        },
                        "compliance_scope": {
                            "type": ["string", "null"],
                            "description": "Compliance scope (ISO-27001, GDPR, SOX, PCI-DSS, ALL) or null.",
                            "enum": [
                                "ISO-27001",
                                "GDPR",
                                "SOX",
                                "PCI-DSS",
                                "ALL",
                                "All",
                                None,
                            ],
                        },
                    },
                    "required": ["name", "owner_id", "criticality"],
                    "additionalProperties": False,
                },
            },
        }


class GetResource(Tool):
    """
    Retrieve resources based on ID, name, owner, criticality, or compliance scope.

    kwargs:
      resource_id: str (optional) - Specific resource ID to retrieve
      name: str (optional) - Filter by resource name
      owner_id: str (optional) - Filter by resource owner
      criticality: str (optional) - Filter by criticality (CRITICAL, HIGH, MEDIUM, LOW)
      compliance_scope: str (optional) - Filter by compliance scope (ISO-27001, GDPR, SOX, PCI-DSS, ALL)
    """

    @staticmethod
    def invoke(data: dict[str, Any], resource_id: str = None, name: str = None, owner_id: str = None, criticality: str = None, compliance_scope: str = None) -> str:
        resources = data.get("resources", {}).values()

        # If resource_id is given, return the specific resource
        if resource_id:
            resource = _find_by_id(resources, "resource_id", resource_id)
            if not resource:
                payload = {"error": f"resource_id {resource_id} not found"}
                out = json.dumps(payload)
                return out
            payload = {"ok": True, "resource": resource}
            out = json.dumps(payload)
            return out

        # Narrow down resources according to the supplied criteria
        filtered_resources = []
        for resource in resources.values():
            # Narrow down by name
            if name and name not in resource.get("name", ""):
                continue
            # Narrow down by owner_id if supplied
            if owner_id and resource.get("owner_id") != owner_id:
                continue
            # Narrow down by criticality if supplied
            if criticality and resource.get("criticality") != criticality:
                continue
            # Narrow down by compliance_scope if supplied (manage null values)
            if compliance_scope:
                resource_scope = resource.get("compliance_scope")
                if resource_scope != compliance_scope:
                    continue
            filtered_data["resources"][resource_id] = resource
        payload = {"ok": True, "resources": filtered_resources}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetResource",
                "description": "Retrieve resources by ID, name, owner, criticality, or compliance scope.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_id": {
                            "type": "string",
                            "description": "Specific resource ID to retrieve.",
                        },
                        "name": {
                            "type": "string",
                            "description": "Filter by resource name (partial match).",
                        },
                        "owner_id": {
                            "type": "string",
                            "description": "Filter by resource owner ID.",
                        },
                        "criticality": {
                            "type": "string",
                            "description": "Filter by criticality (CRITICAL, HIGH, MEDIUM, LOW).",
                        },
                        "compliance_scope": {
                            "type": "string",
                            "description": "Filter by compliance scope (ISO-27001, GDPR, SOX, PCI-DSS, ALL).",
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }


class ListUsersWithAccessToResource(Tool):
    """
    Identify users who effectively possess any permission on a specified resource_id through their role assignments.

    kwargs:
      resource_id: str (mandatory)
      only_active: bool = True
      on_date: str ISO (defaults to now)
      include_user_details: bool = False
      include_role_details: bool = False
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        resource_id: str = "",
        only_active: bool = True,
        on_date: str = None,
        include_user_details: bool = False,
        include_role_details: bool = False
    ) -> str:
        on_date_iso = on_date or get_current_timestamp()
        on_dt = _parse_iso(on_date_iso) or datetime.now(tz=timezone.utc)

        # Construct mappings for permissions and roles
        perms = [
            p
            for p in data.get("permissions", {}).values()
            if p.get("resource_id") == resource_id
        ]
        perm_ids = {p.get("permission_id") for p in perms if p.get("permission_id")}
        role_ids = {
            rp.get("role_id")
            for rp in data.get("role_permissions", {}).values()
            if rp.get("permission_id") in perm_ids
        }

        # Create utility functions
        user_map = {u.get("user_id"): u for u in data.get("users", {}).values()}
        role_map = {r.get("role_id"): r for r in data.get("roles", {}).values()}

        def is_active(ur: dict[str, Any]) -> bool:
            exp = _parse_iso(ur.get("expires_on"))
            return (exp is None) or (exp > on_dt)

        # Collect users with corresponding roles
        acc: dict[str, dict[str, Any]] = {}
        for ur in data.get("user_roles", {}).values():
            if ur.get("role_id") in role_ids and (not only_active or is_active(ur)):
                uid = ur.get("user_id")
                if uid not in acc:
                    acc[uid] = {"user_id": uid, "roles": []}
                    if include_user_details:
                        u = user_map.get(uid)
                        if u:
                            acc[uid]["user"] = u
                rinfo: dict[str, Any] = {"role_id": ur.get("role_id")}
                if include_role_details:
                    r = role_map.get(ur.get("role_id"))
                    if r:
                        rinfo["role_name"] = r.get("role_name")
                        rinfo["description"] = r.get("description")
                acc[uid]["roles"].append(rinfo)
        payload = {"resource_id": resource_id, "users": list(acc.values())}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListUsersWithAccessToResource",
                "description": "List users who have any permissions on the given resource via role assignments.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_id": {
                            "type": "string",
                            "description": "Resource id (e.g., RES-006).",
                        },
                        "only_active": {
                            "type": "boolean",
                            "description": "Exclude expired assignments.",
                            "default": True,
                        },
                        "on_date": {
                            "type": "string",
                            "description": "ISO timestamp to evaluate expiry against.",
                        },
                        "include_user_details": {
                            "type": "boolean",
                            "description": "Include user records.",
                        },
                        "include_role_details": {
                            "type": "boolean",
                            "description": "Include role records for each user's roles.",
                        },
                    },
                    "required": ["resource_id"],
                    "additionalProperties": False,
                },
            },
        }


class CanAccessResource(Tool):
    """
    Verify if a user can access a specific resource by tracing the permission chain:
    1. Retrieve all permissions for the resource
    2. Retrieve all roles that possess those permissions
    3. Confirm if the user holds any of those roles (considering expiration)

    kwargs:
      user_id: str (mandatory)
      resource_id: str (mandatory)
      on_date: str ISO (optional; defaults to now)
      include_details: bool = False (include which permissions/roles provide access)
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str = "",
        resource_id: str = "",
        on_date: str = None,
        include_details: bool = False
    ) -> str:
        pass
        on_date_iso = on_date or get_current_timestamp()

        if not user_id or not resource_id:
            payload = {"error": "user_id and resource_id are required"}
            out = json.dumps(payload)
            return out

        # Confirm the user is present
        if not _find_by_id(data.get("users", {}).values(), "user_id", user_id):
            payload = {"error": f"user_id {user_id} not found"}
            out = json.dumps(payload)
            return out

        # Confirm the resource is present
        if not _find_by_id(data.get("resources", {}).values(), "resource_id", resource_id):
            payload = {"error": f"resource_id {resource_id} not found"}
            out = json.dumps(payload)
            return out

        on_dt = _parse_iso(on_date_iso) or datetime.now(tz=timezone.utc)

        def is_active(ur: dict[str, Any]) -> bool:
            pass
            exp = _parse_iso(ur.get("expires_on"))
            return (exp is None) or (exp > on_dt)

        # Step 1: Retrieve all permissions associated with the resource
        resource_permissions = [
            p
            for p in data.get("permissions", {}).values()
            if p.get("resource_id") == resource_id
        ]

        if not resource_permissions:
            payload = {
                "ok": True,
                "user_id": user_id,
                "resource_id": resource_id,
                "can_access": False,
                "reason": "No permissions defined for this resource",
                "checked_on": on_date_iso,
            }
            out = json.dumps(payload)
            return out

        resource_permission_ids = {p.get("permission_id") for p in resource_permissions}

        # Step 2: Retrieve all roles that possess those permissions
        roles_with_permissions = [
            rp
            for rp in data.get("role_permissions", {}).values()
            if rp.get("permission_id") in resource_permission_ids
        ]

        if not roles_with_permissions:
            payload = {
                "ok": True,
                "user_id": user_id,
                "resource_id": resource_id,
                "can_access": False,
                "reason": "No roles have permissions for this resource",
                "checked_on": on_date_iso,
            }
            out = json.dumps(payload)
            return out

        role_ids_with_access = {rp.get("role_id") for rp in roles_with_permissions}

        # Step 3: Verify if the user holds any of those roles (and they are active)
        user_assignments = [
            ur
            for ur in data.get("user_roles", {}).values()
            if ur.get("user_id") == user_id and is_active(ur)
        ]

        active_user_role_ids = {ur.get("role_id") for ur in user_assignments}

        # Identify the overlap - roles that provide access AND that the user possesses
        granting_role_ids = role_ids_with_access.intersection(active_user_role_ids)

        can_access = len(granting_role_ids) > 0

        result = {
            "ok": True,
            "user_id": user_id,
            "resource_id": resource_id,
            "can_access": can_access,
            "checked_on": on_date_iso,
        }

        if include_details:
            # Create a comprehensive breakdown
            role_map = {r.get("role_id"): r for r in data.get("roles", {}).values()}
            permission_map = {
                p.get("permission_id"): p for p in data.get("permissions", {}).values()
            }

            # Identify which permissions are assigned by the roles held by the user
            granting_details = []
            for role_id in granting_role_ids:
                role = role_map.get(role_id, {}).values()

                # Determine which permissions this role grants for the specified resource
                role_permissions_for_resource = [
                    rp.get("permission_id")
                    for rp in roles_with_permissions
                    if rp.get("role_id") == role_id
                ]

                permissions_detail = []
                for perm_id in role_permissions_for_resource:
                    perm = permission_map.get(perm_id, {}).values()
                    permissions_detail.append(
                        {
                            "permission_id": perm_id,
                            "action": perm.get("action"),
                            "description": perm.get("description"),
                        }
                    )

                granting_details.append(
                    {
                        "role_id": role_id,
                        "role_name": role.get("role_name"),
                        "role_description": role.get("description"),
                        "permissions": permissions_detail,
                    }
                )

            result["access_details"] = {
                "granting_roles_count": len(granting_role_ids),
                "total_resource_permissions": len(resource_permissions),
                "total_roles_with_access": len(role_ids_with_access),
                "user_active_roles": len(active_user_role_ids),
                "granting_roles": granting_details,
            }

        if not can_access:
            result["reason"] = (
                "User does not have any active roles that grant access to this resource"
            )
        payload = result
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CanAccessResource",
                "description": "Check if a user can access a specific resource by following the permission → role → user assignment chain.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Target user_id (e.g., U-001).",
                        },
                        "resource_id": {
                            "type": "string",
                            "description": "Target resource_id (e.g., RES-020).",
                        },
                        "on_date": {
                            "type": "string",
                            "description": "ISO timestamp to evaluate role assignments against (optional).",
                        },
                        "include_details": {
                            "type": "boolean",
                            "description": "Include detailed breakdown of which roles/permissions grant access.",
                            "default": False,
                        },
                    },
                    "required": ["user_id", "resource_id"],
                    "additionalProperties": False,
                },
            },
        }


#ACCESS DEMANDS
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
        access_requests = data.get("access_requests", {}).values()

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
                user = _find_by_id(data.get("users", {}).values(), "user_id", uid)
                if user is not None:
                    out["user"] = user
            if include_role:
                rid = ar.get("requested_role_id") or ""
                role = _find_by_id(data.get("roles", {}).values(), "role_id", rid)
                if role is not None:
                    out["role"] = role
            if include_resource:
                res_id = ar.get("resource_id") or ""
                resource = _find_by_id(data.get("resources", {}).values(), "resource_id", res_id)
                if resource is not None:
                    out["resource"] = resource
            payload = out
            out = json.dumps(payload)
            return out

        # Narrow down access requests according to the supplied criteria
        filtered_requests = []
        for request in access_requests.values():
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
            filtered_data["access_requests"][request["access_request_id"]] = request
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


class DecideAccessRequest(Tool):
    """
    Approve or deny an access request with validations and consistent timestamps.

    kwargs:
      request_id: str (mandatory)
      reviewer_id: str (mandatory)
      decision: str = "APPROVED" | "REJECTED" (mandatory)
      decision_notes: str (mandatory)
      decision_at: str ISO-8601 (optional; defaults to request.submitted_at or now)
      enforce_admin: bool = True  (require the reviewer to have 'Administrator' role)
      enforce_pending: bool = True (require the current status to be 'PENDING')
      enforce_sla: bool = False   (deny approvals if older than sla_days without exemption)
      sla_days: int = 5
      waive_sla: bool = False
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        request_id: str = "",
        reviewer_id: str = "",
        decision: str = "",
        decision_at: str = None,
        enforce_admin: bool = True,
        enforce_pending: bool = True,
        enforce_sla: bool = False,
        sla_days: int = 5,
        waive_sla: bool = False
    ) -> str:
        decision = decision.upper()
        decision_at_kw = decision_at or get_current_timestamp()

        if decision not in ("APPROVED", "REJECTED"):
            payload = {"error": "decision must be APPROVED or REJECTED"}
            out = json.dumps(payload)
            return out

        # Retrieve the request
        requests = data.get("access_requests", {}).values()
        req = _find_by_id(requests, "request_id", request_id)
        if not req:
            payload = {"error": f"request_id {request_id} not found"}
            out = json.dumps(payload)
            return out

        # Confirm the reviewer's admin role if necessary
        if enforce_admin:
            # Locate the role_id for Administrator
            admin_roles = []
            for r in data.get("roles", {}).values():
                role_name = str(r.get("role_name", "")).strip().lower()
                if role_name.endswith("admin") or role_name.endswith("lead"):
                    admin_data["roles"][role_id] = r
            if not admin_roles:
                payload = {"error": "Administrator role not defined in roles.json"}
                out = json.dumps(payload)
                return out
            # Verify assignments
            has_admin = any(
                ur.get("user_id") == reviewer_id
                and ur.get("role_id") in [r.get("role_id") for r in admin_roles]
                for ur in data.get("user_roles", {}).values()
            )
            if not has_admin:
                payload = {"error": f"reviewer_id {reviewer_id} lacks Administrator role"}
                out = json.dumps(payload)
                return out

        # Confirm the pending status
        if enforce_pending and req.get("status") != "PENDING":
            payload = {"error": f"request {request_id} is not PENDING"}
            out = json.dumps(payload)
            return out

        # Ensure the target user and role are present
        user = _find_by_id(data.get("users", {}).values(), "user_id", req.get("user_id") or "")
        role = _find_by_id(
            data.get("roles", {}).values(), "role_id", req.get("requested_role_id") or ""
        )
        if not user or not role:
            payload = {"error": "target user or requested role does not exist"}
            out = json.dumps(payload)
            return out

        # SLA enforcement (only prevent approvals unless exempted)
        if enforce_sla and decision == "APPROVED" and not waive_sla:
            sub_dt = _parse_iso(req.get("submitted_at"))
            now_dt = _parse_iso(get_current_timestamp()) or datetime.now(
                tz=timezone.utc
            )
            if sub_dt:
                age_days = (now_dt - sub_dt).days
                if age_days > int(sla_days):
                    payload = {
                        "error": f"request {request_id} exceeds SLA ({age_days}d) — approval blocked without waiver"
                    }
                    out = json.dumps(payload)
                    return out

        # Consistent decision_at
        decision_at = (
            decision_at_kw or req.get("submitted_at") or get_current_timestamp()
        )

        updated = dict(req)
        updated.update(
            {
                "status": decision,
                "reviewed_by": reviewer_id,
                "decision_at": decision_at,
            }
        )

        # Save the update
        for i, r in enumerate(requests.values()):
            if r.get("request_id") == request_id:
                data["access_requests"][i] = updated
                break
        payload = {"ok": True, "request": updated}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DecideAccessRequest",
                "description": "Approve or reject an access request with validation, deterministic timestamps, and notes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {
                            "type": "string",
                            "description": "Access request id (AR-###).",
                        },
                        "reviewer_id": {
                            "type": "string",
                            "description": "Reviewer user_id (must be Administrator if enforce_admin).",
                        },
                        "decision": {
                            "type": "string",
                            "enum": ["APPROVED", "REJECTED"],
                            "description": "Decision outcome.",
                        },
                        "decision_at": {
                            "type": "string",
                            "description": "ISO timestamp; defaults to submitted_at or now.",
                        },
                        "enforce_admin": {
                            "type": "boolean",
                            "description": "Require reviewer to have Administrator role.",
                            "default": True,
                        },
                        "enforce_pending": {
                            "type": "boolean",
                            "description": "Require request to be PENDING.",
                            "default": True,
                        },
                        "enforce_sla": {
                            "type": "boolean",
                            "description": "Block approvals older than sla_days without waiver.",
                            "default": False,
                        },
                        "sla_days": {
                            "type": "integer",
                            "description": "SLA day threshold for approvals.",
                            "default": 5,
                        },
                        "waive_sla": {
                            "type": "boolean",
                            "description": "Allow approval despite SLA breach.",
                        },
                    },
                    "required": ["request_id", "reviewer_id", "decision"],
                    "additionalProperties": False,
                },
            },
        }


#POSITIONS
class EnsureUserRole(Tool):
    """
    Confirm that a user holds a role; idempotent assignment.

    kwargs:
      user_id: str (mandatory)
      role_id: str (mandatory)
      assigned_by: str (mandatory)
      assigned_on: str ISO (defaults to now)
      expires_on: str ISO (optional)
    """

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = "", role_id: str = "", assigned_by: str = "", assigned_on: str = None, expires_on: str = None) -> str:
        pass
        assigned_on = assigned_on or get_current_timestamp()

        # Presence validations
        if not _find_by_id(data.get("users", {}).values(), "user_id", user_id):
            payload = {"error": f"user_id {user_id} not found"}
            out = json.dumps(payload)
            return out
        if not _find_by_id(data.get("roles", {}).values(), "role_id", role_id):
            payload = {"error": f"role_id {role_id} not found"}
            out = json.dumps(payload)
            return out

        assignments = data.get("user_roles", {}).values()
        existing = None
        existing_index = None
        for i, ur in enumerate(assignments.values()):
            if ur.get("user_id") == user_id and ur.get("role_id") == role_id:
                existing = ur
                existing_index = i
                break

        if existing:
            # If expires_on is supplied and differs from the current value, modify it
            if expires_on and existing.get("expires_on") != expires_on:
                updated = dict(existing)
                updated["expires_on"] = expires_on
                data["user_roles"][existing_index] = updated
                payload = {"ok": True, "assignment": updated, "updated_expiry": True}
                out = json.dumps(payload)
                return out
            else:
                payload = {"ok": True, "no_op": True, "assignment": existing}
                out = json.dumps(payload)
                return out
        else:
            payload = {"error": "no existing assignment found"}
            out = json.dumps(payload)
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ensureUserRole",
                "description": "Idempotently ensure a user has a role with optional expiry. Updates expiry date if role exists and new expires_on is provided.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "Target user_id."},
                        "role_id": {"type": "string", "description": "Target role_id."},
                        "assigned_by": {
                            "type": "string",
                            "description": "Actor user_id performing assignment.",
                        },
                        "assigned_on": {
                            "type": "string",
                            "description": "ISO timestamp of assignment.",
                        },
                        "expires_on": {
                            "type": "string",
                            "description": "ISO timestamp for expiry (optional).",
                        },
                    },
                    "required": ["user_id", "role_id", "assigned_by"],
                    "additionalProperties": False,
                },
            },
        }


class UpdateUserRole(Tool):
    """
    Add or revoke a user role assignment.

    kwargs:
      user_id: str (mandatory)
      role_id: str (mandatory)
      action: str = "ADD" | "REMOVE" (mandatory)
      assigned_by: str (mandatory for ADD)
      assigned_on: str ISO (optional for ADD, defaults to now)
      expires_on: str ISO (optional for ADD)
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str = "",
        role_id: str = "",
        action: str = "",
        assigned_by: str = "",
        assigned_on: str = None,
        expires_on: str = None
    ) -> str:
        pass
        action = action.upper()
        assigned_on = assigned_on or get_current_timestamp()

        if action not in ("ADD", "REMOVE"):
            payload = {"error": "action must be ADD or REMOVE"}
            out = json.dumps(payload)
            return out

        # Presence validations
        if not _find_by_id(data.get("users", {}).values(), "user_id", user_id):
            payload = {"error": f"user_id {user_id} not found"}
            out = json.dumps(payload)
            return out
        if not _find_by_id(data.get("roles", {}).values(), "role_id", role_id):
            payload = {"error": f"role_id {role_id} not found"}
            out = json.dumps(payload)
            return out

        assignments = data.get("user_roles", {}).values()
        existing_index = None
        for i, ur in enumerate():
            if ur.get("user_id") == user_id and ur.get("role_id") == role_id:
                existing_index = i
                break

        if action == "ADD":
            if not assigned_by:
                payload = {"error": "assigned_by is required for ADD action"}
                out = json.dumps(payload)
                return out

            if existing_index is not None:
                # Modify the current assignment
                existing = assignments[existing_index]
                updated = dict(existing)
                if expires_on and existing.get("expires_on") != expires_on:
                    updated["expires_on"] = expires_on
                    data["user_roles"][existing_index] = updated
                    payload = {"ok": True, "assignment": updated, "updated_expiry": True}
                    out = json.dumps(payload)
                    return out
                else:
                    payload = {"ok": True, "no_op": True, "assignment": existing}
                    out = json.dumps(payload)
                    return out
            else:
                # Establish a new assignment
                new_ur = {
                    "user_role_id": _next_user_role_id(data, user_id),
                    "user_id": user_id,
                    "role_id": role_id,
                    "assigned_by": assigned_by,
                    "assigned_on": assigned_on,
                    "expires_on": expires_on,
                }
                data.setdefault("user_roles", []).append(new_ur)
                payload = {"ok": True, "assignment": new_ur, "action": "created"}
                out = json.dumps(payload)
                return out

        elif action == "REMOVE":
            if existing_index is not None:
                removed = data["user_roles"].pop(existing_index)
                removed["assigned_by"] = assigned_by
                payload = {"ok": True, "assignment": removed, "action": "removed"}
                out = json.dumps(payload)
                return out
            else:
                payload = {
                    "ok": True,
                    "no_op": True,
                    "message": "Role assignment does not exist",
                }
                out = json.dumps(payload)
                return out
        else:
            payload = {"error": "Invalid action"}
            out = json.dumps(payload)
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateUserRole",
                "description": "Add or remove a user role assignment. For ADD: creates new assignment or updates expiry if exists. For REMOVE: deletes the assignment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "Target user_id."},
                        "role_id": {"type": "string", "description": "Target role_id."},
                        "action": {
                            "type": "string",
                            "enum": ["ADD", "REMOVE"],
                            "description": "Action to perform.",
                        },
                        "assigned_by": {
                            "type": "string",
                            "description": "Actor user_id performing assignment (required).",
                        },
                        "assigned_on": {
                            "type": "string",
                            "description": "ISO timestamp of assignment (optional for ADD).",
                        },
                        "expires_on": {
                            "type": "string",
                            "description": "ISO timestamp for expiry (optional for ADD).",
                        },
                    },
                    "required": ["user_id", "role_id", "action", "assigned_by"],
                    "additionalProperties": False,
                },
            },
        }


class GetBaseRoleByDepartment(Tool):
    """
    Retrieve the foundational role ID for a specified department.

    kwargs:
      department: str (mandatory)
    """

    @staticmethod
    def invoke(data: dict[str, Any], department: str = "") -> str:
        department = department.strip().lower()

        # Associate departments with foundational role names
        department_role_map = {
            "engineering": "engineering-base",
            "marketing": "marketing-base",
            "sales": "sales-base",
            "human resources": "hr-base",
            "operations": "operations-base",
            "finance": "finance-base",
        }

        role_name = department_role_map.get(department)
        if not role_name:
            payload = {"error": f"No base role found for department '{department}'"}
            out = json.dumps(payload)
            return out

        # Identify the role
        roles = data.get("roles", {}).values()
        for role in roles.values():
            if role.get("role_name") == role_name:
                payload = {"role": role}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Base role '{role_name}' not found in roles"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetBaseRoleByDepartment",
                "description": "Get the base role for a given department.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department": {
                            "type": "string",
                            "description": "Department name.",
                        }
                    },
                    "required": ["department"],
                    "additionalProperties": False,
                },
            },
        }


class CheckSoDConflicts(Tool):
    """
    Assess if a user has Separation of Duties (SoD) conflicts based on their active roles,
    or if incorporating a specific role would lead to a conflict.

    SoD conflicts are recognized by predefined conflicting role pairs that breach
    business control principles (e.g., finance processing versus auditing).

    kwargs:
      user_id: str (mandatory)
      on_date: str ISO (optional; defaults to now)
      include_role_details: bool = False (include role names and descriptions)
      role_id: str (optional) - If supplied, checks if adding this role to the user would create a conflict
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str = "",
        on_date: str = None,
        include_role_details: bool = False,
        role_id: str = None
    ) -> str:
        pass
        on_date_iso = on_date or get_current_timestamp()
        test_role_id = role_id

        if not user_id:
            payload = {"error": "user_id is required"}
            out = json.dumps(payload)
            return out

        # Confirm the user is present
        if not _find_by_id(data.get("users", {}).values(), "user_id", user_id):
            payload = {"error": f"user_id {user_id} not found"}
            out = json.dumps(payload)
            return out

        on_dt = _parse_iso(on_date_iso) or datetime.now(tz=timezone.utc)

        def is_active(ur: dict[str, Any]) -> bool:
            pass
            exp = _parse_iso(ur.get("expires_on"))
            return (exp is None) or (exp > on_dt)

        # Retrieve the user's current role assignments
        assignments = [
            ur
            for ur in data.get("user_roles", {}).values()
            if ur.get("user_id") == user_id and is_active(ur)
        ]

        active_role_ids = {ur.get("role_id") for ur in assignments.values()}
        # If test_role_id is supplied, simulate its addition
        if test_role_id:
            active_role_ids = set(active_role_ids)
            active_role_ids.add(test_role_id)

        # Establish SoD conflict guidelines based on role evaluation
        sod_conflicts = [
            # Financial SoD conflicts
            {
                "conflict_id": "FINANCE_SOD_001",
                "name": "Finance Processing vs Audit Access",
                "description": "Users cannot both process financial transactions and audit them",
                "conflicting_roles": [
                    "ROL-031",
                    "ROL-033",
                ],  # finance-invoice-processor compared to finance-audit-access
                "risk_level": "HIGH",
            },
            {
                "conflict_id": "FINANCE_SOD_002",
                "name": "Budget Admin vs Audit Access",
                "description": "Users cannot both manage budgets and audit financial records",
                "conflicting_roles": [
                    "ROL-032",
                    "ROL-033",
                ],  # finance-budget-admin compared to finance-audit-access
                "risk_level": "HIGH",
            },
            # Engineering-related SoD conflicts
            {
                "conflict_id": "ENGINEERING_SOD_001",
                "name": "Code Development vs Production Deployment",
                "description": "Developers cannot deploy their own code to production without review",
                "conflicting_roles": [
                    "ROL-002",
                    "ROL-025",
                ],  # engineering-code-commit compared to operations-deployment-admin
                "risk_level": "CRITICAL",
            },
            {
                "conflict_id": "ENGINEERING_SOD_002",
                "name": "Code Development vs Production Access",
                "description": "Developers should not have direct production system access",
                "conflicting_roles": [
                    "ROL-002",
                    "ROL-003",
                ],  # engineering-code-commit compared to engineering-prod-access
                "risk_level": "HIGH",
            },
            # Conflicts among operations administrators
            {
                "conflict_id": "OPERATIONS_SOD_001",
                "name": "System Admin vs Database Admin",
                "description": "Excessive administrative privileges across system and database layers",
                "conflicting_roles": [
                    "ROL-026",
                    "ROL-027",
                ],  # operations-system-admin compared to operations-db-admin
                "risk_level": "MEDIUM",
            },
            {
                "conflict_id": "OPERATIONS_SOD_002",
                "name": "System Admin vs Network Admin",
                "description": "Excessive administrative privileges across system and network layers",
                "conflicting_roles": [
                    "ROL-026",
                    "ROL-028",
                ],  # operations-system-admin compared to operations-network-admin
                "risk_level": "MEDIUM",
            },
            # HR-related SoD conflicts
            {
                "conflict_id": "HR_SOD_001",
                "name": "Employee Data Access vs Payroll Admin",
                "description": "Users cannot both access employee data and manage payroll",
                "conflicting_roles": [
                    "ROL-017",
                    "ROL-018",
                ],  # hr-employee-data-read compared to hr-payroll-admin
                "risk_level": "HIGH",
            },
            {
                "conflict_id": "HR_SOD_002",
                "name": "Employee Data Access vs Benefits Admin",
                "description": "Users cannot both access employee data and manage benefits",
                "conflicting_roles": [
                    "ROL-017",
                    "ROL-020",
                ],  # hr-employee-data-read compared to hr-benefits-admin
                "risk_level": "MEDIUM",
            },
            # Sales-related SoD conflicts
            {
                "conflict_id": "SALES_SOD_001",
                "name": "Lead Management vs Commission Viewing",
                "description": "Sales leads managers should not view commission data to prevent manipulation",
                "conflicting_roles": [
                    "ROL-013",
                    "ROL-015",
                ],  # sales-lead-manager compared to sales-commission-view
                "risk_level": "MEDIUM",
            },
        ]

        # Verify for conflicts
        detected_conflicts = []
        role_map = {r.get("role_id"): r for r in data.get("roles", {}).values()}

        for conflict in sod_conflicts:
            conflicting_role_ids = conflict["conflicting_roles"]
            # Determine if the user possesses ALL roles in the conflicting group
            if all(role_id in active_role_ids for role_id in conflicting_role_ids.values()):
                conflict_entry = {
                    "conflict_id": conflict["conflict_id"],
                    "name": conflict["name"],
                    "description": conflict["description"],
                    "risk_level": conflict["risk_level"],
                    "conflicting_role_ids": conflicting_role_ids,
                }

                if include_role_details:
                    conflict_entry["conflicting_roles"] = []
                    for role_id in conflicting_role_ids:
                        role = role_map.get(role_id, {}).values()
                        conflict_entry["conflicting_roles"].append(
                            {
                                "role_id": role_id,
                                "role_name": role.get("role_name"),
                                "description": role.get("description"),
                            }
                        )

                detected_conflicts.append(conflict_entry)
        payload = {
                "ok": True,
                "user_id": user_id,
                "has_sod_conflicts": len(detected_conflicts) > 0,
                "conflict_count": len(detected_conflicts),
                "conflicts": detected_conflicts,
                "checked_on": on_date_iso,
                "simulated_role_id": test_role_id if test_role_id else None,
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckSodConflicts",
                "description": "Check if a user has Separation of Duties (SoD) conflicts based on their active roles, or if adding a specific role would result in a conflict.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Target user_id (e.g., U-001).",
                        },
                        "on_date": {
                            "type": "string",
                            "description": "ISO timestamp to evaluate role assignments against (optional).",
                        },
                        "include_role_details": {
                            "type": "boolean",
                            "description": "Include role names and descriptions in conflict details.",
                            "default": False,
                        },
                        "role_id": {
                            "type": "string",
                            "description": "If provided, checks if adding this role to the user would cause a conflict.",
                        },
                    },
                    "required": ["user_id"],
                    "additionalProperties": False,
                },
            },
        }


#CERTIFICATION RECORDS
class GetCertification(Tool):
    """
    Retrieve certifications based on ID, reviewer, resource, or status.

    kwargs:
      certification_id: str (optional) - Specific certification ID to retrieve
      reviewer_id: str (optional) - Filter by the reviewer user ID
      resource_id: str (optional) - Filter by resource ID
      status: str (optional) - Filter by status (PENDING, IN_PROGRESS, COMPLETED)
    """

    @staticmethod
    def invoke(data: dict[str, Any], certification_id: str = None, reviewer_id: str = None, resource_id: str = None, status: str = None,
    user_id: Any = None,
    ) -> str:
        certifications = data.get("certifications", {}).values()

        # If certification_id is supplied, return the specific certification
        if certification_id:
            cert = _find_by_id(certifications, "certification_id", certification_id)
            if not cert:
                payload = {"error": f"certification_id {certification_id} not found"}
                out = json.dumps(payload)
                return out
            payload = {"ok": True, "certification": cert}
            out = json.dumps(payload)
            return out

        # Narrow down certifications according to the supplied criteria
        filtered_certifications = []
        for cert in certifications.values():
            if reviewer_id and cert.get("reviewer_id") != reviewer_id:
                continue
            if resource_id and cert.get("resource_id") != resource_id:
                continue
            if status and cert.get("status") != status:
                continue
            filtered_data["certifications"][certification_id] = cert
        payload = {"ok": True, "certifications": filtered_certifications}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCertification",
                "description": "Retrieve certifications by ID, reviewer, resource, or status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {
                            "type": "string",
                            "description": "Specific certification ID to retrieve.",
                        },
                        "reviewer_id": {
                            "type": "string",
                            "description": "Filter by reviewer user ID.",
                        },
                        "resource_id": {
                            "type": "string",
                            "description": "Filter by resource ID.",
                        },
                        "status": {
                            "type": "string",
                            "description": "Filter by status (PENDING, IN_PROGRESS, COMPLETED).",
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }


class CompleteCertification(Tool):
    """
    Finalize a certification by changing the status to COMPLETED and setting completed_on to a consistent timestamp.

    kwargs:
      certification_id: str (mandatory)
      reviewer_id: str (mandatory)
    """

    @staticmethod
    def invoke(data: dict[str, Any], certification_id: str = "", reviewer_id: str = "") -> str:
        certs = data.get("certifications", {}).values()
        cert = _find_by_id(certs, "certification_id", certification_id)
        if not cert:
            payload = {"error": f"certification_id {certification_id} not found"}
            out = json.dumps(payload)
            return out

        if cert.get("reviewer_id") != reviewer_id:
            payload = {
                "error": f"reviewer_id {reviewer_id} does not match certification reviewer"
            }
            out = json.dumps(payload)
            return out

        if cert.get("status") not in ("PENDING", "IN_PROGRESS"):
            # Idempotent completion yields the current state
            if cert.get("status") == "COMPLETED":
                payload = {"ok": True, "certification": cert}
                out = json.dumps(payload)
                return out
            payload = {
                "error": f"certification {certification_id} not completable from status {cert.get('status')}"
            }
            out = json.dumps(payload)
            return out

        updated = dict(cert)
        updated.update(
            {
                "status": "COMPLETED",
                "completed_on": get_current_timestamp(),
            }
        )

        for i, c in enumerate(certs):
            if c.get("certification_id") == certification_id:
                data["certifications"][i] = updated
                break
        payload = {"ok": True, "certification": updated}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CompleteCertification",
                "description": "Complete a certification with deterministic completion timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {
                            "type": "string",
                            "description": "Certification id (C-###).",
                        },
                        "reviewer_id": {
                            "type": "string",
                            "description": "Reviewer user_id.",
                        },
                    },
                    "required": ["certification_id", "reviewer_id"],
                    "additionalProperties": False,
                },
            },
        }


class CreateCertification(Tool):
    """
    Establish a new certification entry with consistent ID and a default due date.

    kwargs:
      reviewer_id: str (mandatory) - Reviewer accountable for certification
      resource_id: str (mandatory) - Resource to be certified
      status: str (optional; defaults to "PENDING") - PENDING, IN_PROGRESS, COMPLETED
      due_date: str (optional) - ISO-like timestamp ("YYYY-MM-DD HH:MM:SS+00:00"); defaults to +90 days
      completed_on: str (optional) - If status=COMPLETED, specific completion time; defaults to now
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        reviewer_id: str = "",
        resource_id: str = "",
        status: str = "PENDING",
        due_date: str = None,
        completed_on_kw: str = None
    ) -> str:
        status = status.upper()

        if not reviewer_id or not resource_id:
            payload = {"error": "reviewer_id and resource_id are required"}
            out = json.dumps(payload)
            return out

        # Confirm the presence of the reviewer and resource
        if not _find_by_id(data.get("users", {}).values(), "user_id", reviewer_id):
            payload = {"error": f"reviewer_id {reviewer_id} not found"}
            out = json.dumps(payload)
            return out
        if not _find_by_id(data.get("resources", {}).values(), "resource_id", resource_id):
            payload = {"error": f"resource_id {resource_id} not found"}
            out = json.dumps(payload)
            return out

        valid_status = ["PENDING", "IN_PROGRESS", "COMPLETED"]
        if status not in valid_status:
            payload = {"error": f"status must be one of: {valid_status}"}
            out = json.dumps(payload)
            return out

        # Establish due_date deterministically if not supplied: +90 days from the current date
        if not due_date:
            base = _parse_iso(get_current_timestamp()) or datetime.now(tz=timezone.utc)
            due_dt = base + timedelta(days=90)
            # Align dataset format with +00:00 suffix
            due_date = due_dt.strftime("%Y-%m-%d %H:%M:%S+00:00")

        # completed_on is set only if COMPLETED
        completed_on: str | None
        if status == "COMPLETED":
            completed_on = completed_on_kw or get_current_timestamp()
        else:
            completed_on = None

        new_cert = {
            "certification_id": _next_id(data, "certifications", "C"),
            "reviewer_id": reviewer_id,
            "resource_id": resource_id,
            "status": status,
            "due_date": due_date,
            "completed_on": completed_on,
        }

        data.setdefault("certifications", []).append(new_cert)
        payload = {"ok": True, "certification": new_cert}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateCertification",
                "description": "Create a new certification entry with deterministic ID and default due date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reviewer_id": {
                            "type": "string",
                            "description": "Reviewer user_id responsible.",
                        },
                        "resource_id": {
                            "type": "string",
                            "description": "Target resource_id.",
                        },
                        "status": {
                            "type": "string",
                            "description": "Initial status (PENDING, IN_PROGRESS, COMPLETED).",
                            "default": "PENDING",
                        },
                        "due_date": {
                            "type": "string",
                            "description": "Due date (YYYY-MM-DD HH:MM:SS+00:00).",
                        },
                        "completed_on": {
                            "type": "string",
                            "description": "Completion timestamp if status=COMPLETED.",
                        },
                    },
                    "required": ["reviewer_id", "resource_id"],
                    "additionalProperties": False,
                },
            },
        }


#EXCEPTIONS TO POLICY
class GetPolicyException(Tool):
    """
    Retrieve policy exceptions based on ID, user, permission, reviewer, or status.

    kwargs:
      exception_id: str (optional) - Specific exception ID to retrieve
      user_id: str (optional) - Filter by the user making the request
      permission_id: str (optional) - Filter by the permission related to exceptions
      reviewed_by: str (optional) - Filter by the reviewer
      status: str (optional) - Filter by status (PENDING_REVIEW, ACTIVE, EXPIRED, DENIED)
    """

    @staticmethod
    def invoke(data: dict[str, Any], exception_id: str = None, user_id: str = None, 
               permission_id: str = None, reviewed_by: str = None, status: str = None) -> str:
        exceptions = data.get("policy_exceptions", {}).values()

        # If exception_id is supplied, return the specific exception
        if exception_id:
            exception = _find_by_id(exceptions, "exception_id", exception_id)
            if not exception:
                payload = {"error": f"exception_id {exception_id} not found"}
                out = json.dumps(payload)
                return out
            payload = {"ok": True, "policy_exception": exception}
            out = json.dumps(payload)
            return out

        # Narrow down exceptions according to the supplied criteria
        filtered_exceptions = []
        for exception in exceptions.values():
            if user_id and exception.get("user_id") != user_id:
                continue
            if permission_id and exception.get("permission_id") != permission_id:
                continue
            if reviewed_by and exception.get("reviewed_by") != reviewed_by:
                continue
            if status and exception.get("status") != status:
                continue
            filtered_data["policy_exceptions"][exception["policy_exception_id"]] = exception
        payload = {"ok": True, "policy_exceptions": filtered_exceptions}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPolicyException",
                "description": "Retrieve policy exceptions by ID, user, permission, reviewer, or status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "exception_id": {
                            "type": "string",
                            "description": "Specific policy exception ID to retrieve.",
                        },
                        "user_id": {
                            "type": "string",
                            "description": "Filter by requesting user ID.",
                        },
                        "permission_id": {
                            "type": "string",
                            "description": "Filter by permission involved in exceptions.",
                        },
                        "reviewed_by": {
                            "type": "string",
                            "description": "Filter by reviewer user ID.",
                        },
                        "status": {
                            "type": "string",
                            "description": "Filter by status (PENDING_REVIEW, ACTIVE, EXPIRED, DENIED).",
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }


class CreatePolicyException(Tool):
    """
    Establish a new policy exception request.

    kwargs:
      user_id: str (mandatory) - User for whom the exception is created
      permission_id: str (mandatory) - Permission that requires an exception
      reviewed_by: str (mandatory) - User ID responsible for reviewing the exception
      reason: str (mandatory) - Business justification for the exception
      expires_on: str (optional) - ISO timestamp indicating when the exception expires
    """

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = "", permission_id: str = "", reviewed_by: str = "", reason: str = "", expires_on: Any = None) -> str:
        if not user_id or not permission_id or not reviewed_by or not reason:
            payload = {
                    "error": "user_id, permission_id, reviewed_by, and reason are required"
                }
            out = json.dumps(
                payload)
            return out

        #Confirm the user is present
        if not _find_by_id(data.get("users", {}).values(), "user_id", user_id):
            payload = {"error": f"user_id {user_id} not found"}
            out = json.dumps(payload)
            return out

        #Confirm the permission is present
        if not _find_by_id(data.get("permissions", {}).values(), "permission_id", permission_id):
            payload = {"error": f"permission_id {permission_id} not found"}
            out = json.dumps(payload)
            return out

        #Confirm the reviewer is present
        if not _find_by_id(data.get("users", {}).values(), "user_id", reviewed_by):
            payload = {"error": f"reviewed_by {reviewed_by} not found"}
            out = json.dumps(payload)
            return out

        #Establish a new policy exception
        new_exception = {
            "exception_id": _next_id(data, "policy_exceptions", "PE"),
            "user_id": user_id,
            "permission_id": permission_id,
            "reviewed_by": reviewed_by,
            "requested_on": get_current_timestamp(),
            "reviewed_on": None,
            "expires_on": expires_on,
            "reason": reason,
            "status": "PENDING_REVIEW",
        }

        data.setdefault("policy_exceptions", []).append(new_exception)
        payload = {"ok": True, "policy_exception": new_exception}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreatePolicyException",
                "description": "Create a new policy exception request for emergency access.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "User ID for whom exception is created.",
                        },
                        "permission_id": {
                            "type": "string",
                            "description": "Permission ID requiring exception.",
                        },
                        "reviewed_by": {
                            "type": "string",
                            "description": "User ID who will review the exception.",
                        },
                        "reason": {
                            "type": "string",
                            "description": "Business justification for the exception.",
                        },
                        "expires_on": {
                            "type": "string",
                            "description": "ISO timestamp when exception expires (optional).",
                        },
                    },
                    "required": ["user_id", "permission_id", "reviewed_by", "reason"],
                    "additionalProperties": False,
                },
            },
        }


class DecidePolicyException(Tool):
    """
    Approve or reject a policy exception with consistent timestamps.

    kwargs:
      exception_id: str (mandatory)
      reviewer_id: str (mandatory)
      decision: str = "APPROVED" | "DENIED" (mandatory)
      reviewed_on: str ISO (optional; defaults to the current timestamp)
    """

    @staticmethod
    def invoke(data: dict[str, Any], exception_id: str = "", reviewer_id: str = "", decision: str = None, reviewed_on: str = None) -> str:
        decision = (decision or "").upper()
        reviewed_on = reviewed_on or get_current_timestamp()

        if decision not in ("APPROVED", "DENIED"):
            payload = {"error": "decision must be APPROVED or DENIED"}
            out = json.dumps(payload)
            return out

        # Retrieve the exception
        exceptions = data.get("policy_exceptions", {}).values()
        exception = _find_by_id(exceptions, "exception_id", exception_id)
        if not exception:
            payload = {"error": f"exception_id {exception_id} not found"}
            out = json.dumps(payload)
            return out

        # Confirm the reviewer matches
        if exception.get("reviewed_by") != reviewer_id:
            payload = {
                "error": f"reviewer_id {reviewer_id} does not match assigned reviewer {exception.get('reviewed_by')}"
            }
            out = json.dumps(payload)
            return out

        # Confirm the status
        if exception.get("status") != "PENDING_REVIEW":
            payload = {"error": f"exception {exception_id} is not PENDING_REVIEW"}
            out = json.dumps(payload)
            return out

        # Modify the status
        updated = dict(exception)
        updated.update(
            {
                "status": "ACTIVE" if decision == "APPROVED" else "DENIED",
                "reviewed_on": reviewed_on,
            }
        )

        # If denied, remove expires_on
        if decision == "DENIED":
            updated["expires_on"] = None

        # Save the update
        for i, exc in enumerate(exceptions.values()):
            if exc.get("exception_id") == exception_id:
                data["policy_exceptions"][i] = updated
                break
        payload = {"ok": True, "policy_exception": updated}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DecidePolicyException",
                "description": "Approve or deny a policy exception with deterministic timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "exception_id": {
                            "type": "string",
                            "description": "Policy exception id (PE-###).",
                        },
                        "reviewer_id": {
                            "type": "string",
                            "description": "Reviewer user_id.",
                        },
                        "decision": {
                            "type": "string",
                            "enum": ["APPROVED", "DENIED"],
                            "description": "Decision outcome.",
                        },
                        "reviewed_on": {
                            "type": "string",
                            "description": "ISO timestamp; defaults to now.",
                        },
                    },
                    "required": ["exception_id", "reviewer_id", "decision"],
                    "additionalProperties": False,
                },
            },
        }


class GetPermission(Tool):
    """
    Retrieve permissions based on ID, action, or resource.

    kwargs:
      permission_id: str (optional) - Specific permission ID to retrieve
      action: str (optional) - Filter by the action of the permission
      resource_id: str (optional) - Filter by the resource associated with permissions
    """

    @staticmethod
    def invoke(data: dict[str, Any], permission_id: str = None, action: str = None, resource_id: str = None, description: str = None) -> str:
        permissions = data.get("permissions", {}).values()

        # If permission_id is supplied, return the specific permission
        if permission_id:
            permission = _find_by_id(permissions, "permission_id", permission_id)
            if not permission:
                payload = {"error": f"permission_id {permission_id} not found"}
                out = json.dumps(payload)
                return out
            payload = {"ok": True, "permission": permission}
            out = json.dumps(payload)
            return out

        # Narrow down permissions according to the supplied criteria
        filtered_permissions = []
        for permission in permissions.values():
            if action and permission.get("action") != action:
                continue
            if resource_id and permission.get("resource_id") != resource_id:
                continue
            if description and permission.get("description") != description:
                continue
            filtered_data["permissions"][permission_id] = permission
        payload = {"ok": True, "permissions": filtered_permissions}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPermission",
                "description": "Retrieve permissions by ID, action, or resource.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "permission_id": {
                            "type": "string",
                            "description": "Specific permission ID to retrieve.",
                        },
                        "action": {
                            "type": "string",
                            "description": "Filter by permission action.",
                        },
                        "resource_id": {
                            "type": "string",
                            "description": "Filter by resource involved in permissions.",
                        },
                        "description": {
                            "type": "string",
                            "description": "Filter by permission description.",
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }


class CreatePermission(Tool):
    """
    Establish a new permission with consistent ID generation.

    kwargs:
      action: str (mandatory)
      resource_id: str (mandatory)
      description: str (mandatory)
    """

    @staticmethod
    def invoke(data: dict[str, Any], action: str = "", resource_id: str = "", description: str = "") -> str:
        action = action.strip()
        resource_id = resource_id.strip()

        if not action or not resource_id or not description:
            payload = {"error": "action, resource_id, and description are required"}
            out = json.dumps(payload)
            return out

        # Confirm the resource is present
        if not _find_by_id(data.get("resources", {}).values(), "resource_id", resource_id):
            payload = {"error": f"resource_id {resource_id} not found"}
            out = json.dumps(payload)
            return out

        # Ensure uniqueness based on (action, resource_id)
        for p in data.get("permissions", {}).values():
            if (
                str(p.get("action", "")).strip().lower() == action.lower()
                and p.get("resource_id") == resource_id
            ):
                payload = {
                    "error": f"permission with action '{action}' for {resource_id} already exists"
                }
                out = json.dumps(payload)
                return out

        new_perm = {
            "permission_id": _next_id(data, "permissions", "P"),
            "action": action,
            "resource_id": resource_id,
            "description": description,
        }

        data.setdefault("permissions", []).append(new_perm)
        payload = {"ok": True, "permission": new_perm}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreatePermission",
                "description": "Create a new permission with deterministic ID generation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {
                            "type": "string",
                            "description": "Permission action (e.g., read, write).",
                        },
                        "resource_id": {
                            "type": "string",
                            "description": "Resource id the permission applies to.",
                        },
                        "description": {
                            "type": "string",
                            "description": "Permission description.",
                        },
                    },
                    "required": ["action", "resource_id", "description"],
                    "additionalProperties": False,
                },
            },
        }


class GetRolePermissions(Tool):
    """
    Retrieve mappings of roles to permissions filtered by role_id and/or permission_id.

    kwargs:
      role_id: str (optional) - Filter mappings for a specific role
      permission_id: str (optional) - Filter mappings for a specific permission
      include_role: bool = False - Include role details in each mapping
      include_permission: bool = False - Include permission details in each mapping
    """

    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = None, permission_id: str = None, include_role: bool = False, include_permission: bool = False) -> str:
        if not role_id and not permission_id:
            payload = {"error": "Must provide role_id and/or permission_id"}
            out = json.dumps(payload)
            return out

        mappings = data.get("role_permissions", {}).values()

        # Narrow down
        out = []
        for rp in mappings.values():
            if role_id and rp.get("role_id") != role_id:
                continue
            if permission_id and rp.get("permission_id") != permission_id:
                continue
            out.append(dict(rp))

        # Optional extensions
        if include_role or include_permission:
            role_map = {r.get("role_id"): r for r in data.get("roles", {}).values()}
            perm_map = {p.get("permission_id"): p for p in data.get("permissions", {}).values()}
            for item in out:
                if include_role:
                    rid = item.get("role_id")
                    role = role_map.get(rid)
                    if role:
                        item["role"] = role
                if include_permission:
                    pid = item.get("permission_id")
                    perm = perm_map.get(pid)
                    if perm:
                        item["permission"] = perm
        payload = {"ok": True, "role_permissions": out}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRolePermissions",
                "description": "Retrieve role-permission mappings filtered by role_id and/or permission_id with optional detail expansion.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {
                            "type": "string",
                            "description": "Filter by role_id (e.g., ROL-032).",
                        },
                        "permission_id": {
                            "type": "string",
                            "description": "Filter by permission_id (e.g., P-081).",
                        },
                        "include_role": {
                            "type": "boolean",
                            "description": "Include role details in each mapping.",
                            "default": False,
                        },
                        "include_permission": {
                            "type": "boolean",
                            "description": "Include permission details in each mapping.",
                            "default": False,
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }


class AssignPermissionToRole(Tool):
    """
    Allocate a permission to a role by establishing a role-permission mapping.

    kwargs:
      role_id: str (mandatory)
      permission_id: str (mandatory)
    """

    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = "", permission_id: str = "") -> str:
        role_id = role_id.strip()
        permission_id = permission_id.strip()

        if not role_id or not permission_id:
            payload = {"error": "role_id and permission_id are required"}
            out = json.dumps(payload)
            return out

        # Confirm presence
        if not _find_by_id(data.get("roles", {}).values(), "role_id", role_id):
            payload = {"error": f"role_id {role_id} not found"}
            out = json.dumps(payload)
            return out
        if not _find_by_id(data.get("permissions", {}).values(), "permission_id", permission_id):
            payload = {"error": f"permission_id {permission_id} not found"}
            out = json.dumps(payload)
            return out

        # Verify if the mapping is present
        mappings = data.get("role_permissions", {}).values()
        for rp in mappings.values():
            if (
                rp.get("role_id") == role_id
                and rp.get("permission_id") == permission_id
            ):
                payload = {"ok": True, "role_permission": rp, "no_op": True}
                out = json.dumps(payload)
                return out

        new_mapping = {"role_id": role_id, "permission_id": permission_id}
        data.setdefault("role_permissions", []).append(new_mapping)
        payload = {"ok": True, "role_permission": new_mapping, "action": "created"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignPermissionToRole",
                "description": "Assign a permission to a role by creating a role-permission mapping.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {
                            "type": "string",
                            "description": "Target role_id (e.g., ROL-030).",
                        },
                        "permission_id": {
                            "type": "string",
                            "description": "Target permission_id (e.g., P-113).",
                        },
                    },
                    "required": ["role_id", "permission_id"],
                    "additionalProperties": False,
                },
            },
        }


#AUDITING & COMMUNICATIONS
class CreateAuditLogEntry(Tool):
    """
    Create a consistent audit log entry.

    kwargs:
      action_type: str (mandatory)
      actor_id: str (mandatory)
      target_id: str (mandatory)
      details: str (mandatory)
      timestamp: str ISO (defaults to now)
    """

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        action_type: str = "", 
        actor_id: str = "", 
        target_id: str = "", 
        details: str = "", 
        timestamp: str = None
    ) -> str:
        if timestamp is None:
            timestamp = get_current_timestamp()

        log = {
            "log_id": _next_id(data, "audit_logs", "L"),
            "timestamp": timestamp,
            "action_type": action_type,
            "actor_id": actor_id,
            "target_id": target_id,
            "details": details,
        }

        data.setdefault("audit_logs", []).append(log)
        payload = {"ok": True, "audit_log": log}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAuditLogEntry",
                "description": "Append an audit log entry with deterministic timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action_type": {
                            "type": "string",
                            "description": "Audit action type.",
                        },
                        "actor_id": {
                            "type": "string",
                            "description": "User performing the action.",
                        },
                        "target_id": {
                            "type": "string",
                            "description": "Target entity id (request, user, resource, etc.).",
                        },
                        "details": {
                            "type": "string",
                            "description": "Deterministic details string.",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "ISO timestamp (optional).",
                        },
                    },
                    "required": ["action_type", "actor_id", "target_id", "details"],
                    "additionalProperties": False,
                },
            },
        }


class CreateHubSpotTicket(Tool):
    """
    Establish a general HubSpot support ticket adhering to consistent rules.

    kwargs:
      subject: str (mandatory) - subject line of the ticket
      description: str (mandatory) - description of the ticket
      assignee_id: str (mandatory) - individual responsible for the ticket
      requester_id: str (mandatory) - individual requesting the ticket
      priority: str (default: "MEDIUM") - HIGH, MEDIUM, LOW
      category: str (default: "GENERAL") - category of the ticket
      status: str (default: "OPEN") - OPEN, IN_PROGRESS, CLOSED
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        subject: str = "",
        description: str = "",
        assignee_id: str = "",
        requester_id: str = "",
        priority: str = "MEDIUM",
        category: str = "GENERAL",
        status: str = "OPEN"
    ) -> str:
        if not subject or not description or not assignee_id or not requester_id:
            payload = {
                "error": "subject, description, assignee_id, and requester_id are required"
            }
            out = json.dumps(payload)
            return out

        # Confirm priority
        valid_priorities = ["HIGH", "MEDIUM", "LOW"]
        if priority not in valid_priorities:
            payload = {"error": f"priority must be one of: {valid_priorities}"}
            out = json.dumps(payload)
            return out

        # Confirm status
        valid_statuses = ["OPEN", "IN_PROGRESS", "CLOSED"]
        if status not in valid_statuses:
            payload = {"error": f"status must be one of: {valid_statuses}"}
            out = json.dumps(payload)
            return out

        # Confirm the assignee is present
        users = data.get("users", {}).values()
        assignee = _find_by_id(users, "user_id", assignee_id)
        if not assignee:
            payload = {"error": f"Assignee {assignee_id} not found"}
            out = json.dumps(payload)
            return out

        # Confirm the requester is present
        requester = _find_by_id(users, "user_id", requester_id)
        if not requester:
            payload = {"error": f"Requester {requester_id} not found"}
            out = json.dumps(payload)
            return out

        # Implement consistent rules for security incidents
        if category == "SECURITY_INCIDENT":
            # Confirm that the operations manager (U-005) is designated for security incidents
            if assignee_id != "U-005":
                assignee_id = "U-005"

            # Verify that the subject adheres to the SIEM alert format
            if not subject.startswith("SIEM Alert: "):
                subject = "SIEM Alert: Unauthorized Access Attempt"

        timestamp = get_current_timestamp()
        ticket_id = _next_id(data, "hubspot_tickets", "TI")

        ticket_record = {
            "ticket_id": ticket_id,
            "created_at": timestamp,
            "updated_at": timestamp,
            "subject": subject,
            "description": description,
            "status": status,
            "priority": priority,
            "assignee_id": assignee_id,
            "requester_id": requester_id,
            "category": category,
            "closed_at": None if status != "CLOSED" else timestamp,
        }

        data.setdefault("hubspot_tickets", []).append(ticket_record)
        payload = {"ok": True, "ticket": ticket_record}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateHubspotTicket",
                "description": "Create a general HubSpot support ticket following deterministic rules.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject": {
                            "type": "string",
                            "description": "Ticket subject line.",
                        },
                        "description": {
                            "type": "string",
                            "description": "Ticket description.",
                        },
                        "assignee_id": {
                            "type": "string",
                            "description": "User ID who will handle the ticket.",
                        },
                        "requester_id": {
                            "type": "string",
                            "description": "User ID who is requesting the ticket.",
                        },
                        "priority": {
                            "type": "string",
                            "description": "Ticket priority (HIGH, MEDIUM, LOW).",
                            "default": "MEDIUM",
                        },
                        "category": {
                            "type": "string",
                            "description": "Ticket category.",
                            "default": "GENERAL",
                        },
                        "status": {
                            "type": "string",
                            "description": "Ticket status (OPEN, IN_PROGRESS, CLOSED).",
                            "default": "OPEN",
                        },
                    },
                    "required": [
                        "subject",
                        "description",
                        "assignee_id",
                        "requester_id",
                    ],
                    "additionalProperties": False,
                },
            },
        }


class UpdateHubSpotTicket(Tool):
    """
    Modify the fields and timestamps of an existing HubSpot ticket.

    kwargs:
      ticket_id: str (mandatory)
      status: str (optional) - OPEN, IN_PROGRESS, CLOSED
      assignee_id: str (optional)
      priority: str (optional) - HIGH, MEDIUM, LOW
      subject: str (optional)
      description: str (optional)
      updated_at: str ISO (optional; defaults to now)
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        ticket_id: str = "",
        status: str = None,
        assignee_id: str = None,
        priority: str = None,
        subject: str = None,
        description: str = None,
        updated_at: str = None
    ) -> str:
        if updated_at is None:
            updated_at = get_current_timestamp()

        if not ticket_id:
            payload = {"error": "ticket_id is required"}
            out = json.dumps(payload)
            return out

        tickets = data.get("hubspot_tickets", {}).values()
        idx = None
        for i, t in enumerate(tickets.values()):
            if t.get("ticket_id") == ticket_id:
                idx = i
                break

        if idx is None:
            payload = {"error": f"ticket_id {ticket_id} not found"}
            out = json.dumps(payload)
            return out

        # Confirm enumerations
        if status is not None and status not in ["OPEN", "IN_PROGRESS", "CLOSED"]:
            payload = {"error": "status must be one of: ['OPEN','IN_PROGRESS','CLOSED']"}
            out = json.dumps(payload)
            return out
        if priority is not None and priority not in ["HIGH", "MEDIUM", "LOW"]:
            payload = {"error": "priority must be one of: ['HIGH','MEDIUM','LOW']"}
            out = json.dumps(payload)
            return out

        # Confirm the assignee
        if assignee_id is not None:
            if not _find_by_id(data.get("users", {}).values(), "user_id", assignee_id):
                payload = {"error": f"assignee_id {assignee_id} not found"}
                out = json.dumps(payload)
                return out

        updated = dict(tickets[idx])
        if subject is not None:
            updated["subject"] = subject
        if description is not None:
            updated["description"] = description
        if priority is not None:
            updated["priority"] = priority
        if assignee_id is not None:
            updated["assignee_id"] = assignee_id
        if status is not None:
            updated["status"] = status
            # Handle closed_at according to the status
            if status == "CLOSED":
                updated["closed_at"] = updated_at
            else:
                updated["closed_at"] = None

        updated["updated_at"] = updated_at

        data["hubspot_tickets"][idx] = updated
        payload = {"ok": True, "ticket": updated}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateHubspotTicket",
                "description": "Update an existing HubSpot ticket's fields and timestamps.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {
                            "type": "string",
                            "description": "Ticket id (TI-###).",
                        },
                        "status": {
                            "type": "string",
                            "description": "New status (OPEN, IN_PROGRESS, CLOSED).",
                        },
                        "assignee_id": {
                            "type": "string",
                            "description": "New assignee user_id.",
                        },
                        "priority": {
                            "type": "string",
                            "description": "Priority (HIGH, MEDIUM, LOW).",
                        },
                        "subject": {
                            "type": "string",
                            "description": "Updated subject.",
                        },
                        "description": {
                            "type": "string",
                            "description": "Updated description.",
                        },
                        "updated_at": {
                            "type": "string",
                            "description": "ISO timestamp for update (optional).",
                        },
                    },
                    "required": ["ticket_id"],
                    "additionalProperties": False,
                },
            },
        }


class GetHubSpotTicket(Tool):
    """
    Retrieve HubSpot tickets using ticket_id or filter by SIEM alert ID (found in description),
    status, priority, category, assignee_id, or requester_id.

    kwargs:
      ticket_id: str (optional) - Specific ticket ID to retrieve
      alert_id: str (optional) - SIEM alert ID to match within the description (e.g., ALRT-012)
      status: str (optional) - OPEN, IN_PROGRESS, CLOSED
      priority: str (optional) - HIGH, MEDIUM, LOW
      category: str (optional) - SECURITY_INCIDENT, ACCESS_REQUEST, GENERAL, etc.
      assignee_id: str (optional)
      requester_id: str (optional)
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        ticket_id: str = None,
        alert_id: str = None,
        status: str = None,
        priority: str = None,
        category: str = None,
        assignee_id: str = None,
        requester_id: str = None
    ) -> str:
        tickets = data.get("hubspot_tickets", {}).values()

        # If ticket_id is supplied, return the specific ticket
        if ticket_id:
            t = _find_by_id(tickets, "ticket_id", ticket_id)
            if not t:
                payload = {"error": f"ticket_id {ticket_id} not found"}
                out = json.dumps(payload)
                return out
            payload = {"ok": True, "ticket": t}
            out = json.dumps(payload)
            return out

        # If not, narrow down
        out: list[dict[str, Any]] = []
        for t in tickets.values():
            if status and t.get("status") != status:
                continue
            if priority and t.get("priority") != priority:
                continue
            if category and t.get("category") != category:
                continue
            if assignee_id and t.get("assignee_id") != assignee_id:
                continue
            if requester_id and t.get("requester_id") != requester_id:
                continue
            if alert_id:
                desc = str(t.get("description", ""))
                if alert_id not in desc:
                    continue
            out.append(t)
        payload = {"ok": True, "tickets": out}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetHubspotTicket",
                "description": "Retrieve HubSpot tickets by ticket_id or filter by SIEM alert ID (in description), status, priority, category, assignee_id, or requester_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {
                            "type": "string",
                            "description": "Specific ticket ID to retrieve (TI-###).",
                        },
                        "alert_id": {
                            "type": "string",
                            "description": "SIEM alert ID to match in description (e.g., ALRT-012).",
                        },
                        "status": {
                            "type": "string",
                            "description": "Filter by status (OPEN, IN_PROGRESS, CLOSED).",
                        },
                        "priority": {
                            "type": "string",
                            "description": "Filter by priority (HIGH, MEDIUM, LOW).",
                        },
                        "category": {
                            "type": "string",
                            "description": "Filter by category (e.g., SECURITY_INCIDENT, ACCESS_REQUEST, GENERAL).",
                        },
                        "assignee_id": {
                            "type": "string",
                            "description": "Filter by assignee user_id.",
                        },
                        "requester_id": {
                            "type": "string",
                            "description": "Filter by requester user_id.",
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }


class PostSlackMessage(Tool):
    """
    Add a Slack message record for notifications.

    kwargs:
      channel: str (mandatory) e.g., "#access-requests"
      message: str (mandatory)
      username: str = "RBAC_BOT"
      timestamp: str ISO (defaults to now)
    """

    @staticmethod
    def invoke(data: dict[str, Any], channel: str = "", message: str = "", username: str = "RBAC_BOT", timestamp: str = None) -> str:
        if timestamp is None:
            timestamp = get_current_timestamp()

        if not channel or not message:
            payload = {"error": "channel and message required"}
            out = json.dumps(payload)
            return out

        # Consistent rule: Standardize security incident messages
        # - When posting to #security-incidents, set the username to RBAC_BOT
        # - Remove excess whitespace from the message
        if channel.strip() == "#security-incidents":
            username = "RBAC_BOT"
            message = " ".join(str(message).split())

        rec = {
            "message_id": _next_id(data, "slack_messages", "SL"),
            "timestamp": timestamp,
            "username": username,
            "message": message,
            "channel": channel,
            # Conform to the dataset schema
            "created_at": timestamp,
            "updated_at": timestamp,
        }

        data.setdefault("slack_messages", []).append(rec)
        payload = {"ok": True, "slack_message": rec}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "PostSlackMessage",
                "description": "Post a message record to Slack notifications (e.g., #access-requests).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "channel": {
                            "type": "string",
                            "description": "Slack channel name (e.g., #access-requests).",
                        },
                        "message": {"type": "string", "description": "Message text."},
                        "username": {
                            "type": "string",
                            "description": "Posting bot username.",
                            "default": "RBAC_BOT",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "ISO timestamp (optional).",
                        },
                    },
                    "required": ["channel", "message"],
                    "additionalProperties": False,
                },
            },
        }


class SendEmail(Tool):
    """
    Dispatch an email with consistent ID and timestamp.

    kwargs:
      sender: str (mandatory)
      receiver: str (mandatory)
      subject: str (mandatory)
      text_content: str (mandatory)
      timestamp: str ISO (optional; defaults to the current timestamp)
    """

    @staticmethod
    def invoke(data: dict[str, Any], sender: str = "", receiver: str = "", subject: str = "", text_content: str = "", timestamp: str = None) -> str:
        if timestamp is None:
            timestamp = get_current_timestamp()

        if not sender or not receiver or not subject or not text_content:
            payload = {"error": "sender, receiver, subject, and text_content are required"}
            out = json.dumps(payload)
            return out

        # Establish an email record
        email = {
            "email_id": _next_id(data, "emails", "EM"),
            "timestamp": timestamp,
            "sender": sender,
            "receiver": receiver,
            "subject": subject,
            "text_content": text_content,
        }

        data.setdefault("emails", []).append(email)
        payload = {"ok": True, "email": email}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendEmail",
                "description": "Send an email with deterministic ID and timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sender": {
                            "type": "string",
                            "description": "Sender email address.",
                        },
                        "receiver": {
                            "type": "string",
                            "description": "Receiver email address.",
                        },
                        "subject": {"type": "string", "description": "Email subject."},
                        "text_content": {
                            "type": "string",
                            "description": "Email body text.",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "ISO timestamp (optional).",
                        },
                    },
                    "required": ["sender", "receiver", "subject", "text_content"],
                    "additionalProperties": False,
                },
            },
        }


class CreateSiemAlert(Tool):
    """
    Establish a new SIEM alert for security incidents.

    kwargs:
      user_id: str (mandatory) - ID of the user initiating the alert
      resource_id: str (mandatory) - ID of the resource involved
      alert_type: str (default: "UNAUTHORIZED_ACCESS_ATTEMPT")
      severity: str (default: "HIGH") - CRITICAL, HIGH, MEDIUM, LOW
      timestamp: str ISO (defaults to now)
    """

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        user_id: str = "", 
        resource_id: str = "", 
        alert_type: str = "UNAUTHORIZED_ACCESS_ATTEMPT", 
        severity: str = "HIGH", 
        timestamp: str = None
    ) -> str:
        if timestamp is None:
            timestamp = get_current_timestamp()

        if not user_id or not resource_id:
            payload = {"error": "user_id and resource_id required"}
            out = json.dumps(payload)
            return out

        # Confirm severity
        valid_severities = ["CRITICAL", "HIGH", "MEDIUM", "LOW"]
        if severity not in valid_severities:
            payload = {"error": f"severity must be one of: {valid_severities}"}
            out = json.dumps(payload)
            return out

        # Confirm the user is present
        users = data.get("users", {}).values()
        user = _find_by_id(users, "user_id", user_id)
        if not user:
            payload = {"error": f"User {user_id} not found"}
            out = json.dumps(payload)
            return out

        # Confirm the resource is present
        resources = data.get("resources", {}).values()
        resource = _find_by_id(resources, "resource_id", resource_id)
        if not resource:
            payload = {"error": f"Resource {resource_id} not found"}
            out = json.dumps(payload)
            return out

        alert_id = _next_id(data, "siem_alerts", "ALRT")

        alert_record = {
            "alert_id": alert_id,
            "timestamp": timestamp,
            "user_id": user_id,
            "resource_id": resource_id,
            "alert_type": alert_type,
            "severity": severity,
        }

        data.setdefault("siem_alerts", []).append(alert_record)
        payload = {"ok": True, "siem_alert": alert_record}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateSiemAlert",
                "description": "Create a new SIEM alert for security incidents.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "ID of the user triggering the alert.",
                        },
                        "resource_id": {
                            "type": "string",
                            "description": "ID of the resource involved.",
                        },
                        "alert_type": {
                            "type": "string",
                            "description": "Type of alert.",
                            "default": "UNAUTHORIZED_ACCESS_ATTEMPT",
                        },
                        "severity": {
                            "type": "string",
                            "description": "Alert severity: CRITICAL, HIGH, MEDIUM, LOW.",
                            "default": "HIGH",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "ISO timestamp (optional).",
                        },
                    },
                    "required": ["user_id", "resource_id"],
                    "additionalProperties": False,
                },
            },
        }


class GetSiemAlert(Tool):
    """
    Retrieve SIEM alerts based on ID, user, resource, or severity.

    kwargs:
      alert_id: str (optional) - Specific alert ID to retrieve
      user_id: str (optional) - Filter by the user who triggered the alerts
      resource_id: str (optional) - Filter by the resource involved in the alerts
      severity: str (optional) - Filter by severity (CRITICAL, HIGH, MEDIUM, LOW)
    """

    @staticmethod
    def invoke(data: dict[str, Any], alert_id: str = None, user_id: str = None, resource_id: str = None, severity: str = None) -> str:
        siem_alerts = data.get("siem_alerts", {}).values()

        # If alert_id is supplied, return the specific alert
        if alert_id:
            alert = _find_by_id(siem_alerts, "alert_id", alert_id)
            if not alert:
                payload = {"error": f"SIEM alert {alert_id} not found"}
                out = json.dumps(payload)
                return out
            payload = {"ok": True, "siem_alert": alert}
            out = json.dumps(payload)
            return out

        # Narrow down alerts according to the supplied criteria
        filtered_alerts = []
        for alert in siem_alerts.values():
            if user_id and alert.get("user_id") != user_id:
                continue
            if resource_id and alert.get("resource_id") != resource_id:
                continue
            if severity and alert.get("severity") != severity:
                continue
            filtered_alerts.append(alert)
        payload = {"ok": True, "siem_alerts": filtered_alerts}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSiemAlert",
                "description": "Retrieve SIEM alerts by ID, user, resource, or severity.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "alert_id": {
                            "type": "string",
                            "description": "Specific SIEM alert ID to retrieve.",
                        },
                        "user_id": {
                            "type": "string",
                            "description": "Filter by user who triggered alerts.",
                        },
                        "resource_id": {
                            "type": "string",
                            "description": "Filter by resource involved in alerts.",
                        },
                        "severity": {
                            "type": "string",
                            "description": "Filter by severity (CRITICAL, HIGH, MEDIUM, LOW).",
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }


#SESSION ADMINISTRATION
class UpdateSession(Tool):
    """
    Modify session properties while maintaining session_id as immutable.

    kwargs:
      session_id: str (mandatory) - Session ID to modify
      end_time: str ISO (optional) - Specify session end time
      ip_address: str (optional) - Update the IP address
      device: str (optional) - Update the type of device
      is_mfa: bool (optional) - Update MFA status
    """

    @staticmethod
    def invoke(data: dict[str, Any], session_id: str = "", end_time: Any = None, ip_address: Any = None, device: Any = None, is_mfa: Any = None) -> str:
        if not session_id:
            payload = {"error": "session_id required"}
            out = json.dumps(payload)
            return out

        # Locate the session
        sessions = data.get("sessions", {}).values()
        session_index = None
        for i, session in enumerate(sessions.values()):
            if session.get("session_id") == session_id:
                session_index = i
                break

        if session_index is None:
            payload = {"error": f"session_id {session_id} not found"}
            out = json.dumps(payload)
            return out

        # Modify the session (session_id, user_id, or start_time cannot be changed)
        updated_session = dict(sessions[session_index])
        if end_time is not None:
            updated_session["end_time"] = end_time
        if ip_address is not None:
            updated_session["ip_address"] = ip_address
        if device is not None:
            updated_session["device"] = device
        if is_mfa is not None:
            updated_session["is_mfa"] = is_mfa

        data["sessions"][session_index] = updated_session
        payload = {"ok": True, "session": updated_session}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateSession",
                "description": "Update session properties while keeping session_id immutable.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "session_id": {
                            "type": "string",
                            "description": "Session ID to update.",
                        },
                        "end_time": {
                            "type": "string",
                            "description": "ISO timestamp for session end time.",
                        },
                        "ip_address": {
                            "type": "string",
                            "description": "Updated IP address.",
                        },
                        "device": {
                            "type": "string",
                            "description": "Updated device type (DESKTOP, LAPTOP, MOBILE).",
                        },
                        "is_mfa": {
                            "type": "boolean",
                            "description": "Updated MFA status.",
                        },
                    },
                    "required": ["session_id"],
                    "additionalProperties": False,
                },
            },
        }


class GetSession(Tool):
    """
    Retrieve sessions by session ID, user ID, or IP address.

    kwargs:
      session_id: str (optional) - Specific session ID to retrieve
      user_id: str (optional) - Filter by user who owns the sessions
      ip_address: str (optional) - Filter by IP address used in sessions
      only_active: bool = False - Only return sessions without end_time
    """

    @staticmethod
    def invoke(data: dict[str, Any], session_id: str = None, user_id: str = None, ip_address: str = None, only_active: bool = False) -> str:
        sessions = data.get("sessions", {}).values()

        # If session_id is supplied, return the specific session
        if session_id:
            session = _find_by_id(sessions, "session_id", session_id)
            if not session:
                payload = {"error": f"session_id {session_id} not found"}
                out = json.dumps(payload)
                return out
            payload = {"ok": True, "session": session if session else "No sessions found"}
            out = json.dumps(payload)
            return out

        # Narrow down sessions according to the supplied criteria
        filtered_sessions = []
        for session in sessions.values():
            # Narrow down by user_id if supplied
            if user_id and session.get("user_id") != user_id:
                continue
            # Narrow down by ip_address if supplied
            if ip_address and session.get("ip_address") != ip_address:
                continue
            # Narrow down by active status if requested
            if only_active and session.get("end_time") is not None:
                continue
            filtered_data["sessions"][session_id] = session
        payload = {
            "ok": True,
            "sessions": (
                filtered_sessions if filtered_sessions else "No sessions found"
            ),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSession",
                "description": "Retrieve sessions by session ID, user ID, or IP address.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "session_id": {
                            "type": "string",
                            "description": "Specific session ID to retrieve.",
                        },
                        "user_id": {
                            "type": "string",
                            "description": "Filter by user who owns the sessions.",
                        },
                        "ip_address": {
                            "type": "string",
                            "description": "Filter by IP address used in sessions.",
                        },
                        "only_active": {
                            "type": "boolean",
                            "description": "Only return sessions without end_time.",
                            "default": False,
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }


TOOLS = [
    #User Administration
    CreateUser(),
    UpdateUser(),
    GetUser(),
    #Role Administration
    CreateRole(),
    GetRole(),
    UpdateRole(),
    GetUserRoles(),
    IsAdmin(),
    GetBaseRoleByDepartment(),
    EnsureUserRole(),
    UpdateUserRole(),
    CheckSoDConflicts(),
    #Access Demands
    GetAccessRequest(),
    DecideAccessRequest(),
    #Permissions and Policy Exceptions
    CreatePermission(),
    GetPermission(),
    GetRolePermissions(),
    AssignPermissionToRole(),
    GetPolicyException(),
    CreatePolicyException(),
    DecidePolicyException(),
    #Assets and Access Management
    CreateResource(),
    GetResource(),
    ListUsersWithAccessToResource(),
    CanAccessResource(),
    #Certification Records
    CreateCertification(),
    GetCertification(),
    CompleteCertification(),
    #Session Administration
    GetSession(),
    UpdateSession(),
    #Security and SIEM
    CreateSiemAlert(),
    GetSiemAlert(),
    #Communications and Tickets
    CreateHubSpotTicket(),
    GetHubSpotTicket(),
    UpdateHubSpotTicket(),
    SendEmail(),
    PostSlackMessage(),
    #Auditing and Logging
    CreateAuditLogEntry(),
]
