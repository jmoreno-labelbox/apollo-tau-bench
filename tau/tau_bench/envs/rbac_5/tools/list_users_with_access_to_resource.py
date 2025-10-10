# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


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
        perms = [p for p in list(data.get("permissions", {}).values()) if p.get("resource_id") == resource_id]
        perm_ids = {p.get("permission_id") for p in perms if p.get("permission_id")}
        role_ids = {rp.get("role_id") for rp in data.get("role_permissions", []) if rp.get("permission_id") in perm_ids}

        # Build helpers
        user_map = {u.get("user_id"): u for u in list(data.get("users", {}).values())}
        role_map = {r.get("role_id"): r for r in list(data.get("roles", {}).values())}

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
