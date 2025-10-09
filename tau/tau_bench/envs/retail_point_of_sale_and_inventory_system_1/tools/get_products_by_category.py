from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetProductsByCategory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], category: str = None) -> str:
        products = data.get("products", {}).values()
        results = [
            product for product in products.values() if product.get("category") == category
        ]
        payload = results
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductsByCategory",
                "description": "Retrieves all products that belong to a specific category.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "The category of the products to retrieve.",
                        },
                    },
                    "required": ["category"],
                },
            },
        }
