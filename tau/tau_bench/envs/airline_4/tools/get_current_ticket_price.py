from __future__ import annotations
from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, timedelta  #required for fallback window enlargement
from decimal import ROUND_HALF_UP, Decimal
from typing import Any
import re
from datetime import date as _date

class GetCurrentTicketPrice(Tool):
    """Retrieve the ticket price for a flight/date/fare_class from flights.json."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        flight_number: str,
        date: str,
        fare_class: str,
        fallback_to_flights: bool | None = None,  # accept the caller's argument
    ) -> str:
        day = date
        flight = _get_flight(data, flight_number)
        if not flight:
            return _json({"error": "flight_not_found"})

        rec = _get_date_record(flight, day)
        if not rec or _norm_status(rec.get("status")) != "available":
            return _json({"error": "price_not_available_for_date"})

        prices = rec.get("prices") or {}
        if not isinstance(prices, dict):
            return _json({"error": "fare_class_not_found"})

        price = prices.get(fare_class)
        if price is None:
            return _json({"error": "fare_class_not_found"})

        return _json(
            {
                "flight_number": flight_number,
                "date": day,
                "fare_class": fare_class,
                "price": price,
                "price_source": "flights_json",
                "fallback_to_flights": (
                    bool(fallback_to_flights)
                    if fallback_to_flights is not None
                    else None
                ),
            }
        )
        pass
        day = date
        flight = _get_flight(data, flight_number)
        if not flight:
            return _json({"error": "flight_not_found"})

        rec = _get_date_record(flight, day)
        if not rec or _norm_status(rec.get("status")) != "available":
            return _json({"error": "price_not_available_for_date"})

        prices = rec.get("prices") or {}
        if not isinstance(prices, dict):
            return _json({"error": "fare_class_not_found"})

        price = prices.get(fare_class)
        if price is None:
            return _json({"error": "fare_class_not_found"})

        return _json(
            {
                "flight_number": flight_number,
                "date": day,
                "fare_class": fare_class,
                "price": price,
                "price_source": "flights_json",
                "fallback_to_flights": (
                    bool(fallback_to_flights)
                    if fallback_to_flights is not None
                    else None
                ),
            }
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCurrentTicketPrice",
                "description": "Get price for flight/date/fare_class from flights.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "date": {"type": "string"},
                        "fare_class": {
                            "type": "string",
                            "enum": ["basic_economy", "economy", "business"],
                        },
                        "fallback_to_flights": {
                            "type": "boolean",
                            "description": "Ignored; kept for compatibility with callers.",
                        },
                    },
                    "required": ["flight_number", "date", "fare_class"],
                    "additionalProperties": False,
                },
            },
        }
