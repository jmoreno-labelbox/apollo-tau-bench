# Sierra Copyright.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateReservationStatus(Tool):
    """
    A tool to update the status of a reservation.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], reservation_id: str, new_status: str) -> str:
        reservations = list(data.get("reservations", {}).values())
        new_status = new_status.upper()
        for res in reservations:
            if res.get("reservation_id") == reservation_id:
                res["status"] = new_status
                return json.dumps(res)
        return json.dumps({"error": "Reservation not found", "reservation_id": reservation_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_reservation_status",
                "description": "Updates the status of a specific reservation (e.g., 'CONFIRMED', 'CANCELLED').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The ID of the reservation to update."},
                        "new_status": {"type": "string", "description": "The new status for the reservation."}
                    },
                    "required": ["reservation_id", "new_status"]
                }
            }
        }
