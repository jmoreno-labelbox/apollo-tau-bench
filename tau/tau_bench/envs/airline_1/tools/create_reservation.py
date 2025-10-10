# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateReservation(Tool):
    """
    A tool to create a new reservation for a user.
    """
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        user_email: str,
        flight_details: List[Dict[str, str]],
        passengers: List[Dict[str, str]],
        cabin: str
    ) -> str:
        users = list(data.get("users", {}).values())
        reservations = list(data.get("reservations", {}).values())

        target_user = None
        for user in users:
            if user.get("email") == user_email:
                first_name = user.get("name", {}).get("first_name", "").lower()
                last_name = user.get("name", {}).get("last_name", "").lower()
                user_id = f"{first_name}_{last_name}_1234"
                target_user = {"email": user_email, "id": user_id}
                break

        if not target_user:
            return json.dumps({"error": "User not found", "email": user_email})

        last_reservation_numeric_id = 0
        if reservations:
            numeric_ids = [
                int(r["reservation_id"][3:])
                for r in reservations
                if r.get("reservation_id", "").startswith("RES") and r["reservation_id"][3:].isdigit()
            ]
            if numeric_ids:
                last_reservation_numeric_id = max(numeric_ids)
            else:
                last_reservation_numeric_id = 0
        else:
            last_reservation_numeric_id = 0

        new_reservation_id = f"RES{last_reservation_numeric_id + 1:04d}"

        new_reservation = {
            "reservation_id": new_reservation_id,
            "user_id": target_user["id"],
            "origin": flight_details[0]["origin"],
            "destination": flight_details[-1]["destination"],
            "flight_type": "one_way" if len(flight_details) == 1 else "round_trip",
            "cabin": cabin,
            "flights": flight_details,
            "passengers": passengers,
            "payment_history": [],
            "total_baggages": len(passengers),
            "nonfree_baggages": 0,
            "insurance": "no",
            "status": "CONFIRMED"
        }

        reservations.append(new_reservation)

        for user in users:
            if user.get("email") == user_email:
                if "reservations" not in user:
                    user["reservations"] = []
                user["reservations"].append(new_reservation_id)
                break

        return json.dumps(new_reservation)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_reservation",
                "description": "Creates a new flight reservation for a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_email": {"type": "string", "description": "The email of the user making the reservation."},
                        "flight_details": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "flight_number": {"type": "string"},
                                    "date": {"type": "string", "description": "Date in YYYY-MM-DD format."},
                                    "origin": {"type": "string"},
                                    "destination": {"type": "string"}
                                },
                                "required": ["flight_number", "date", "origin", "destination"]
                            }
                        },
                        "passengers": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "first_name": {"type": "string"},
                                    "last_name": {"type": "string"},
                                    "dob": {"type": "string", "description": "Date of birth in YYYY-MM-DD format."}
                                },
                                "required": ["first_name", "last_name", "dob"]
                            }
                        },
                        "cabin": {"type": "string", "description": "The cabin class (e.g., 'economy', 'business')."}
                    },
                    "required": ["user_email", "flight_details", "passengers", "cabin"]
                }
            }
        }
