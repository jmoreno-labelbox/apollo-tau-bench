# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetOrderIdsByProductIds(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], product_ids: List[str], user_id: str = None) -> str:
        """
        Get list of order IDs that contain specified product IDs

        Data Sources: orders.json (order items)
        """
        if not product_ids:
            return json.dumps({"error": "Product IDs list cannot be empty", "status": "failed"})

        # Rule: Validate user identity exists before processing any user requests (if user_id provided)
        if user_id:
            users = list(data.get("users", {}).values())
            user = next((u for u in users if u.get("user_id") == user_id), None)
            if not user:
                return json.dumps({"error": f"User {user_id} not found", "status": "failed"})

        # Search through all orders to find matches
        orders = list(data.get("orders", {}).values())
        matching_orders = []

        for order in orders:
            order_id = order.get("order_id")
            order_user_id = order.get("user_id")
            order_items = order.get("items", [])

            # Filter by user_id if specified
            if user_id and order_user_id != user_id:
                continue

            # Check which products this order contains
            for item in order_items:
                item_product_id = item.get("product_id")
                if item_product_id in product_ids:
                    matching_orders.append({
                        "order_id": order_id,
                        "user_id": order_user_id,
                        "order_status": order.get("status"),
                        "order_date": order.get("timestamp")
                    })
                    break  # Found a match, no need to check other items in this order

        # Remove duplicates and get unique order IDs
        unique_order_ids = list(set(order["order_id"] for order in matching_orders))

        result = {
            "status": "success",
            "order_ids": unique_order_ids,
            "order_details": matching_orders,
            "total_orders_found": len(unique_order_ids)
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_order_ids_by_product_ids",
                "description": "Get list of order IDs that contain specified product IDs",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of product identifiers to find orders for"
                        },
                        "user_id": {
                            "type": "string",
                            "description": "Optional user identifier to filter orders by specific customer"
                        }
                    },
                    "required": ["product_ids"]
                }
            }
        }
