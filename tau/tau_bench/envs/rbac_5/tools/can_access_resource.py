# Copyright Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _parse_iso(ts: Optional[str]) -> Optional[datetime]:
    if not ts or not isinstance(ts, str):
        return None
    t = ts.replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(t)
    except Exception:
        return None

def _find_by_id(items: List[Dict[str, Any]], key: str, value: str) -> Optional[Dict[str, Any]]:
    for it in items or []:
        if it.get(key) == value:
            return it
    return None

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
    def invoke(data: Dict[str, Any], on_date, include_details = False, resource_id = "", user_id = "") -> str:
        on_date_iso = on_date or get_current_timestamp()

        if not user_id or not resource_id:
            return json.dumps({"error": "user_id and resource_id are required"})

        # Check if the user is present.
        if not _find_by_id(list(data.get("users", {}).values()), "user_id", user_id):
            return json.dumps({"error": f"user_id {user_id} not found"})

        # Check if the resource is present.
        if not _find_by_id(data.get("resources", []), "resource_id", resource_id):
            return json.dumps({"error": f"resource_id {resource_id} not found"})

        on_dt = _parse_iso(on_date_iso) or datetime.now(tz=timezone.utc)

        def is_active(ur: Dict[str, Any]) -> bool:
            exp = _parse_iso(ur.get("expires_on"))
            return (exp is None) or (exp > on_dt)

        # Step 1: Retrieve all permissions associated with the resource.
        resource_permissions = [
            p for p in list(data.get("permissions", {}).values())
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

        # Step 2: Retrieve all roles associated with those permissions.
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

        # Step 3: Verify if the user possesses any of the specified roles and that they are currently active.
        user_assignments = [
            ur for ur in data.get("user_roles", [])
            if ur.get("user_id") == user_id and is_active(ur)
        ]

        active_user_role_ids = {ur.get("role_id") for ur in user_assignments}

        # Identify roles that provide access and that the user possesses.
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
            # Create a comprehensive analysis.
            role_map = {r.get("role_id"): r for r in list(data.get("roles", {}).values())}
            permission_map = {p.get("permission_id"): p for p in list(data.get("permissions", {}).values())}

            # Associate the permissions with the roles assigned to the user.
            granting_details = []
            for role_id in granting_role_ids:
                role = role_map.get(role_id, {})

                # Determine the permissions granted by this role for the specified resource.
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