from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

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
