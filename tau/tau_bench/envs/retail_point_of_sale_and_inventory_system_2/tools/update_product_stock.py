from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateProductStock(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sku: str, new_stock_quantity: int) -> str:
        products = data.get("products", {}).values()

        for i, product in enumerate(products):
            if product.get("sku") == sku:
                products[i]["stock_quantity"] = new_stock_quantity
                data["products"] = products
                payload = products[i]
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Product with SKU {sku} not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateProductStock",
                "description": "Update the stock quantity of an existing product.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "Product SKU to update.",
                        },
                        "new_stock_quantity": {
                            "type": "integer",
                            "description": "New stock quantity for the product.",
                        },
                    },
                    "required": ["sku", "new_stock_quantity"],
                },
            },
        }
