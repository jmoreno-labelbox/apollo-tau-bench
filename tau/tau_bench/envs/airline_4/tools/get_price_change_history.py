from __future__ import annotations
from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, timedelta  #required for fallback window enlargement
from decimal import ROUND_HALF_UP, Decimal
from typing import Any
import re
from datetime import date as _date

class GetPriceChangeHistory(Tool):
    """Provide change points from flights.json for a fare_class, with optional windowing."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        flight_number: str,
        fare_class: str,
        start_date: str | None = None,
        end_date: str | None = None
    ) -> str:
        flight = _get_flight(data, flight_number)
        if not flight:
            return _json({"error": "flight_not_found"})

        changes = []
        prev = None
        for d in sorted((flight.get("dates") or {}).keys()):
            if (start_date and d < start_date) or (end_date and d > end_date):
                continue
            rec = flight["dates"][d]
            if (
                _norm_status(rec.get("status")) == "available"
                and rec.get("prices")
                and fare_class in rec["prices"]
            ):
                p = rec["prices"][fare_class]
                if prev is None or p != prev:
                    changes.append({"date": d, "price": p})
                    prev = p

        if not changes:
            return _json({"error": "no_price_changes_found"})
        return _json(
            {
                "flight_number": flight_number,
                "fare_class": fare_class,
                "changes": changes,
            }
        )
        pass
        flight = _get_flight(data, flight_number)
        if not flight:
            return _json({"error": "flight_not_found"})

        changes = []
        prev = None
        for d in sorted((flight.get("dates") or {}).keys()):
            if (start_date and d < start_date) or (end_date and d > end_date):
                continue
            rec = flight["dates"][d]
            if (
                _norm_status(rec.get("status")) == "available"
                and rec.get("prices")
                and fare_class in rec["prices"]
            ):
                p = rec["prices"][fare_class]
                if prev is None or p != prev:
                    changes.append({"date": d, "price": p})
                    prev = p

        if not changes:
            return _json({"error": "no_price_changes_found"})
        return _json(
            {
                "flight_number": flight_number,
                "fare_class": fare_class,
                "changes": changes,
            }
        )

    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetPriceChangeHistory",
                "description": "Extract change points for prices across dates.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "fare_class": {
                            "type": "string",
                            "enum": ["basic_economy", "economy", "business"],
                        },
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"},
                    },
                    "required": ["flight_number", "fare_class"],
                },
            },
        }
