from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FindProductByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], name: Any) -> str:
        match = next((p for p in data.get("products", {}).values() if p.get("name") == name), {}).values()
        payload = match
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindProductByName",
                "description": "Returns product by exact name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }
