# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RecordSale(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str, items: List[Dict[str, Any]], payment_method: str) -> str:
        customers = list(data.get("customers", {}).values())
        customer = next((c for c in customers if c.get("customer_id") == customer_id), None)
        if not customer:
            return json.dumps({"error": f"Customer with ID {customer_id} not found."})

        products = list(data.get("products", {}).values())
        inventory = list(data.get("inventory", {}).values())
        total_amount = 0.0
        validated_items = []

        for item in items:
            sku = item.get("sku")
            quantity = item.get("quantity", 1)

            product = next((p for p in products if p.get("sku") == sku), None)
            if not product:
                return json.dumps({"error": f"Product with SKU {sku} not found."})

            # Verify stock levels
            total_available = 0
            for inv in inventory:
                if inv.get("sku") == sku:
                    total_available += inv.get("quantity", 0) - inv.get("reserved_quantity", 0)

            if total_available < quantity:
                return json.dumps({"error": f"Insufficient stock for product {sku}. Available: {total_available}, Requested: {quantity}"})

            # Refresh stock levels
            remaining_quantity = quantity
            for inv in inventory:
                if inv.get("sku") == sku and remaining_quantity > 0:
                    available = inv.get("quantity", 0) - inv.get("reserved_quantity", 0)
                    if available > 0:
                        deduct = min(available, remaining_quantity)
                        inv["quantity"] = inv.get("quantity", 0) - deduct
                        remaining_quantity -= deduct

            unit_price = product.get("price", 0.0)
            item_total = unit_price * quantity
            total_amount += item_total

            validated_items.append({
                "sku": sku,
                "name": product.get('name'),
                "quantity": quantity,
                "unit_price": unit_price,
                "total_price": item_total
            })

        transactions = list(data.get("transactions", {}).values())
        transaction_id = _get_next_transaction_id(transactions)

        transaction = {
            "transaction_id": transaction_id,
            "customer_id": customer_id,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "items": validated_items,
            "total_amount": total_amount,
            "payment_method": payment_method,
            "status": "completed"
        }

        transactions.append(transaction)
        data["transactions"][transaction_id] = transaction
        return json.dumps(transaction, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "record_sale",
                "description": "Record a new sale transaction.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Unique identifier of the customer."},
                        "items": {
                            "type": "array",
                            "description": "List of items being purchased.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {"type": "string", "description": "Product SKU."},
                                    "quantity": {"type": "integer", "description": "Quantity being purchased."}
                                },
                                "required": ["sku", "quantity"]
                            }
                        },
                        "payment_method": {"type": "string", "description": "Payment method used."}
                    },
                    "required": ["customer_id", "items", "payment_method"]
                }
            }
        }
