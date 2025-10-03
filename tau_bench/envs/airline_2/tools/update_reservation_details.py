from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class UpdateReservationDetails(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        reservation_id: str,
        flights: list[dict[str, str]] | None = None,
        passengers: list[dict[str, str]] | None = None,
        cabin: str | None = None,
        seat: str | None = None,
        contact_email: str | None = None,
        contact_phone: str | None = None,
        insurance: str | None = None,
        total_baggages: int | None = None,
        nonfree_baggages: int | None = None,
    ) -> str:
        reservations = data.get("reservations", [])
        for r in reservations:
            if r.get("reservation_id") == reservation_id:
                if cabin is not None:
                    r["cabin"] = cabin
                if seat is not None:
                    r["seat"] = seat
                if insurance is not None:
                    r["insurance"] = insurance
                if total_baggages is not None:
                    r["total_baggages"] = total_baggages
                if nonfree_baggages is not None:
                    r["nonfree_baggages"] = nonfree_baggages

                if flights is not None:
                    r["flights"] = flights
                if passengers is not None:
                    r["passengers"] = passengers
                if contact_email is not None:
                    r.setdefault("contact", {})["email"] = contact_email
                if contact_phone is not None:
                    r.setdefault("contact", {})["phone"] = contact_phone
                return _j(r)
        return _j({"error": "reservation_not_found", "reservation_id": reservation_id})
                
                
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateReservationDetails",
                "description": "Update editable reservation fields (cabin, seat, contact email/phone).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string"},
                        "cabin": {"type": "string"},
                        "seat": {"type": "string"},
                        "contact_email": {"type": "string"},
                        "contact_phone": {"type": "string"},
                        "insurance": {"type": "string"},
                        "total_baggages": {"type": "int"},
                        "nonfree_baggages": {"type": "int"},
                        "flights": {
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
                    },
                    "required": ["reservation_id"],
                },
            },
        }
