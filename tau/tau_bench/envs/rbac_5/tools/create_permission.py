# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _next_id(data: Dict[str, Any], collection: str, prefix: str) -> str:
    n = len(data.get(collection, [])) + 1
    return f"{prefix}-{n:03d}"

def _find_by_id(items: List[Dict[str, Any]], key: str, value: str) -> Optional[Dict[str, Any]]:
    for it in items or []:
        if it.get(key) == value:
            return it
    return None

class CreatePermission(Tool):
    """
    Create a new permission with deterministic ID generation.

    kwargs:
      action: str (required)
      resource_id: str (required)
      description: str (required)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], action = "", description = "", resource_id = "") -> str:
        action = (action or "").strip()
        resource_id = (resource_id or "").strip()

        if not action or not resource_id or not description:
            return json.dumps({"error": "action, resource_id, and description are required"})

        # Check for resource existence.
        if not _find_by_id(data.get("resources", []), "resource_id", resource_id):
            return json.dumps({"error": f"resource_id {resource_id} not found"})

        # Ensure that (action, resource_id) combination is unique.
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