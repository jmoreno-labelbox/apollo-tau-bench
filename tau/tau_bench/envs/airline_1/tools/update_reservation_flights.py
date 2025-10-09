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

class UpdateReservationFlights(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        reservation_id: str,
        cabin: str,
        flights: list[dict[str, Any]],
        payment_id: str,
    ) -> str:
        reservations = data.get("reservations", [])
        flights_data = data.get("flights", [])

        reservation = next(
            (r for r in reservations if r.get("reservation_id") == reservation_id), None
        )
        if not reservation:
            payload = {"error": "Reservation not found", "reservation_id": reservation_id}
            out = json.dumps(payload)
            return out

        original_price = sum(f.get("price", 0) for f in reservation.get("flights", []))
        num_passengers = len(reservation.get("passengers", []))
        original_total_cost = original_price * num_passengers

        new_total_cost = 0
        for flight_info in flights:
            flight_number = flight_info.get("flight_number")
            date = flight_info.get("date")

            flight_route = next(
                (f for f in flights_data if f.get("flight_number") == flight_number),
                None,
            )
            if not flight_route:
                payload = {"error": f"Flight {flight_number} not found"}
                out = json.dumps(payload)
                return out

            date_details = flight_route.get("dates", {}).get(date)
            if not date_details:
                payload = {"error": f"Flight {flight_number} on date {date} not found"}
                out = json.dumps(payload)
                return out

            new_total_cost += (
                date_details.get("prices", {}).get(cabin, 0) * num_passengers
            )

        price_difference = original_total_cost - new_total_cost

        if (
            "payment_history" not in reservation
            or reservation["payment_history"] is None
        ):
            reservation["payment_history"] = []
        if price_difference != 0:
            refund_transaction = {
                "payment_id": payment_id,
                "amount": -price_difference,
                "type": "REFUND" if price_difference > 0 else "CHARGE",
            }
            reservation["payment_history"].append(refund_transaction)

        reservation["cabin"] = cabin
        reservation["flights"] = [
            {"flight_number": f.get("flight_number"), "date": f.get("date")}
            for f in flights
        ]

        response_fields = [
            "reservation_id",
            "user_id",
            "origin",
            "destination",
            "flight_type",
            "cabin",
            "flights",
            "passengers",
            "created_at",
            "total_baggages",
            "nonfree_baggages",
            "insurance",
        ]
        response = {key: reservation.get(key) for key in response_fields}
        payload = response
        out = json.dumps(payload)
        return out


    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateReservationFlights",
                "description": "Updates the flight details (like cabin class) for an existing reservation and processes payment adjustments.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string"},
                        "cabin": {
                            "type": "string",
                            "description": "The new cabin class.",
                        },
                        "flights": {
                            "type": "array",
                            "description": "The complete new list of flight segments for the reservation.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "flight_number": {"type": "string"},
                                    "date": {"type": "string"},
                                },
                                "required": ["flight_number", "date"],
                            },
                        },
                        "payment_id": {
                            "type": "string",
                            "description": "The original payment ID for refund processing or a new one for charges.",
                        },
                    },
                    "required": ["reservation_id", "cabin", "flights", "payment_id"],
                },
            },
        }
