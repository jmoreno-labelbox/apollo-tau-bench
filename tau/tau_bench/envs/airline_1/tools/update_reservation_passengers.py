# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateReservationPassengers(Tool):
    """
    A tool to update the passenger list for a reservation.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], reservation_id: str, passengers: List[Dict[str, str]]) -> str:
        reservations = list(data.get("reservations", {}).values())
        reservation = next((r for r in reservations if r.get("reservation_id") == reservation_id), None)

        if not reservation:
            return json.dumps({"error": "Reservation not found", "reservation_id": reservation_id})

        reservation["passengers"] = passengers

        return json.dumps(reservation)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_reservation_passengers",
                "description": "Updates the passenger list for a specific reservation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "The unique ID of the reservation to update."
                        },
                        "passengers": {
                            "type": "array",
                            "description": "The new, complete list of passengers for the reservation.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "first_name": {"type": "string"},
                                    "last_name": {"type": "string"},
                                    "dob": {"type": "string", "description": "Date of birth in YYYY-MM-DD format."}
                                },
                                "required": ["first_name", "last_name", "dob"]
                            }
                        }
                    },
                    "required": ["reservation_id", "passengers"]
                }
            }
        }
