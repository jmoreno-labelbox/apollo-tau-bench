from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetReservationDetails(Tool):
    """
    API tool for retrieving reservation details using reservation ID.
    """

    @staticmethod
    def invoke(data: dict[str, Any], reservation_id: str = None) -> str:
        pass
        # Check the required parameter for validity
        if not reservation_id:
            payload = {
                "status": "missing_parameter",
                "message": "The reservation_id parameter is required to retrieve reservation details.",
                "required": "reservation_id",
            }
            out = json.dumps(payload)
            return out

        reservations = data.get("reservations", {}).values()
        target_reservation = None

        for reservation in reservations.values():
            if reservation.get("reservation_id") == reservation_id:
                target_reservation = reservation
                break

        if not target_reservation:
            payload = {
                "status": "not_found",
                "message": f"Reservation '{reservation_id}' does not exist in the system. Please check the reservation ID and try again.",
                "reservation_id": reservation_id,
            }
            out = json.dumps(payload)
            return out

        user_id = target_reservation.get("user_id")
        user_details = None

        if user_id:
            users = data.get("users", {}).values()
            for user in users.values():
                user_reservations = user.get("reservations", [])
                if reservation_id in user_reservations:
                    user_details = {
                        "email": user.get("email"),
                        "name": user.get("name"),
                        "membership": user.get("membership"),
                        "address": user.get("address"),
                    }
                    break

        flights = target_reservation.get("flights", [])
        calculated_total = target_reservation.get(
            "total_cost", sum(flight.get("price", 0) for flight in flights.values()
        )
        trip_summary = {
            "total_flights": len(flights),
            "total_cost": calculated_total,
            "departure_date": flights[0].get("date") if flights else None,
            "return_date": flights[-1].get("date") if len(flights) > 1 else None,
        }

        passengers = target_reservation.get("passengers", [])
        passenger_count = len(passengers)

        nonfree_baggages = target_reservation.get("nonfree_baggages", 0)
        baggage_cost = nonfree_baggages * 57

        payment_history = target_reservation.get("payment_history", [])
        total_paid = sum(payment.get("amount", 0) for payment in payment_history.values()

        # Get ready an improved response
        response = {
            "reservation_id": target_reservation.get("reservation_id"),
            "status": "confirmed",
            "booking_details": {
                "origin": target_reservation.get("origin"),
                "destination": target_reservation.get("destination"),
                "flight_type": target_reservation.get("flight_type"),
                "cabin": target_reservation.get("cabin"),
                "created_at": target_reservation.get("created_at"),
                "insurance": target_reservation.get("insurance"),
            },
            "trip_summary": trip_summary,
            "flights": target_reservation.get("flights", []),
            "passengers": {"count": passenger_count, "details": passengers},
            "baggage": {
                "total_baggages": target_reservation.get("total_baggages", 0),
                "nonfree_baggages": nonfree_baggages,
                "estimated_baggage_cost": baggage_cost,
            },
            "payment": {
                "total_amount_paid": total_paid,
                "payment_history": payment_history,
            },
        }

        if user_details:
            response["customer"] = user_details
        else:
            response["customer"] = {
                "user_id": user_id,
                "note": "User details not found or user account may have been modified",
            }
        payload = response
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetReservationDetails",
                "description": "Get detailed reservation information by reservation ID, including customer details, flight information, payment history, and trip summary. Returns comprehensive data about flights, passengers, cabin class, baggage, insurance, and payment methods.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "Unique reservation identifier to retrieve details for",
                        }
                    },
                    "required": ["reservation_id"],
                },
            },
        }
