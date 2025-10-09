from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class CreateReservation(Tool):

    #--- utility functions (internal style) ---
    @staticmethod
    def _find_user(
        users: list[dict[str, Any]], user_email: str
    ) -> dict[str, str] | None:
        pass
        for u in users:
            if u.get("email") == user_email:
                first = (u.get("name", {}).get("first_name") or "").lower()
                last = (u.get("name", {}).get("last_name") or "").lower()
                return {"email": user_email, "id": f"{first}_{last}_1234"}
        return None

    @staticmethod
    def _next_reservation_id(reservations: list[dict[str, Any]]) -> str:
        pass
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
    def _attach_reservation_to_user(
        users: list[dict[str, Any]], user_email: str, res_id: str
    ) -> None:
        pass
        for u in users:
            if u.get("email") == user_email:
                u.setdefault("reservations", []).append(res_id)
                break

    #--- tool main entry point ---
    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_email: str,
        flight_details: list[dict[str, str]],
        passengers: list[dict[str, str]],
        cabin: str,
    ) -> str:
        users = data.get("users", [])
        reservations = data.get("reservations", [])

        # find user and generate a deterministic user_id (maintaining original logic)
        target_user = CreateReservation._find_user(users, user_email)
        if not target_user:
            payload = {"error": "User not found", "email": user_email}
            out = json.dumps(payload)
            return out

        # create the next reservation id (following the same format: RES####)
        new_res_id = CreateReservation._next_reservation_id(reservations)

        # construct reservation record (field names/values remain the same)
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
            # "created_at": datetime.now().isoformat(),
            "total_baggages": len(passengers),
            "nonfree_baggages": 0,
            "insurance": "no",
            "status": "CONFIRMED",
        }

        # store in the supplied data dictionary
        reservations.append(new_reservation)
        CreateReservation._attach_reservation_to_user(users, user_email, new_res_id)
        payload = new_reservation
        out = json.dumps(payload)
        return out
        

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateReservation",
                "description": "Creates a new flight reservation for a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_email": {
                            "type": "string",
                            "description": "The email of the user making the reservation.",
                        },
                        "flight_details": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "flight_number": {"type": "string"},
                                    "date": {
                                        "type": "string",
                                        "description": "Date in YYYY-MM-DD format.",
                                    },
                                    "origin": {"type": "string"},
                                    "destination": {"type": "string"},
                                },
                                "required": [
                                    "flight_number",
                                    "date",
                                    "origin",
                                    "destination",
                                ],
                            },
                        },
                        "passengers": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "first_name": {"type": "string"},
                                    "last_name": {"type": "string"},
                                    "dob": {
                                        "type": "string",
                                        "description": "Date of birth in YYYY-MM-DD format.",
                                    },
                                },
                                "required": ["first_name", "last_name", "dob"],
                            },
                        },
                        "cabin": {
                            "type": "string",
                            "description": "The cabin class (e.g., 'economy', 'business', 'basic_economy').",
                        },
                    },
                    "required": ["user_email", "flight_details", "passengers", "cabin"],
                },
            },
        }
