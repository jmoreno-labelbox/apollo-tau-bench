from __future__ import annotations
from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, timedelta  #required for fallback window enlargement
from decimal import ROUND_HALF_UP, Decimal
from typing import Any
import re
from datetime import date as _date

class ListOperatingDates(Tool):
    """Enumerate all dates when a flight is operational (status == 'available'), sorted in ascending order."""

    @staticmethod
    def invoke(data: dict[str, Any], flight_number: str) -> str:
        f = _get_flight(data, flight_number)

        if not f:
            return _json({"error": "flight_not_found"})
        dates = [
            d
            for d, rec in (f.get("dates") or {}).items()
            if _norm_status(rec.get("status")) == "available"
        ]
        dates.sort()
        return _json({"flight_number": flight_number, "dates": dates})
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "listOperatingDates",
                "description": "Return sorted available operating dates for a flight.",
                "parameters": {
                    "type": "object",
                    "properties": {"flight_number": {"type": "string"}},
                    "required": ["flight_number"],
                },
            },
        }
