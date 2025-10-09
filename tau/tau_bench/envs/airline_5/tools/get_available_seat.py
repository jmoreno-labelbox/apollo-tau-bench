from __future__ import annotations
from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, timedelta  #required for fallback window enlargement
from decimal import ROUND_HALF_UP, Decimal
from typing import Any
import re
from datetime import date as _date

class GetAvailableSeat(Tool):
    """Provide the available seats for a cabin on a flight/date (accesses available_seats[cabin])."""

    @staticmethod
    def invoke(
        data: dict[str, Any], flight_number: str, date: str, cabin: str
    ) -> str:
        f = _get_flight(data, flight_number)
        if not f:
            return _json({"error": "flight_not_found"})
        rec = _get_date_record(f, date)
        if not rec or _norm_status(rec.get("status")) != "available":
            return _json({"error": "price_not_available_for_date"})
        seats = (rec.get("available_seats") or {}).get(cabin)
        if seats is None:
            return _json({"error": "fare_class_not_found"})
        return _json(
            {
                "flight_number": flight_number,
                "date": date,
                "cabin": cabin,
                "available_seats": seats,
            }
        )
        pass
        f = _get_flight(data, flight_number)
        if not f:
            return _json({"error": "flight_not_found"})
        rec = _get_date_record(f, date)
        if not rec or _norm_status(rec.get("status")) != "available":
            return _json({"error": "price_not_available_for_date"})
        seats = (rec.get("available_seats") or {}).get(cabin)
        if seats is None:
            return _json({"error": "fare_class_not_found"})
        return _json(
            {
                "flight_number": flight_number,
                "date": date,
                "cabin": cabin,
                "available_seats": seats,
            }
        )

    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetAvailableSeat",
                "description": "Available seats for a cabin on a flight/date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "date": {"type": "string"},
                        "cabin": {
                            "type": "string",
                            "enum": ["basic_economy", "economy", "business"],
                        },
                    },
                    "required": ["flight_number", "date", "cabin"],
                },
            },
        }
