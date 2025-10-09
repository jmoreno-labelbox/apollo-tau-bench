from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetResourcesByOwner(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], owner_id: str = None) -> str:
        owned_resources = [
            resource
            for resource in data.get("resources", [])
            if resource.get("owner_id") == owner_id
        ]
        payload = {"resources": owned_resources}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetResourcesByOwner",
                "description": "Retrieves a list of all resources owned by a specific user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner_id": {
                            "type": "string",
                            "description": "The user_id of the resource owner.",
                        }
                    },
                    "required": ["owner_id"],
                },
            },
        }
