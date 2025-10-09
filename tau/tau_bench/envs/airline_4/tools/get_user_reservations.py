from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetUserReservations(Tool):
    """API tool for retrieving all reservations for a user using user_id or email address."""

    @staticmethod
    def invoke(
        data: dict[str, Any], user_id: str | None = None, user_email: str | None = None
    ) -> str:
        pass
        #Ensure that at least one parameter is supplied
        if not user_id and not user_email:
            payload = {
                    "error": "Missing required parameter",
                    "required": "Either user_id or user_email must be provided",
                }
            out = json.dumps(
                payload)
            return out

        #If an email is given, locate the user_id initially
        target_user = None
        users = data.get("users", [])

        if user_email:
            #Locate user using their email
            for user in users:
                if user.get("email") == user_email:
                    target_user = user
                    #Obtain user_id from reservation data for cross-referencing
                    reservations = data.get("reservations", [])
                    user_reservation_ids = user.get("reservations", [])

                    #Determine the actual user_id by checking any reservation
                    if user_reservation_ids:
                        for reservation in reservations:
                            if (
                                reservation.get("reservation_id")
                                in user_reservation_ids
                            ):
                                user_id = reservation.get("user_id")
                                break
                    break

            if not target_user:
                payload = {"error": "User not found", "email": user_email}
                out = json.dumps(payload)
                return out
        else:
            #Locate user using user_id via reservations
            reservations = data.get("reservations", [])
            user_reservation_ids = []

            #Initially, locate all reservations associated with this user_id
            for reservation in reservations:
                if reservation.get("user_id") == user_id:
                    user_reservation_ids.append(reservation.get("reservation_id"))

            #Subsequently, locate the user profile that includes these reservations
            for user in users:
                user_reservations = user.get("reservations", [])
                if any(res_id in user_reservation_ids for res_id in user_reservations):
                    target_user = user
                    break

        if not user_id:
            payload = {
                    "error": "User ID not found",
                    "provided_email": user_email if user_email else None,
                }
            out = json.dumps(
                payload)
            return out

        #Retrieve all reservations for this user
        reservations = data.get("reservations", [])
        user_reservations = []

        for reservation in reservations:
            if reservation.get("user_id") == user_id:
                #Generate a summary for each reservation
                flights = reservation.get("flights", [])
                passengers = reservation.get("passengers", [])
                total_cost = sum(flight.get("price", 0) for flight in flights)

                reservation_summary = {
                    "reservation_id": reservation.get("reservation_id"),
                    "origin": reservation.get("origin"),
                    "destination": reservation.get("destination"),
                    "flight_type": reservation.get("flight_type"),
                    "cabin": reservation.get("cabin"),
                    "created_at": reservation.get("created_at"),
                    "total_cost": total_cost,
                    "passenger_count": len(passengers),
                    "flight_count": len(flights),
                    "departure_date": flights[0].get("date") if flights else None,
                    "return_date": (
                        flights[-1].get("date") if len(flights) > 1 else None
                    ),
                    "insurance": reservation.get("insurance"),
                    "flights": flights,
                    "passengers": passengers,
                }

                user_reservations.append(reservation_summary)

        #Organize reservations by creation date (latest first)
        user_reservations.sort(key=lambda x: x.get("created_at", ""), reverse=True)

        #Formulate response containing user information and reservations
        response = {
            "user_id": user_id,
            "total_reservations": len(user_reservations),
            "reservations": user_reservations,
        }

        #Include user profile details if accessible
        if target_user:
            response["user_profile"] = {
                "email": target_user.get("email"),
                "name": target_user.get("name"),
                "membership": target_user.get("membership"),
                "total_payment_methods": len(target_user.get("payment_methods", {})),
            }
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserReservations",
                "description": "Get all reservations for a user by user_id or email address. Returns a comprehensive list of reservations with summary information for each booking.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Unique user identifier (e.g., 'chen_jackson_3290'). Either user_id or user_email must be provided.",
                        },
                        "user_email": {
                            "type": "string",
                            "description": "User email address (e.g., 'mia.li3818@example.com'). Either user_id or user_email must be provided.",
                        },
                    },
                    "required": [],
                },
            },
        }
