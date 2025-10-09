from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CancelReservation(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], reservation_id: str) -> str:
        reservations = data.get("reservations", [])
        users = data.get("users", [])

        reservation = next(
            (r for r in reservations if r.get("reservation_id") == reservation_id), None
        )

        if not reservation:
            payload = {"error": "Reservation not found", "reservation_id": reservation_id}
            out = json.dumps(payload)
            return out

        if reservation.get("status") == "cancelled":
            payload = {
                "error": "Reservation is already cancelled.",
                "reservation_id": reservation_id,
            }
            out = json.dumps(payload)
            return out

        user_id = reservation.get("user_id")
        user = next((u for u in users if u.get("email", "").startswith(user_id)), None)

        refund_transactions = []
        for payment in reservation.get("payment_history", []):
            amount = payment.get("amount", 0)
            payment_id = payment.get("payment_id")

            refund_transactions.append(
                {"payment_id": payment_id, "amount": -amount, "type": "REFUND"}
            )

            if user and payment_id:
                payment_method = user.get("payment_methods", {}).get(payment_id)
                if payment_method and payment_method.get("source") in [
                    "gift_card",
                    "certificate",
                ]:
                    payment_method["amount"] = payment_method.get("amount", 0) + amount

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
                "description": "Cancels a reservation and processes refunds to the original payment methods.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "The unique ID of the reservation to cancel.",
                        }
                    },
                    "required": ["reservation_id"],
                },
            },
        }
