# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPurchasedItems(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, order_id: str) -> str:
        """
        Retrieve detailed list of purchased items from a specific order

        Data Sources: orders.json (order items), products.json (additional product details), users.json (user validation)
        """
        # Policy: Confirm the existence of user identity prior to handling any requests.
        users = list(data.get("users", {}).values())
        user = next((u for u in users if u.get("user_id") == user_id), None)

        if not user:
            return json.dumps({"error": f"User {user_id} not found", "status": "failed"})

        # Determine the exact sequence.
        orders = list(data.get("orders", {}).values())
        target_order = None

        for order in orders:
            if order.get("order_id") == order_id and order.get("user_id") == user_id:
                target_order = order
                break

        if not target_order:
            return json.dumps({
                "error": f"Order {order_id} not found or does not belong to user {user_id}",
                "status": "failed"
            })

        # Retrieve order information.
        order_status = target_order.get("status")
        order_timestamp = target_order.get("timestamp")
        order_items = target_order.get("items", [])
        payment_history = target_order.get("payment_history", [])
        fulfillments = target_order.get("fulfillments", [])

        if not order_items:
            return json.dumps({
                "error": f"No items found in order {order_id}",
                "status": "failed"
            })

        # Augment item specifications with supplementary product data.
        products = list(data.get("products", {}).values())
        detailed_items = []
        total_order_value = 0.0

        for order_item in order_items:
            item_id = order_item.get("item_id")
            product_id = order_item.get("product_id")
            item_price = order_item.get("price", 0)
            item_name = order_item.get("name")
            item_options = order_item.get("options", {})

            # Retrieve more product information from products.json.
            additional_details = {}
            for product in products:
                if product.get("product_id") == product_id:
                    variants = product.get("variants", {})
                    if item_id in variants:
                        variant_info = variants[item_id]
                        additional_details = {
                            "current_availability": variant_info.get("available", False),
                            "current_price": variant_info.get("price", 0),
                            "full_options": variant_info.get("options", {}),
                            "supplier_id": product.get("supplier_id")
                        }
                    break

            # Determine if the price has fluctuated since the time of purchase.
            current_price = additional_details.get("current_price", item_price)
            price_change = current_price - item_price if current_price != item_price else 0

            # Create detailed specifications for the item.
            item_detail = {
                "item_id": item_id,
                "product_id": product_id,
                "product_name": item_name,
                "purchase_details": {
                    "purchased_price": item_price,
                    "purchased_options": item_options,
                    "purchase_date": order_timestamp
                },
                "current_details": {
                    "current_price": current_price,
                    "price_change": round(price_change, 2),
                    "currently_available": additional_details.get("current_availability", False),
                    "supplier_id": additional_details.get("supplier_id")
                },
                "product_specifications": additional_details.get("full_options", item_options)
            }

            detailed_items.append(item_detail)
            total_order_value += item_price

        # Compute summary details for the order.
        total_paid = sum(payment.get("amount", 0) for payment in payment_history if payment.get("transaction_type") == "payment")
        total_refunded = sum(payment.get("amount", 0) for payment in payment_history if payment.get("transaction_type") == "refund")

        # Retrieve tracking details if present.
        tracking_info = []
        for fulfillment in fulfillments:
            tracking_info.append({
                "tracking_id": fulfillment.get("tracking_id"),
                "courier_name": fulfillment.get("courier_name"),
                "courier_id": fulfillment.get("courier_id"),
                "status": fulfillment.get("status"),
                "timestamp": fulfillment.get("timestamp")
            })

        # Rule: Ensure data accuracy: order totals should equal the aggregate of item prices.
        price_integrity_check = abs(total_order_value - total_paid + total_refunded) < 0.01

        result = {
            "status": "success",
            "order_info": {
                "order_id": order_id,
                "user_id": user_id,
                "order_status": order_status,
                "order_date": order_timestamp,
                "delivery_address": target_order.get("address", {})
            },
            "financial_summary": {
                "total_order_value": round(total_order_value, 2),
                "total_paid": round(total_paid, 2),
                "total_refunded": round(total_refunded, 2),
                "net_amount": round(total_paid - total_refunded, 2),
                "price_integrity_verified": price_integrity_check
            },
            "purchased_items": {
                "total_items": len(detailed_items),
                "items": detailed_items
            },
            "fulfillment_info": {
                "tracking_available": len(tracking_info) > 0,
                "tracking_details": tracking_info
            },
            "returns_info": {
                "returns_requested": "returns" in target_order,
                "return_requests": target_order.get("returns", [])
            }
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_purchased_items",
                "description": "Retrieve detailed list of purchased items from a specific customer order",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "Customer identifier"},
                        "order_id": {"type": "string", "description": "Order identifier to retrieve items from"}
                    },
                    "required": ["user_id", "order_id"]
                }
            }
        }
