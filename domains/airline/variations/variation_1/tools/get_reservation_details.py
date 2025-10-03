from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any

class GetReservationDetails(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], reservation_id: str) -> str:
        reservations = data.get("reservations", [])
        for reservation in reservations:
            if reservation.get("reservation_id") == reservation_id:
                payload = reservation
                out = json.dumps(payload)
                return out
        payload = {"error": "Reservation not found", "reservation_id": reservation_id}
        out = json.dumps(payload)
        return out
    
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetReservationDetails",
                "description": "Retrieve the details of a reservation using its reservation ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "The unique ID of the reservation (e.g., 'RNL6HR').",
                        }
                    },
                    "required": ["reservation_id"],
                },
            },
        }
