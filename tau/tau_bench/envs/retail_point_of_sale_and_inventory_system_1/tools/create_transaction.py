# Copyright Sierra

import re
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateTransaction(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id, employee_id, payment_method, store_id, discount_total = 0.0, line_items = [], tax_amount = 0.0, total_amount = 0.0) -> str:

        transactions = list(data.get("transactions", {}).values())

        max_transaction_id_num = 0
        for transaction in transactions:
            txn_id = transaction.get("transaction_id")
            if isinstance(txn_id, str):
                match = re.match(r"TXN-(\d+)", txn_id)
                if match:
                    num = int(match.group(1))
                    max_transaction_id_num = max(max_transaction_id_num, num)

        next_transaction_id_num = max_transaction_id_num + 1
        new_transaction_id = f"TXN-{next_transaction_id_num:04d}"

        new_transaction = {
            "transaction_id": new_transaction_id,
            "store_id": store_id,
            "employee_id": employee_id,
            "total_amount": total_amount,
            "tax_amount": tax_amount,
            "payment_method": payment_method,
            "tax_rate": 0.0825,
            "discount_total": discount_total,
            "change_given": 0.0,
            "status": "completed",
            "customer_id": customer_id,
            "line_items": line_items,
        }

        transactions.append(new_transaction)
        data["transactions"] = transactions

        return json.dumps({"transaction_id": new_transaction_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_transaction",
                "description": "Creates a new transaction record for a completed sale.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {
                            "type": "string",
                            "description": "The ID of the store where the transaction occurred.",
                        },
                        "employee_id": {
                            "type": "string",
                            "description": "The ID of the employee who processed the transaction.",
                        },
                        "total_amount": {
                            "type": "number",
                            "format": "float",
                            "description": "The total amount of the transaction.",
                        },
                        "tax_amount": {
                            "type": "number",
                            "format": "float",
                            "description": "The total tax amount applied to the transaction.",
                        },
                        "payment_method": {
                            "type": "string",
                            "description": "The method of payment used for the transaction (e.g., 'credit_card', 'cash', 'mobile_wallet').",
                        },
                        "discount_total": {
                            "type": "number",
                            "format": "float",
                            "description": "The total discount applied to the transaction.",
                        },
                        "customer_id": {
                            "type": "string",
                            "description": "The ID of the customer associated with the transaction.",
                        },
                        "line_items": {
                            "type": "array",
                            "description": "A list of items included in the transaction.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {"type": "string"},
                                    "quantity": {"type": "integer"},
                                    "unit_price": {"type": "number", "format": "float"},
                                    "discount": {"type": "number", "format": "float"},
                                },
                                "required": ["sku", "quantity", "unit_price", "discount"],
                            },
                        },
                    },
                    "required": ["store_id", "employee_id", "total_amount", "tax_amount", "payment_method", "discount_total", "customer_id", "line_items"],
                },
            },
        }
