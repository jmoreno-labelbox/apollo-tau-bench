from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreatePermission(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], action: str = None, resource_id: str = None, description: str = None) -> str:
        permissions = data.get("permissions", [])
        new_id_num = (
            max((int(p["permission_id"][2:]) for p in permissions), default=0) + 1
        )
        new_permission_id = f"P-{new_id_num:03d}"
        new_permission = {
            "permission_id": new_permission_id,
            "action": action,
            "resource_id": resource_id,
            "description": description,
        }
        permissions.append(new_permission)
        data["permissions"] = permissions
        payload = new_permission
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreatePermission",
                "description": "Creates a new permission.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {
                            "type": "string",
                            "description": "The action the permission grants (e.g., read, write).",
                        },
                        "resource_id": {
                            "type": "string",
                            "description": "The ID of the resource this permission applies to.",
                        },
                        "description": {
                            "type": "string",
                            "description": "A description of the permission.",
                        },
                    },
                    "required": ["action", "resource_id"],
                },
            },
        }
