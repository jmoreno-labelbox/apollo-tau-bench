from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any

class UpdateReservationBaggages(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        reservation_id: str,
        total_baggages: int,
        nonfree_baggages: int,
        payment_id: str,
    ) -> str:
        users = data.get("users", [])
        reservations = data.get("reservations", [])

        reservation = next(
            (r for r in reservations if r.get("reservation_id") == reservation_id), None
        )
        if not reservation:
            payload = {"error": "Reservation not found"}
            out = json.dumps(payload)
            return out

        user = next(
            (u for u in users if reservation_id in u.get("reservations", [])), None
        )
        if not user:
            payload = {"error": "User not found for this reservation"}
            out = json.dumps(payload)
            return out

        bag_fee = 35
        current_nonfree = reservation.get("nonfree_baggages", 0)
        additional_cost = (nonfree_baggages - current_nonfree) * bag_fee

        if additional_cost > 0:
            payment_method = user.get("payment_methods", {}).get(payment_id)
            if not payment_method:
                payload = {"error": "Payment method not found"}
                out = json.dumps(payload)
                return out

            if payment_method.get("source") == "gift_card":
                if payment_method.get("amount", 0) < additional_cost:
                    payload = {"error": "Insufficient gift card balance"}
                    out = json.dumps(payload)
                    return out
                payment_method["amount"] -= additional_cost

            if "payment_history" not in reservation:
                reservation["payment_history"] = []
            reservation["payment_history"].append(
                {
                    "payment_id": payment_id,
                    "amount": additional_cost,
                    "type": "BAGGAGE_FEE",
                }
            )

        reservation["total_baggages"] = total_baggages
        reservation["nonfree_baggages"] = nonfree_baggages
        payload = reservation
        out = json.dumps(payload)
        return out
        

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateReservationBaggages",
                "description": "Updates the baggage information for a reservation and handles payment for any additional fees.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string"},
                        "total_baggages": {
                            "type": "integer",
                            "description": "The new total number of bags.",
                        },
                        "nonfree_baggages": {
                            "type": "integer",
                            "description": "The new number of non-free bags.",
                        },
                        "payment_id": {
                            "type": "string",
                            "description": "The payment ID to charge for the new bags.",
                        },
                    },
                    "required": [
                        "reservation_id",
                        "total_baggages",
                        "nonfree_baggages",
                        "payment_id",
                    ],
                },
            },
        }
