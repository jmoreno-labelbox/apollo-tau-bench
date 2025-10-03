from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class ProcessReturn(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        original_transaction_id: str,
        items_to_return: list[dict[str, Any]],
        reason: str
    ) -> str:
        transactions = data.get("transactions", [])
        original_txn = next(
            (
                t
                for t in transactions
                if t.get("transaction_id") == original_transaction_id
            ),
            None,
        )
        if not original_txn:
            payload = {"error": f"Original transaction {original_transaction_id} not found."}
            out = json.dumps(payload)
            return out

        inventory = data.get("inventory", [])
        return_amount = 0.0
        validated_returns = []

        for return_item in items_to_return:
            sku = return_item.get("sku")
            return_quantity = return_item.get("quantity", 1)

            original_item = next(
                (
                    item
                    for item in original_txn.get("line_items", [])
                    if item.get("sku") == sku
                ),
                None,
            )
            if not original_item:
                payload = {
                    "error": f"Product {sku} was not in original transaction {original_transaction_id}."
                }
                out = json.dumps(payload)
                return out

            if return_quantity > original_item.get("quantity", 0):
                payload = {
                    "error": f"Cannot return {return_quantity} of {sku}. Original quantity was {original_item.get('quantity', 0)}."
                }
                out = json.dumps(payload)
                return out

            # Revise stock levels (reintroduce returned products)
            any_store_inventory = next(
                (inv for inv in inventory if inv.get("sku") == sku), None
            )
            if any_store_inventory:
                any_store_inventory["quantity"] = (
                    any_store_inventory.get("quantity", 0) + return_quantity
                )

            unit_price = original_item.get("unit_price", 0.0)
            item_return_amount = unit_price * return_quantity
            return_amount += item_return_amount

            validated_returns.append(
                {
                    "sku": sku,
                    "name": original_item.get("name"),
                    "quantity": return_quantity,
                    "unit_price": unit_price,
                    "return_amount": item_return_amount,
                }
            )

        return_transaction_id = f"RTN-{len(transactions) + 1:04d}"

        return_transaction = {
            "transaction_id": return_transaction_id,
            "type": "return",
            "original_transaction_id": original_transaction_id,
            "customer_id": original_txn.get("customer_id"),
            "date": datetime.now().strftime("%Y-%m-%d"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "items": validated_returns,
            "total_amount": -return_amount,
            "reason": reason,
            "status": "completed",
        }

        transactions.append(return_transaction)
        data["transactions"] = transactions
        payload = return_transaction
        out = json.dumps(payload, indent=2)
        return out
        pass
        transactions = data.get("transactions", [])
        original_txn = next(
            (
                t
                for t in transactions
                if t.get("transaction_id") == original_transaction_id
            ),
            None,
        )
        if not original_txn:
            payload = {"error": f"Original transaction {original_transaction_id} not found."}
            out = json.dumps(
                payload)
            return out

        inventory = data.get("inventory", [])
        return_amount = 0.0
        validated_returns = []

        for return_item in items_to_return:
            sku = return_item.get("sku")
            return_quantity = return_item.get("quantity", 1)

            original_item = next(
                (
                    item
                    for item in original_txn.get("line_items", [])
                    if item.get("sku") == sku
                ),
                None,
            )
            if not original_item:
                payload = {
                        "error": f"Product {sku} was not in original transaction {original_transaction_id}."
                    }
                out = json.dumps(
                    payload)
                return out

            if return_quantity > original_item.get("quantity", 0):
                payload = {
                        "error": f"Cannot return {return_quantity} of {sku}. Original quantity was {original_item.get('quantity', 0)}."
                    }
                out = json.dumps(
                    payload)
                return out

            #Revise stock levels (reintroduce returned products)
            any_store_inventory = next(
                (inv for inv in inventory if inv.get("sku") == sku), None
            )
            if any_store_inventory:
                any_store_inventory["quantity"] = (
                    any_store_inventory.get("quantity", 0) + return_quantity
                )

            unit_price = original_item.get("unit_price", 0.0)
            item_return_amount = unit_price * return_quantity
            return_amount += item_return_amount

            validated_returns.append(
                {
                    "sku": sku,
                    "name": original_item.get("name"),
                    "quantity": return_quantity,
                    "unit_price": unit_price,
                    "return_amount": item_return_amount,
                }
            )

        return_transaction_id = f"RTN-{len(transactions) + 1:04d}"

        return_transaction = {
            "transaction_id": return_transaction_id,
            "type": "return",
            "original_transaction_id": original_transaction_id,
            "customer_id": original_txn.get("customer_id"),
            "date": datetime.now().strftime("%Y-%m-%d"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "items": validated_returns,
            "total_amount": -return_amount,
            "reason": reason,
            "status": "completed",
        }

        transactions.append(return_transaction)
        data["transactions"] = transactions
        payload = return_transaction
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ProcessReturn",
                "description": "Process a return for items from a previous transaction.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "original_transaction_id": {
                            "type": "string",
                            "description": "ID of the original transaction.",
                        },
                        "items_to_return": {
                            "type": "array",
                            "description": "List of items being returned.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {
                                        "type": "string",
                                        "description": "Product SKU.",
                                    },
                                    "quantity": {
                                        "type": "integer",
                                        "description": "Quantity being returned.",
                                    },
                                },
                                "required": ["sku", "quantity"],
                            },
                        },
                        "reason": {
                            "type": "string",
                            "description": "Reason for the return.",
                        },
                    },
                    "required": [
                        "original_transaction_id",
                        "items_to_return",
                        "reason",
                    ],
                },
            },
        }
