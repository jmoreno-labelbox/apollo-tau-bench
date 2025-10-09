from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateResourceOwner(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], resource_id: str = None, new_owner_id: str = None) -> str:
        for res in data.get("resources", {}).values():
            if res.get("resource_id") == resource_id:
                res["owner_id"] = new_owner_id
                payload = res
                out = json.dumps(payload)
                return out
        payload = {"error": "Resource not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateResourceOwner",
                "description": "Updates the owner of a resource.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_id": {"type": "string"},
                        "new_owner_id": {"type": "string"},
                    },
                    "required": ["resource_id", "new_owner_id"],
                },
            },
        }
