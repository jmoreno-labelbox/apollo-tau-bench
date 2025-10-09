from tau_bench.envs.tool import Tool
import json
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetProductByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], name: Any) -> str:
        products = data.get("products", {}).values()
        match = next((p for p in products.values() if p.get("name") == name), None)
        payload = match or {}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductByName",
                "description": "Return a product by exact display name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }
