from tau_bench.envs.tool import Tool
from __future__ import annotations
import json
from datetime import date, datetime, timedelta  #required for fallback window enlargement
from decimal import ROUND_HALF_UP, Decimal
from typing import Any
import re
from datetime import date as _date

class GetFlightSchedule(Tool):
    """Provide the schedule for a flight within [start_date, end_date] along with status for each date."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        flight_number: str,
        start_date: str | None = None,
        end_date: str | None = None
    ) -> str:
        f = _get_flight(data, flight_number)
        if not f:
            return _json({"error": "flight_not_found"})
        rows = []
        for d, rec in (f.get("dates") or {}).items():
            if (not start_date or d >= start_date) and (not end_date or d <= end_date):
                rows.append({"date": d, "status": _norm_status(rec.get("status"))})
        rows.sort(key=lambda r: r["date"])
        return _json({"flight_number": flight_number, "schedule": rows})
        pass
        f = _get_flight(data, flight_number)
        if not f:
            return _json({"error": "flight_not_found"})
        rows = []
        for d, rec in (f.get("dates") or {}).items():
            if (not start_date or d >= start_date) and (not end_date or d <= end_date):
                rows.append({"date": d, "status": _norm_status(rec.get("status"))})
        rows.sort(key=lambda r: r["date"])
        return _json({"flight_number": flight_number, "schedule": rows})

    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetFlightSchedule",
                "description": "List per-date status for a flight within a window.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"},
                    },
                    "required": ["flight_number"],
                },
            },
        }
