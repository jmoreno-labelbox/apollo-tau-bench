from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any

class BookReservation(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str,
        origin: str,
        destination: str,
        flight_type: str,
        cabin: str,
        flights: list[dict[str, any]],
        passengers: list[dict[str, any]],
        payment_methods: list[dict[str, any]],
        total_baggages: int,
        nonfree_baggages: int,
        insurance: str,
    ) -> str:
        reservations = data.get("reservations", [])
        8000 + len(reservations)
        new_res_id = "RES0001"

        if not passengers or not flights:
            payload = {"error": "Passengers and flights are required."}
            out = json.dumps(payload)
            return out

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
            "status": "CONFIRMED",
        }

        reservations.append(new_reservation)
        payload = new_reservation
        out = json.dumps(payload)
        return out
           

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "BookReservation",
                "description": "Books a flight reservation after all details have been validated.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "origin": {"type": "string"},
                        "destination": {"type": "string"},
                        "flight_type": {
                            "type": "string",
                            "enum": ["one_way", "round_trip"],
                        },
                        "cabin": {
                            "type": "string",
                            "enum": ["basic_economy", "economy", "business"],
                        },
                        "flights": {"type": "array", "items": {"type": "object"}},
                        "passengers": {"type": "array", "items": {"type": "object"}},
                        "payment_methods": {
                            "type": "array",
                            "items": {"type": "object"},
                        },
                        "total_baggages": {"type": "integer"},
                        "nonfree_baggages": {"type": "integer"},
                        "insurance": {"type": "string", "enum": ["yes", "no"]},
                    },
                    "required": [
                        "user_id",
                        "origin",
                        "destination",
                        "flight_type",
                        "cabin",
                        "flights",
                        "passengers",
                        "payment_methods",
                        "total_baggages",
                        "nonfree_baggages",
                        "insurance",
                    ],
                },
            },
        }
