# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateRefundTransaction(Tool): # CREATE
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        sku: str,
        quantity: int,
        employee_id: str,
        current_time: str,
        original_transaction_id: str,
    ) -> str:
        transactions = data["transactions"]
        for transaction in transactions:
            if transaction["transaction_id"] == original_transaction_id:
                original_transaction = transaction
                break

        refund_transaction = original_transaction.copy()
        refund_transaction["transaction_id"] = original_transaction_id + "REFUND" + sku
        refund_transaction["employee_id"] = employee_id
        refund_transaction["status"] = "refund"
        refund_transaction["timestamp"] = current_time

        item_info = {}
        for item in original_transaction["line_items"]:
            if item["sku"] == sku:
                item_info = item

        total_refund_amount = item_info["unit_price"] * (1 + original_transaction["tax_rate"]) * quantity - item_info["discount"]
        refund_transaction["total_amount"] = total_refund_amount * -1  # Refund not approved.

        total_tax = item_info["unit_price"] * original_transaction["tax_rate"] * quantity
        refund_transaction["tax_amount"] = total_tax
        refund_transaction["discount_total"] = 0.0
        refund_transaction["change_given"] = 0.0
        refund_transaction["status"] = "refund"
        item_info["quantity"] = quantity
        refund_transaction["line_items"] = [item_info]

        # Add to transactions table
        transactions.append(refund_transaction)

        return json.dumps(refund_transaction)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_refund_transaction",
                "description": "Create a new refund transaction for a given product SKU and customer, using the original transaction's context.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the refunded product."
                        },
                        "quantity": {
                            "type": "integer",
                            "description": "The quantity of items being refunded."
                        },
                        "employee_id": {
                            "type": "string",
                            "description": "The employee issuing the refund."
                        },
                        "current_time": {
                            "type": "string",
                            "format": "date-time",
                            "description": "The current time for the refund transaction."
                        },
                        "original_transaction_id": {
                            "type": "string",
                            "description": "The ID of the original transaction being refunded."
                        }
                    },
                    "required": ["customer_id", "sku", "quantity", "employee_id", "origional_transaction_id"]
                }
            }
        }
