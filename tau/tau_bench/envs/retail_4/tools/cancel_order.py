# Copyright Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CancelOrder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, order_id: str, cancellation_reason: str = "customer_request") -> str:
        """
        Cancel a customer order and process refund if applicable

        Writes to: orders.json (updates order status to cancelled)
        Data Sources: users.json for validation
        """
        # Requirement: Confirm the existence of user identity prior to handling any user requests.
        users = list(data.get("users", {}).values())
        user = next((u for u in users if u.get("user_id") == user_id), None)

        if not user:
            return json.dumps({"error": f"User {user_id} not found", "status": "failed"})

        # Determine the cancellation sequence.
        orders = list(data.get("orders", {}).values())
        order_to_cancel = None
        order_index = None

        for i, order in enumerate(orders):
            if order.get("order_id") == order_id and order.get("user_id") == user_id:
                order_to_cancel = order
                order_index = i
                break

        if not order_to_cancel:
            return json.dumps({
                "error": f"Order {order_id} not found or does not belong to user {user_id}",
                "status": "failed"
            })

        current_status = order_to_cancel.get("status")

        # Condition: Process orders solely with a valid status - cancellation of delivered orders is not permitted.
        if current_status == "cancelled":
            return json.dumps({
                "error": f"Order {order_id} is already cancelled",
                "status": "failed"
            })

        if current_status == "delivered":
            return json.dumps({
                "error": f"Cannot cancel delivered order {order_id}. Please contact customer service for returns.",
                "status": "failed"
            })

        # Determine the refund total based on the payment records.
        payment_history = order_to_cancel.get("payment_history", [])
        total_paid = sum(payment.get("amount", 0) for payment in payment_history if payment.get("transaction_type") == "payment")

        # UPDATE OPERATION: Set order status to cancelled
        order_to_cancel["status"] = "cancelled"
        order_to_cancel["cancellation_info"] = {
            "cancelled_by": "customer",
            "cancellation_reason": cancellation_reason,
            "cancelled_date": datetime.now().isoformat(),
            "previous_status": current_status
        }

        # Include refund transactions in the payment history.
        if total_paid > 0:
            refund_transaction = {
                "transaction_type": "refund",
                "amount": total_paid,
                "refund_reason": "order_cancellation",
                "processed_date": datetime.now().isoformat()
            }
            order_to_cancel["payment_history"].append(refund_transaction)

        order_to_cancel["last_updated"] = datetime.now().isoformat()

        # Modify the order within the data structure.
        data["orders"][order_index] = order_to_cancel

        result = {
            "status": "success",
            "order_id": order_id,
            "user_id": user_id,
            "cancellation_status": "cancelled",
            "previous_order_status": current_status,
            "refund_info": {
                "refund_amount": total_paid,
                "refund_processed": total_paid > 0
            },
            "cancellation_reason": cancellation_reason,
            "cancelled_date": order_to_cancel["cancellation_info"]["cancelled_date"]
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "cancel_order",
                "description": "Cancel a customer order and process refund",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "Customer identifier"},
                        "order_id": {"type": "string", "description": "Order identifier to cancel"},
                        "cancellation_reason": {"type": "string", "description": "Reason for cancellation (optional)"}
                    },
                    "required": ["user_id", "order_id"]
                }
            }
        }
