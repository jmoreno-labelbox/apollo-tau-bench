# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CancelReservation(Tool):
    """
    A tool to cancel a reservation and process refunds.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], reservation_id: str = None) -> str:
        reservations = list(data.get("reservations", {}).values())
        users = list(data.get("users", {}).values())

        reservation = next((r for r in reservations if r.get("reservation_id") == reservation_id), None)

        if not reservation_id:
            return json.dumps({"status": "missing_parameter", "required": "reservation_id"})

        if not reservation:
            return json.dumps({"status": "not_found", "reservation_id": reservation_id})

        if reservation.get("status") == "cancelled":
            return json.dumps({"status": "already_cancelled", "reservation_id": reservation_id})

        # Process refunds
        user_id = reservation.get("user_id")
        user = next((u for u in users if u.get("email", "").startswith(user_id)), None)

        refund_transactions = []
        for payment in reservation.get("payment_history", []):
            amount = payment.get("amount", 0)
            payment_id = payment.get("payment_id")

            # Create a refund transaction record
            refund_transactions.append({
                "payment_id": payment_id,
                "amount": -amount,
                "type": "REFUND"
            })

            # If the user and payment method can be found, restore the balance for gift cards/certificates
            if user and payment_id:
                payment_method = user.get("payment_methods", {}).get(payment_id)
                if payment_method and payment_method.get("source") in ["gift_card", "certificate"]:
                    payment_method["amount"] = payment_method.get("amount", 0) + amount

        # Update reservation status and payment history
        reservation["status"] = "cancelled"
        if "payment_history" not in reservation:
            reservation["payment_history"] = []
        reservation["payment_history"].extend(refund_transactions)

        return json.dumps(reservation)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "cancel_reservation",
                "description": "Cancels a reservation and processes refunds to the original payment methods. Automatically restores gift card and certificate balances. Updates reservation status to 'cancelled' and creates refund transaction records.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "The unique ID of the reservation to cancel"
                        }
                    },
                    "required": ["reservation_id"]
                }
            }
        }
