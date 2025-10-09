from tau_bench.envs.tool import Tool
import json
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ListProductsInCategory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], category_id: Any, products: list = None) -> str:
        if products is None:
            products = data.get("products", {}).values()
        category_id = _as_id(category_id)
        rows = [p for p in products.values() if _as_id(p.get("category_id")) == category_id]
        payload = {"products": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListProductsInCategory",
                "description": "List products belonging to a category_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"category_id": {"type": "string"}},
                    "required": ["category_id"],
                },
            },
        }
