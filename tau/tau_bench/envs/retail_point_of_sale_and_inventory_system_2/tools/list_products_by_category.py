from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ListProductsByCategory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], category: str) -> str:
        _categoryL = category or ''.lower()
        pass
        products = data.get("products", [])
        category_products = [
            p for p in products if p.get("category", "").lower() == category.lower()
        ]
        payload = {
                "products": category_products,
                "count": len(category_products),
                "category": category,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListProductsByCategory",
                "description": "List all products in a specific category.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "Product category to filter by.",
                        }
                    },
                    "required": ["category"],
                },
            },
        }
