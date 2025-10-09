from tau_bench.envs.tool import Tool
from __future__ import annotations
import json
from datetime import date, datetime, timedelta  #required for fallback window enlargement
from decimal import ROUND_HALF_UP, Decimal
from typing import Any
import re
from datetime import date as _date

class GetFlightStatusByDate(Tool):
    """Provide the status for a particular flight/date."""

    @staticmethod
    def invoke(data: dict[str, Any], flight_number: str, date: str) -> str:
        f = _get_flight(data, flight_number)
        if not f:
            return _json({"error": "flight_not_found"})
        rec = _get_date_record(f, date)
        if not rec:
            return _json({"error": "price_not_available_for_date"})
        return _json(
            {
                "flight_number": flight_number,
                "date": date,
                "flight_status": _norm_status(rec.get("status")),
            }
        )
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetFlightStatusByDate",
                "description": "Status for a flight on a given date.",
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
