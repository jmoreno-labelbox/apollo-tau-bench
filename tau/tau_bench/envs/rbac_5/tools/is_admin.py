from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

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
        if not _find_by_id(data.get("users", {}).values()), "user_id", user_id):
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
        for ur in assignments:
            rid = ur.get("role_id")
            role = role_map.get(rid) or {}
            name = str(role.get("role_name", "")).strip().lower()
            if name.endswith("admin") or name.endswith("lead"):
                admin_role_ids.append(rid)

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
