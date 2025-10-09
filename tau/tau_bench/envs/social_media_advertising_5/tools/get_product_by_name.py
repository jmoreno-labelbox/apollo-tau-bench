from tau_bench.envs.tool import Tool
import ast
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetProductByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], product_name: str = None) -> str:
        n = product_name
        for p in data.get("dim_product", []):
            if p.get("name") == n:
                payload = p
                out = json.dumps(payload)
                return out
        payload = {"error": f"product {n} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getProductByName",
                "description": "Looks up a product by name.",
                "parameters": {
                    "type": "object",
                    "properties": {"product_name": {"type": "string"}},
                    "required": ["product_name"],
                },
            },
        }
