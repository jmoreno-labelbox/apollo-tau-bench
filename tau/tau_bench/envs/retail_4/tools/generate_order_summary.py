from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GenerateOrderSummary(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str,
        item_list: list[dict[str, Any]],
        payment_methods_source: list[str],
        shipping_cost: float = 0.0,
    ) -> str:
        """
        Generate comprehensive order summary with pricing, taxes, and fulfillment requirements

        Data Sources: users.json (user_id, payment_methods), products.json (variants, pricing)
        """
        pass
        #Rule: Validate user identity exists before processing any user requests
        users = data.get("users", {}).values()
        user = next((u for u in users.values() if u.get("user_id") == user_id), None)

        if not user:
            payload = {"error": f"User {user_id} not found", "status": "failed"}
            out = json.dumps(
                payload)
            return out

        #Validate payment methods and prepare payment breakdown
        payment_methods = user.get("payment_methods", {}).values()
        selected_payments = []

        for payment_method_id in payment_methods_source:
            selected_payment = None

            #Find payment method by ID
            for method_id in payment_methods:
                if payment_method_id in method_id or method_id in payment_method_id:
                    selected_payment = payment_methods[method_id]
                    break

            if not selected_payment:
                payload = {
                        "error": f"Payment method {payment_method_id} not found",
                        "status": "failed",
                    }
                out = json.dumps(
                    payload)
                return out

            payment_source = selected_payment.get("source")
            if payment_source not in ["credit_card", "paypal", "gift_card"]:
                payload = {
                        "error": f"Invalid payment method type: {payment_source}",
                        "status": "failed",
                    }
                out = json.dumps(
                    payload)
                return out

            payment_info = {
                "payment_method_id": payment_method_id,
                "payment_source": payment_source,
                "payment_details": selected_payment,
            }
            selected_payments.append(payment_info)

        #Validate and price all items
        products = data.get("products", {}).values()
        order_items = []
        subtotal = 0.0

        #Rule: Multi-item orders need all items available before confirmation
        for item in item_list:
            item_id = item.get("item_id")
            quantity = item.get("quantity", 1)

            #Rule: Confirm item_id exists in product variants before including in orders
            variant_found = None
            product_found = None

            for product in products.values():
                variants = product.get("variants", {}).values()
                if item_id in variants:
                    variant_found = variants[item_id]
                    product_found = product
                    break

            if not variant_found:
                payload = {"error": f"Item {item_id} not found", "status": "failed"}
                out = json.dumps(
                    payload)
                return out

            #Rule: Use exact variant pricing from product catalog - no unauthorized price modifications
            unit_price = variant_found.get("price", 0)
            line_total = unit_price * quantity
            subtotal += line_total

            order_items.append(
                {
                    "item_id": item_id,
                    "product_name": product_found.get("name"),
                    "quantity": quantity,
                    "unit_price": unit_price,
                    "line_total": line_total,
                    "options": variant_found.get("options", {}).values()),
                }
            )

        #Calculate taxes and fees (simplified)
        tax_rate = 0.08  #8% sales tax
        tax_amount = subtotal * tax_rate
        total_amount = subtotal + tax_amount

        total_amount += shipping_cost

        #Rule: High-value orders (>$1000 total) require payment verification before fulfillment
        requires_verification = total_amount > 1000.0

        #Calculate payment allocation across multiple payment methods with smart allocation
        remaining_amount = total_amount
        payment_breakdown = []
        payment_validation = {"overall_valid": True, "messages": []}

        for i, payment_info in enumerate(selected_payments):
            payment_source = payment_info["payment_source"]
            payment_details = payment_info["payment_details"]

            #Determine how much to allocate to this payment method
            if payment_source == "gift_card":
                #For gift cards, allocate up to available balance
                available_balance = payment_details.get("balance", 0)
                allocated_amount = min(available_balance, remaining_amount)

                #Validate gift card has some balance
                if available_balance == 0:
                    payment_validation["overall_valid"] = False
                    payment_validation["messages"].append(
                        f"{payment_info['payment_method_id']}: Gift card has no available balance"
                    )
            else:
                #For other payment methods, allocate remaining amount or even distribution
                if (
                    i == len(selected_payments) - 1
                ):  #Last payment method gets remaining amount
                    allocated_amount = remaining_amount
                else:
                    #Calculate even distribution among remaining non-gift-card methods
                    remaining_methods = len(selected_payments) - i
                    allocated_amount = round(remaining_amount / remaining_methods, 2)
                    if allocated_amount > remaining_amount:
                        allocated_amount = remaining_amount

            #Validate payment method
            method_validation = {"valid": True, "message": "Payment method validated"}
            if payment_source == "gift_card":
                available_balance = payment_details.get("balance", 0)
                if available_balance == 0:
                    method_validation = {
                        "valid": False,
                        "message": "Gift card has no available balance",
                    }
                    allocated_amount = 0
                elif (
                    allocated_amount < remaining_amount
                    and allocated_amount == available_balance
                ):
                    #Gift card doesn't cover full remaining amount, but this is handled by allocation logic
                    method_validation["message"] = (
                        f"Gift card covers ${allocated_amount:.2f} of remaining ${remaining_amount:.2f}"
                    )

            payment_breakdown.append(
                {
                    "payment_method_id": payment_info["payment_method_id"],
                    "payment_source": payment_source,
                    "allocated_amount": round(allocated_amount, 2),
                    "validation": method_validation,
                    "payment_details": {
                        "brand": (
                            payment_details.get("brand")
                            if payment_source == "credit_card"
                            else None
                        ),
                        "last_four": (
                            payment_details.get("last_four")
                            if payment_source == "credit_card"
                            else None
                        ),
                        "balance": (
                            payment_details.get("balance")
                            if payment_source == "gift_card"
                            else None
                        ),
                        "remaining_balance": (
                            (payment_details.get("balance", 0) - allocated_amount)
                            if payment_source == "gift_card"
                            else None
                        ),
                    },
                }
            )

            remaining_amount -= allocated_amount
            if not method_validation["valid"]:
                payment_validation["overall_valid"] = False

            #Break if we've allocated the full amount
            if remaining_amount <= 0.01:  #Account for floating point precision
                break

        #Check if we still have remaining amount after all allocations
        if remaining_amount > 0.01:
            payment_validation["overall_valid"] = False
            payment_validation["messages"].append(
                f"Insufficient payment methods to cover ${remaining_amount:.2f}"
            )

        #Rule: Maintain data integrity: order totals must match sum of item prices
        calculated_subtotal = sum(item["line_total"] for item in order_items.values()
        calculated_payment_total = sum(
            payment["allocated_amount"] for payment in payment_breakdown
        )
        integrity_check = abs(calculated_subtotal - subtotal) < 0.01
        payment_allocation_check = (
            abs(calculated_payment_total - (total_amount - max(0, remaining_amount)))
            < 0.01
        )

        result = {
            "status": "success",
            "order_summary": {
                "user_id": user_id,
                "pricing": {
                    "subtotal": round(subtotal, 2),
                    "tax_amount": round(tax_amount, 2),
                    "shipping_cost": round(shipping_cost, 2),
                    "total_amount": round(total_amount, 2),
                },
                "total_items": len(order_items),
                "items": order_items,
                "payment_breakdown": {
                    "total_payment_methods": len(payment_breakdown),
                    "payment_methods": payment_breakdown,
                    "total_allocated": round(calculated_payment_total, 2),
                    "remaining_amount": round(max(0, remaining_amount), 2),
                    "validation": payment_validation,
                },
                "fulfillment_requirements": {
                    "requires_verification": requires_verification,
                    "high_value_order": total_amount > 1000.0,
                },
                "data_integrity": {
                    "totals_match": integrity_check,
                    "calculated_subtotal": round(calculated_subtotal, 2),
                    "payment_allocation_correct": payment_allocation_check,
                },
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
                "name": "GenerateOrderSummary",
                "description": "Generate comprehensive order summary with pricing and payment breakdown across multiple methods",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Customer identifier",
                        },
                        "item_list": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "item_id": {"type": "string"},
                                    "quantity": {"type": "integer"},
                                },
                                "required": ["item_id", "quantity"],
                            },
                            "description": "List of items in the order",
                        },
                        "payment_methods_source": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of payment method identifiers to use for payment",
                        },
                        "shipping_cost": {
                            "type": "number",
                            "description": "Optional shipping cost to include in order summary, if applicable",
                        },
                    },
                    "required": ["user_id", "item_list", "payment_methods_source"],
                },
            },
        }
