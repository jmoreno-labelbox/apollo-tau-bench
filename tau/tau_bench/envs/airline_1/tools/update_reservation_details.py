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

class UpdateReservationDetails(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        reservation_id: str,
        new_cabin: str | None = None,
        new_status: str | None = None,
    ) -> str:
        reservations = data.get("reservations", {}).values()
        for res in reservations:
            if res.get("reservation_id") == reservation_id:
                if new_cabin:
                    res["cabin"] = new_cabin
                if new_status:
                    res["status"] = new_status
                payload = res
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
                "name": "UpdateReservationDetails",
                "description": "Updates details of a specific reservation, such as cabin or status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "The unique ID of the reservation to update.",
                        },
                        "new_cabin": {
                            "type": "string",
                            "description": "Optional: The new cabin class for the reservation.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "Optional: The new status for the reservation.",
                        },
                    },
                    "required": ["reservation_id"],
                },
            },
        }
