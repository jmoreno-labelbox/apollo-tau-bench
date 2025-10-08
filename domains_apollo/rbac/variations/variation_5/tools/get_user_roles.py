from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any

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
            ur for ur in data.get("user_roles", []) if ur.get("user_id") == user_id
        ]

        def is_active(ur: dict[str, Any]) -> bool:
            exp = _parse_iso(ur.get("expires_on"))
            return (exp is None) or (exp > on_dt)

        if only_active:
            assignments = [ur for ur in assignments if is_active(ur)]

        # Construct a role mapping
        role_map = {r["role_id"]: r for r in data.get("roles", []) if "role_id" in r}
        out = []

        for ur in assignments:
            entry = {"role_id": ur.get("role_id")}
            if include_role_details:
                entry["role_name"] = role_map.get(ur.get("role_id"), {}).get(
                    "role_name"
                )
                entry["description"] = role_map.get(ur.get("role_id"), {}).get(
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
