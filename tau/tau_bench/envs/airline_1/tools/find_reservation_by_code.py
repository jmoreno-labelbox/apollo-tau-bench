from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FindReservationByCode(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], reservation_code: str) -> str:
        reservations = data.get("reservations", [])
        for res in reservations:
            if res.get("reservation_id") == reservation_code:
                payload = res
                out = json.dumps(payload)
                return out
        payload = {"error": "Reservation not found", "reservation_code": reservation_code}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindReservationByCode",
                "description": "Retrieves the full details of a reservation using its unique code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_code": {
                            "type": "string",
                            "description": "The unique reservation code (e.g., '4WQ150').",
                        }
                    },
                    "required": ["reservation_code"],
                },
            },
        }
