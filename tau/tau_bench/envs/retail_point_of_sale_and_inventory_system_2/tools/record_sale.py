from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class RecordSale(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        customer_id: str,
        items: list[dict[str, Any]],
        payment_method: str
    ) -> str:
        customers = data.get("customers", [])
        customer = next(
            (c for c in customers if c.get("customer_id") == customer_id), None
        )
        if not customer:
            payload = {"error": f"Customer with ID {customer_id} not found."}
            out = json.dumps(payload)
            return out

        products = data.get("products", [])
        inventory = data.get("inventory", [])
        total_amount = 0.0
        validated_items = []

        for item in items:
            sku = item.get("sku")
            quantity = item.get("quantity", 1)

            product = next((p for p in products if p.get("sku") == sku), None)
            if not product:
                payload = {"error": f"Product with SKU {sku} not found."}
                out = json.dumps(payload)
                return out

            # Verify stock availability
            total_available = 0
            for inv in inventory:
                if inv.get("sku") == sku:
                    total_available += inv.get("quantity", 0) - inv.get(
                        "reserved_quantity", 0
                    )

            if total_available < quantity:
                payload = {
                    "error": f"Insufficient stock for product {sku}. Available: {total_available}, Requested: {quantity}"
                }
                out = json.dumps(payload)
                return out

            # Revise stock levels
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

            validated_items.append(
                {
                    "sku": sku,
                    "name": product.get("name"),
                    "quantity": quantity,
                    "unit_price": unit_price,
                    "total_price": item_total,
                }
            )

        transactions = data.get("transactions", [])
        transaction_id = _get_next_transaction_id(transactions)

        # Calculate tax amount (assuming 8.25% tax rate)
        tax_rate = 0.0825
        tax_amount = total_amount * tax_rate
        final_total = total_amount + tax_amount

        # Convert validated_items to line_items format
        line_items = []
        for item in validated_items:
            line_items.append({
                "sku": item["sku"],
                "quantity": item["quantity"],
                "unit_price": item["unit_price"],
                "discount": 0.0  # No discount applied in RecordSale
            })

        # Create transaction with proper structure matching data file
        transaction = {
            "transaction_id": transaction_id,
            "store_id": "STORE-001",  # Default store
            "employee_id": "EMP-1002",  # Default employee
            "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "total_amount": final_total,
            "tax_amount": tax_amount,
            "payment_method": payment_method,
            "tax_rate": tax_rate,
            "discount_total": 0.0,
            "change_given": 0.0,
            "status": "completed",
            "customer_id": customer_id,
            "line_items": line_items,
        }

        transactions.append(transaction)
        data["transactions"] = transactions
        payload = transaction
        out = json.dumps(payload, indent=2)
        return out
        pass
        customers = data.get("customers", [])
        customer = next(
            (c for c in customers if c.get("customer_id") == customer_id), None
        )
        if not customer:
            payload = {"error": f"Customer with ID {customer_id} not found."}
            out = json.dumps(payload)
            return out

        products = data.get("products", [])
        inventory = data.get("inventory", [])
        total_amount = 0.0
        validated_items = []

        for item in items:
            sku = item.get("sku")
            quantity = item.get("quantity", 1)

            product = next((p for p in products if p.get("sku") == sku), None)
            if not product:
                payload = {"error": f"Product with SKU {sku} not found."}
                out = json.dumps(payload)
                return out

            #Verify stock availability
            total_available = 0
            for inv in inventory:
                if inv.get("sku") == sku:
                    total_available += inv.get("quantity", 0) - inv.get(
                        "reserved_quantity", 0
                    )

            if total_available < quantity:
                payload = {
                        "error": f"Insufficient stock for product {sku}. Available: {total_available}, Requested: {quantity}"
                    }
                out = json.dumps(
                    payload)
                return out

            #Revise stock levels
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

            validated_items.append(
                {
                    "sku": sku,
                    "name": product.get("name"),
                    "quantity": quantity,
                    "unit_price": unit_price,
                    "total_price": item_total,
                }
            )

        transactions = data.get("transactions", [])
        transaction_id = _get_next_transaction_id(transactions)

        # Calculate tax amount (assuming 8.25% tax rate)
        tax_rate = 0.0825
        tax_amount = total_amount * tax_rate
        final_total = total_amount + tax_amount

        # Convert validated_items to line_items format
        line_items = []
        for item in validated_items:
            line_items.append({
                "sku": item["sku"],
                "quantity": item["quantity"],
                "unit_price": item["unit_price"],
                "discount": 0.0  # No discount applied in RecordSale
            })

        # Create transaction with proper structure matching data file
        transaction = {
            "transaction_id": transaction_id,
            "store_id": "STORE-001",  # Default store
            "employee_id": "EMP-1002",  # Default employee
            "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "total_amount": final_total,
            "tax_amount": tax_amount,
            "payment_method": payment_method,
            "tax_rate": tax_rate,
            "discount_total": 0.0,
            "change_given": 0.0,
            "status": "completed",
            "customer_id": customer_id,
            "line_items": line_items,
        }

        transactions.append(transaction)
        data["transactions"] = transactions
        payload = transaction
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordSale",
                "description": "Record a new sale transaction.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique identifier of the customer.",
                        },
                        "items": {
                            "type": "array",
                            "description": "List of items being purchased.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {
                                        "type": "string",
                                        "description": "Product SKU.",
                                    },
                                    "quantity": {
                                        "type": "integer",
                                        "description": "Quantity being purchased.",
                                    },
                                },
                                "required": ["sku", "quantity"],
                            },
                        },
                        "payment_method": {
                            "type": "string",
                            "description": "Payment method used.",
                        },
                    },
                    "required": ["customer_id", "items", "payment_method"],
                },
            },
        }
