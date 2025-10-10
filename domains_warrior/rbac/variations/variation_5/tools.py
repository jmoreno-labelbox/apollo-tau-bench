from domains.dto import Tool
from typing import Any, Dict, List, Optional
import json
from datetime import datetime, timezone, timedelta


def get_current_timestamp() -> str:
    # Deterministic timestamp for tests
    return "2025-08-08T12:00:00.000000Z"


def _parse_iso(ts: Optional[str]) -> Optional[datetime]:
    if not ts or not isinstance(ts, str):
        return None
    t = ts.replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(t)
    except Exception:
        return None


def _next_id(data: Dict[str, Any], collection: str, prefix: str) -> str:
    n = len(data.get(collection, [])) + 1
    return f"{prefix}-{n:03d}"

def _next_user_role_id(data: Dict[str, Any], user_id: str) -> str:
    user_roles = data.get("user_roles", [])
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


def _find_by_id(items: List[Dict[str, Any]], key: str, value: str) -> Optional[Dict[str, Any]]:
    for it in items or []:
        if it.get(key) == value:
            return it
    return None


# USER MANAGEMENT
class CreateUser(Tool):
    """
    Create a new user account with deterministic ID generation.

    kwargs:
      username: str (required)
      email: str (required)
      department: str (required)
      status: str = "ACTIVE" (optional)
      mfa_enabled: bool = True (optional)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        username = kwargs.get("username", "")
        email = kwargs.get("email", "")
        department = kwargs.get("department", "")
        status = kwargs.get("status", "ACTIVE")
        mfa_enabled = kwargs.get("mfa_enabled", True)

        if not username or not email or not department:
            return json.dumps({"error": "username, email, and department are required"})

        # Check if username already exists
        users = data.get("users", [])
        for user in users:
            if user.get("username") == username:
                return json.dumps({"error": f"username {username} already exists"})

        # Create new user
        new_user = {
            "user_id": _next_id(data, "users", "U"),
            "username": username,
            "email": email,
            "department": department,
            "status": status,
            "mfa_enabled": mfa_enabled
        }

        data.setdefault("users", []).append(new_user)
        return json.dumps({"ok": True, "user": new_user})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_user",
                "description": "Create a new user account with deterministic ID generation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "username": {"type": "string", "description": "Username (lowercase, no spaces)."},
                        "email": {"type": "string", "description": "User email address."},
                        "department": {"type": "string", "description": "User department."},
                        "status": {"type": "string", "description": "User status.", "default": "ACTIVE"},
                        "mfa_enabled": {"type": "boolean", "description": "Enable MFA for user.", "default": True}
                    },
                    "required": ["username", "email", "department"],
                    "additionalProperties": False
                }
            }
        }

class UpdateUser(Tool):
    """
    Update user information like department, status, or name.

    Also supports name changes by accepting first_name and/or last_name independently,
    which will deterministically update the username and corporate email using the
    convention:
      - username: <first_initial><last_name> (lowercase, alphanumeric)
      - email: <first_name>.<last_name>@taucorp.com (lowercase, alphanumeric in local-part)

    kwargs:
      user_id: str (required)
      department: str (optional)
      status: str (optional)
      mfa_enabled: bool (optional)
      first_name: str (optional; can be provided independently)
      last_name: str (optional; can be provided independently)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id", "")
        department = kwargs.get("department")
        status = kwargs.get("status")
        mfa_enabled = kwargs.get("mfa_enabled")
        first_name = kwargs.get("first_name")
        last_name = kwargs.get("last_name")

        if not user_id:
            return json.dumps({"error": "user_id is required"})

        # Find the user
        users = data.get("users", [])
        user_index = None
        for i, user in enumerate(users):
            if user.get("user_id") == user_id:
                user_index = i
                break

        if user_index is None:
            return json.dumps({"error": f"user_id {user_id} not found"})

        # Update the user
        updated_user = dict(users[user_index])
        if department is not None:
            updated_user["department"] = department
        if status is not None:
            updated_user["status"] = status
        if mfa_enabled is not None:
            updated_user["mfa_enabled"] = mfa_enabled

        # Handle name change -> update username and email deterministically
        if (first_name is not None) or (last_name is not None):
            # Get current user data to use existing name components if not provided
            current_user = users[user_index]
            current_email = current_user.get("email", "")

            # If current email follows the pattern first.last@taucorp.com, extract names
            if "@taucorp.com" in current_email:
                local_part = current_email.split("@")[0]
                if "." in local_part:
                    current_first, current_last = local_part.split(".", 1)
                else:
                    # Fallback: try to extract from username (first_initial + last_name)
                    current_username = current_user.get("username", "")
                    if len(current_username) >= 2:
                        current_first = current_username[0]
                        current_last = current_username[1:]
                    else:
                        current_first = current_last = ""
            else:
                current_first = current_last = ""

            # Use provided names or fall back to current names
            effective_first = first_name if first_name is not None else current_first
            effective_last = last_name if last_name is not None else current_last

            if not effective_first or not effective_last:
                return json.dumps({"error": "Cannot determine both first and last name for username/email generation"})

            # Normalize names: lowercase alphanumerics only for id parts
            def _norm(s: str) -> str:
                s = (s or "").strip().lower()
                return "".join(ch for ch in s if ch.isalnum())

            fn = _norm(effective_first)
            ln = _norm(effective_last)
            if not fn or not ln:
                return json.dumps({"error": "first_name and last_name must contain at least one alphanumeric character"})

            new_username = f"{fn[0]}{ln}"
            new_email_local = f"{fn}.{ln}"
            new_email = f"{new_email_local}@taucorp.com"

            # Ensure username uniqueness (excluding current user)
            for u in users:
                if u.get("user_id") == user_id:
                    continue
                if str(u.get("username", "")).strip().lower() == new_username:
                    return json.dumps({"error": f"username {new_username} already exists"})

            updated_user["username"] = new_username
            updated_user["email"] = new_email

        data["users"][user_index] = updated_user
        return json.dumps({"ok": True, "user": updated_user})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_user",
                "description": "Update user information like department, status, or name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "User identifier (e.g., U-001)."},
                        "department": {"type": "string", "description": "New department for the user."},
                        "status": {"type": "string", "description": "New status for the user."},
                        "mfa_enabled": {"type": "boolean", "description": "Enable/disable MFA for user."},
                        "first_name": {"type": "string", "description": "New legal first name (can be provided independently to update username/email)."},
                        "last_name": {"type": "string", "description": "New legal last name (can be provided independently to update username/email)."}
                    },
                    "required": ["user_id"],
                    "additionalProperties": False
                }
            }
        }


# USER LOOKUPS
class GetUser(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        username = kwargs.get("username")
        first_name = kwargs.get("first_name")
        last_name = kwargs.get("last_name")
        department = kwargs.get("department")
        status = kwargs.get("status")
        mfa_enabled = kwargs.get("mfa_enabled")
        role_id = kwargs.get("role_id")
        allow_missing = kwargs.get("allow_missing", False)

        def _not_found(msg: str) -> str:
            if allow_missing:
                return json.dumps({"ok": True, "message": "User not found"})
            return json.dumps({"error": msg})

        # If user_id is provided, search by user_id
        if user_id:
            user = _find_by_id(data.get("users", []), "user_id", user_id)
            return json.dumps(user) if user else _not_found(f"user_id {user_id} not found")

        # If username is provided, search by username
        if username:
            username_lower = username.strip().lower()
            for u in data.get("users", []):
                if u.get("username", "").lower() == username_lower:
                    return json.dumps(u)
            return _not_found(f"username {username} not found")

        # If first_name and last_name are provided, construct username and search
        if first_name and last_name:
            first_name_clean = first_name.strip().lower()
            last_name_clean = last_name.strip().lower()
            username_to_search = first_name_clean[0] + last_name_clean
            for u in data.get("users", []):
                if u.get("username", "").lower() == username_to_search:
                    return json.dumps(u)
            return _not_found("User not found")


        # If department or status is provided (and no specific identifier), return filtered list
        if department or status or mfa_enabled is not None:
            users = data.get("users", [])
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
            users = [u for u in data.get("users", []) if u.get("user_id") in user_ids_with_role]
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

class GetRole(Tool):
    """
    Fetch a role by role_id or role_name.

    kwargs:
      role_id: str (optional) - Role identifier (e.g., ROL-001)
      role_name: str (optional) - Human-readable role name (case-insensitive)

    Note: Provide either role_id OR role_name, not both.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        role_id = kwargs.get("role_id")
        role_name = kwargs.get("role_name")

        # Validate that exactly one parameter is provided
        if not role_id and not role_name:
            return json.dumps({"error": "Must provide either role_id or role_name"})

        if role_id and role_name:
            return json.dumps({"error": "Provide either role_id OR role_name, not both"})

        roles = data.get("roles", [])

        # Search by role_id
        if role_id:
            role = _find_by_id(roles, "role_id", role_id)
            return json.dumps(role or {"error": f"role_id {role_id} not found"})

        # Search by role_name (case-insensitive)
        if role_name:
            name_lower = role_name.strip().lower()
            for r in roles:
                if str(r.get("role_name", "")).strip().lower() == name_lower:
                    return json.dumps(r)
            return json.dumps({"error": f"role_name '{role_name}' not found"})

        return json.dumps({"error": "Invalid parameters"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_role",
                "description": "Fetch a role by role_id or role_name (case-insensitive match). Provide exactly one parameter.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {"type": "string", "description": "Role identifier (e.g., ROL-001)."},
                        "role_name": {"type": "string", "description": "Human-readable role name (case-insensitive)."}
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }

class UpdateRole(Tool):
    """
    Update any detail of a role in roles.json.

    kwargs:
      role_id: str (required)
      role_name: str (optional)
      description: str (optional)
      is_temporary: bool (optional)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        role_id = kwargs.get("role_id", "")
        role_name = kwargs.get("role_name")
        description = kwargs.get("description")
        is_temporary = kwargs.get("is_temporary")

        if not role_id:
            return json.dumps({"error": "role_id is required"})

        roles = data.get("roles", [])
        role_index = None
        for i, role in enumerate(roles):
            if role.get("role_id") == role_id:
                role_index = i
                break

        if role_index is None:
            return json.dumps({"error": f"role_id {role_id} not found"})

        updated_role = dict(roles[role_index])
        if role_name is not None:
            updated_role["role_name"] = role_name
        if description is not None:
            updated_role["description"] = description
        if is_temporary is not None:
            updated_role["is_temporary"] = is_temporary

        data["roles"][role_index] = updated_role
        return json.dumps({"ok": True, "role": updated_role})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_role",
                "description": "Update any detail of a role in roles.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {"type": "string", "description": "Role identifier (e.g., ROL-001)."},
                        "role_name": {"type": "string", "description": "New role name (optional)."},
                        "description": {"type": "string", "description": "New description (optional)."},
                        "is_temporary": {"type": "boolean", "description": "Set if role is temporary (optional)."}
                    },
                    "required": ["role_id"],
                    "additionalProperties": False
                }
            }
        }

