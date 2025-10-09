from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class RefundReservationsByFlightDay(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], flight_number: str, date: str) -> str:
        out = []
        for r in data.get("reservations", []):
            for seg in r.get("flights", []):
                if (
                    seg.get("flight_number") == flight_number
                    and seg.get("date") == date
                ):
                    seg["status"] = "refunded"
                    out.append(r)

        return _j(out)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RefundReservationsByFlightDay",
                "description": "Refund reservations that include a segment with the given flight_number on the given date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "date": {"type": "string"},
                    },
                    "required": ["flight_number", "date"],
                },
            },
        }
