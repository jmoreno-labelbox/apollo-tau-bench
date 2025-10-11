# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListLowStockProducts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], threshold: int = 10) -> str:
        inventory = list(data.get("inventory", {}).values())
        products = list(data.get("products", {}).values())
        low_stock_products = []

        for inv_record in inventory:
            quantity = inv_record.get("quantity", 0)
            if quantity <= threshold:
                product = next((p for p in products if p.get("sku") == inv_record.get("sku")), None)

                low_stock_info = {
                    "sku": inv_record.get("sku"),
                    "name": product.get("name") if product else "Unknown",
                    "store_id": inv_record.get("store_id"),
                    "current_stock": quantity,
                    "threshold": threshold,
                    "category": product.get("category") if product else "Unknown"
                }
                low_stock_products.append(low_stock_info)
        return json.dumps({"low_stock_products": low_stock_products, "count": len(low_stock_products), "threshold": threshold}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_low_stock_products",
                "description": "List products with stock levels below the specified threshold.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "threshold": {"type": "integer", "description": "Stock level threshold. Default is 10."}
                    },
                    "required": []
                }
            }
        }