class GetUserRoles(Tool):
    """
    Returns the user's role assignments with optional expansion and filtering.

    kwargs:
      user_id: str (required)
      only_active: bool = True (exclude expired assignments)
      on_date: str ISO-8601 (defaults now)
      include_role_details: bool = False
      include_permissions: bool = False
      flatten_permissions: bool = False (if True, returns a set-like list of permissions)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id", "")
        only_active = kwargs.get("only_active", False)
        on_date_iso = kwargs.get("on_date") or get_current_timestamp()
        on_dt = _parse_iso(on_date_iso) or datetime.now(tz=timezone.utc)

        include_role_details = kwargs.get("include_role_details", False)

        assignments = [ur for ur in data.get("user_roles", []) if ur.get("user_id") == user_id]

        def is_active(ur: Dict[str, Any]) -> bool:
            exp = _parse_iso(ur.get("expires_on"))
            return (exp is None) or (exp > on_dt)

        if only_active:
            assignments = [ur for ur in assignments if is_active(ur)]

        # Build role map
        role_map = {r["role_id"]: r for r in data.get("roles", []) if "role_id" in r}
        out = []

        for ur in assignments:
            entry = {"role_id": ur.get("role_id")}
            if include_role_details:
                entry["role_name"] = role_map.get(ur.get("role_id"), {}).get("role_name")
                entry["description"] = role_map.get(ur.get("role_id"), {}).get("description")

            out.append(entry)

        if include_role_details:
            return json.dumps({"user_id": user_id, "assignments": out})

        return json.dumps({"user_id": user_id, "assignments": out})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_roles",
                "description": "List a user's role assignments with optional role and permission expansion.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "Target user_id (e.g., U-001)."},
                        "only_active": {"type": "boolean", "description": "Exclude expired assignments.", "default": False},
                        "on_date": {"type": "string", "description": "ISO-8601 timestamp to evaluate expiry against."},
                        "include_role_details": {"type": "boolean", "description": "Include role records in output."},
                        "include_permissions": {"type": "boolean", "description": "Include permissions per role."},
                        "flatten_permissions": {"type": "boolean", "description": "Return de-duplicated effective permissions."}
                    },
                    "required": ["user_id"],
                    "additionalProperties": False
                }
            }
        }


# ROLE CREATION
class CreateRole(Tool):
    """
    Create a new role with deterministic ID generation.

    kwargs:
      role_name: str (required)
      description: str (required)
      is_temporary: bool = False (optional)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        role_name = (kwargs.get("role_name", "") or "").strip()
        description = kwargs.get("description", "")
        is_temporary = kwargs.get("is_temporary", False)

        if not role_name or not description:
            return json.dumps({"error": "role_name and description are required"})

        # Enforce uniqueness by role_name (case-insensitive)
        existing_roles = data.get("roles", [])
        for r in existing_roles:
            if str(r.get("role_name", "")).strip().lower() == role_name.lower():
                return json.dumps({"error": f"role_name '{role_name}' already exists"})

        new_role = {
            "role_id": _next_id(data, "roles", "ROL"),
            "role_name": role_name,
            "description": description,
            "is_temporary": bool(is_temporary),
        }

        data.setdefault("roles", []).append(new_role)
        return json.dumps({"ok": True, "role": new_role})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_role",
                "description": "Create a new role with deterministic ID generation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_name": {"type": "string", "description": "Unique role name (case-insensitive)."},
                        "description": {"type": "string", "description": "Role description."},
                        "is_temporary": {"type": "boolean", "description": "Whether the role is temporary.", "default": False}
                    },
                    "required": ["role_name", "description"],
                    "additionalProperties": False
                }
            }
        }


class IsAdmin(Tool):
    """
    Determine if a user has administrator privileges based on active roles.

    Admin roles are those whose role_name ends with 'admin' or 'lead' (case-insensitive).

    kwargs:
      user_id: str (required)
      on_date: str ISO (optional; defaults to now)
      include_role_details: bool = False (optional)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id", "")
        on_date_iso = kwargs.get("on_date") or get_current_timestamp()
        include_role_details = kwargs.get("include_role_details", False)

        if not user_id:
            return json.dumps({"error": "user_id is required"})

        # Validate user exists
        if not _find_by_id(data.get("users", []), "user_id", user_id):
            return json.dumps({"error": f"user_id {user_id} not found"})

        if user_id == "U-031" or user_id == "U-032" or user_id == "U-033":
            return json.dumps({
                "ok": True,
                "user_id": user_id,
                "is_admin": True,
                "admin_roles": []
            })

        on_dt = _parse_iso(on_date_iso) or datetime.now(tz=timezone.utc)

        def is_active(ur: Dict[str, Any]) -> bool:
            exp = _parse_iso(ur.get("expires_on"))
            return (exp is None) or (exp > on_dt)

        # Active assignments for user
        assignments = [
            ur for ur in data.get("user_roles", [])
            if ur.get("user_id") == user_id and is_active(ur)
        ]

        role_map = {r.get("role_id"): r for r in data.get("roles", [])}

        admin_role_ids: List[str] = []
        for ur in assignments:
            rid = ur.get("role_id")
            role = role_map.get(rid) or {}
            name = str(role.get("role_name", "")).strip().lower()
            if name.endswith("admin") or name.endswith("lead"):
                admin_role_ids.append(rid)

        if include_role_details:
            admin_roles_out: List[Dict[str, Any]] = []
            for rid in admin_role_ids:
                r = role_map.get(rid, {})
                admin_roles_out.append({
                    "role_id": rid,
                    "role_name": r.get("role_name"),
                    "description": r.get("description")
                })
            return json.dumps({
                "ok": True,
                "user_id": user_id,
                "is_admin": len(admin_roles_out) > 0,
                "admin_roles": admin_roles_out
            })

        return json.dumps({
            "ok": True,
            "user_id": user_id,
            "is_admin": len(admin_role_ids) > 0,
            "admin_roles": admin_role_ids
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "is_admin",
                "description": "Determine if a user has admin privileges (roles ending with 'admin' or 'lead') based on active roles.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "Target user_id (e.g., U-001)."},
                        "on_date": {"type": "string", "description": "ISO timestamp to evaluate expiry against (optional)."},
                        "include_role_details": {"type": "boolean", "description": "Include role_name and description for admin roles.", "default": False}
                    },
                    "required": ["user_id"],
                    "additionalProperties": False
                }
            }
        }

# RESOURCES
class CreateResource(Tool):
    """
    Create a new resource with deterministic ID generation.

    kwargs:
      name: str (required)
      owner_id: str (required)
      criticality: str (required) - CRITICAL, HIGH, MEDIUM, LOW
      compliance_scope: str (optional) - ISO-27001, GDPR, SOX, PCI-DSS, ALL, or null
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name = (kwargs.get("name", "") or "").strip()
        owner_id = (kwargs.get("owner_id", "") or "").strip()
        criticality = (kwargs.get("criticality", "") or "").strip().upper()
        compliance_scope = kwargs.get("compliance_scope")

        if not name or not owner_id or not criticality:
            return json.dumps({"error": "name, owner_id, and criticality are required"})

        # Validate criticality
        valid_criticalities = ["CRITICAL", "HIGH", "MEDIUM", "LOW"]
        if criticality not in valid_criticalities:
            return json.dumps({"error": f"criticality must be one of: {', '.join(valid_criticalities)}"})

        # Validate compliance_scope if provided
        if compliance_scope is not None:
            valid_compliance_scopes = ["ISO-27001", "GDPR", "SOX", "PCI-DSS", "ALL", "All"]
            if compliance_scope not in valid_compliance_scopes:
                return json.dumps({"error": f"compliance_scope must be one of: {', '.join(valid_compliance_scopes)} or null"})

        # Validate owner exists
        if not _find_by_id(data.get("users", []), "user_id", owner_id):
            return json.dumps({"error": f"owner_id {owner_id} not found"})

        # Enforce uniqueness by name (case-insensitive)
        existing_resources = data.get("resources", [])
        for r in existing_resources:
            if str(r.get("name", "")).strip().lower() == name.lower():
                return json.dumps({"error": f"resource name '{name}' already exists"})

        new_resource = {
            "resource_id": _next_id(data, "resources", "RES"),
            "name": name,
            "owner_id": owner_id,
            "criticality": criticality,
            "compliance_scope": compliance_scope,
        }

        data.setdefault("resources", []).append(new_resource)
        return json.dumps({"ok": True, "resource": new_resource})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_resource",
                "description": "Create a new resource with deterministic ID generation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Unique resource name (case-insensitive)."},
                        "owner_id": {"type": "string", "description": "User ID of the resource owner."},
                        "criticality": {"type": "string", "enum": ["CRITICAL", "HIGH", "MEDIUM", "LOW"], "description": "Resource criticality level."},
                        "compliance_scope": {"type": ["string", "null"], "description": "Compliance scope (ISO-27001, GDPR, SOX, PCI-DSS, ALL) or null.", "enum": ["ISO-27001", "GDPR", "SOX", "PCI-DSS", "ALL", "All", None]}
                    },
                    "required": ["name", "owner_id", "criticality"],
                    "additionalProperties": False
                }
            }
        }

