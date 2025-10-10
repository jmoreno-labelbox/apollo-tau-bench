# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAvailableSeat(Tool):
    """Return available seats for a cabin on a flight/date (reads available_seats[cabin])."""
    @staticmethod
    def invoke(
        data: Dict[str, Any], *,
        flight_number: str,
        date: str,
            cabin: str
    ) -> str:
        f = _get_flight(data, flight_number)
        if not f: return _json({"error":"flight_not_found"})
        rec = _get_date_record(f, date)
        if not rec or _norm_status(rec.get("status")) != "available":
            return _json({"error":"price_not_available_for_date"})
        seats = (rec.get("available_seats") or {}).get(cabin)
        if seats is None:
            return _json({"error":"fare_class_not_found"})
        return _json({"flight_number": flight_number,
                      "date": date,
                      "cabin": cabin,
                      "available_seats": seats})

    @staticmethod
    def get_info():
        return {
            "type":"function",
            "function":{
                "name": "get_available_seat",
                "description": "Available seats for a cabin on a flight/date.",
                "parameters": {
                    "type":"object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "date": {"type": "string"},
                        "cabin": {"type": "string", "enum": ["basic_economy", "economy", "business"]}
                    },
                    "required":["flight_number", "date", "cabin"]
                }
            }
        }
