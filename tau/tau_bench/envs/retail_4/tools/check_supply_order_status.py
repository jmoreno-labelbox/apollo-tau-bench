from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class CheckSupplyOrderStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], product_id: str) -> str:
        """
        Check supply order status for inventory replenishment planning
        """
        # Rule: Supply orders must reference valid supplier_id and existing product_id
        supply_orders = data.get("supply_orders", [])
        product_supply_orders = [
            so for so in supply_orders if so.get("product_id") == product_id
        ]

        if not product_supply_orders:
            payload = {
                "error": f"No supply orders found for product {product_id}",
                "status": "not_found",
            }
            out = json.dumps(payload)
            return out

        # Rule: Supply orders with status 'cancelled' require alternative sourcing and cannot be fulfilled
        active_orders = []
        cancelled_orders = []
        fulfilled_orders = []

        for order in product_supply_orders:
            status = order.get("status")
            if status == "cancelled":
                cancelled_orders.append(order)
            elif status == "fulfilled":
                fulfilled_orders.append(order)
            elif status == "pending":
                active_orders.append(order)

        # Calculate totals
        total_pending_quantity = sum(
            order.get("quantity", 0) for order in active_orders
        )
        total_fulfilled_quantity = sum(
            order.get("quantity", 0) for order in fulfilled_orders
        )
        total_cancelled_quantity = sum(
            order.get("quantity", 0) for order in cancelled_orders
        )

        result = {
            "status": "success",
            "product_id": product_id,
            "total_supply_orders": len(product_supply_orders),
            "pending_orders": len(active_orders),
            "fulfilled_orders": len(fulfilled_orders),
            "cancelled_orders": len(cancelled_orders),
            "pending_quantity": total_pending_quantity,
            "fulfilled_quantity": total_fulfilled_quantity,
            "cancelled_quantity": total_cancelled_quantity,
            "requires_alternative_sourcing": len(cancelled_orders) > 0,
            "recent_orders": (
                product_supply_orders[-3:]
                if len(product_supply_orders) >= 3
                else product_supply_orders
            ),
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckSupplyOrderStatus",
                "description": "Check supply order status and inventory replenishment for a product",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {
                            "type": "string",
                            "description": "Product identifier to check supply orders for",
                        }
                    },
                    "required": ["product_id"],
                },
            },
        }
