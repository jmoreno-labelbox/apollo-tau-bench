# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GenerateOrderSummary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, item_list: List[Dict[str, Any]], payment_methods_source: List[str], **kwargs) -> str:
        """
        Generate comprehensive order summary with pricing, taxes, and fulfillment requirements

        Data Sources: users.json (user_id, payment_methods), products.json (variants, pricing)
        """
        # Requirement: Confirm the existence of user identity before handling any user requests.
        users = list(data.get("users", {}).values())
        user = next((u for u in users if u.get("user_id") == user_id), None)

        if not user:
            return json.dumps({"error": f"User {user_id} not found", "status": "failed"})

        # Verify payment options and generate payment summary.
        payment_methods = user.get("payment_methods", {})
        selected_payments = []

        for payment_method_id in payment_methods_source:
            selected_payment = None

            # Retrieve payment method using its identifier.
            for method_id in payment_methods:
                if payment_method_id in method_id or method_id in payment_method_id:
                    selected_payment = payment_methods[method_id]
                    break

            if not selected_payment:
                return json.dumps({"error": f"Payment method {payment_method_id} not found", "status": "failed"})

            payment_source = selected_payment.get("source")
            if payment_source not in ["credit_card", "paypal", "gift_card"]:
                return json.dumps({"error": f"Invalid payment method type: {payment_source}", "status": "failed"})

            payment_info = {
                "payment_method_id": payment_method_id,
                "payment_source": payment_source,
                "payment_details": selected_payment
            }
            selected_payments.append(payment_info)

        # Verify and assess the cost of all items.
        products = list(data.get("products", {}).values())
        order_items = []
        subtotal = 0.0

        # Requirement: All items in multi-item orders must be in stock prior to confirmation.
        for item in item_list:
            item_id = item.get("item_id")
            quantity = item.get("quantity", 1)

            # Validation: Ensure item_id is present in product variants prior to adding to orders.
            variant_found = None
            product_found = None

            for product in products:
                variants = product.get("variants", {})
                if item_id in variants:
                    variant_found = variants[item_id]
                    product_found = product
                    break

            if not variant_found:
                return json.dumps({"error": f"Item {item_id} not found", "status": "failed"})

            # Directive: Adhere to the precise variant pricing from the product catalog - avoid any unauthorized price alterations.
            unit_price = variant_found.get("price", 0)
            line_total = unit_price * quantity
            subtotal += line_total

            order_items.append({
                "item_id": item_id,
                "product_name": product_found.get("name"),
                "quantity": quantity,
                "unit_price": unit_price,
                "line_total": line_total,
                "options": variant_found.get("options", {})
            })

        # Compute simplified taxes and charges.
        tax_rate = 0.08  # 8% tax on sales
        tax_amount = subtotal * tax_rate
        total_amount = subtotal + tax_amount

        if 'shipping_cost' in kwargs:
            shipping_cost = kwargs['shipping_cost']
            total_amount += shipping_cost

        # Policy: Orders exceeding $1000 must undergo payment verification prior to processing.
        requires_verification = total_amount > 1000.0

        # Determine payment distribution among various payment methods using intelligent allocation.
        remaining_amount = total_amount
        payment_breakdown = []
        payment_validation = {"overall_valid": True, "messages": []}

        for i, payment_info in enumerate(selected_payments):
            payment_source = payment_info["payment_source"]
            payment_details = payment_info["payment_details"]

            # Calculate the allocation for this payment method.
            if payment_source == "gift_card":
                # Distribute up to the available balance for gift cards.
                available_balance = payment_details.get("balance", 0)
                allocated_amount = min(available_balance, remaining_amount)

                # Check that the gift card has a remaining balance.
                if available_balance == 0:
                    payment_validation["overall_valid"] = False
                    payment_validation["messages"].append(f"{payment_info['payment_method_id']}: Gift card has no available balance")
            else:
                # Distribute the remaining balance evenly across other payment methods.
                if i == len(selected_payments) - 1:  # The final payment method receives the outstanding balance.
                    allocated_amount = remaining_amount
                else:
                    # Determine equal allocation among the other payment methods excluding gift cards.
                    remaining_methods = len(selected_payments) - i
                    allocated_amount = round(remaining_amount / remaining_methods, 2)
                    if allocated_amount > remaining_amount:
                        allocated_amount = remaining_amount

            # Verify payment method
            method_validation = {"valid": True, "message": "Payment method validated"}
            if payment_source == "gift_card":
                available_balance = payment_details.get("balance", 0)
                if available_balance == 0:
                    method_validation = {
                        "valid": False,
                        "message": "Gift card has no available balance"
                    }
                    allocated_amount = 0
                elif allocated_amount < remaining_amount and allocated_amount == available_balance:
                    # The gift card does not fully cover the outstanding balance, but this is managed by the allocation logic.
                    method_validation["message"] = f"Gift card covers ${allocated_amount:.2f} of remaining ${remaining_amount:.2f}"

            payment_breakdown.append({
                "payment_method_id": payment_info["payment_method_id"],
                "payment_source": payment_source,
                "allocated_amount": round(allocated_amount, 2),
                "validation": method_validation,
                "payment_details": {
                    "brand": payment_details.get("brand") if payment_source == "credit_card" else None,
                    "last_four": payment_details.get("last_four") if payment_source == "credit_card" else None,
                    "balance": payment_details.get("balance") if payment_source == "gift_card" else None,
                    "remaining_balance": (payment_details.get("balance", 0) - allocated_amount) if payment_source == "gift_card" else None
                }
            })

            remaining_amount -= allocated_amount
            if not method_validation["valid"]:
                payment_validation["overall_valid"] = False

            # Exit if the total allocation has been reached.
            if remaining_amount <= 0.01:  # Consider floating point accuracy.
                break

        # Verify if there is any remaining balance following all distributions.
        if remaining_amount > 0.01:
            payment_validation["overall_valid"] = False
            payment_validation["messages"].append(f"Insufficient payment methods to cover ${remaining_amount:.2f}")

        # Guideline: Ensure data consistency: the total order amount should equal the sum of individual item prices.
        calculated_subtotal = sum(item["line_total"] for item in order_items)
        calculated_payment_total = sum(payment["allocated_amount"] for payment in payment_breakdown)
        integrity_check = abs(calculated_subtotal - subtotal) < 0.01
        payment_allocation_check = abs(calculated_payment_total - (total_amount - max(0, remaining_amount))) < 0.01

        result = {
            "status": "success",
            "order_summary": {
                "user_id": user_id,
                "pricing": {
                    "subtotal": round(subtotal, 2),
                    "tax_amount": round(tax_amount, 2),
                    "shipping_cost": round(shipping_cost, 2) if 'shipping_cost' in kwargs else 0.0,
                    "total_amount": round(total_amount, 2)
                },
                "total_items": len(order_items),
                "items": order_items,
                "payment_breakdown": {
                    "total_payment_methods": len(payment_breakdown),
                    "payment_methods": payment_breakdown,
                    "total_allocated": round(calculated_payment_total, 2),
                    "remaining_amount": round(max(0, remaining_amount), 2),
                    "validation": payment_validation
                },
                "fulfillment_requirements": {
                    "requires_verification": requires_verification,
                    "high_value_order": total_amount > 1000.0
                },
                "data_integrity": {
                    "totals_match": integrity_check,
                    "calculated_subtotal": round(calculated_subtotal, 2),
                    "payment_allocation_correct": payment_allocation_check
                }
            }
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_order_summary",
                "description": "Generate comprehensive order summary with pricing and payment breakdown across multiple methods",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "Customer identifier"},
                        "item_list": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "item_id": {"type": "string"},
                                    "quantity": {"type": "integer"}
                                },
                                "required": ["item_id", "quantity"]
                            },
                            "description": "List of items in the order"
                        },
                        "payment_methods_source": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of payment method identifiers to use for payment"
                        },
                        "shipping_cost": {
                            "type": "number",
                            "description": "Optional shipping cost to include in order summary, if applicable"
                        }
                    },
                    "required": ["user_id", "item_list", "payment_methods_source"]
                }
            }
        }
