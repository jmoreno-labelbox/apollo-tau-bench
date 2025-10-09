from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetPurchasedItems(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, order_id: str = None) -> str:
        """
        Retrieve detailed list of purchased items from a specific order

        Data Sources: orders.json (order items), products.json (additional product details), users.json (user validation)
        """
        if not user_id or not order_id:
            payload = {"error": "user_id and order_id are required", "status": "failed"}
            out = json.dumps(payload)
            return out
            
        # Rule: Validate user identity exists before processing any user requests
        users = data.get("users", {}).values()
        user = next((u for u in users.values() if u.get("user_id") == user_id), None)

        if not user:
            payload = {"error": f"User {user_id} not found", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Find the specific order
        orders = data.get("orders", {}).values()
        target_order = None

        for order in orders.values():
            if order.get("order_id") == order_id and order.get("user_id") == user_id:
                target_order = order
                break

        if not target_order:
            payload = {
                "error": f"Order {order_id} not found or does not belong to user {user_id}",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Get order details
        order_status = target_order.get("status")
        order_timestamp = target_order.get("timestamp")
        order_items = target_order.get("items", [])
        payment_history = target_order.get("payment_history", [])
        fulfillments = target_order.get("fulfillments", [])

        if not order_items:
            payload = {"error": f"No items found in order {order_id}", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Enrich item details with additional product information
        products = data.get("products", {}).values()
        detailed_items = []
        total_order_value = 0.0

        for order_item in order_items:
            item_id = order_item.get("item_id")
            product_id = order_item.get("product_id")
            item_price = order_item.get("price", 0)
            item_name = order_item.get("name")
            item_options = order_item.get("options", {}).values()

            # Find additional product details from products.json
            additional_details = {}
            for product in products.values():
                if product.get("product_id") == product_id:
                    variants = product.get("variants", {}).values()
                    if item_id in variants:
                        variant_info = variants[item_id]
                        additional_details = {
                            "current_availability": variant_info.get("available", False),
                            "current_price": variant_info.get("price", 0),
                            "full_options": list(variant_info.get("options", {}).values()),
                            "supplier_id": product.get("supplier_id"),
                        }
                    break

            # Calculate if price has changed since purchase
            current_price = additional_details.get("current_price", item_price)
            price_change = (
                current_price - item_price if current_price != item_price else 0
            )

            # Build comprehensive item details
            item_detail = {
                "item_id": item_id,
                "product_id": product_id,
                "product_name": item_name,
                "purchase_details": {
                    "purchased_price": item_price,
                    "purchased_options": item_options,
                    "purchase_date": order_timestamp,
                },
                "current_details": {
                    "current_price": current_price,
                    "price_change": round(price_change, 2),
                    "currently_available": additional_details.get(
                        "current_availability", False
                    ),
                    "supplier_id": additional_details.get("supplier_id"),
                },
                "product_specifications": additional_details.get(
                    "full_options", item_options
                ),
            }

            detailed_items.append(item_detail)
            total_order_value += item_price

        # Calculate order summary information
        total_paid = sum(
            payment.get("amount", 0)
            for payment in payment_history
            if payment.get("transaction_type") == "payment"
        )
        total_refunded = sum(
            payment.get("amount", 0)
            for payment in payment_history
            if payment.get("transaction_type") == "refund"
        )

        # Get tracking information if available
        tracking_info = []
        for fulfillment in fulfillments:
            tracking_info.append(
                {
                    "tracking_id": fulfillment.get("tracking_id"),
                    "courier_name": fulfillment.get("courier_name"),
                    "courier_id": fulfillment.get("courier_id"),
                    "status": fulfillment.get("status"),
                    "timestamp": fulfillment.get("timestamp"),
                }
            )

        # Rule: Maintain data integrity: order totals must match sum of item prices
        price_integrity_check = abs(total_order_value - total_paid + total_refunded) < 0.01

        result = {
            "status": "success",
            "order_info": {
                "order_id": order_id,
                "user_id": user_id,
                "order_status": order_status,
                "order_date": order_timestamp,
                "delivery_address": list(target_order.get("address", {}).values()),
            },
            "financial_summary": {
                "total_order_value": round(total_order_value, 2),
                "total_paid": round(total_paid, 2),
                "total_refunded": round(total_refunded, 2),
                "net_amount": round(total_paid - total_refunded, 2),
                "price_integrity_verified": price_integrity_check,
            },
            "purchased_items": {
                "total_items": len(detailed_items),
                "items": detailed_items,
            },
            "fulfillment_info": {
                "tracking_available": len(tracking_info) > 0,
                "tracking_details": tracking_info,
            },
            "returns_info": {
                "returns_requested": "returns" in target_order,
                "return_requests": target_order.get("returns", []),
            },
        }
        payload = result
        out = json.dumps(payload)
        return out
        
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPurchasedItems",
                "description": "Retrieve detailed list of purchased items from a specific customer order",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Customer identifier",
                        },
                        "order_id": {
                            "type": "string",
                            "description": "Order identifier to retrieve items from",
                        },
                    },
                    "required": ["user_id", "order_id"],
                },
            },
        }
