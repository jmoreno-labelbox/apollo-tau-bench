from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateReservationPassengers(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any], reservation_id: str, passengers: list[dict[str, str]]
    ) -> str:
        reservations = data.get("reservations", {}).values()
        reservation = next(
            (r for r in reservations.values() if r.get("reservation_id") == reservation_id), None
        )

        if not reservation:
            payload = {"error": "Reservation not found", "reservation_id": reservation_id}
            out = json.dumps(payload)
            return out

        reservation["passengers"] = passengers
        payload = reservation
        out = json.dumps(payload)
        return out
        

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateReservationPassengers",
                "description": "Updates the passenger list for a specific reservation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "The unique ID of the reservation to update.",
                        },
                        "passengers": {
                            "type": "array",
                            "description": "The new, complete list of passengers for the reservation.",
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
                    "required": ["reservation_id", "passengers"],
                },
            },
        }
