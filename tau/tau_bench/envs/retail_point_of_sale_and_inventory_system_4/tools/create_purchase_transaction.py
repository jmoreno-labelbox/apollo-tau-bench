# Copyright Sierra Technologies

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreatePurchaseTransaction(Tool): # CREATE
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        customer_id: str,
        employee_id: str,
        items: Dict[str, int],
        store_id: str,
        current_time: str,
        payment_method: str
    ) -> str:
        products = {p["sku"]: p for p in list(data.get("products", {}).values())}
        inventory = list(data.get("inventory", {}).values())
        transactions = list(data.get("transactions", {}).values())

        line_items = []
        total_amount = 0.0
        total_tax = 0.0
        discount_total = 0.0
        for sku, quantity in items.items():
            product = products.get(sku)
            if not product:
                return json.dumps({"error": f"Product with SKU {sku} not found."})

            # Verify stock levels in inventory.
            inv_item = next((i for i in inventory if i["sku"] == sku and i["store_id"] == store_id), None)
            if not inv_item or inv_item.get("quantity", 0) < quantity:
                return json.dumps({"error": f"Insufficient stock of SKU {sku} in store {store_id}."})

            unit_price = product["price"]
            if product.get("is_discountable", True):
                discount_rate = product.get("discount_rate", 0.0)
                # assign 0 if the value is neither a float nor an integer
                if not isinstance(discount_rate, (float, int)):
                    discount_rate = 0.0
            else:
                discount_rate = 0.0
            discount = discount_rate * unit_price * quantity
            tax = unit_price * quantity * product["tax_rate"]
            line_items.append({
                "sku": sku,
                "quantity": quantity,
                "unit_price": unit_price,
                "discount": discount
            })
            total_amount += (unit_price * quantity) - discount +tax
            total_tax += tax
            discount_total += discount

            # Subtract inventory
            inv_item["quantity"] -= quantity

        transaction_id = f"TXN-{1000+ len(transactions) + 1}"
        transaction = {
            "transaction_id": transaction_id,
            "store_id": store_id,
            "employee_id": employee_id,
            "timestamp": current_time,
            "total_amount": round(total_amount, 2),
            "tax_amount": round(total_tax, 2),
            "payment_method": payment_method,
            "tax_rate": product["tax_rate"],
            "discount_total": round(discount_total,2),
            "change_given": 0.0,
            "status": "completed",
            "customer_id": customer_id,
            "line_items": line_items,
        }
        transactions.append(transaction)
        return json.dumps(transaction)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_purchase_transaction",
                "description": "Create a new purchase transaction for a customer, specifying items (SKU:quantity), employee, store, timestamp, and payment method. This checks the stock (but doesn't update it) and also calculates total amount, tax, and discounts. Returns the transaction details.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "The ID of the customer making the purchase."
                        },
                        "employee_id": {
                            "type": "string",
                            "description": "The ID of the employee processing the transaction."
                        },
                        "items": {
                            "type": "object",
                            "description": "Dictionary of SKU to quantity pairs for items being purchased."
                        },
                        "store_id": {
                            "type": "string",
                            "description": "The ID of the store where the purchase is made."
                        },
                        "current_time": {
                            "type": "string",
                            "format": "date-time",
                            "description": "Timestamp of the transaction (ISO format)."
                        },
                        "payment_method": {
                            "type": "string",
                            "description": "Payment method used for the transaction (e.g., 'credit_card', 'cash')."
                        }
                    },
                    "required": ["customer_id", "employee_id", "items", "store_id", "timestamp", "payment_method"]
                }
            }
        }
