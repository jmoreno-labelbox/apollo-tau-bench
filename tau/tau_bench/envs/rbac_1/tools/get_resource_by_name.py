from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetResourceByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], name: str = None) -> str:
        for res in data.get("resources", []):
            if res.get("name") == name:
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
                "name": "GetResourceByName",
                "description": "Retrieves a resource by its name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }
