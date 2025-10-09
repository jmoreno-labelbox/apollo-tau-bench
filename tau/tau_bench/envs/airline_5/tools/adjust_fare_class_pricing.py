from tau_bench.envs.tool import Tool
from __future__ import annotations
import json
from datetime import date, datetime, timedelta  #required for fallback window enlargement
from decimal import ROUND_HALF_UP, Decimal
from typing import Any
import re
from datetime import date as _date

class AdjustFareClassPricing(Tool):
    """Introduce a delta amount to the current price for a date/fare_class (can be positive or negative)."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        flight_number: str,
        date: str,
        fare_class: str,
        delta: float
    ) -> str:
        try:
            delta = float(delta)
        except Exception:
            return _json({"error": "invalid_delta"})

        flight = _get_flight(data, flight_number)
        if not flight:
            return _json({"error": "flight_not_found"})
        rec = _get_date_record(flight, date)
        if not rec or _norm_status(rec.get("status")) != "available":
            return _json({"error": "price_not_available_for_date"})
        prices = rec.get("prices") or {}
        if fare_class not in prices:
            return _json({"error": "fare_class_not_found"})

        try:
            old_price = float(prices[fare_class])
        except Exception:
            return _json({"error": "invalid_price_value"})

        new_price = round(old_price + delta, 2)
        prices[fare_class] = new_price

        return _json(
            {
                "success": True,
                "flight_number": flight_number,
                "date": date,
                "fare_class": fare_class,
                "old_price": round(old_price, 2),
                "price": prices[fare_class],
                "new_price": new_price,
            }
        )
        pass
        try:
            delta = float(delta)
        except Exception:
            return _json({"error": "invalid_delta"})

        flight = _get_flight(data, flight_number)
        if not flight:
            return _json({"error": "flight_not_found"})
        rec = _get_date_record(flight, date)
        if not rec or _norm_status(rec.get("status")) != "available":
            return _json({"error": "price_not_available_for_date"})
        prices = rec.get("prices") or {}
        if fare_class not in prices:
            return _json({"error": "fare_class_not_found"})

        try:
            old_price = float(prices[fare_class])
        except Exception:
            return _json({"error": "invalid_price_value"})

        new_price = round(old_price + delta, 2)
        prices[fare_class] = new_price

        return _json(
            {
                "success": True,
                "flight_number": flight_number,
                "date": date,
                "fare_class": fare_class,
                "old_price": round(old_price, 2),
                "price": prices[fare_class],
                "new_price": new_price,
            }
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AdjustFareClassPricing",
                "description": "Add delta to current price.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "date": {"type": "string"},
                        "fare_class": {
                            "type": "string",
                            "enum": ["basic_economy", "economy", "business"],
                        },
                        "delta": {"type": "number"},
                    },
                    "required": ["flight_number", "date", "fare_class", "delta"],
                },
            },
        }
