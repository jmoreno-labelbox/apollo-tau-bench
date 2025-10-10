# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTopNMostExpensiveProductsByStore(Tool): # RETRIEVE
    @staticmethod
    def invoke(data: Dict[str, Any], store_id: str, n: int) -> str:
        products = {p["sku"]: p["price"] for p in list(data.get("products", {}).values())}
        inventory = {i["sku"]: i["store_id"] for i in list(data.get("inventory", {}).values())}

        items = [{"sku":sku, "price":price} for sku, price in products.items() if inventory.get(sku) == store_id]

        # Order by price in descending order and select the top x.
        top_items = sorted(items, key=lambda i: i["price"], reverse=True)[:n]
        return json.dumps(top_items)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_top_n_most_expensive_products_by_store",
                "description": "Return the top n most expensive products available in a given store, based on product price.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {
                            "type": "string",
                            "description": "The unique ID of the store."
                        },
                        "n": {
                            "type": "integer",
                            "description": "The number of top expensive products to return."
                        }
                    },
                    "required": ["store_id", "n"]
                }
            }
        }
