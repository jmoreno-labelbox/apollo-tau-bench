from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FindUsersByCity(Tool):
    """Enumerate users in a specified city (exact match)."""

    @staticmethod
    def invoke(data, city: str = None) -> str:
        if not city:
            payload = {"error": "city is required"}
            out = json.dumps(payload, indent=2)
            return out
        users = data.get("users", {}).values()
        out = [u for u in users.values() if u.get("address", {}).values().get("city") == city]
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "findUsersByCity",
                "description": "Find all users whose address.city equals the given city.",
                "parameters": {
                    "type": "object",
                    "properties": {"city": {"type": "string"}},
                    "required": ["city"],
                },
            },
        }