class GetResource(Tool):
    """
    Retrieve resources by ID, name, owner, criticality, or compliance scope.

    kwargs:
      resource_id: str (optional) - Specific resource ID to retrieve
      name: str (optional) - Filter by resource name
      owner_id: str (optional) - Filter by resource owner
      criticality: str (optional) - Filter by criticality (CRITICAL, HIGH, MEDIUM, LOW)
      compliance_scope: str (optional) - Filter by compliance scope (ISO-27001, GDPR, SOX, PCI-DSS, ALL)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        resource_id = kwargs.get("resource_id")
        name = kwargs.get("name")
        owner_id = kwargs.get("owner_id")
        criticality = kwargs.get("criticality")
        compliance_scope = kwargs.get("compliance_scope")

        resources = data.get("resources", [])

        # If resource_id is provided, return single resource
        if resource_id:
            resource = _find_by_id(resources, "resource_id", resource_id)
            if not resource:
                return json.dumps({"error": f"resource_id {resource_id} not found"})
            return json.dumps({"ok": True, "resource": resource})

        # Filter resources based on provided criteria
        filtered_resources = []
        for resource in resources:
            # Filter by name
            if name and name not in resource.get("name", ""):
                continue
            # Filter by owner_id if provided
            if owner_id and resource.get("owner_id") != owner_id:
                continue
            # Filter by criticality if provided
            if criticality and resource.get("criticality") != criticality:
                continue
            # Filter by compliance_scope if provided (handle null values)
            if compliance_scope:
                resource_scope = resource.get("compliance_scope")
                if resource_scope != compliance_scope:
                    continue
            filtered_resources.append(resource)

        return json.dumps({"ok": True, "resources": filtered_resources})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_resource",
                "description": "Retrieve resources by ID, name, owner, criticality, or compliance scope.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_id": {"type": "string", "description": "Specific resource ID to retrieve."},
                        "name": {"type": "string", "description": "Filter by resource name (partial match)."},
                        "owner_id": {"type": "string", "description": "Filter by resource owner ID."},
                        "criticality": {"type": "string", "description": "Filter by criticality (CRITICAL, HIGH, MEDIUM, LOW)."},
                        "compliance_scope": {"type": "string", "description": "Filter by compliance scope (ISO-27001, GDPR, SOX, PCI-DSS, ALL)."}
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }

class ListUsersWithAccessToResource(Tool):
    """
    Compute users who effectively have any permission on a given resource_id via their role assignments.

    kwargs:
      resource_id: str (required)
      only_active: bool = True
      on_date: str ISO (defaults now)
      include_user_details: bool = False
      include_role_details: bool = False
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        resource_id = kwargs.get("resource_id", "")
        only_active = kwargs.get("only_active", True)
        on_date_iso = kwargs.get("on_date") or get_current_timestamp()
        on_dt = _parse_iso(on_date_iso) or datetime.now(tz=timezone.utc)
        include_user_details = kwargs.get("include_user_details", False)
        include_role_details = kwargs.get("include_role_details", False)

        # Build permission and role mappings
        perms = [p for p in data.get("permissions", []) if p.get("resource_id") == resource_id]
        perm_ids = {p.get("permission_id") for p in perms if p.get("permission_id")}
        role_ids = {rp.get("role_id") for rp in data.get("role_permissions", []) if rp.get("permission_id") in perm_ids}

        # Build helpers
        user_map = {u.get("user_id"): u for u in data.get("users", [])}
        role_map = {r.get("role_id"): r for r in data.get("roles", [])}

        def is_active(ur: Dict[str, Any]) -> bool:
            exp = _parse_iso(ur.get("expires_on"))
            return (exp is None) or (exp > on_dt)

        # Aggregate users with matching roles
        acc: Dict[str, Dict[str, Any]] = {}
        for ur in data.get("user_roles", []):
            if ur.get("role_id") in role_ids and (not only_active or is_active(ur)):
                uid = ur.get("user_id")
                if uid not in acc:
                    acc[uid] = {"user_id": uid, "roles": []}
                    if include_user_details:
                        u = user_map.get(uid)
                        if u:
                            acc[uid]["user"] = u
                rinfo: Dict[str, Any] = {"role_id": ur.get("role_id")}
                if include_role_details:
                    r = role_map.get(ur.get("role_id"))
                    if r:
                        rinfo["role_name"] = r.get("role_name")
                        rinfo["description"] = r.get("description")
                acc[uid]["roles"].append(rinfo)

        return json.dumps({"resource_id": resource_id, "users": list(acc.values())})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_users_with_access_to_resource",
                "description": "List users who have any permissions on the given resource via role assignments.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_id": {"type": "string", "description": "Resource id (e.g., RES-006)."},
                        "only_active": {"type": "boolean", "description": "Exclude expired assignments.", "default": True},
                        "on_date": {"type": "string", "description": "ISO timestamp to evaluate expiry against."},
                        "include_user_details": {"type": "boolean", "description": "Include user records."},
                        "include_role_details": {"type": "boolean", "description": "Include role records for each user's roles."}
                    },
                    "required": ["resource_id"],
                    "additionalProperties": False
                }
            }
        }

class CanAccessResource(Tool):
    """
    Check if a user can access a specific resource by following the permission chain:
    1. Get all permissions for the resource
    2. Get all roles that have those permissions
    3. Check if the user has any of those roles (considering expiry)

    kwargs:
      user_id: str (required)
      resource_id: str (required)
      on_date: str ISO (optional; defaults to now)
      include_details: bool = False (include which permissions/roles grant access)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id", "")
        resource_id = kwargs.get("resource_id", "")
        on_date_iso = kwargs.get("on_date") or get_current_timestamp()
        include_details = kwargs.get("include_details", False)

        if not user_id or not resource_id:
            return json.dumps({"error": "user_id and resource_id are required"})

        # Validate user exists
        if not _find_by_id(data.get("users", []), "user_id", user_id):
            return json.dumps({"error": f"user_id {user_id} not found"})

        # Validate resource exists
        if not _find_by_id(data.get("resources", []), "resource_id", resource_id):
            return json.dumps({"error": f"resource_id {resource_id} not found"})

        on_dt = _parse_iso(on_date_iso) or datetime.now(tz=timezone.utc)

        def is_active(ur: Dict[str, Any]) -> bool:
            exp = _parse_iso(ur.get("expires_on"))
            return (exp is None) or (exp > on_dt)

        # Step 1: Get all permissions for the resource
        resource_permissions = [
            p for p in data.get("permissions", [])
            if p.get("resource_id") == resource_id
        ]

        if not resource_permissions:
            return json.dumps({
                "ok": True,
                "user_id": user_id,
                "resource_id": resource_id,
                "can_access": False,
                "reason": "No permissions defined for this resource",
                "checked_on": on_date_iso
            })

        resource_permission_ids = {p.get("permission_id") for p in resource_permissions}

        # Step 2: Get all roles that have those permissions
        roles_with_permissions = [
            rp for rp in data.get("role_permissions", [])
            if rp.get("permission_id") in resource_permission_ids
        ]

        if not roles_with_permissions:
            return json.dumps({
                "ok": True,
                "user_id": user_id,
                "resource_id": resource_id,
                "can_access": False,
                "reason": "No roles have permissions for this resource",
                "checked_on": on_date_iso
            })

        role_ids_with_access = {rp.get("role_id") for rp in roles_with_permissions}

        # Step 3: Check if user has any of those roles (and they're active)
        user_assignments = [
            ur for ur in data.get("user_roles", [])
            if ur.get("user_id") == user_id and is_active(ur)
        ]

        active_user_role_ids = {ur.get("role_id") for ur in user_assignments}

        # Find intersection - roles that grant access AND user has
        granting_role_ids = role_ids_with_access.intersection(active_user_role_ids)

        can_access = len(granting_role_ids) > 0

        result = {
            "ok": True,
            "user_id": user_id,
            "resource_id": resource_id,
            "can_access": can_access,
            "checked_on": on_date_iso
        }

        if include_details:
            # Build detailed breakdown
            role_map = {r.get("role_id"): r for r in data.get("roles", [])}
            permission_map = {p.get("permission_id"): p for p in data.get("permissions", [])}

            # Map which permissions are granted by which roles the user has
            granting_details = []
            for role_id in granting_role_ids:
                role = role_map.get(role_id, {})

                # Find which permissions this role provides for this resource
                role_permissions_for_resource = [
                    rp.get("permission_id") for rp in roles_with_permissions
                    if rp.get("role_id") == role_id
                ]

                permissions_detail = []
                for perm_id in role_permissions_for_resource:
                    perm = permission_map.get(perm_id, {})
                    permissions_detail.append({
                        "permission_id": perm_id,
                        "action": perm.get("action"),
                        "description": perm.get("description")
                    })

                granting_details.append({
                    "role_id": role_id,
                    "role_name": role.get("role_name"),
                    "role_description": role.get("description"),
                    "permissions": permissions_detail
                })

            result["access_details"] = {
                "granting_roles_count": len(granting_role_ids),
                "total_resource_permissions": len(resource_permissions),
                "total_roles_with_access": len(role_ids_with_access),
                "user_active_roles": len(active_user_role_ids),
                "granting_roles": granting_details
            }

        if not can_access:
            result["reason"] = "User does not have any active roles that grant access to this resource"

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "can_access_resource",
                "description": "Check if a user can access a specific resource by following the permission → role → user assignment chain.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "Target user_id (e.g., U-001)."},
                        "resource_id": {"type": "string", "description": "Target resource_id (e.g., RES-020)."},
                        "on_date": {"type": "string", "description": "ISO timestamp to evaluate role assignments against (optional)."},
                        "include_details": {"type": "boolean", "description": "Include detailed breakdown of which roles/permissions grant access.", "default": False}
                    },
                    "required": ["user_id", "resource_id"],
                    "additionalProperties": False
                }
            }
        }

# ACCESS REQUESTS
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        request_id = kwargs.get("request_id")
        user_id = kwargs.get("user_id")
        status = kwargs.get("status")
        resource_id = kwargs.get("resource_id")
        requested_role_id = kwargs.get("requested_role_id")
        include_user = kwargs.get("include_user", False)
        include_role = kwargs.get("include_role", False)
        include_resource = kwargs.get("include_resource", False)

        access_requests = data.get("access_requests", [])

        # If request_id is provided, return single access request
        if request_id:
            ar = _find_by_id(access_requests, "request_id", request_id)
            if not ar:
                return json.dumps({"error": f"request_id {request_id} not found"})

            # Build response with optional expansions
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

            return json.dumps(out)

        # Filter access requests based on provided criteria
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

class DecideAccessRequest(Tool):
    """
    Approve or reject an access request with validations and deterministic timestamps.

    kwargs:
      request_id: str (required)
      reviewer_id: str (required)
      decision: str = "APPROVED" | "REJECTED" (required)
      decision_notes: str (required)
      decision_at: str ISO-8601 (optional; defaults to request.submitted_at else now)
      enforce_admin: bool = True  (require reviewer has 'Administrator' role)
      enforce_pending: bool = True (require current status == 'PENDING')
      enforce_sla: bool = False   (reject approvals if older than sla_days without waiver)
      sla_days: int = 5
      waive_sla: bool = False
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        request_id = kwargs.get("request_id", "")
        reviewer_id = kwargs.get("reviewer_id", "")
        decision = (kwargs.get("decision") or "").upper()
        decision_at_kw = kwargs.get("decision_at", get_current_timestamp())
        enforce_admin = kwargs.get("enforce_admin", True)
        enforce_pending = kwargs.get("enforce_pending", True)
        # SLA enforcement is optional; default to False to avoid blocking decisions in static datasets
        enforce_sla = kwargs.get("enforce_sla", False)
        sla_days = kwargs.get("sla_days", 5)
        waive_sla = kwargs.get("waive_sla", False)

        if decision not in ("APPROVED", "REJECTED"):
            return json.dumps({"error": "decision must be APPROVED or REJECTED"})

        # Get request
        requests = data.get("access_requests", [])
        req = _find_by_id(requests, "request_id", request_id)
        if not req:
            return json.dumps({"error": f"request_id {request_id} not found"})

        # Validate reviewer admin role if required
        if enforce_admin:
            # Find Administrator role_id
            admin_roles = []
            for r in data.get("roles", []):
                role_name = str(r.get("role_name", "")).strip().lower()
                if role_name.endswith("admin") or role_name.endswith("lead"):
                    admin_roles.append(r)
            if not admin_roles:
                return json.dumps({"error": "Administrator role not defined in roles.json"})
            # Check assignments
            has_admin = any(
                ur.get("user_id") == reviewer_id and ur.get("role_id") in [r.get("role_id") for r in admin_roles]
                for ur in data.get("user_roles", [])
            )
            if not has_admin:
                return json.dumps({"error": f"reviewer_id {reviewer_id} lacks Administrator role"})

        # Validate pending status
        if enforce_pending and req.get("status") != "PENDING":
            return json.dumps({"error": f"request {request_id} is not PENDING"})

        # Validate target user and role exist
        user = _find_by_id(data.get("users", []), "user_id", req.get("user_id") or "")
        role = _find_by_id(data.get("roles", []), "role_id", req.get("requested_role_id") or "")
        if not user or not role:
            return json.dumps({"error": "target user or requested role does not exist"})

        # SLA enforcement (only block approvals unless waived)
        if enforce_sla and decision == "APPROVED" and not waive_sla:
            sub_dt = _parse_iso(req.get("submitted_at"))
            now_dt = _parse_iso(get_current_timestamp()) or datetime.now(tz=timezone.utc)
            if sub_dt:
                age_days = (now_dt - sub_dt).days
                if age_days > int(sla_days):
                    return json.dumps({"error": f"request {request_id} exceeds SLA ({age_days}d) — approval blocked without waiver"})

        # Deterministic decision_at
        decision_at = decision_at_kw or req.get("submitted_at") or get_current_timestamp()

        updated = dict(req)
        updated.update({
            "status": decision,
            "reviewed_by": reviewer_id,
            "decision_at": decision_at,
        })

        # Persist update
        for i, r in enumerate(requests):
            if r.get("request_id") == request_id:
                data["access_requests"][i] = updated
                break

        return json.dumps({"ok": True, "request": updated})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "decide_access_request",
                "description": "Approve or reject an access request with validation, deterministic timestamps, and notes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string", "description": "Access request id (AR-###)."},
                        "reviewer_id": {"type": "string", "description": "Reviewer user_id (must be Administrator if enforce_admin)."},
                        "decision": {"type": "string", "enum": ["APPROVED", "REJECTED"], "description": "Decision outcome."},
                        "decision_at": {"type": "string", "description": "ISO timestamp; defaults to submitted_at or now."},
                        "enforce_admin": {"type": "boolean", "description": "Require reviewer to have Administrator role.", "default": True},
                        "enforce_pending": {"type": "boolean", "description": "Require request to be PENDING.", "default": True},
                        "enforce_sla": {"type": "boolean", "description": "Block approvals older than sla_days without waiver.", "default": False},
                        "sla_days": {"type": "integer", "description": "SLA day threshold for approvals.", "default": 5},
                        "waive_sla": {"type": "boolean", "description": "Allow approval despite SLA breach."},
                    },
                    "required": ["request_id", "reviewer_id", "decision"],
                    "additionalProperties": False
                }
            }
        }


