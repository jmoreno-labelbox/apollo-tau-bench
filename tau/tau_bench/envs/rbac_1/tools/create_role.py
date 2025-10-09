from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateRole(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], role_name: str = None, description: str = None, is_temporary: bool = False) -> str:
        roles = data.get("roles", {}).values()
        new_id_num = max((int(r["role_id"][4:]) for r in roles.values()), default=0) + 1
        new_role_id = f"ROL-{new_id_num:03d}"
        new_role = {
            "role_id": new_role_id,
            "role_name": role_name,
            "description": description,
            "is_temporary": is_temporary,
        }
        data["roles"][role_id] = new_role
        data["roles"] = roles
        payload = new_role
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateRole",
                "description": "Creates a new role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_name": {"type": "string"},
                        "description": {"type": "string"},
                        "temporary": {"type": \"boolean\"},
                    },
                    "required": ["role_name", "description"],
                },
            },
        }
