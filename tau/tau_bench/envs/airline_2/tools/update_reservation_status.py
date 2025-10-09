from tau_bench.envs.tool import Tool
import json
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
        for r in reservations:
            if r.get("reservation_id") == reservation_id:
                r["status"] = new_status
                return _j(r)
        return _j({"error": "reservation_not_found", "reservation_id": reservation_id})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateReservationStatus",
                "description": "Update the status of a reservation (e.g., confirmed, ticketed, cancelled).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string"},
                        "new_status": {"type": "string"},
                    },
                    "required": ["reservation_id", "new_status"],
                },
            },
        }