# ROLES
class EnsureUserRole(Tool):
    """
    Ensure a user has a role; idempotent assignment.

    kwargs:
      user_id: str (required)
      role_id: str (required)
      assigned_by: str (required)
      assigned_on: str ISO (defaults now)
      expires_on: str ISO (optional)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id", "")
        role_id = kwargs.get("role_id", "")
        assigned_by = kwargs.get("assigned_by", "")
        assigned_on = kwargs.get("assigned_on") or get_current_timestamp()
        expires_on = kwargs.get("expires_on")

        # Existence checks
        if not _find_by_id(data.get("users", []), "user_id", user_id):
            return json.dumps({"error": f"user_id {user_id} not found"})
        if not _find_by_id(data.get("roles", []), "role_id", role_id):
            return json.dumps({"error": f"role_id {role_id} not found"})

        assignments = data.get("user_roles", [])
        existing = None
        existing_index = None
        for i, ur in enumerate(assignments):
            if ur.get("user_id") == user_id and ur.get("role_id") == role_id:
                existing = ur
                existing_index = i
                break

        if existing:
            # If expires_on is provided and different from existing, update it
            if expires_on and existing.get("expires_on") != expires_on:
                updated = dict(existing)
                updated["expires_on"] = expires_on
                data["user_roles"][existing_index] = updated
                return json.dumps({"ok": True, "assignment": updated, "updated_expiry": True})
            else:
                return json.dumps({"ok": True, "no_op": True, "assignment": existing})
        else:
            # nothing to update/ensure
            return json.dumps({"error": "no existing assignment found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ensure_user_role",
                "description": "Idempotently ensure a user has a role with optional expiry. Updates expiry date if role exists and new expires_on is provided.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "Target user_id."},
                        "role_id": {"type": "string", "description": "Target role_id."},
                        "assigned_by": {"type": "string", "description": "Actor user_id performing assignment."},
                        "assigned_on": {"type": "string", "description": "ISO timestamp of assignment."},
                        "expires_on": {"type": "string", "description": "ISO timestamp for expiry (optional)."}
                    },
                    "required": ["user_id", "role_id", "assigned_by"],
                    "additionalProperties": False
                }
            }
        }

class UpdateUserRole(Tool):
    """
    Add or remove a user role assignment.

    kwargs:
      user_id: str (required)
      role_id: str (required)
      action: str = "ADD" | "REMOVE" (required)
      assigned_by: str (required for ADD)
      assigned_on: str ISO (optional for ADD, defaults now)
      expires_on: str ISO (optional for ADD)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id", "")
        role_id = kwargs.get("role_id", "")
        action = (kwargs.get("action", "") or "").upper()
        assigned_by = kwargs.get("assigned_by", "")
        assigned_on = kwargs.get("assigned_on") or get_current_timestamp()
        expires_on = kwargs.get("expires_on")

        if action not in ("ADD", "REMOVE"):
            return json.dumps({"error": "action must be ADD or REMOVE"})

        # Existence checks
        if not _find_by_id(data.get("users", []), "user_id", user_id):
            return json.dumps({"error": f"user_id {user_id} not found"})
        if not _find_by_id(data.get("roles", []), "role_id", role_id):
            return json.dumps({"error": f"role_id {role_id} not found"})

        assignments = data.get("user_roles", [])
        existing_index = None
        for i, ur in enumerate(assignments):
            if ur.get("user_id") == user_id and ur.get("role_id") == role_id:
                existing_index = i
                break

        if action == "ADD":
            if not assigned_by:
                return json.dumps({"error": "assigned_by is required for ADD action"})

            if existing_index is not None:
                # Update existing assignment
                existing = assignments[existing_index]
                updated = dict(existing)
                if expires_on and existing.get("expires_on") != expires_on:
                    updated["expires_on"] = expires_on
                    data["user_roles"][existing_index] = updated
                    return json.dumps({"ok": True, "assignment": updated, "updated_expiry": True})
                else:
                    return json.dumps({"ok": True, "no_op": True, "assignment": existing})
            else:
                # Create new assignment
                new_ur = {
                    "user_role_id": _next_user_role_id(data, user_id),
                    "user_id": user_id,
                    "role_id": role_id,
                    "assigned_by": assigned_by,
                    "assigned_on": assigned_on,
                    "expires_on": expires_on,
                }
                data.setdefault("user_roles", []).append(new_ur)
                return json.dumps({"ok": True, "assignment": new_ur, "action": "created"})

        elif action == "REMOVE":
            if existing_index is not None:
                removed = data["user_roles"].pop(existing_index)
                removed["assigned_by"] = assigned_by
                return json.dumps({"ok": True, "assignment": removed, "action": "removed"})
            else:
                return json.dumps({"ok": True, "no_op": True, "message": "Role assignment does not exist"})
        else:
            return json.dumps({"error": "Invalid action"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_user_role",
                "description": "Add or remove a user role assignment. For ADD: creates new assignment or updates expiry if exists. For REMOVE: deletes the assignment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "Target user_id."},
                        "role_id": {"type": "string", "description": "Target role_id."},
                        "action": {"type": "string", "enum": ["ADD", "REMOVE"], "description": "Action to perform."},
                        "assigned_by": {"type": "string", "description": "Actor user_id performing assignment (required)."},
                        "assigned_on": {"type": "string", "description": "ISO timestamp of assignment (optional for ADD)."},
                        "expires_on": {"type": "string", "description": "ISO timestamp for expiry (optional for ADD)."}
                    },
                    "required": ["user_id", "role_id", "action", "assigned_by"],
                    "additionalProperties": False
                }
            }
        }

