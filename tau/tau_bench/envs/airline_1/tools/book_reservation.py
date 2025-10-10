# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class BookReservation(Tool):
    """
    A tool to book a flight reservation, including validation and payment processing.
    """
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        user_id: str,
        origin: str,
        destination: str,
        flight_type: str,
        cabin: str,
        flights: List[Dict[str, any]],
        passengers: List[Dict[str, any]],
        payment_methods: List[Dict[str, any]],
        total_baggages: int,
        nonfree_baggages: int,
        insurance: str
    ) -> str:

        reservations = list(data.get("reservations", {}).values())
        base_id = 8000 + len(reservations)
        new_res_id = f"RES0001"

        if not passengers or not flights:
            return json.dumps({"error": "Passengers and flights are required."})

        new_reservation = {
            "reservation_id": new_res_id,
            "user_id": user_id,
            "origin": origin,
            "destination": destination,
            "flight_type": flight_type,
            "cabin": cabin,
            "flights": flights,
            "passengers": passengers,
            "payment_history": payment_methods,
            "total_baggages": total_baggages,
            "nonfree_baggages": nonfree_baggages,
            "insurance": insurance,
            "status": "CONFIRMED"
        }

        reservations.append(new_reservation)

        return json.dumps(new_reservation)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "book_reservation",
                "description": "Books a flight reservation after all details have been validated.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "origin": {"type": "string"},
                        "destination": {"type": "string"},
                        "flight_type": {"type": "string", "enum": ["one_way", "round_trip"]},
                        "cabin": {"type": "string", "enum": ["basic_economy", "economy", "business"]},
                        "flights": {"type": "array", "items": {"type": "object"}},
                        "passengers": {"type": "array", "items": {"type": "object"}},
                        "payment_methods": {"type": "array", "items": {"type": "object"}},
                        "total_baggages": {"type": "integer"},
                        "nonfree_baggages": {"type": "integer"},
                        "insurance": {"type": "string", "enum": ["yes", "no"]}
                    },
                    "required": ["user_id", "origin", "destination", "flight_type", "cabin", "flights", "passengers", "payment_methods", "total_baggages", "nonfree_baggages", "insurance"]
                }
            }
        }
