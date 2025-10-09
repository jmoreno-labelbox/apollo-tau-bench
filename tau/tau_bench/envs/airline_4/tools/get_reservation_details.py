from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class GetReservationDetails(Tool):
    """API tool for retrieving reservation details using the reservation ID."""

    @staticmethod
    def invoke(data: dict[str, Any], reservation_id: str) -> str:
        pass
        #Check that the necessary parameter is valid
        if not reservation_id:
            payload = {"error": "Missing required parameter", "required": "reservation_id"}
            out = json.dumps(
                payload)
            return out

        #Locate the reservation
        reservations = data.get("reservations", [])
        target_reservation = None

        for reservation in reservations:
            if reservation.get("reservation_id") == reservation_id:
                target_reservation = reservation
                break

        if not target_reservation:
            payload = {"error": "Reservation not found", "reservation_id": reservation_id}
            out = json.dumps(
                payload)
            return out

        #Retrieve user details if the user_id is present
        user_id = target_reservation.get("user_id")
        user_details = None

        if user_id:
            users = data.get("users", [])
            for user in users:
                #Attempt to match the user by verifying if any reservation in their list corresponds
                user_reservations = user.get("reservations", [])
                if reservation_id in user_reservations:
                    user_details = {
                        "email": user.get("email"),
                        "name": user.get("name"),
                        "membership": user.get("membership"),
                        "address": user.get("address"),
                    }
                    break

        #Compute a summary of the trip
        flights = target_reservation.get("flights", [])
        #Utilize the reservation's total_cost if present (includes upgrades), otherwise total the flight prices
        calculated_total = target_reservation.get(
            "total_cost", sum(flight.get("price", 0) for flight in flights)
        )
        trip_summary = {
            "total_flights": len(flights),
            "total_cost": calculated_total,
            "departure_date": flights[0].get("date") if flights else None,
            "return_date": flights[-1].get("date") if len(flights) > 1 else None,
        }

        #Retrieve the number of passengers
        passengers = target_reservation.get("passengers", [])
        passenger_count = len(passengers)

        #Compute baggage fees (assuming $50 for each non-free bag)
        nonfree_baggages = target_reservation.get("nonfree_baggages", 0)
        baggage_cost = nonfree_baggages * 50

        #Retrieve payment information
        payment_history = target_reservation.get("payment_history", [])
        total_paid = sum(payment.get("amount", 0) for payment in payment_history)

        #Formulate an improved response
        response = {
            "reservation_id": target_reservation.get("reservation_id"),
            "status": "confirmed",  #All recorded reservations are validated
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

        #Include user details if located
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
                "description": "Get detailed reservation information by reservation ID, including customer details, flight information, payment history, and trip summary.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "Unique reservation identifier (e.g., '4WQ150', 'A7K2M9')",
                        }
                    },
                    "required": ["reservation_id"],
                },
            },
        }