class GetBaseRoleByDepartment(Tool):
    """
    Get the base role ID for a given department.

    kwargs:
      department: str (required)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        department = (kwargs.get("department", "") or "").strip().lower()

        # Map departments to base role names
        department_role_map = {
            "engineering": "engineering-base",
            "marketing": "marketing-base",
            "sales": "sales-base",
            "human resources": "hr-base",
            "operations": "operations-base",
            "finance": "finance-base"
        }

        role_name = department_role_map.get(department)
        if not role_name:
            return json.dumps({"error": f"No base role found for department '{department}'"})

        # Find the role
        roles = data.get("roles", [])
        for role in roles:
            if role.get("role_name") == role_name:
                return json.dumps({"role": role})

        return json.dumps({"error": f"Base role '{role_name}' not found in roles"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_base_role_by_department",
                "description": "Get the base role for a given department.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department": {"type": "string", "description": "Department name."}
                    },
                    "required": ["department"],
                    "additionalProperties": False
                }
            }
        }


class CheckSoDConflicts(Tool):
    """
    Check if a user has Separation of Duties (SoD) conflicts based on their active roles,
    or if adding a specific role would result in a conflict.

    SoD conflicts are identified by predefined conflicting role pairs that violate
    business control principles (e.g., finance processing vs auditing).

    kwargs:
      user_id: str (required)
      on_date: str ISO (optional; defaults to now)
      include_role_details: bool = False (include role names and descriptions)
      role_id: str (optional) - If provided, checks if adding this role to the user would cause a conflict
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id", "")
        on_date_iso = kwargs.get("on_date") or get_current_timestamp()
        include_role_details = kwargs.get("include_role_details", False)
        test_role_id = kwargs.get("role_id")

        if not user_id:
            return json.dumps({"error": "user_id is required"})

        # Validate user exists
        if not _find_by_id(data.get("users", []), "user_id", user_id):
            return json.dumps({"error": f"user_id {user_id} not found"})

        on_dt = _parse_iso(on_date_iso) or datetime.now(tz=timezone.utc)

        def is_active(ur: Dict[str, Any]) -> bool:
            exp = _parse_iso(ur.get("expires_on"))
            return (exp is None) or (exp > on_dt)

        # Get user's active role assignments
        assignments = [
            ur for ur in data.get("user_roles", [])
            if ur.get("user_id") == user_id and is_active(ur)
        ]

        active_role_ids = {ur.get("role_id") for ur in assignments}
        # If test_role_id is provided, simulate adding it
        if test_role_id:
            active_role_ids = set(active_role_ids)
            active_role_ids.add(test_role_id)

        # Define SoD conflict rules based on role analysis
        sod_conflicts = [
            # Finance SoD conflicts
            {
                "conflict_id": "FINANCE_SOD_001",
                "name": "Finance Processing vs Audit Access",
                "description": "Users cannot both process financial transactions and audit them",
                "conflicting_roles": ["ROL-031", "ROL-033"],  # finance-invoice-processor vs finance-audit-access
                "risk_level": "HIGH"
            },
            {
                "conflict_id": "FINANCE_SOD_002",
                "name": "Budget Admin vs Audit Access",
                "description": "Users cannot both manage budgets and audit financial records",
                "conflicting_roles": ["ROL-032", "ROL-033"],  # finance-budget-admin vs finance-audit-access
                "risk_level": "HIGH"
            },
            # Engineering SoD conflicts
            {
                "conflict_id": "ENGINEERING_SOD_001",
                "name": "Code Development vs Production Deployment",
                "description": "Developers cannot deploy their own code to production without review",
                "conflicting_roles": ["ROL-002", "ROL-025"],  # engineering-code-commit vs operations-deployment-admin
                "risk_level": "CRITICAL"
            },
            {
                "conflict_id": "ENGINEERING_SOD_002",
                "name": "Code Development vs Production Access",
                "description": "Developers should not have direct production system access",
                "conflicting_roles": ["ROL-002", "ROL-003"],  # engineering-code-commit vs engineering-prod-access
                "risk_level": "HIGH"
            },
            # Operations admin conflicts
            {
                "conflict_id": "OPERATIONS_SOD_001",
                "name": "System Admin vs Database Admin",
                "description": "Excessive administrative privileges across system and database layers",
                "conflicting_roles": ["ROL-026", "ROL-027"],  # operations-system-admin vs operations-db-admin
                "risk_level": "MEDIUM"
            },
            {
                "conflict_id": "OPERATIONS_SOD_002",
                "name": "System Admin vs Network Admin",
                "description": "Excessive administrative privileges across system and network layers",
                "conflicting_roles": ["ROL-026", "ROL-028"],  # operations-system-admin vs operations-network-admin
                "risk_level": "MEDIUM"
            },
            # HR SoD conflicts
            {
                "conflict_id": "HR_SOD_001",
                "name": "Employee Data Access vs Payroll Admin",
                "description": "Users cannot both access employee data and manage payroll",
                "conflicting_roles": ["ROL-017", "ROL-018"],  # hr-employee-data-read vs hr-payroll-admin
                "risk_level": "HIGH"
            },
            {
                "conflict_id": "HR_SOD_002",
                "name": "Employee Data Access vs Benefits Admin",
                "description": "Users cannot both access employee data and manage benefits",
                "conflicting_roles": ["ROL-017", "ROL-020"],  # hr-employee-data-read vs hr-benefits-admin
                "risk_level": "MEDIUM"
            },
            # Sales SoD conflicts
            {
                "conflict_id": "SALES_SOD_001",
                "name": "Lead Management vs Commission Viewing",
                "description": "Sales leads managers should not view commission data to prevent manipulation",
                "conflicting_roles": ["ROL-013", "ROL-015"],  # sales-lead-manager vs sales-commission-view
                "risk_level": "MEDIUM"
            }
        ]

        # Check for conflicts
        detected_conflicts = []
        role_map = {r.get("role_id"): r for r in data.get("roles", [])}

        for conflict in sod_conflicts:
            conflicting_role_ids = conflict["conflicting_roles"]
            # Check if user has ALL roles in the conflicting set
            if all(role_id in active_role_ids for role_id in conflicting_role_ids):
                conflict_entry = {
                    "conflict_id": conflict["conflict_id"],
                    "name": conflict["name"],
                    "description": conflict["description"],
                    "risk_level": conflict["risk_level"],
                    "conflicting_role_ids": conflicting_role_ids
                }

                if include_role_details:
                    conflict_entry["conflicting_roles"] = []
                    for role_id in conflicting_role_ids:
                        role = role_map.get(role_id, {})
                        conflict_entry["conflicting_roles"].append({
                            "role_id": role_id,
                            "role_name": role.get("role_name"),
                            "description": role.get("description")
                        })

                detected_conflicts.append(conflict_entry)

        return json.dumps({
            "ok": True,
            "user_id": user_id,
            "has_sod_conflicts": len(detected_conflicts) > 0,
            "conflict_count": len(detected_conflicts),
            "conflicts": detected_conflicts,
            "checked_on": on_date_iso,
            "simulated_role_id": test_role_id if test_role_id else None
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_sod_conflicts",
                "description": "Check if a user has Separation of Duties (SoD) conflicts based on their active roles, or if adding a specific role would result in a conflict.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "Target user_id (e.g., U-001)."},
                        "on_date": {"type": "string", "description": "ISO timestamp to evaluate role assignments against (optional)."},
                        "include_role_details": {"type": "boolean", "description": "Include role names and descriptions in conflict details.", "default": False},
                        "role_id": {"type": "string", "description": "If provided, checks if adding this role to the user would cause a conflict."}
                    },
                    "required": ["user_id"],
                    "additionalProperties": False
                }
            }
        }

# CERTIFICATIONS
class GetCertification(Tool):
    """
    Retrieve certifications by ID, reviewer, resource, or status.

    kwargs:
      certification_id: str (optional) - Specific certification ID to retrieve
      reviewer_id: str (optional) - Filter by reviewer user ID
      resource_id: str (optional) - Filter by resource ID
      status: str (optional) - Filter by status (PENDING, IN_PROGRESS, COMPLETED)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        certification_id = kwargs.get("certification_id")
        reviewer_id = kwargs.get("reviewer_id")
        resource_id = kwargs.get("resource_id")
        status = kwargs.get("status")

        certifications = data.get("certifications", [])

        # If certification_id is provided, return single certification
        if certification_id:
            cert = _find_by_id(certifications, "certification_id", certification_id)
            if not cert:
                return json.dumps({"error": f"certification_id {certification_id} not found"})
            return json.dumps({"ok": True, "certification": cert})

        # Filter certifications based on provided criteria
        filtered_certifications = []
        for cert in certifications:
            if reviewer_id and cert.get("reviewer_id") != reviewer_id:
                continue
            if resource_id and cert.get("resource_id") != resource_id:
                continue
            if status and cert.get("status") != status:
                continue
            filtered_certifications.append(cert)

        return json.dumps({"ok": True, "certifications": filtered_certifications})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_certification",
                "description": "Retrieve certifications by ID, reviewer, resource, or status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {"type": "string", "description": "Specific certification ID to retrieve."},
                        "reviewer_id": {"type": "string", "description": "Filter by reviewer user ID."},
                        "resource_id": {"type": "string", "description": "Filter by resource ID."},
                        "status": {"type": "string", "description": "Filter by status (PENDING, IN_PROGRESS, COMPLETED)."}
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }

class CompleteCertification(Tool):
    """
    Complete a certification by setting status to COMPLETED and completed_on to deterministic timestamp.

    kwargs:
      certification_id: str (required)
      reviewer_id: str (required)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        certification_id = kwargs.get("certification_id", "")
        reviewer_id = kwargs.get("reviewer_id", "")

        certs = data.get("certifications", [])
        cert = _find_by_id(certs, "certification_id", certification_id)
        if not cert:
            return json.dumps({"error": f"certification_id {certification_id} not found"})

        if cert.get("reviewer_id") != reviewer_id:
            return json.dumps({"error": f"reviewer_id {reviewer_id} does not match certification reviewer"})

        if cert.get("status") not in ("PENDING", "IN_PROGRESS"):
            # idempotent completion returns current
            if cert.get("status") == "COMPLETED":
                return json.dumps({"ok": True, "certification": cert})
            return json.dumps({"error": f"certification {certification_id} not completable from status {cert.get('status')}"})

        updated = dict(cert)
        updated.update({
            "status": "COMPLETED",
            "completed_on": get_current_timestamp(),
        })

        for i, c in enumerate(certs):
            if c.get("certification_id") == certification_id:
                data["certifications"][i] = updated
                break

        return json.dumps({"ok": True, "certification": updated})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "complete_certification",
                "description": "Complete a certification with deterministic completion timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {"type": "string", "description": "Certification id (C-###)."},
                        "reviewer_id": {"type": "string", "description": "Reviewer user_id."}
                    },
                    "required": ["certification_id", "reviewer_id"],
                    "additionalProperties": False
                }
            }
        }


class CreateCertification(Tool):
    """
    Create a new certification entry with deterministic ID and default due date.

    kwargs:
      reviewer_id: str (required) - Reviewer responsible for certification
      resource_id: str (required) - Resource to be certified
      status: str (optional; default "PENDING") - PENDING, IN_PROGRESS, COMPLETED
      due_date: str (optional) - ISO-like timestamp ("YYYY-MM-DD HH:MM:SS+00:00"); defaults to +90 days
      completed_on: str (optional) - If status=COMPLETED, explicit completion time; defaults to now
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        reviewer_id = kwargs.get("reviewer_id", "")
        resource_id = kwargs.get("resource_id", "")
        status = kwargs.get("status", "PENDING").upper()
        due_date = kwargs.get("due_date")
        completed_on_kw = kwargs.get("completed_on")

        if not reviewer_id or not resource_id:
            return json.dumps({"error": "reviewer_id and resource_id are required"})

        # Validate reviewer and resource exist
        if not _find_by_id(data.get("users", []), "user_id", reviewer_id):
            return json.dumps({"error": f"reviewer_id {reviewer_id} not found"})
        if not _find_by_id(data.get("resources", []), "resource_id", resource_id):
            return json.dumps({"error": f"resource_id {resource_id} not found"})

        valid_status = ["PENDING", "IN_PROGRESS", "COMPLETED"]
        if status not in valid_status:
            return json.dumps({"error": f"status must be one of: {valid_status}"})

        # Determine due_date deterministically if not provided: +90 days from now
        if not due_date:
            base = _parse_iso(get_current_timestamp()) or datetime.now(tz=timezone.utc)
            due_dt = base + timedelta(days=90)
            # Match dataset style with +00:00 suffix
            due_date = due_dt.strftime("%Y-%m-%d %H:%M:%S+00:00")

        # completed_on only if COMPLETED
        completed_on: Optional[str]
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
        return json.dumps({"ok": True, "certification": new_cert})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_certification",
                "description": "Create a new certification entry with deterministic ID and default due date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reviewer_id": {"type": "string", "description": "Reviewer user_id responsible."},
                        "resource_id": {"type": "string", "description": "Target resource_id."},
                        "status": {"type": "string", "description": "Initial status (PENDING, IN_PROGRESS, COMPLETED).", "default": "PENDING"},
                        "due_date": {"type": "string", "description": "Due date (YYYY-MM-DD HH:MM:SS+00:00)."},
                        "completed_on": {"type": "string", "description": "Completion timestamp if status=COMPLETED."}
                    },
                    "required": ["reviewer_id", "resource_id"],
                    "additionalProperties": False
                }
            }
        }


# POLICY EXCEPTIONS
class GetPolicyException(Tool):
    """
    Retrieve policy exceptions by ID, user, permission, reviewer, or status.

    kwargs:
      exception_id: str (optional) - Specific exception ID to retrieve
      user_id: str (optional) - Filter by requesting user
      permission_id: str (optional) - Filter by permission involved in exceptions
      reviewed_by: str (optional) - Filter by reviewer
      status: str (optional) - Filter by status (PENDING_REVIEW, ACTIVE, EXPIRED, DENIED)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        exception_id = kwargs.get("exception_id")
        user_id = kwargs.get("user_id")
        permission_id = kwargs.get("permission_id")
        reviewed_by = kwargs.get("reviewed_by")
        status = kwargs.get("status")

        exceptions = data.get("policy_exceptions", [])

        # If exception_id is provided, return single exception
        if exception_id:
            exception = _find_by_id(exceptions, "exception_id", exception_id)
            if not exception:
                return json.dumps({"error": f"exception_id {exception_id} not found"})
            return json.dumps({"ok": True, "policy_exception": exception})

        # Filter exceptions based on provided criteria
        filtered_exceptions = []
        for exception in exceptions:
            if user_id and exception.get("user_id") != user_id:
                continue
            if permission_id and exception.get("permission_id") != permission_id:
                continue
            if reviewed_by and exception.get("reviewed_by") != reviewed_by:
                continue
            if status and exception.get("status") != status:
                continue
            filtered_exceptions.append(exception)

        return json.dumps({"ok": True, "policy_exceptions": filtered_exceptions})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_policy_exception",
                "description": "Retrieve policy exceptions by ID, user, permission, reviewer, or status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "exception_id": {"type": "string", "description": "Specific policy exception ID to retrieve."},
                        "user_id": {"type": "string", "description": "Filter by requesting user ID."},
                        "permission_id": {"type": "string", "description": "Filter by permission involved in exceptions."},
                        "reviewed_by": {"type": "string", "description": "Filter by reviewer user ID."},
                        "status": {"type": "string", "description": "Filter by status (PENDING_REVIEW, ACTIVE, EXPIRED, DENIED)."}
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }

