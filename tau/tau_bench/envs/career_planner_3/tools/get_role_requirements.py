from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetRoleRequirements(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], role_name: str = None) -> str:
        role_catalog = data.get("role_skill_catalog", [])
        result = [r for r in role_catalog if r["role"] == role_name]

        if not result:
            payload = {
                    "error": "Role not found",
                    "role_name": role_name,
                    "available_roles": [r["role"] for r in role_catalog],
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = result[0]
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getRoleRequirements",
                "description": "Retrieves the required skills and certifications for a given role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_name": {
                            "type": "string",
                            "description": "The name of the target role.",
                        }
                    },
                    "required": ["role_name"],
                },
            },
        }
