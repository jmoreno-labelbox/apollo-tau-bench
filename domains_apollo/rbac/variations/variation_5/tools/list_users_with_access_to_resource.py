from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any

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
            for p in data.get("permissions", [])
            if p.get("resource_id") == resource_id
        ]
        perm_ids = {p.get("permission_id") for p in perms if p.get("permission_id")}
        role_ids = {
            rp.get("role_id")
            for rp in data.get("role_permissions", [])
            if rp.get("permission_id") in perm_ids
        }

        # Create utility functions
        user_map = {u.get("user_id"): u for u in data.get("users", [])}
        role_map = {r.get("role_id"): r for r in data.get("roles", [])}

        def is_active(ur: dict[str, Any]) -> bool:
            exp = _parse_iso(ur.get("expires_on"))
            return (exp is None) or (exp > on_dt)

        # Collect users with corresponding roles
        acc: dict[str, dict[str, Any]] = {}
        for ur in data.get("user_roles", []):
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
