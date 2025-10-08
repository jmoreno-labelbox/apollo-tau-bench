from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class GetProductSupplierSummary(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], product_id: str = None) -> str:
        if not product_id:
            payload = {"error": "product_id is required"}
            out = json.dumps(payload)
            return out

        products = data["products"]
        suppliers = data["suppliers"]
        supply_orders = data["supply_orders"]

        product = next((p for p in products if p["product_id"] == product_id), None)
        if not product:
            payload = {"error": f"Product {product_id} not found"}
            out = json.dumps(payload)
            return out

        supplier = next(
            (s for s in suppliers if s["supplier_id"] == product["supplier_id"]), None
        )

        # Retrieve supply orders associated with this product
        product_supply_orders = [
            o for o in supply_orders if o["product_id"] == product_id
        ]

        # Compute the stock summary
        stock_summary = {}
        if supplier:
            for variant_id in product["variants"].keys():
                stock_level = supplier["item_stock"].get(variant_id, "unknown")
                stock_summary[variant_id] = stock_level
        payload = {
            "product": product,
            "supplier": supplier,
            "stock_summary": stock_summary,
            "total_supply_orders": len(product_supply_orders),
            "recent_supply_orders": product_supply_orders[-5:],  # Most recent 5 orders
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
                "name": "getProductSupplierSummary",
                "description": "Get comprehensive information about a product, its supplier, stock levels, and recent supply orders.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {
                            "type": "string",
                            "description": "Product ID to get summary for",
                        }
                    },
                    "required": ["product_id"],
                },
            },
        }