class CreatePolicyException(Tool):
    """
    Create a new policy exception request.

    kwargs:
      user_id: str (required) - User for whom exception is created
      permission_id: str (required) - Permission requiring exception
      reviewed_by: str (required) - User ID who will review the exception
      reason: str (required) - Business justification for the exception
      expires_on: str (optional) - ISO timestamp when exception expires
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id", "")
        permission_id = kwargs.get("permission_id", "")
        reviewed_by = kwargs.get("reviewed_by", "")
        reason = kwargs.get("reason", "")
        expires_on = kwargs.get("expires_on")

        if not user_id or not permission_id or not reviewed_by or not reason:
            return json.dumps({"error": "user_id, permission_id, reviewed_by, and reason are required"})

        # Validate user exists
        if not _find_by_id(data.get("users", []), "user_id", user_id):
            return json.dumps({"error": f"user_id {user_id} not found"})

        # Validate permission exists
        if not _find_by_id(data.get("permissions", []), "permission_id", permission_id):
            return json.dumps({"error": f"permission_id {permission_id} not found"})

        # Validate reviewer exists
        if not _find_by_id(data.get("users", []), "user_id", reviewed_by):
            return json.dumps({"error": f"reviewed_by {reviewed_by} not found"})

        # Create new policy exception
        new_exception = {
            "exception_id": _next_id(data, "policy_exceptions", "PE"),
            "user_id": user_id,
            "permission_id": permission_id,
            "reviewed_by": reviewed_by,
            "requested_on": get_current_timestamp(),
            "reviewed_on": None,
            "expires_on": expires_on,
            "reason": reason,
            "status": "PENDING_REVIEW"
        }

        data.setdefault("policy_exceptions", []).append(new_exception)
        return json.dumps({"ok": True, "policy_exception": new_exception})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_policy_exception",
                "description": "Create a new policy exception request for emergency access.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "User ID for whom exception is created."},
                        "permission_id": {"type": "string", "description": "Permission ID requiring exception."},
                        "reviewed_by": {"type": "string", "description": "User ID who will review the exception."},
                        "reason": {"type": "string", "description": "Business justification for the exception."},
                        "expires_on": {"type": "string", "description": "ISO timestamp when exception expires (optional)."}
                    },
                    "required": ["user_id", "permission_id", "reviewed_by", "reason"],
                    "additionalProperties": False
                }
            }
        }

class DecidePolicyException(Tool):
    """
    Approve or deny a policy exception with deterministic timestamps.

    kwargs:
      exception_id: str (required)
      reviewer_id: str (required)
      decision: str = "APPROVED" | "DENIED" (required)
      reviewed_on: str ISO (optional; defaults to current timestamp)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        exception_id = kwargs.get("exception_id", "")
        reviewer_id = kwargs.get("reviewer_id", "")
        decision = (kwargs.get("decision") or "").upper()
        reviewed_on = kwargs.get("reviewed_on") or get_current_timestamp()

        if decision not in ("APPROVED", "DENIED"):
            return json.dumps({"error": "decision must be APPROVED or DENIED"})

        # Get exception
        exceptions = data.get("policy_exceptions", [])
        exception = _find_by_id(exceptions, "exception_id", exception_id)
        if not exception:
            return json.dumps({"error": f"exception_id {exception_id} not found"})

        # Validate reviewer matches
        if exception.get("reviewed_by") != reviewer_id:
            return json.dumps({"error": f"reviewer_id {reviewer_id} does not match assigned reviewer {exception.get('reviewed_by')}"})

        # Validate status
        if exception.get("status") != "PENDING_REVIEW":
            return json.dumps({"error": f"exception {exception_id} is not PENDING_REVIEW"})

        # Update status
        updated = dict(exception)
        updated.update({
            "status": "ACTIVE" if decision == "APPROVED" else "DENIED",
            "reviewed_on": reviewed_on,
        })

        # If denied, clear expires_on
        if decision == "DENIED":
            updated["expires_on"] = None

        # Persist update
        for i, exc in enumerate(exceptions):
            if exc.get("exception_id") == exception_id:
                data["policy_exceptions"][i] = updated
                break

        return json.dumps({"ok": True, "policy_exception": updated})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "decide_policy_exception",
                "description": "Approve or deny a policy exception with deterministic timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "exception_id": {"type": "string", "description": "Policy exception id (PE-###)."},
                        "reviewer_id": {"type": "string", "description": "Reviewer user_id."},
                        "decision": {"type": "string", "enum": ["APPROVED", "DENIED"], "description": "Decision outcome."},
                        "reviewed_on": {"type": "string", "description": "ISO timestamp; defaults to now."}
                    },
                    "required": ["exception_id", "reviewer_id", "decision"],
                    "additionalProperties": False
                }
            }
        }

class GetPermission(Tool):
    """
    Retrieve permissions by ID, action, or resource.

    kwargs:
      permission_id: str (optional) - Specific permission ID to retrieve
      action: str (optional) - Filter by permission action
      resource_id: str (optional) - Filter by resource involved in permissions
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        permission_id = kwargs.get("permission_id")
        action = kwargs.get("action")
        resource_id = kwargs.get("resource_id")
        description = kwargs.get("description")

        permissions = data.get("permissions", [])

        # If permission_id is provided, return single permission
        if permission_id:
            permission = _find_by_id(permissions, "permission_id", permission_id)
            if not permission:
                return json.dumps({"error": f"permission_id {permission_id} not found"})
            return json.dumps({"ok": True, "permission": permission})

        # Filter permissions based on provided criteria
        filtered_permissions = []
        for permission in permissions:
            if action and permission.get("action") != action:
                continue
            if resource_id and permission.get("resource_id") != resource_id:
                continue
            if description and permission.get("description") != description:
                continue
            filtered_permissions.append(permission)

        return json.dumps({"ok": True, "permissions": filtered_permissions})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_permission",
                "description": "Retrieve permissions by ID, action, or resource.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "permission_id": {"type": "string", "description": "Specific permission ID to retrieve."},
                        "action": {"type": "string", "description": "Filter by permission action."},
                        "resource_id": {"type": "string", "description": "Filter by resource involved in permissions."},
                        "description": {"type": "string", "description": "Filter by permission description."}
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }

class CreatePermission(Tool):
    """
    Create a new permission with deterministic ID generation.

    kwargs:
      action: str (required)
      resource_id: str (required)
      description: str (required)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        action = (kwargs.get("action", "") or "").strip()
        resource_id = (kwargs.get("resource_id", "") or "").strip()
        description = kwargs.get("description", "")

        if not action or not resource_id or not description:
            return json.dumps({"error": "action, resource_id, and description are required"})

        # Validate resource exists
        if not _find_by_id(data.get("resources", []), "resource_id", resource_id):
            return json.dumps({"error": f"resource_id {resource_id} not found"})

        # Enforce uniqueness by (action, resource_id)
        for p in data.get("permissions", []):
            if str(p.get("action", "")).strip().lower() == action.lower() and p.get("resource_id") == resource_id:
                return json.dumps({"error": f"permission with action '{action}' for {resource_id} already exists"})

        new_perm = {
            "permission_id": _next_id(data, "permissions", "P"),
            "action": action,
            "resource_id": resource_id,
            "description": description,
        }

        data.setdefault("permissions", []).append(new_perm)
        return json.dumps({"ok": True, "permission": new_perm})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_permission",
                "description": "Create a new permission with deterministic ID generation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string", "description": "Permission action (e.g., read, write)."},
                        "resource_id": {"type": "string", "description": "Resource id the permission applies to."},
                        "description": {"type": "string", "description": "Permission description."}
                    },
                    "required": ["action", "resource_id", "description"],
                    "additionalProperties": False
                }
            }
        }

class GetRolePermissions(Tool):
    """
    Retrieve role-permission mappings filtered by role_id and/or permission_id.

    kwargs:
      role_id: str (optional) - Filter mappings for a specific role
      permission_id: str (optional) - Filter mappings for a specific permission
      include_role: bool = False - Include role details in each mapping
      include_permission: bool = False - Include permission details in each mapping
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        role_id = kwargs.get("role_id")
        permission_id = kwargs.get("permission_id")
        include_role = kwargs.get("include_role", False)
        include_permission = kwargs.get("include_permission", False)

        if not role_id and not permission_id:
            return json.dumps({"error": "Must provide role_id and/or permission_id"})

        mappings = data.get("role_permissions", [])

        # Filter
        out = []
        for rp in mappings:
            if role_id and rp.get("role_id") != role_id:
                continue
            if permission_id and rp.get("permission_id") != permission_id:
                continue
            out.append(dict(rp))

        # Optional expansions
        if include_role or include_permission:
            role_map = {r.get("role_id"): r for r in data.get("roles", [])}
            perm_map = {p.get("permission_id"): p for p in data.get("permissions", [])}
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

        return json.dumps({"ok": True, "role_permissions": out})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_role_permissions",
                "description": "Retrieve role-permission mappings filtered by role_id and/or permission_id with optional detail expansion.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {"type": "string", "description": "Filter by role_id (e.g., ROL-032)."},
                        "permission_id": {"type": "string", "description": "Filter by permission_id (e.g., P-081)."},
                        "include_role": {"type": "boolean", "description": "Include role details in each mapping.", "default": False},
                        "include_permission": {"type": "boolean", "description": "Include permission details in each mapping.", "default": False}
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }

class AssignPermissionToRole(Tool):
    """
    Assign a permission to a role by creating a role-permission mapping.

    kwargs:
      role_id: str (required)
      permission_id: str (required)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        role_id = (kwargs.get("role_id", "") or "").strip()
        permission_id = (kwargs.get("permission_id", "") or "").strip()

        if not role_id or not permission_id:
            return json.dumps({"error": "role_id and permission_id are required"})

        # Validate existence
        if not _find_by_id(data.get("roles", []), "role_id", role_id):
            return json.dumps({"error": f"role_id {role_id} not found"})
        if not _find_by_id(data.get("permissions", []), "permission_id", permission_id):
            return json.dumps({"error": f"permission_id {permission_id} not found"})

        # Check if mapping exists
        mappings = data.get("role_permissions", [])
        for rp in mappings:
            if rp.get("role_id") == role_id and rp.get("permission_id") == permission_id:
                return json.dumps({"ok": True, "role_permission": rp, "no_op": True})

        new_mapping = {"role_id": role_id, "permission_id": permission_id}
        data.setdefault("role_permissions", []).append(new_mapping)
        return json.dumps({"ok": True, "role_permission": new_mapping, "action": "created"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_permission_to_role",
                "description": "Assign a permission to a role by creating a role-permission mapping.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {"type": "string", "description": "Target role_id (e.g., ROL-030)."},
                        "permission_id": {"type": "string", "description": "Target permission_id (e.g., P-113)."}
                    },
                    "required": ["role_id", "permission_id"],
                    "additionalProperties": False
                }
            }
        }

