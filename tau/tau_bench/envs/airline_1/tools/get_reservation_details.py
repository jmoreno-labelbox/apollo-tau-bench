# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetReservationDetails(Tool):
    """
    A tool to retrieve the full details of a reservation using its reservation ID.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], reservation_id: str) -> str:
        reservations = list(data.get("reservations", {}).values())
        for reservation in reservations:
            if reservation.get("reservation_id") == reservation_id:
                return json.dumps(reservation)
        return json.dumps({"error": "Reservation not found", "reservation_id": reservation_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_reservation_details",
                "description": "Retrieve the details of a reservation using its reservation ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "The unique ID of the reservation (e.g., 'RNL6HR')."
                        }
                    },
                    "required": ["reservation_id"]
                }
            }
        }
