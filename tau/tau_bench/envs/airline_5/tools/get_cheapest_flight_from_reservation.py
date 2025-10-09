from tau_bench.envs.tool import Tool
from __future__ import annotations
import json
from datetime import date, datetime, timedelta  #required for fallback window enlargement
from decimal import ROUND_HALF_UP, Decimal
from typing import Any
import re
from datetime import date as _date

class GetCheapestFlightFromReservation(Tool):
    """
    Locate the most affordable flight leg within a reservation.
    Notes:
      • Dates are standardized to an ISO day (YYYY-MM-DD) for both searching and output.
      • Prices are converted to float for consistent comparisons/sorting.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        reservation_id: str,
        fallback_to_flights: bool = True,
        require_available: bool = False,
        return_all: bool = False
    ) -> str:
        pass

        if "reservations" not in data:
            return _json({"error": "reservations_not_loaded"})

        res = _get_reservation(data, reservation_id)
        if not res:
            return _json({"error": "reservation_not_found"})

        legs: list[dict[str, Any]] = res.get("flights") or []
        if not legs:
            return _json({"error": "no_flights_in_reservation"})

        cabin = (res.get("cabin") or "").lower()

        def _as_number(x):
            pass
            try:
                return float(x) if x is not None else None
            except (TypeError, ValueError):
                return None

        evaluated: list[dict[str, Any]] = []
        # potential options: (price_float, iso_day, flight_number, leg_out)
        candidates: list[tuple[float, str, str, dict[str, Any]]] = []

        for leg in legs:
            orig_date = leg.get("date")
            iso_day = _to_iso_day(orig_date)  # standardize a single time

            leg_out = {
                "flight_number": leg.get("flight_number"),
                "origin": leg.get("origin"),
                "destination": leg.get("destination"),
                # Provide the standardized ISO day for downstream users
                "date": iso_day,
            }

            price = _as_number(leg.get("price"))
            price_source = None
            status_ok = True

            if price is None and fallback_to_flights:
                if "flights" in data and cabin:
                    fdoc = _get_flight(data, leg.get("flight_number"))
                    rec = _get_date_record(fdoc, iso_day) if fdoc else None
                    if rec is not None:
                        status = _norm_status(rec.get("status"))
                        status_ok = (
                            (status == "available") if require_available else True
                        )
                        if status_ok:
                            price_bucket = (rec.get("prices") or {}).get(cabin)
                            price = _as_number(price_bucket)
                            if price is not None:
                                price_source = "flights_json"

            # If a price is still unavailable, or the status is not permitted, log and proceed
            if price is None:
                leg_out["error"] = "price_unavailable"
                evaluated.append(leg_out)
                continue

            if not status_ok:
                leg_out["error"] = "status_not_available"
                evaluated.append(leg_out)
                continue

            # Valid candidate
            leg_out["price"] = price
            leg_out["price_source"] = price_source or "reservation"
            evaluated.append(leg_out)

            # Predictable sorting tuple: (price_float, iso_day_str, flight_number_str)
            d_key = iso_day or "9999-12-31"
            fn = leg_out.get("flight_number") or ""
            candidates.append((price, d_key, fn, leg_out))

        if not candidates:
            return _json(
                {
                    "error": "no_priced_legs",
                    "details": {
                        "reservation_id": reservation_id,
                        "fallback_to_flights": fallback_to_flights,
                        "require_available": require_available,
                    },
                }
            )

        candidates.sort(key=lambda x: (x[0], x[1], x[2]))
        cheapest_leg = candidates[0][3]

        out = {
            "reservation_id": reservation_id,
            "cabin": cabin or None,
            "cheapest_leg": cheapest_leg,
        }
        if return_all:
            out["evaluated_legs"] = evaluated
        return _json(out)
        pass

        if "reservations" not in data:
            return _json({"error": "reservations_not_loaded"})

        res = _get_reservation(data, reservation_id)
        if not res:
            return _json({"error": "reservation_not_found"})

        legs: list[dict[str, Any]] = res.get("flights") or []
        if not legs:
            return _json({"error": "no_flights_in_reservation"})

        cabin = (res.get("cabin") or "").lower()

        def _as_number(x):
            pass
            try:
                return float(x) if x is not None else None
            except (TypeError, ValueError):
                return None

        evaluated: list[dict[str, Any]] = []
        #potential options: (price_float, iso_day, flight_number, leg_out)
        candidates: list[tuple[float, str, str, dict[str, Any]]] = []

        for leg in legs:
            orig_date = leg.get("date")
            iso_day = _to_iso_day(orig_date)  #standardize a single time

            leg_out = {
                "flight_number": leg.get("flight_number"),
                "origin": leg.get("origin"),
                "destination": leg.get("destination"),
                #Provide the standardized ISO day for downstream users
                "date": iso_day,
            }

            price = _as_number(leg.get("price"))
            price_source = None
            status_ok = True

            if price is None and fallback_to_flights:
                if "flights" in data and cabin:
                    fdoc = _get_flight(data, leg.get("flight_number"))
                    rec = _get_date_record(fdoc, iso_day) if fdoc else None
                    if rec is not None:
                        status = _norm_status(rec.get("status"))
                        status_ok = (
                            (status == "available") if require_available else True
                        )
                        if status_ok:
                            price_bucket = (rec.get("prices") or {}).get(cabin)
                            price = _as_number(price_bucket)
                            if price is not None:
                                price_source = "flights_json"

            #If a price is still unavailable, or the status is not permitted, log and proceed
            if price is None:
                leg_out["error"] = "price_unavailable"
                evaluated.append(leg_out)
                continue

            if not status_ok:
                leg_out["error"] = "status_not_available"
                evaluated.append(leg_out)
                continue

            #Valid candidate
            leg_out["price"] = price
            leg_out["price_source"] = price_source or "reservation"
            evaluated.append(leg_out)

            #Predictable sorting tuple: (price_float, iso_day_str, flight_number_str)
            d_key = iso_day or "9999-12-31"
            fn = leg_out.get("flight_number") or ""
            candidates.append((price, d_key, fn, leg_out))

        if not candidates:
            return _json(
                {
                    "error": "no_priced_legs",
                    "details": {
                        "reservation_id": reservation_id,
                        "fallback_to_flights": fallback_to_flights,
                        "require_available": require_available,
                    },
                }
            )

        candidates.sort(key=lambda x: (x[0], x[1], x[2]))
        cheapest_leg = candidates[0][3]

        out = {
            "reservation_id": reservation_id,
            "cabin": cabin or None,
            "cheapest_leg": cheapest_leg,
        }
        if return_all:
            out["evaluated_legs"] = evaluated
        return _json(out)

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCheapestFlightFromReservation",
                "description": (
                    "Find the cheapest leg within a reservation. Uses the leg's own price first; "
                    "optionally falls back to flights.json using the reservation cabin and leg date. "
                    "The 'date' returned in outputs (e.g., cheapest_leg.date and evaluated_legs[].date when return_all=True) "
                    "is always normalized to an ISO day string (YYYY-MM-DD)."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string"},
                        "fallback_to_flights": {
                            "type": "boolean",
                            "description": "If True (default), fill missing leg prices from flights.json.",
                        },
                        "require_available": {
                            "type": "boolean",
                            "description": "If True, only consider legs whose flight-date status is 'available' in flights.json.",
                        },
                        "return_all": {
                            "type": "boolean",
                            "description": "If True, include evaluated_legs for debugging/traceability.",
                        },
                    },
                    "required": ["reservation_id"],
                },
            },
        }
