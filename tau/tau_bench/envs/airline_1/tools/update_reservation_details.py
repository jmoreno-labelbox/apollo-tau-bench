# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateReservationDetails(Tool):
    """
    A tool to update specific details of a reservation, such as cabin class or status.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], reservation_id: str, new_cabin: Optional[str] = None, new_status: Optional[str] = None) -> str:
        reservations = list(data.get("reservations", {}).values())
        if new_status:
            new_status = new_status.upper()
        for res in reservations:
            if res.get("reservation_id") == reservation_id:
                if new_cabin:
                    res["cabin"] = new_cabin
                if new_status:
                    res["status"] = new_status
                return json.dumps(res)
        return json.dumps({"error": "Reservation not found", "reservation_id": reservation_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_reservation_details",
                "description": "Updates details of a specific reservation, such as cabin or status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "The unique ID of the reservation to update."
                        },
                        "new_cabin": {
                            "type": "string",
                            "description": "Optional: The new cabin class for the reservation."
                        },
                        "new_status": {
                            "type": "string",
                            "description": "Optional: The new status for the reservation."
                        }
                    },
                    "required": ["reservation_id"]
                }
            }
        }
