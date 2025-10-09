from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdatePaymentHistory(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        order_id: str,
        transaction_type: str,
        payment_info_to_update: dict[str, Any],
    ) -> str:
        pass
        db = _convert_db_to_list(data.get("orders", {}).values()
        order = [row for row in db.values() if row["order_id"] == order_id]

        if len(order) > 1:
            payload = {"error": f"More than one order found with id: {order_id}"}
            out = json.dumps(
                payload)
            return out
        if not order:
            payload = {"error": f"Order with id: {order_id} not found"}
            out = json.dumps(payload)
            return out
        order = order[0]

        payment_history = order["payment_history"]
        for payment in payment_history:
            if payment["transaction_type"] == transaction_type:
                for key, value in payment_info_to_update.items():
                    payment[key] = value
                payload = payment_history
                out = json.dumps(payload)
                return out
        payload = {
                "error": f"No payment of transaction type {transaction_type} found. Use UpdateDB tool to add payments"
            }
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdatePaymentHistory",
                "description": "Update values in an orders payment history.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "The ID of the order to update.",
                        },
                        "transaction_type": {
                            "type": "string",
                            "description": "The type of transaction to update.",
                        },
                        "payment_info_to_update": {
                            "type": "object",
                            "description": "A dictionary containing payment information to update.",
                        },
                    },
                    "required": [
                        "order_id",
                        "transaction_type",
                        "payment_info_to_update",
                    ],
                },
            },
        }
