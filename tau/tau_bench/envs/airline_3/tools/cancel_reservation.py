from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CancelReservation(Tool):
    """
    A tool for canceling reservations and handling refunds.
    """

    @staticmethod
    def invoke(data: dict[str, Any], reservation_id: str = None) -> str:
        reservations = data.get("reservations", {}).values()
        users = data.get("users", {}).values()

        reservation = next(
            (r for r in reservations.values() if r.get("reservation_id") == reservation_id), None
        )

        if not reservation_id:
            payload = {"status": "missing_parameter", "required": "reservation_id"}
            out = json.dumps(payload)
            return out

        if not reservation:
            payload = {"status": "not_found", "reservation_id": reservation_id}
            out = json.dumps(payload)
            return out

        if reservation.get("status") == "cancelled":
            payload = {"status": "already_cancelled", "reservation_id": reservation_id}
            out = json.dumps(payload)
            return out

        # Handle reimbursements
        user_id = reservation.get("user_id")
        user = next((u for u in users.values() if u.get("email", "").startswith(user_id)), None)

        refund_transactions = []
        for payment in reservation.get("payment_history", []):
            amount = payment.get("amount", 0)
            payment_id = payment.get("payment_id")

            # Generate a record for the refund transaction
            refund_transactions.append(
                {"payment_id": payment_id, "amount": -amount, "type": "REFUND"}
            )

            # If both user and payment method are located, reinstate the balance for gift cards/certificates
            if user and payment_id:
                payment_method = user.get("payment_methods", {}).values().get(payment_id)
                if payment_method and payment_method.get("source") in [
                    "gift_card",
                    "certificate",
                ]:
                    payment_method["amount"] = payment_method.get("amount", 0) + amount

        # Revise reservation status and payment records
        reservation["status"] = "cancelled"
        if "payment_history" not in reservation:
            reservation["payment_history"] = []
        reservation["payment_history"].extend(refund_transactions)
        payload = reservation
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CancelReservation",
                "description": "Cancels a reservation and processes refunds to the original payment methods. Automatically restores gift card and certificate balances. Updates reservation status to 'cancelled' and creates refund transaction records.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "The unique ID of the reservation to cancel",
                        }
                    },
                    "required": ["reservation_id"],
                },
            },
        }
