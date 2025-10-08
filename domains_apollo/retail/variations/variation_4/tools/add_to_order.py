from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class AddToOrder(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        order_id: str = None,
        item_id: str = None,
        payment_method: str = None,
        quantity: int = 1,
        tax_amount: float = None,
        shipping_cost: float = None,
    ) -> str:
        """
        Add an item to an existing order (only for pending orders) with payment processing

        Writes to: orders.json (updates existing order items)
        Data Sources: orders.json (order validation), products.json (item validation), users.json (payment validation)
        """
        if not order_id or not order_id.strip():
            payload = {"error": "Order ID is required", "status": "failed"}
            out = json.dumps(payload)
            return out

        if not item_id or not item_id.strip():
            payload = {"error": "Item ID is required", "status": "failed"}
            out = json.dumps(payload)
            return out

        if not payment_method or not payment_method.strip():
            payload = {"error": "Payment method is required", "status": "failed"}
            out = json.dumps(payload)
            return out

        if quantity <= 0:
            payload = {"error": "Quantity must be greater than 0", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Validate optional amounts
        if tax_amount is not None and tax_amount < 0:
            payload = {"error": "Tax amount cannot be negative", "status": "failed"}
            out = json.dumps(payload)
            return out

        if shipping_cost is not None and shipping_cost < 0:
            payload = {"error": "Shipping cost cannot be negative", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Add # prefix if not provided (for convenience)
        formatted_order_id = order_id if order_id.startswith("#") else f"#{order_id}"

        # Find the order to update
        orders = data.get("orders", [])
        order_to_update = None
        order_index = None

        for i, order in enumerate(orders):
            if order.get("order_id") == formatted_order_id:
                order_to_update = order
                order_index = i
                break

        if not order_to_update:
            payload = {"error": f"Order {formatted_order_id} not found", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Rule: Can only add items to pending orders
        current_status = order_to_update.get("status")
        if current_status != "pending":
            payload = {
                "error": f"Cannot add items to order with status '{current_status}'. Items can only be added to pending orders.",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Get user ID from order for payment validation
        user_id = order_to_update.get("user_id")
        if not user_id:
            payload = {"error": "Order does not have associated user ID", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Rule: Validate user identity exists before processing any user requests
        users = data.get("users", [])
        user = next((u for u in users if u.get("user_id") == user_id), None)

        if not user:
            payload = {"error": f"User {user_id} not found", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Validate payment method
        payment_methods = user.get("payment_methods", {})
        selected_payment = None

        for method_id in payment_methods:
            if payment_method in method_id:
                selected_payment = payment_methods[method_id]
                break

        if not selected_payment:
            payload = {
                "error": f"Payment method {payment_method} not found for user",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        payment_source = selected_payment.get("source")
        if payment_source not in ["credit_card", "paypal", "gift_card"]:
            payload = {
                "error": f"Invalid payment method type: {payment_source}",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Rule: Confirm item_id exists in product variants before including in orders
        products = data.get("products", [])
        variant_found = None
        product_found = None

        for product in products:
            variants = product.get("variants", {})
            if item_id in variants:
                variant_found = variants[item_id]
                product_found = product
                break

        if not variant_found:
            payload = {
                "error": f"Item {item_id} not found in product catalog",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Rule: Check product availability status before allocation - never allocate unavailable items
        if not variant_found.get("available", False):
            payload = {
                "error": f"Item {item_id} ({product_found.get('name')}) is not available",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Get item details
        unit_price = variant_found.get("price", 0)
        line_total = unit_price * quantity

        # Capture current order state before modification
        current_order_items = order_to_update.get("items", []).copy()
        current_subtotal = sum(
            item.get("price", 0) * item.get("quantity", 1)
            for item in current_order_items
        )
        current_payment_history = order_to_update.get("payment_history", []).copy()
        current_total_paid = sum(
            payment.get("amount", 0)
            for payment in current_payment_history
            if payment.get("transaction_type") == "payment"
        )

        # WRITE OPERATION: Add item to order
        order_items = order_to_update.get("items", [])

        # Check if item already exists in the order
        item_exists = False
        added_quantity = quantity
        for existing_item in order_items:
            if existing_item.get("item_id") == item_id:
                # Update quantity of existing item
                old_quantity = existing_item.get("quantity", 1)
                new_quantity = old_quantity + quantity
                existing_item["quantity"] = new_quantity
                existing_item["price"] = unit_price  # Update price in case it changed
                item_exists = True

                result_message = f"Updated quantity of existing item from {old_quantity} to {new_quantity}"
                break

        if not item_exists:
            # Add new item to order
            new_item = {
                "name": product_found.get("name"),
                "product_id": product_found.get("product_id"),
                "item_id": item_id,
                "price": unit_price,
                "options": variant_found.get("options", {}),
                "quantity": quantity,
            }
            order_items.append(new_item)
            result_message = "Added new item to order"

        order_to_update["items"] = order_items

        # Calculate new order totals
        new_subtotal = sum(
            item.get("price", 0) * item.get("quantity", 1) for item in order_items
        )

        # Calculate additional costs
        additional_tax = tax_amount if tax_amount is not None else 0
        additional_shipping = shipping_cost if shipping_cost is not None else 0

        # Calculate total additional amount (item cost + additional fees)
        total_additional_amount = line_total + additional_tax + additional_shipping
        new_order_total = new_subtotal + additional_tax + additional_shipping

        # Rule: High-value orders (>$1000 total) require payment verification before fulfillment
        requires_verification = new_order_total > 1000.0

        # Rule: Gift card payments cannot exceed available balance - verify balance sufficiency before processing
        if payment_source == "gift_card":
            available_balance = selected_payment.get("balance", 0)
            if total_additional_amount > available_balance:
                payload = {
                    "error": f"Insufficient gift card balance. Available: ${available_balance}, Required: ${total_additional_amount}",
                    "status": "failed",
                }
                out = json.dumps(payload)
                return out

        # Process payment for the additional amount
        payment_result = {
            "payment_method_id": payment_method,
            "payment_source": payment_source,
            "amount": total_additional_amount,
            "verification_required": requires_verification,
            "transaction_id": f"TXN_{user_id}_{payment_method}_{int(total_additional_amount)}",
        }

        # Add specific details based on payment type
        if payment_source == "gift_card":
            new_balance = selected_payment.get("balance", 0) - total_additional_amount
            payment_result["remaining_gift_card_balance"] = new_balance
        elif payment_source == "credit_card":
            payment_result["card_brand"] = selected_payment.get("brand")
            payment_result["card_last_four"] = selected_payment.get("last_four")

        # Add payment transaction to order history
        payment_transaction = {
            "transaction_type": "payment",
            "amount": total_additional_amount,
            "payment_method_id": payment_method,
            "payment_source": payment_source,
            "processed_date": datetime.now().isoformat(),
            "reason": "item_addition",
        }

        if "payment_history" not in order_to_update:
            order_to_update["payment_history"] = []
        order_to_update["payment_history"].append(payment_transaction)

        # Add order modification log
        if "modifications" not in order_to_update:
            order_to_update["modifications"] = []

        order_to_update["modifications"].append(
            {
                "type": "item_added",
                "item_id": item_id,
                "quantity": added_quantity,
                "unit_price": unit_price,
                "line_total": line_total,
                "additional_tax": additional_tax,
                "additional_shipping": additional_shipping,
                "total_additional_cost": total_additional_amount,
                "payment_method": payment_method,
                "timestamp": datetime.now().isoformat(),
                "action": result_message,
            }
        )

        order_to_update["last_updated"] = datetime.now().isoformat()

        # Update the order in the data structure
        data["orders"][order_index] = order_to_update

        # Calculate comprehensive metrics
        total_items_count = len(order_items)
        total_quantity = sum(item.get("quantity", 1) for item in order_items)
        new_total_paid = current_total_paid + total_additional_amount

        result = {
            "status": "success",
            "order_id": formatted_order_id,
            "user_id": user_id,
            "item_added": {
                "item_id": item_id,
                "product_name": product_found.get("name"),
                "product_id": product_found.get("product_id"),
                "quantity": added_quantity,
                "unit_price": unit_price,
                "line_total": line_total,
                "options": variant_found.get("options", {}),
            },
            "action_performed": result_message,
            "current_order_before_addition": {
                "items": current_order_items,
                "total_items": len(current_order_items),
                "total_quantity": sum(
                    item.get("quantity", 1) for item in current_order_items
                ),
                "subtotal": round(current_subtotal, 2),
                "total_paid": round(current_total_paid, 2),
            },
            "updated_order_after_addition": {
                "items": order_items,
                "total_items": total_items_count,
                "total_quantity": total_quantity,
                "new_subtotal": round(new_subtotal, 2),
                "additional_costs": {
                    "tax_amount": additional_tax,
                    "shipping_cost": additional_shipping,
                    "total_additional": round(total_additional_amount, 2),
                },
                "new_order_total": round(new_order_total, 2),
                "requires_verification": requires_verification,
                "new_total_paid": round(new_total_paid, 2),
            },
            "payment_processing": {
                "payment_method": payment_method,
                "payment_source": payment_source,
                "amount_charged": round(total_additional_amount, 2),
                "payment_breakdown": {
                    "item_cost": round(line_total, 2),
                    "tax_amount": additional_tax,
                    "shipping_cost": additional_shipping,
                },
                "payment_result": payment_result,
                "verification_required": requires_verification,
            },
            "order_changes": {
                "subtotal_increase": round(new_subtotal - current_subtotal, 2),
                "total_payment_increase": round(total_additional_amount, 2),
                "items_added": 1 if not item_exists else 0,
                "quantity_added": added_quantity,
            },
            "last_updated": order_to_update["last_updated"],
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddToOrder",
                "description": "Add an item to an existing pending order with payment processing. Shows both current and updated order details. Only works for pending orders.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "Order identifier (e.g., 'W6893533' or '#W6893533')",
                        },
                        "item_id": {
                            "type": "string",
                            "description": "Product variant identifier to add to the order",
                        },
                        "payment_method": {
                            "type": "string",
                            "description": "Payment method identifier from customer's stored methods (required)",
                        },
                        "quantity": {
                            "type": "integer",
                            "description": "Quantity of the item to add (defaults to 1 if not specified)",
                            "default": 1,
                        },
                        "tax_amount": {
                            "type": "number",
                            "description": "Optional additional tax amount for the added item (defaults to 0)",
                        },
                        "shipping_cost": {
                            "type": "number",
                            "description": "Optional additional shipping cost for the added item (defaults to 0)",
                        },
                    },
                    "required": ["order_id", "item_id", "payment_method"],
                },
            },
        }
