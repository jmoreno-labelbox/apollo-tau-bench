from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetProductInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sku: str) -> str:
        products = data.get("products", {}).values()
        result = [item for item in products.values() if item["sku"] == sku]
        if result:
            payload = result[0]
            out = json.dumps(payload)
            return out
        payload = {"error": f"Product {sku} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductInfo",
                "parameters": {"sku": {"type": "string"}},
                "required": ["sku"],
            },
        }
