# Sierra copyright notice.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateReservation(Tool):
    """
    Create a reservation for an existing user identified by email.
    """

    # --- internal utility functions ---
    @staticmethod
    def _find_user(data: Dict[str, Any],users: List[Dict[str, Any]], user_email: str) -> Dict[str, str]:
        # retrieve user using email address
        for u in users:
            if u.get("email") == user_email:
                # verify the reservations list
                res_ids = u.get("reservations", [])
                # query global reservations for corresponding id

                for r in list(data.get("reservations", {}).values()):
                    if r.get("reservation_id") in res_ids and r.get("user_id"):
                        return {"email": user_email, "id": r["user_id"]}

                # alternative if no reservation is matched
                first = (u.get("name", {}).get("first_name") or "").lower()
                last = (u.get("name", {}).get("last_name") or "").lower()
                return {"email": user_email, "id": f"{first}_{last}_1234"}
        return None

    @staticmethod
    def _next_reservation_id(reservations: List[Dict[str, Any]]) -> str:
        last_num = 0
        if reservations:
            nums = [
                int(r.get("reservation_id", "0")[-4:])
                for r in reservations
                if r.get("reservation_id", "")[-4:].isdigit()
            ]
            if nums:
                last_num = max(nums)
        return f"RES{last_num + 1:04d}"

    @staticmethod
    def _attach_reservation_to_user(users: List[Dict[str, Any]], user_email: str, res_id: str) -> None:
        for u in users:
            if u.get("email") == user_email:
                u.setdefault("reservations", []).append(res_id)
                break

    # --- tool initialization point ---
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        user_email: str,
        flight_details: List[Dict[str, str]],
        passengers: List[Dict[str, str]],
        cabin: str,
        total_baggages: int = None
    ) -> str:
        users = list(data.get("users", {}).values())
        reservations = list(data.get("reservations", {}).values())

        # find user and generate a consistent user_id (maintaining original logic)
        target_user = CreateReservation._find_user(data,users, user_email)
        if not target_user:
            return json.dumps({"error": "User not found", "email": user_email})

        # generate next reservation id (same scheme: RES#### create the next reservation identifier (following the format: RES####)
        new_res_id = CreateReservation._next_reservation_id(reservations)

        # create reservation entry (field names/values remain the same)
        new_reservation = {
            "reservation_id": new_res_id,
            "user_id": target_user["id"],
            "origin": flight_details[0]["origin"],
            "destination": flight_details[-1]["destination"],
            "flight_type": "one_way" if len(flight_details) == 1 else "round_trip",
            "cabin": cabin,
            "flights": flight_details,
            "passengers": passengers,
            "payment_history": [],
            "total_baggages": total_baggages if total_baggages is not None else len(passengers),
            "nonfree_baggages": 0,
            "insurance": "no",
            "status": "CONFIRMED",
        }

        # store in the given data dictionary
        reservations.append(new_reservation)
        CreateReservation._attach_reservation_to_user(users, user_email, new_res_id)

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
                        "user_email": {
                            "type": "string",
                            "description": "The email of the user making the reservation."
                        },
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
                        "cabin": {
                            "type": "string",
                            "description": "The cabin class (e.g., 'economy', 'business', 'basic_economy')."
                        },
                        "total_baggages": {
                            "type": "integer",
                            "description": "Total baggages. optional"
                        }
                    },
                    "required": ["user_email", "flight_details", "passengers", "cabin"]
                }
            }
        }
