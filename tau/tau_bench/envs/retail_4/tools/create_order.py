# Copyright Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateOrder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, items: List[Dict[str, Any]], payment_method_sources: List[str], return_refund_amount: float = None, return_order_id: str = None, **kwargs) -> str:
        """
        Create a new order for a customer with items, address, and payment processing using multiple payment methods
        Supports replacement orders with automatic refund deduction

        Writes to: orders.json (creates new order entry)
        Data Sources: users.json, products.json for validation
        """
        # Check the return parameters for validity if they are given.
        if return_refund_amount is not None and return_refund_amount < 0:
            return json.dumps({
                "error": "Return refund amount cannot be negative",
                "status": "failed"
            })

        # Condition: Confirm user identity is present prior to handling any requests.
        users = list(data.get("users", {}).values())
        user = next((u for u in users if u.get("user_id") == user_id), None)

        if not user:
            return json.dumps({"error": f"User {user_id} not found", "status": "failed"})

        # Check if the return order is present when return_order_id is supplied.
        if return_order_id:
            orders = list(data.get("orders", {}).values())
            return_order_found = False
            for order in orders:
                if order.get("order_id") == return_order_id and order.get("user_id") == user_id:
                    return_order_found = True
                    break

            if not return_order_found:
                return json.dumps({
                    "error": f"Return order {return_order_id} not found or does not belong to user {user_id}",
                    "status": "failed"
                })

        # Verify payment options and generate payment summary.
        payment_methods = user.get("payment_methods", {})
        selected_payments = []

        for payment_method_source in payment_method_sources:
            selected_payment = None

            # Retrieve payment method using its identifier.
            for method_id in payment_methods:
                if payment_method_source in method_id:
                    selected_payment = payment_methods[method_id]
                    break

            if not selected_payment:
                return json.dumps({"error": f"Payment method {payment_method_source} not found", "status": "failed"})

            payment_source = selected_payment.get("source")
            if payment_source not in ["credit_card", "paypal", "gift_card"]:
                return json.dumps({"error": f"Invalid payment method type: {payment_source}", "status": "failed"})

            payment_info = {
                "payment_method_id": payment_method_source,
                "payment_source": payment_source,
                "payment_details": selected_payment
            }
            selected_payments.append(payment_info)

        # Verify and handle items.
        products = list(data.get("products", {}).values())
        order_items = []
        subtotal_amount = 0.0

        # Condition: All items in multi-item orders must be in stock prior to confirmation.
        for item in items:
            item_id = item.get("item_id")
            quantity = item.get("quantity", 1)

            # Policy: Verify the presence of item_id in product variants prior to adding to orders.
            variant_found = None
            product_found = None

            for product in products:
                variants = product.get("variants", {})
                if item_id in variants:
                    variant_found = variants[item_id]
                    product_found = product
                    break

            if not variant_found:
                return json.dumps({"error": f"Item {item_id} not found in catalog", "status": "failed"})

            # Guideline: Verify product availability prior to allocation - do not allocate items that are not available.
            if not variant_found.get("available", False):
                return json.dumps({
                    "error": f"Item {item_id} ({product_found.get('name')}) is not available",
                    "status": "failed"
                })

            # Guideline: Apply precise variant pricing from the product catalog.
            unit_price = variant_found.get("price", 0)
            line_total = unit_price * quantity
            subtotal_amount += line_total

            order_items.append({
                "name": product_found.get("name"),
                "product_id": product_found.get("product_id"),
                "item_id": item_id,
                "price": unit_price,
                "options": variant_found.get("options", {}),
                "quantity": quantity
            })

        # Compute the total prior to refund subtraction.
        total_before_refund = subtotal_amount

        # Include shipping fees if available.
        if "shipping_cost" in kwargs:
            shipping_cost = kwargs["shipping_cost"]
            if shipping_cost < 0:
                return json.dumps({"error": "Shipping cost cannot be negative", "status": "failed"})
            total_before_refund += shipping_cost

        if 'tax_amount' in kwargs:
            tax_amount = kwargs["tax_amount"]
            if tax_amount < 0:
                return json.dumps({"error": "Tax amount cannot be negative", "status": "failed"})
            total_before_refund += tax_amount

        # Implement return refund adjustment.
        refund_applied = 0.0
        customer_refund_due = 0.0
        total_amount = total_before_refund

        if return_refund_amount is not None and return_refund_amount > 0:
            refund_applied = min(return_refund_amount, total_before_refund)
            total_amount = max(0, total_before_refund - return_refund_amount)

            # Determine the customer refund if the return amount surpasses the order total.
            if return_refund_amount > total_before_refund:
                customer_refund_due = return_refund_amount - total_before_refund

        # Proceed with payment processing only if there is an outstanding balance.
        payment_breakdown = []
        payment_validation = {"overall_valid": True, "messages": []}

        if total_amount > 0:
            # Determine payment distribution among various methods using intelligent allocation.
            remaining_amount = total_amount

            for i, payment_info in enumerate(selected_payments):
                payment_source = payment_info["payment_source"]
                payment_details = payment_info["payment_details"]

                # Calculate the allocation amount for this payment method.
                if payment_source == "gift_card":
                    # Distribute up to the available balance for gift cards.
                    available_balance = payment_details.get("balance", 0)
                    allocated_amount = min(available_balance, remaining_amount)

                    # Check that the gift card has a positive balance.
                    if available_balance == 0:
                        payment_validation["overall_valid"] = False
                        payment_validation["messages"].append(f"{payment_info['payment_method_id']}: Gift card has no available balance")
                        allocated_amount = 0
                else:
                    # Distribute the leftover balance for alternative payment options.
                    if i == len(selected_payments) - 1:  # The final payment method receives the leftover balance.
                        allocated_amount = remaining_amount
                    else:
                        # Compute equal allocation across the other non-gift-card payment methods.
                        remaining_methods = len(selected_payments) - i
                        allocated_amount = round(remaining_amount / remaining_methods, 2)
                        if allocated_amount > remaining_amount:
                            allocated_amount = remaining_amount

                # Verify payment option
                method_validation = {"valid": True, "message": "Payment method validated"}
                if payment_source == "gift_card":
                    available_balance = payment_details.get("balance", 0)
                    if available_balance == 0:
                        method_validation = {
                            "valid": False,
                            "message": "Gift card has no available balance"
                        }
                    elif allocated_amount < remaining_amount and allocated_amount == available_balance:
                        # The gift card does not cover the entire remaining balance, but this is managed by the allocation process.
                        method_validation["message"] = f"Gift card covers ${allocated_amount:.2f} of remaining ${remaining_amount:.2f}"

                if allocated_amount > 0:  # Include only payment methods with assigned amounts.
                    payment_breakdown.append({
                        "payment_method_id": payment_info["payment_method_id"],
                        "payment_source": payment_source,
                        "allocated_amount": round(allocated_amount, 2),
                        "validation": method_validation
                    })

                remaining_amount -= allocated_amount
                if not method_validation["valid"]:
                    payment_validation["overall_valid"] = False

                # Exit if the total allocation has been reached.
                if remaining_amount <= 0.01:  # Consider floating point accuracy.
                    break

            # Verify if there is any leftover amount after all distributions.
            if remaining_amount > 0.01:
                payment_validation["overall_valid"] = False
                payment_validation["messages"].append(f"Insufficient payment methods to cover ${remaining_amount:.2f}")
                return json.dumps({
                    "error": f"Insufficient payment methods to cover total amount of ${total_amount:.2f}. Remaining: ${remaining_amount:.2f}",
                    "status": "failed"
                })

            if not payment_validation["overall_valid"]:
                return json.dumps({
                    "error": "Payment validation failed: " + "; ".join(payment_validation["messages"]),
                    "status": "failed"
                })

        # Create a new order identifier.
        existing_orders = list(data.get("orders", {}).values())
        order_number = len(existing_orders) + 1
        new_order_id = f"#W{str(order_number).zfill(7)}"

        # Policy: Orders exceeding $1000 must undergo payment verification prior to processing.
        requires_verification = total_before_refund > 1000.0

        # Generate payment history records for every payment option.
        payment_history = []

        # Include refund deduction record if necessary.
        if refund_applied > 0:
            payment_history.append({
                "transaction_type": "refund_deduction",
                "amount": refund_applied,
                "return_order_id": return_order_id,
                "processed_date": datetime.now().isoformat(),
                "description": f"Refund deduction from return order {return_order_id}"
            })

        # Insert payment records for the outstanding balance.
        for payment in payment_breakdown:
            if payment["allocated_amount"] > 0:
                payment_history.append({
                    "transaction_type": "payment",
                    "amount": payment["allocated_amount"],
                    "payment_method_id": payment["payment_method_id"],
                    "payment_source": payment["payment_source"],
                    "processed_date": datetime.now().isoformat()
                })

        # Instantiate a new order object.
        new_order = {
            "order_id": new_order_id,
            "user_id": user_id,
            "address": user.get("address", {}),
            "items": order_items,
            "fulfillments": [],
            "status": "pending",
            "payment_history": payment_history,
            "payment_breakdown": payment_breakdown,
            "order_type": "replacement" if return_refund_amount is not None else "standard",
            "timestamp": datetime.now().isoformat()
        }

        # Include return details if this order is a replacement.
        if return_refund_amount is not None:
            new_order["return_replacement_info"] = {
                "original_return_order_id": return_order_id,
                "refund_amount_applied": refund_applied,
                "customer_refund_due": customer_refund_due,
                "replacement_order": True
            }

        # INSERT OPERATION: Append a new order to orders.json
        if "orders" not in data:
            data["orders"] = []
        data["orders"].append(new_order)

        # UPDATE OPERATION: Modify the user's order list in users.json.
        if "orders" not in user:
            user["orders"] = []
        user["orders"].append(new_order_id)

        # Compute the final values for the response.
        final_payment_amount = sum(p["allocated_amount"] for p in payment_breakdown)

        result = {
            "status": "success",
            "order_created": new_order_id,
            "user_id": user_id,
            "order_type": new_order["order_type"],
            "pricing_breakdown": {
                "subtotal": round(subtotal_amount, 2),
                "shipping_cost": round(kwargs.get("shipping_cost", 0), 2),
                "tax_amount": round(kwargs.get("tax_amount", 0), 2),
                "total_before_refund": round(total_before_refund, 2),
                "refund_applied": round(refund_applied, 2),
                "final_order_amount": round(total_amount, 2)
            },
            "total_items": len(order_items),
            "payment_breakdown": {
                "total_payment_methods": len(payment_breakdown),
                "payment_methods": payment_breakdown,
                "total_payment_amount": round(final_payment_amount, 2),
                "validation": payment_validation
            },
            "return_replacement_details": {
                "return_order_id": return_order_id,
                "refund_amount_applied": round(refund_applied, 2),
                "for_customer_refund": round(customer_refund_due, 2),
                "customer_refund_due": customer_refund_due > 0
            } if return_refund_amount is not None else None,
            "requires_verification": requires_verification,
            "order_status": "pending"
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_order",
                "description": "Create a new customer order with items and multiple payment methods processing. Supports replacement orders with automatic refund deduction.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "Customer identifier"},
                        "items": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "item_id": {"type": "string"},
                                    "quantity": {"type": "integer"}
                                },
                                "required": ["item_id", "quantity"]
                            },
                            "description": "List of items to include in order"
                        },
                        "payment_method_sources": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of payment method sources to use for payment"
                        },
                        "return_refund_amount": {
                            "type": "number",
                            "description": "Optional refund amount from returned items to deduct from this order. If greater than order total, excess will be refunded to customer."
                        },
                        "return_order_id": {
                            "type": "string",
                            "description": "Optional order ID that generated the return/refund (for tracking purposes)"
                        },
                        "shipping_cost": {
                            "type": "number",
                            "description": "Shipping costs to include in the order"
                        },
                        "tax_amount": {
                            "type": "number",
                            "description": "Optional tax amount to include in the order"
                        }
                    },
                    "required": ["user_id", "items", "payment_method_sources"]
                }
            }
        }