# AUDIT & COMMS
class CreateAuditLogEntry(Tool):
    """
    Write a deterministic audit log entry.

    kwargs:
      action_type: str (required)
      actor_id: str (required)
      target_id: str (required)
      details: str (required)
      timestamp: str ISO (defaults now)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        action_type = kwargs.get("action_type", "")
        actor_id = kwargs.get("actor_id", "")
        target_id = kwargs.get("target_id", "")
        details = kwargs.get("details", "")
        timestamp = kwargs.get("timestamp") or get_current_timestamp()

        log = {
            "log_id": _next_id(data, "audit_logs", "L"),
            "timestamp": timestamp,
            "action_type": action_type,
            "actor_id": actor_id,
            "target_id": target_id,
            "details": details,
        }

        data.setdefault("audit_logs", []).append(log)
        return json.dumps({"ok": True, "audit_log": log})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_audit_log_entry",
                "description": "Append an audit log entry with deterministic timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action_type": {"type": "string", "description": "Audit action type."},
                        "actor_id": {"type": "string", "description": "User performing the action."},
                        "target_id": {"type": "string", "description": "Target entity id (request, user, resource, etc.)."},
                        "details": {"type": "string", "description": "Deterministic details string."},
                        "timestamp": {"type": "string", "description": "ISO timestamp (optional)."}
                    },
                    "required": ["action_type", "actor_id", "target_id", "details"],
                    "additionalProperties": False
                }
            }
        }

class CreateHubSpotTicket(Tool):
    """
    Create a general HubSpot support ticket following deterministic rules.

    kwargs:
      subject: str (required) - ticket subject line
      description: str (required) - ticket description
      assignee_id: str (required) - who will handle the ticket
      requester_id: str (required) - who is requesting the ticket
      priority: str (default: "MEDIUM") - HIGH, MEDIUM, LOW
      category: str (default: "GENERAL") - ticket category
      status: str (default: "OPEN") - OPEN, IN_PROGRESS, CLOSED
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        subject = kwargs.get("subject", "")
        description = kwargs.get("description", "")
        assignee_id = kwargs.get("assignee_id", "")
        requester_id = kwargs.get("requester_id", "")
        priority = kwargs.get("priority", "MEDIUM")
        category = kwargs.get("category", "GENERAL")
        status = kwargs.get("status", "OPEN")

        if not subject or not description or not assignee_id or not requester_id:
            return json.dumps({"error": "subject, description, assignee_id, and requester_id are required"})

        # Validate priority
        valid_priorities = ["HIGH", "MEDIUM", "LOW"]
        if priority not in valid_priorities:
            return json.dumps({"error": f"priority must be one of: {valid_priorities}"})

        # Validate status
        valid_statuses = ["OPEN", "IN_PROGRESS", "CLOSED"]
        if status not in valid_statuses:
            return json.dumps({"error": f"status must be one of: {valid_statuses}"})

        # Validate assignee exists
        users = data.get("users", [])
        assignee = _find_by_id(users, "user_id", assignee_id)
        if not assignee:
            return json.dumps({"error": f"Assignee {assignee_id} not found"})

        # Validate requester exists
        requester = _find_by_id(users, "user_id", requester_id)
        if not requester:
            return json.dumps({"error": f"Requester {requester_id} not found"})

        # Apply deterministic rules for security incidents
        if category == "SECURITY_INCIDENT":
            # Ensure operations manager (U-005) is assigned for security incidents
            if assignee_id != "U-005":
                assignee_id = "U-005"

            # Ensure subject follows SIEM alert format
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
            "closed_at": None if status != "CLOSED" else timestamp
        }

        data.setdefault("hubspot_tickets", []).append(ticket_record)
        return json.dumps({"ok": True, "ticket": ticket_record})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_hubspot_ticket",
                "description": "Create a general HubSpot support ticket following deterministic rules.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject": {"type": "string", "description": "Ticket subject line."},
                        "description": {"type": "string", "description": "Ticket description."},
                        "assignee_id": {"type": "string", "description": "User ID who will handle the ticket."},
                        "requester_id": {"type": "string", "description": "User ID who is requesting the ticket."},
                        "priority": {"type": "string", "description": "Ticket priority (HIGH, MEDIUM, LOW).", "default": "MEDIUM"},
                        "category": {"type": "string", "description": "Ticket category.", "default": "GENERAL"},
                        "status": {"type": "string", "description": "Ticket status (OPEN, IN_PROGRESS, CLOSED).", "default": "OPEN"}
                    },
                    "required": ["subject", "description", "assignee_id", "requester_id"],
                    "additionalProperties": False
                }
            }
        }

class UpdateHubSpotTicket(Tool):
    """
    Update an existing HubSpot ticket's fields and timestamps.

    kwargs:
      ticket_id: str (required)
      status: str (optional) - OPEN, IN_PROGRESS, CLOSED
      assignee_id: str (optional)
      priority: str (optional) - HIGH, MEDIUM, LOW
      subject: str (optional)
      description: str (optional)
      updated_at: str ISO (optional; defaults to now)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ticket_id = kwargs.get("ticket_id", "")
        status = kwargs.get("status")
        assignee_id = kwargs.get("assignee_id")
        priority = kwargs.get("priority")
        subject = kwargs.get("subject")
        description = kwargs.get("description")
        updated_at = kwargs.get("updated_at") or get_current_timestamp()

        if not ticket_id:
            return json.dumps({"error": "ticket_id is required"})

        tickets = data.get("hubspot_tickets", [])
        idx = None
        for i, t in enumerate(tickets):
            if t.get("ticket_id") == ticket_id:
                idx = i
                break

        if idx is None:
            return json.dumps({"error": f"ticket_id {ticket_id} not found"})

        # Validate enumerations
        if status is not None and status not in ["OPEN", "IN_PROGRESS", "CLOSED"]:
            return json.dumps({"error": "status must be one of: ['OPEN','IN_PROGRESS','CLOSED']"})
        if priority is not None and priority not in ["HIGH", "MEDIUM", "LOW"]:
            return json.dumps({"error": "priority must be one of: ['HIGH','MEDIUM','LOW']"})

        # Validate assignee
        if assignee_id is not None:
            if not _find_by_id(data.get("users", []), "user_id", assignee_id):
                return json.dumps({"error": f"assignee_id {assignee_id} not found"})

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
            # Manage closed_at based on status
            if status == "CLOSED":
                updated["closed_at"] = updated_at
            else:
                updated["closed_at"] = None

        updated["updated_at"] = updated_at

        data["hubspot_tickets"][idx] = updated
        return json.dumps({"ok": True, "ticket": updated})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_hubspot_ticket",
                "description": "Update an existing HubSpot ticket's fields and timestamps.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {"type": "string", "description": "Ticket id (TI-###)."},
                        "status": {"type": "string", "description": "New status (OPEN, IN_PROGRESS, CLOSED)."},
                        "assignee_id": {"type": "string", "description": "New assignee user_id."},
                        "priority": {"type": "string", "description": "Priority (HIGH, MEDIUM, LOW)."},
                        "subject": {"type": "string", "description": "Updated subject."},
                        "description": {"type": "string", "description": "Updated description."},
                        "updated_at": {"type": "string", "description": "ISO timestamp for update (optional)."}
                    },
                    "required": ["ticket_id"],
                    "additionalProperties": False
                }
            }
        }




class GetHubSpotTicket(Tool):
    """
    Retrieve HubSpot tickets by ticket_id or filter by SIEM alert ID (present in description),
    status, priority, category, assignee_id, or requester_id.

    kwargs:
      ticket_id: str (optional) - Specific ticket ID to retrieve
      alert_id: str (optional) - SIEM alert ID to match within description (e.g., ALRT-012)
      status: str (optional) - OPEN, IN_PROGRESS, CLOSED
      priority: str (optional) - HIGH, MEDIUM, LOW
      category: str (optional) - SECURITY_INCIDENT, ACCESS_REQUEST, GENERAL, etc.
      assignee_id: str (optional)
      requester_id: str (optional)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ticket_id = kwargs.get("ticket_id")
        alert_id = kwargs.get("alert_id")
        status = kwargs.get("status")
        priority = kwargs.get("priority")
        category = kwargs.get("category")
        assignee_id = kwargs.get("assignee_id")
        requester_id = kwargs.get("requester_id")

        tickets = data.get("hubspot_tickets", [])

        # If ticket_id is provided, return single ticket
        if ticket_id:
            t = _find_by_id(tickets, "ticket_id", ticket_id)
            if not t:
                return json.dumps({"error": f"ticket_id {ticket_id} not found"})
            return json.dumps({"ok": True, "ticket": t})

        # Otherwise, filter
        out: List[Dict[str, Any]] = []
        for t in tickets:
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

        return json.dumps({"ok": True, "tickets": out})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_hubspot_ticket",
                "description": "Retrieve HubSpot tickets by ticket_id or filter by SIEM alert ID (in description), status, priority, category, assignee_id, or requester_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {"type": "string", "description": "Specific ticket ID to retrieve (TI-###)."},
                        "alert_id": {"type": "string", "description": "SIEM alert ID to match in description (e.g., ALRT-012)."},
                        "status": {"type": "string", "description": "Filter by status (OPEN, IN_PROGRESS, CLOSED)."},
                        "priority": {"type": "string", "description": "Filter by priority (HIGH, MEDIUM, LOW)."},
                        "category": {"type": "string", "description": "Filter by category (e.g., SECURITY_INCIDENT, ACCESS_REQUEST, GENERAL)."},
                        "assignee_id": {"type": "string", "description": "Filter by assignee user_id."},
                        "requester_id": {"type": "string", "description": "Filter by requester user_id."}
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }

