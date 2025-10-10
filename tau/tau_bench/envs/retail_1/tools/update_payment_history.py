# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdatePaymentHistory(Tool): # CREATE
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, transaction_type: str, payment_info_to_update: Dict[str, Any]) -> str:
        db = list(data.get("orders", {}).values())
        order = [row for row in db if row["order_id"] == order_id]

        if len(order) > 1:
            return json.dumps({"error":f"More than one order found with id: {order_id}"})
        if not order:
            return json.dumps({"error":f"Order with id: {order_id} not found"})
        order = order[0]

        payment_history = order["payment_history"]
        for payment in payment_history:
            if payment["transaction_type"] == transaction_type:
                for key, value in payment_info_to_update.items():
                    payment[key] = value
                return json.dumps(payment_history)
        return json.dumps({"error":f"No payment of transaction type {transaction_type} found. Use UpdateDB tool to add payments"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_payment_history",
                "description": "Update values in an orders payment history.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The ID of the order to update."},
                        "transaction_type": {"type": "string", "description": "The type of transaction to update."},
                        "payment_info_to_update": {
                            "type": "object",
                            "description": "A dictionary containing payment information to update."
                        }
                    },
                    "required": ["order_id", "transaction_type", "payment_info_to_update"]
                }
            }
        }
