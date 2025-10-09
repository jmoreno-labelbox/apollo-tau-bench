from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ListLowStockProducts(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], inventory: list = None, products: list = None, threshold: int = 10) -> str:
        inventory = inventory if inventory is not None else data.get("inventory", [])
        products = products if products is not None else data.get("products", [])
        low_stock_products = []

        for inv_record in inventory:
            quantity = inv_record.get("quantity", 0)
            if quantity <= threshold:
                product = next(
                    (p for p in products if p.get("sku") == inv_record.get("sku")), None
                )

                low_stock_info = {
                    "sku": inv_record.get("sku"),
                    "name": product.get("name") if product else "Unknown",
                    "store_id": inv_record.get("store_id"),
                    "current_stock": quantity,
                    "threshold": threshold,
                    "category": product.get("category") if product else "Unknown",
                }
                low_stock_products.append(low_stock_info)
        payload = {
                "low_stock_products": low_stock_products,
                "count": len(low_stock_products),
                "threshold": threshold,
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
                "name": "ListLowStockProducts",
                "description": "List products with stock levels below the specified threshold.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "threshold": {
                            "type": "integer",
                            "description": "Stock level threshold. Default is 10.",
                        }
                    },
                    "required": [],
                },
            },
        }
