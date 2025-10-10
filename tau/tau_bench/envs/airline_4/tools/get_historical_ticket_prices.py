# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetHistoricalTicketPrices(Tool):
    """Return all available daily prices for a flight for the specified fare_class."""

    @staticmethod
    def invoke(
        data: Dict[str, Any], *,
        flight_number: str,
        fare_class: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        require_available: bool = True,
    ) -> str:

        flight = _get_flight(data, flight_number)
        if not flight:
            return _json({"error": "flight_not_found"})

        out: List[Dict[str, Any]] = []
        dates_map = flight.get("dates") or {}
        if not isinstance(dates_map, dict):
            return _json({"flight_number": flight_number, "fare_class": fare_class, "history": []})

        for d, rec in dates_map.items():
            # lexicographic-safe ISO date window
            if start_date and d < start_date:
                continue
            if end_date and d > end_date:
                continue

            if not isinstance(rec, dict):
                continue

            if require_available and _norm_status(rec.get("status")) != "available":
                continue

            prices = rec.get("prices") or {}
            if fare_class not in prices:
                continue

            try:
                price = float(prices[fare_class])
            except Exception:
                continue

            out.append({"date": d, "price": price})

        out.sort(key=lambda x: x["date"])
        return _json({
            "flight_number": flight_number,
            "fare_class": fare_class,
            "start_date": start_date,
            "end_date": end_date,
            "require_available": require_available,
            "history": out
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_historical_ticket_prices",
                "description": "List daily prices for a flight and fare_class, optionally within a date window.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "fare_class": {"type": "string", "enum": ["basic_economy", "economy", "business"]},
                        "start_date": {"type": "string", "description": "Inclusive YYYY-MM-DD"},
                        "end_date": {"type": "string", "description": "Inclusive YYYY-MM-DD"},
                        "require_available": {"type": "boolean", "description": "Default true"}
                    },
                    "required": ["flight_number", "fare_class"],
                    "additionalProperties": False
                }
            }
        }
