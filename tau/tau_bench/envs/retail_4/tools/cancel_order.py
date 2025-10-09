from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CancelOrder(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str,
        order_id: str,
        cancellation_reason: str = "customer_request",
    ) -> str:
        """
        Cancel a customer order and process refund if applicable

        Writes to: orders.json (updates order status to cancelled)
        Data Sources: users.json for validation
        """
        # Rule: Validate user identity exists before processing any user requests
        users = data.get("users", {}).values()
        user = next((u for u in users.values() if u.get("user_id") == user_id), None)

        if not user:
            payload = {"error": f"User {user_id} not found", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Find the order to cancel
        orders = data.get("orders", {}).values()
        order_to_cancel = None
        order_index = None

        for i, order in enumerate(orders.values()):
            if order.get("order_id") == order_id and order.get("user_id") == user_id:
                order_to_cancel = order
                order_index = i
                break

        if not order_to_cancel:
            payload = {
                "error": f"Order {order_id} not found or does not belong to user {user_id}",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        current_status = order_to_cancel.get("status")

        # Rule: Only process orders with valid status - can't cancel delivered orders
        if current_status == "cancelled":
            payload = {"error": f"Order {order_id} is already cancelled", "status": "failed"}
            out = json.dumps(payload)
            return out

        if current_status == "delivered":
            payload = {
                "error": f"Cannot cancel delivered order {order_id}. Please contact customer service for returns.",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Calculate refund amount from payment history
        payment_history = order_to_cancel.get("payment_history", [])
        total_paid = sum(
            payment.get("amount", 0)
            for payment in payment_history
            if payment.get("transaction_type") == "payment"
        )

        # WRITE OPERATION: Update order status to cancelled
        order_to_cancel["status"] = "cancelled"
        order_to_cancel["cancellation_info"] = {
            "cancelled_by": "customer",
            "cancellation_reason": cancellation_reason,
            "cancelled_date": datetime.now().isoformat(),
            "previous_status": current_status,
        }

        # Add refund transaction to payment history
        if total_paid > 0:
            refund_transaction = {
                "transaction_type": "refund",
                "amount": total_paid,
                "refund_reason": "order_cancellation",
                "processed_date": datetime.now().isoformat(),
            }
            order_to_cancel["payment_history"].append(refund_transaction)

        order_to_cancel["last_updated"] = datetime.now().isoformat()

        # Update the order in the data structure
        data["orders"][order_index] = order_to_cancel

        result = {
            "status": "success",
            "order_id": order_id,
            "user_id": user_id,
            "cancellation_status": "cancelled",
            "previous_order_status": current_status,
            "refund_info": {
                "refund_amount": total_paid,
                "refund_processed": total_paid > 0,
            },
            "cancellation_reason": cancellation_reason,
            "cancelled_date": order_to_cancel["cancellation_info"]["cancelled_date"],
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CancelOrder",
                "description": "Cancel a customer order and process refund",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Customer identifier",
                        },
                        "order_id": {
                            "type": "string",
                            "description": "Order identifier to cancel",
                        },
                        "cancellation_reason": {
                            "type": "string",
                            "description": "Reason for cancellation (optional)",
                        },
                    },
                    "required": ["user_id", "order_id"],
                },
            },
        }
