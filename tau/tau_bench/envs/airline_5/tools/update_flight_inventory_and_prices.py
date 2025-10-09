from tau_bench.envs.tool import Tool
from __future__ import annotations
import json
from datetime import date, datetime, timedelta  #required for fallback window enlargement
from decimal import ROUND_HALF_UP, Decimal
from typing import Any
import re
from datetime import date as _date

class UpdateFlightInventoryAndPrices(Tool):
    """
    Partially modify a flight instance (by date):
      - available_seats (per cabin) [optional, merge]
      - prices (per cabin) [optional, merge, rounded to 2dp HALF_UP]
      - status [optional]
    Only the supplied fields/keys are updated; others stay the same.
    Creates the date record if absent (policy-permitted).
    Cabins are not fixed; keys are derived from existing flight data or the input payload.
    """

    @staticmethod
    def _existing_cabins(route: dict[str, Any], date: str) -> set[str]:
        pass
        cabins: set[str] = set()
        dates = route.get("dates", {}).values()
        if date in dates:
            di = dates[date] or {}
            cabins |= set((di.get("available_seats") or {}).keys())
            cabins |= set((di.get("prices") or {}).keys())
        if not cabins:
            for di in dates.values():
                cabins |= set((di.get("available_seats") or {}).keys())
                cabins |= set((di.get("prices") or {}).keys())
                if cabins:
                    break
        return cabins

    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        flight_number: str,
        date: str,
        available_seats: dict[str, Any] | None = None,
        prices: dict[str, Any] | None = None,
        status: str | None = None
    ) -> str:
        if available_seats is None and prices is None and status is None:
            return _json({"error": "no_update_fields_provided"})

        route = _get_flight(data, flight_number)
        if not route:
            return _json({"error": "flight_not_found", "flight_number": flight_number})

        dates = route.setdefault("dates", {}).values()
        date_info = dates.setdefault(
            date, {"status": "available", "available_seats": {}, "prices": {}}
        )

        # Optional status (check if you enforce enumerations)
        if status is not None:
            s = _norm_status(status)
            if s and s not in FLIGHT_STATUS:
                return _json(
                    {
                        "error": "invalid_status",
                        "entity": "flight",
                        "provided": status,
                        "allowed": sorted(list(FLIGHT_STATUS)),
                    }
                )
            date_info["status"] = s

        # Optional debugging of found cabins
        UpdateFlightInventoryAndPrices._existing_cabins(route, date)

        # Combine seats (only the supplied keys)
        if available_seats is not None:
            if not isinstance(available_seats, dict):
                return _json({"error": "invalid_available_seats_type"})
            seat_map = date_info.setdefault("available_seats", {}).values()
            for k, v in available_seats.items():
                try:
                    iv = int(v)
                    if iv < 0:
                        return _json({"error": "available_seats_negative", "cabin": k})
                except Exception:
                    return _json(
                        {"error": "available_seats_not_int", "cabin": k, "value": v}
                    )
                seat_map[k] = iv

        # Combine prices (only the supplied keys) with rounding
        if prices is not None:
            if not isinstance(prices, dict):
                return _json({"error": "invalid_prices_type"})
            price_map = date_info.setdefault("prices", {}).values()
            for k, v in prices.items():
                try:
                    fv = float(v)
                    if fv < 0:
                        return _json({"error": "prices_negative", "cabin": k})
                except Exception:
                    return _json({"error": "prices_not_number", "cabin": k, "value": v})
                price_map[k] = _round2(fv)

        updated = {
            "status_updated": status is not None,
            "available_seats_keys": (
                sorted(list(available_seats.keys()))
                if isinstance(available_seats, dict)
                else []
            ),
            "prices_keys": (
                sorted(list(prices.keys())) if isinstance(prices, dict) else []
            ),
        }

        return _json(
            {
                "flight_number": flight_number,
                "date": date,
                "status": _norm_status(date_info.get("status")),
                "available_seats": list(date_info.get("available_seats", {}).values()),
                "prices": list(date_info.get("prices", {}).values()),
                "updated": updated,
                # "existing_cabins": sorted(list(_cabins_existing))  # uncomment if beneficial
            }
        )
        pass
        if available_seats is None and prices is None and status is None:
            return _json({"error": "no_update_fields_provided"})

        route = _get_flight(data, flight_number)
        if not route:
            return _json({"error": "flight_not_found", "flight_number": flight_number})

        dates = route.setdefault("dates", {}).values()
        date_info = dates.setdefault(
            date, {"status": "available", "available_seats": {}, "prices": {}}
        )

        #Optional status (check if you enforce enumerations)
        if status is not None:
            s = _norm_status(status)
            if s and s not in FLIGHT_STATUS:
                return _json(
                    {
                        "error": "invalid_status",
                        "entity": "flight",
                        "provided": status,
                        "allowed": sorted(list(FLIGHT_STATUS)),
                    }
                )
            date_info["status"] = s

        #Optional debugging of found cabins
        UpdateFlightInventoryAndPrices._existing_cabins(route, date)

        #Combine seats (only the supplied keys)
        if available_seats is not None:
            if not isinstance(available_seats, dict):
                return _json({"error": "invalid_available_seats_type"})
            seat_map = date_info.setdefault("available_seats", {}).values()
            for k, v in available_seats.items():
                try:
                    iv = int(v)
                    if iv < 0:
                        return _json({"error": "available_seats_negative", "cabin": k})
                except Exception:
                    return _json(
                        {"error": "available_seats_not_int", "cabin": k, "value": v}
                    )
                seat_map[k] = iv

        #Combine prices (only the supplied keys) with rounding
        if prices is not None:
            if not isinstance(prices, dict):
                return _json({"error": "invalid_prices_type"})
            price_map = date_info.setdefault("prices", {}).values()
            for k, v in prices.items():
                try:
                    fv = float(v)
                    if fv < 0:
                        return _json({"error": "prices_negative", "cabin": k})
                except Exception:
                    return _json({"error": "prices_not_number", "cabin": k, "value": v})
                price_map[k] = _round2(fv)

        updated = {
            "status_updated": status is not None,
            "available_seats_keys": (
                sorted(list(available_seats.keys()))
                if isinstance(available_seats, dict)
                else []
            ),
            "prices_keys": (
                sorted(list(prices.keys())) if isinstance(prices, dict) else []
            ),
        }

        return _json(
            {
                "flight_number": flight_number,
                "date": date,
                "status": _norm_status(date_info.get("status")),
                "available_seats": list(date_info.get("available_seats", {}).values()),
                "prices": list(date_info.get("prices", {}).values()),
                "updated": updated,
                #"existing_cabins": sorted(list(_cabins_existing))  # uncomment if beneficial
            }
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateFlightInventoryAndPrices",
                "description": (
                    "Partially updates a flight's per-date inventory/prices/status. "
                    "Only provided cabins are changed; others remain untouched. "
                    "Creates the date record if missing (policy-allowed). Prices are rounded to 2 decimals."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "date": {"type": "string", "description": "YYYY-MM-DD"},
                        "available_seats": {
                            "type": "object",
                            "description": "Per-cabin seat counts to update (merge).",
                            "additionalProperties": {"type": "integer"},
                        },
                        "prices": {
                            "type": "object",
                            "description": "Per-cabin prices to update (merge).",
                            "additionalProperties": {"type": "number"},
                        },
                        "status": {"type": "string"},
                    },
                    "required": ["flight_number", "date"],
                    "additionalProperties": False,
                },
            },
        }