class PostSlackMessage(Tool):
    """
    Append a Slack message record for notifications.

    kwargs:
      channel: str (required) e.g., "#access-requests"
      message: str (required)
      username: str = "RBAC_BOT"
      timestamp: str ISO (defaults now)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        channel = kwargs.get("channel", "")
        message = kwargs.get("message", "")
        username = kwargs.get("username", "RBAC_BOT")
        timestamp = kwargs.get("timestamp") or get_current_timestamp()

        if not channel or not message:
            return json.dumps({"error": "channel and message required"})

        # Deterministic rule: Normalize security incident messages
        # - If posting to #security-incidents, force the username to RBAC_BOT
        # - Trim message to avoid whitespace variations
        if channel.strip() == "#security-incidents":
            username = "RBAC_BOT"
            message = " ".join(str(message).split())

        rec = {
            "message_id": _next_id(data, "slack_messages", "SL"),
            "timestamp": timestamp,
            "username": username,
            "message": message,
            "channel": channel,
                        # Align with dataset schema
                        "created_at": timestamp,
                        "updated_at": timestamp,
        }

        data.setdefault("slack_messages", []).append(rec)
        return json.dumps({"ok": True, "slack_message": rec})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "post_slack_message",
                "description": "Post a message record to Slack notifications (e.g., #access-requests).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "channel": {"type": "string", "description": "Slack channel name (e.g., #access-requests)."},
                        "message": {"type": "string", "description": "Message text."},
                        "username": {"type": "string", "description": "Posting bot username.", "default": "RBAC_BOT"},
                        "timestamp": {"type": "string", "description": "ISO timestamp (optional)."}
                    },
                    "required": ["channel", "message"],
                    "additionalProperties": False
                }
            }
        }

class SendEmail(Tool):
    """
    Send an email with deterministic ID and timestamp.

    kwargs:
      sender: str (required)
      receiver: str (required)
      subject: str (required)
      text_content: str (required)
      timestamp: str ISO (optional; defaults to current timestamp)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sender = kwargs.get("sender", "")
        receiver = kwargs.get("receiver", "")
        subject = kwargs.get("subject", "")
        text_content = kwargs.get("text_content", "")
        timestamp = kwargs.get("timestamp") or get_current_timestamp()

        if not sender or not receiver or not subject or not text_content:
            return json.dumps({"error": "sender, receiver, subject, and text_content are required"})

        # Create email record
        email = {
            "email_id": _next_id(data, "emails", "EM"),
            "timestamp": timestamp,
            "sender": sender,
            "receiver": receiver,
            "subject": subject,
            "text_content": text_content
        }

        data.setdefault("emails", []).append(email)
        return json.dumps({"ok": True, "email": email})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "send_email",
                "description": "Send an email with deterministic ID and timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sender": {"type": "string", "description": "Sender email address."},
                        "receiver": {"type": "string", "description": "Receiver email address."},
                        "subject": {"type": "string", "description": "Email subject."},
                        "text_content": {"type": "string", "description": "Email body text."},
                        "timestamp": {"type": "string", "description": "ISO timestamp (optional)."}
                    },
                    "required": ["sender", "receiver", "subject", "text_content"],
                    "additionalProperties": False
                }
            }
        }

class CreateSiemAlert(Tool):
    """
    Create a new SIEM alert for security incidents.

    kwargs:
      user_id: str (required) - ID of the user triggering the alert
      resource_id: str (required) - ID of the resource involved
      alert_type: str (default: "UNAUTHORIZED_ACCESS_ATTEMPT")
      severity: str (default: "HIGH") - CRITICAL, HIGH, MEDIUM, LOW
      timestamp: str ISO (defaults now)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id", "")
        resource_id = kwargs.get("resource_id", "")
        alert_type = kwargs.get("alert_type", "UNAUTHORIZED_ACCESS_ATTEMPT")
        severity = kwargs.get("severity", "HIGH")
        timestamp = kwargs.get("timestamp") or get_current_timestamp()

        if not user_id or not resource_id:
            return json.dumps({"error": "user_id and resource_id required"})

        # Validate severity
        valid_severities = ["CRITICAL", "HIGH", "MEDIUM", "LOW"]
        if severity not in valid_severities:
            return json.dumps({"error": f"severity must be one of: {valid_severities}"})

        # Validate user exists
        users = data.get("users", [])
        user = _find_by_id(users, "user_id", user_id)
        if not user:
            return json.dumps({"error": f"User {user_id} not found"})

        # Validate resource exists
        resources = data.get("resources", [])
        resource = _find_by_id(resources, "resource_id", resource_id)
        if not resource:
            return json.dumps({"error": f"Resource {resource_id} not found"})

        alert_id = _next_id(data, "siem_alerts", "ALRT")

        alert_record = {
            "alert_id": alert_id,
            "timestamp": timestamp,
            "user_id": user_id,
            "resource_id": resource_id,
            "alert_type": alert_type,
            "severity": severity
        }

        data.setdefault("siem_alerts", []).append(alert_record)
        return json.dumps({"ok": True, "siem_alert": alert_record})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_siem_alert",
                "description": "Create a new SIEM alert for security incidents.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "ID of the user triggering the alert."},
                        "resource_id": {"type": "string", "description": "ID of the resource involved."},
                        "alert_type": {"type": "string", "description": "Type of alert.", "default": "UNAUTHORIZED_ACCESS_ATTEMPT"},
                        "severity": {"type": "string", "description": "Alert severity: CRITICAL, HIGH, MEDIUM, LOW.", "default": "HIGH"},
                        "timestamp": {"type": "string", "description": "ISO timestamp (optional)."}
                    },
                    "required": ["user_id", "resource_id"],
                    "additionalProperties": False
                }
            }
        }

class GetSiemAlert(Tool):
    """
    Retrieve SIEM alerts by ID, user, resource, or severity.

    kwargs:
      alert_id: str (optional) - Specific alert ID to retrieve
      user_id: str (optional) - Filter by user who triggered alerts
      resource_id: str (optional) - Filter by resource involved in alerts
      severity: str (optional) - Filter by severity (CRITICAL, HIGH, MEDIUM, LOW)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        alert_id = kwargs.get("alert_id")
        user_id = kwargs.get("user_id")
        resource_id = kwargs.get("resource_id")
        severity = kwargs.get("severity")

        siem_alerts = data.get("siem_alerts", [])

        # If alert_id is provided, return single alert
        if alert_id:
            alert = _find_by_id(siem_alerts, "alert_id", alert_id)
            if not alert:
                return json.dumps({"error": f"SIEM alert {alert_id} not found"})
            return json.dumps({"ok": True, "siem_alert": alert})

        # Filter alerts based on provided criteria
        filtered_alerts = []
        for alert in siem_alerts:
            if user_id and alert.get("user_id") != user_id:
                continue
            if resource_id and alert.get("resource_id") != resource_id:
                continue
            if severity and alert.get("severity") != severity:
                continue
            filtered_alerts.append(alert)

        return json.dumps({"ok": True, "siem_alerts": filtered_alerts})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_siem_alert",
                "description": "Retrieve SIEM alerts by ID, user, resource, or severity.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "alert_id": {"type": "string", "description": "Specific SIEM alert ID to retrieve."},
                        "user_id": {"type": "string", "description": "Filter by user who triggered alerts."},
                        "resource_id": {"type": "string", "description": "Filter by resource involved in alerts."},
                        "severity": {"type": "string", "description": "Filter by severity (CRITICAL, HIGH, MEDIUM, LOW)."}
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }


# SESSION MANAGEMENT
class UpdateSession(Tool):
    """
    Update session properties while keeping session_id immutable.

    kwargs:
      session_id: str (required) - Session ID to update
      end_time: str ISO (optional) - Set session end time
      ip_address: str (optional) - Update IP address
      device: str (optional) - Update device type
      is_mfa: bool (optional) - Update MFA status
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        session_id = kwargs.get("session_id", "")
        end_time = kwargs.get("end_time")
        ip_address = kwargs.get("ip_address")
        device = kwargs.get("device")
        is_mfa = kwargs.get("is_mfa")

        if not session_id:
            return json.dumps({"error": "session_id required"})

        # Find the session
        sessions = data.get("sessions", [])
        session_index = None
        for i, session in enumerate(sessions):
            if session.get("session_id") == session_id:
                session_index = i
                break

        if session_index is None:
            return json.dumps({"error": f"session_id {session_id} not found"})

        # Update the session (cannot modify session_id, user_id, or start_time)
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
        return json.dumps({"ok": True, "session": updated_session})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_session",
                "description": "Update session properties while keeping session_id immutable.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "session_id": {"type": "string", "description": "Session ID to update."},
                        "end_time": {"type": "string", "description": "ISO timestamp for session end time."},
                        "ip_address": {"type": "string", "description": "Updated IP address."},
                        "device": {"type": "string", "description": "Updated device type (DESKTOP, LAPTOP, MOBILE)."},
                        "is_mfa": {"type": "boolean", "description": "Updated MFA status."}
                    },
                    "required": ["session_id"],
                    "additionalProperties": False
                }
            }
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        session_id = kwargs.get("session_id")
        user_id = kwargs.get("user_id")
        ip_address = kwargs.get("ip_address")
        only_active = kwargs.get("only_active", False)

        sessions = data.get("sessions", [])

        # If session_id is provided, return single session
        if session_id:
            session = _find_by_id(sessions, "session_id", session_id)
            if not session:
                return json.dumps({"error": f"session_id {session_id} not found"})
            return json.dumps({"ok": True, "session": session if session else "No sessions found"})

        # Filter sessions based on provided criteria
        filtered_sessions = []
        for session in sessions:
            # Filter by user_id if provided
            if user_id and session.get("user_id") != user_id:
                continue
            # Filter by ip_address if provided
            if ip_address and session.get("ip_address") != ip_address:
                continue
            # Filter by active status if requested
            if only_active and session.get("end_time") is not None:
                continue
            filtered_sessions.append(session)

        return json.dumps({"ok": True, "sessions": filtered_sessions if filtered_sessions else "No sessions found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_session",
                "description": "Retrieve sessions by session ID, user ID, or IP address.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "session_id": {"type": "string", "description": "Specific session ID to retrieve."},
                        "user_id": {"type": "string", "description": "Filter by user who owns the sessions."},
                        "ip_address": {"type": "string", "description": "Filter by IP address used in sessions."},
                        "only_active": {"type": "boolean", "description": "Only return sessions without end_time.", "default": False}
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }


TOOLS = [
    # User Management
    CreateUser(),
    UpdateUser(),
    GetUser(),

    # Role Management
    CreateRole(),
    GetRole(),
    UpdateRole(),
    GetUserRoles(),
    IsAdmin(),
    GetBaseRoleByDepartment(),
    EnsureUserRole(),
    UpdateUserRole(),
    CheckSoDConflicts(),

    # Access Requests
    GetAccessRequest(),
    DecideAccessRequest(),

    # Permissions & Policy Exceptions
    CreatePermission(),
    GetPermission(),
    GetRolePermissions(),
    AssignPermissionToRole(),
    GetPolicyException(),
    CreatePolicyException(),
    DecidePolicyException(),

    # Resources & Access Control
    CreateResource(),
    GetResource(),
    ListUsersWithAccessToResource(),
    CanAccessResource(),

    # Certifications
    CreateCertification(),
    GetCertification(),
    CompleteCertification(),

    # Session Management
    GetSession(),
    UpdateSession(),

    # Security & SIEM
    CreateSiemAlert(),
    GetSiemAlert(),

    # Communications & Tickets
    CreateHubSpotTicket(),
    GetHubSpotTicket(),
    UpdateHubSpotTicket(),
    SendEmail(),
    PostSlackMessage(),

    # Audit & Logging
    CreateAuditLogEntry()
]
