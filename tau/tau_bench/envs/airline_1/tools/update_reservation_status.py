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

class UpdateReservationStatus(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], reservation_id: str, new_status: str) -> str:
        reservations = data.get("reservations", {}).values()
        for res in reservations:
            if res.get("reservation_id") == reservation_id:
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
                "name": "UpdateReservationStatus",
                "description": "Updates the status of a specific reservation (e.g., 'CONFIRMED', 'CANCELLED').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "The ID of the reservation to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status for the reservation.",
                        },
                    },
                    "required": ["reservation_id", "new_status"],
                },
            },
        }
