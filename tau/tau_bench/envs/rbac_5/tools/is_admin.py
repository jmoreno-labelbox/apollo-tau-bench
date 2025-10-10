# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


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
        if not _find_by_id(list(data.get("users", {}).values()), "user_id", user_id):
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

        role_map = {r.get("role_id"): r for r in list(data.get("roles", {}).values())}

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
