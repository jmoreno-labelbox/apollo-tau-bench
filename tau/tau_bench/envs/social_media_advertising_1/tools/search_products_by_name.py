from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SearchProductsByName(Tool):
    """Looks for products whose names include the specified text."""

    @staticmethod
    def invoke(data: dict[str, Any], name_query: str = None) -> str:
        products = data.get("dim_product", [])
        matching_products = []
        
        if not name_query:
            payload = {"product_ids": []}
            out = json.dumps(payload)
            return out

        for product in products:
            if name_query.lower() in product.get("name", "").lower():
                matching_products.append(product.get("product_id"))
        payload = {"product_ids": matching_products}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchProductsByName",
                "description": "Searches for products with names containing the specified text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name_query": {
                            "type": "string",
                            "description": "The text to search for in product names.",
                        }
                    },
                    "required": ["name_query"],
                },
            },
        }
