# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


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
        for p in list(data.get("permissions", {}).values()):
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
