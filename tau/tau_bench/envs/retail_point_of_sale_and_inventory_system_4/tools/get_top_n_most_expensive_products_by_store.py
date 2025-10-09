from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetTopNMostExpensiveProductsByStore(Tool):  #VIEW
    @staticmethod
    def invoke(data: dict[str, Any], store_id: str, n: int) -> str:
        products = {p["sku"]: p["price"] for p in data.get("products", [])}
        inventory = {i["sku"]: i["store_id"] for i in data.get("inventory", [])}

        items = [
            {"sku": sku, "price": price}
            for sku, price in products.items()
            if inventory.get(sku) == store_id
        ]

        # Order by price from highest to lowest and select top x
        top_items = sorted(items, key=lambda i: i["price"], reverse=True)[:n]
        payload = top_items
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTopNMostExpensiveProductsByStore",
                "description": "Return the top n most expensive products available in a given store, based on product price.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {
                            "type": "string",
                            "description": "The unique ID of the store.",
                        },
                        "n": {
                            "type": "integer",
                            "description": "The number of top expensive products to return.",
                        },
                    },
                    "required": ["store_id", "n"],
                },
            },
        }
