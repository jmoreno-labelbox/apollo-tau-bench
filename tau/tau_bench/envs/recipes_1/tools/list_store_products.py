from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ListStoreProducts(Tool):
    """Enumerate store_products for a store (can be filtered by ingredient_id if desired)."""

    @staticmethod
    def invoke(data: dict[str, Any], store_id: int = None, ingredient_id: int = None) -> str:
        if store_id is None:
            return _json_dump({"error": "store_id is required"})
        rows = [
            p
            for p in data.get("store_products", {}).values()
            if int(p.get("store_id")) == int(store_id)
        ]
        if ingredient_id is not None:
            rows = [
                p for p in rows if int(p.get("ingredient_id")) == int(ingredient_id)
            ]
        return _json_dump(rows)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listStoreProducts",
                "description": "List products for a store, optionally for an ingredient.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {"type": "integer"},
                        "ingredient_id": {"type": "integer"},
                    },
                    "required": ["store_id"],
                },
            },
        }
