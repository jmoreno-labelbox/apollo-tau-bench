from tau_bench.envs.tool import Tool
from __future__ import annotations
import json
from datetime import date, datetime, timedelta  #required for fallback window enlargement
from decimal import ROUND_HALF_UP, Decimal
from typing import Any
import re
from datetime import date as _date

class RepriceReservation(Tool):
    """
    Reassess all legs in a reservation using a predictable strategy.

    Strategy:
      - 'match_bucket' (default): assign each leg.price to
        flights[leg.flight_number].dates[ISO(leg.date)].prices[cabin]
        if that record is available (optionally require status=='available').

    Options:
      - require_available (default True)
      - cabins_source: 'reservation' (default) or specific 'cabin' argument
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        reservation_id: str,
        strategy: str,
        require_available: bool = True,
        cabins_source: str | None = "reservation",
        cabin: str | None = None,
        fallback_to_flights: bool | None = None
    ) -> str:
        pass
        cabins_source = cabins_source or "reservation"
        explicit_cabin = (cabin or "").lower()

        def _as_float(v):
            pass
            try:
                return float(v) if v is not None else None
            except Exception:
                return None

        empty_resp = {
            "success": True,
            "reservation_id": reservation_id,
            "strategy": strategy,
            "require_available": require_available,
            "cabin_used": None,
            "legs_updated": 0,
            "total_delta": 0.0,
            "changes": [],
            "price_sources": [],
            "fallback_to_flights": (
                bool(fallback_to_flights) if fallback_to_flights is not None else None
            ),
        }

        res = _get_reservation(data, reservation_id)
        if not res:
            out = dict(empty_resp)
            out["note"] = "noop_reservation_not_found"
            return _json(out)

        #select cabin in a predictable manner
        if cabins_source == "cabin" and explicit_cabin:
            cabin_used = explicit_cabin
        else:
            cabin_used = (res.get("cabin") or "").lower()
        if not cabin_used:
            out = dict(empty_resp)
            out["cabin_used"] = None
            out["success"] = False
            out["error"] = "fare_class_not_found"
            out["reason"] = "Reservation lacks cabin and none provided."
            return _json(out)

        if strategy != "match_bucket":
            out = dict(empty_resp)
            out["cabin_used"] = cabin_used
            out["success"] = False
            out["error"] = "unsupported_strategy"
            return _json(out)

        legs = res.get("flights") or []
        if not legs:
            out = dict(empty_resp)
            out["cabin_used"] = cabin_used
            out["success"] = False
            out["error"] = "no_flights_in_reservation"
            return _json(out)

        changes: list[dict[str, Any]] = []
        price_sources: list[dict[str, Any]] = []
        total_delta = 0.0
        legs_updated = 0

        for leg in legs:
            fn = leg.get("flight_number")
            iso_day = _to_iso_day(leg.get("date"))
            old_price = _as_float(leg.get("price"))
            new_price_report = old_price
            price_source = "reservation"

            if fn and iso_day:
                fdoc = _get_flight(data, fn)
                rec = _get_date_record(fdoc, iso_day) if fdoc else None
                if rec is None:
                    price_source = "reservation"
                else:
                    status_ok = (
                        (_norm_status(rec.get("status")) == "available")
                        if require_available
                        else True
                    )
                    bucket_p = (rec.get("prices") or {}).get(cabin_used)
                    bucket_price = _as_float(bucket_p)

                    if not status_ok:
                        price_source = "unavailable"
                    elif bucket_price is not None:
                        bucket_price = round(bucket_price, 2)
                        new_price_report = bucket_price
                        price_source = "flights_json"

                        if old_price is None or round(old_price, 2) != bucket_price:
                            leg["price"] = bucket_price
                            legs_updated += 1
                            delta = (
                                None
                                if old_price is None
                                else round(bucket_price - round(old_price, 2), 2)
                            )
                            if delta is not None:
                                total_delta = round(total_delta + delta, 2)
                            changes.append(
                                {
                                    "flight_number": fn,
                                    "date": iso_day,
                                    "old_price": (
                                        None
                                        if old_price is None
                                        else round(old_price, 2)
                                    ),
                                    "new_price": bucket_price,
                                    "delta": delta,
                                }
                            )
                    else:
                        price_source = "reservation"

            price_sources.append(
                {
                    "flight_number": fn,
                    "date": iso_day,
                    "cabin": cabin_used or None,
                    "old_price": None if old_price is None else round(old_price, 2),
                    "new_price": (
                        None if new_price_report is None else round(new_price_report, 2)
                    ),
                    "price_source": price_source,
                }
            )

        return _json(
            {
                "success": True,
                "reservation_id": reservation_id,
                "strategy": strategy,
                "require_available": require_available,
                "cabin_used": cabin_used or None,
                "legs_updated": legs_updated,
                "total_delta": round(total_delta, 2),
                "changes": changes,
                "price_sources": price_sources,
                "fallback_to_flights": empty_resp["fallback_to_flights"],
            }
        )
        pass
        cabins_source = cabins_source or "reservation"
        explicit_cabin = (cabin or "").lower()

        def _as_float(v):
            pass
            try:
                return float(v) if v is not None else None
            except Exception:
                return None

        empty_resp = {
            "success": True,
            "reservation_id": reservation_id,
            "strategy": strategy,
            "require_available": require_available,
            "cabin_used": None,
            "legs_updated": 0,
            "total_delta": 0.0,
            "changes": [],
            "price_sources": [],
            "fallback_to_flights": (
                bool(fallback_to_flights) if fallback_to_flights is not None else None
            ),
        }

        res = _get_reservation(data, reservation_id)
        if not res:
            out = dict(empty_resp)
            out["note"] = "noop_reservation_not_found"
            return _json(out)

        #select cabin in a predictable manner
        if cabins_source == "cabin" and explicit_cabin:
            cabin_used = explicit_cabin
        else:
            cabin_used = (res.get("cabin") or "").lower()
        if not cabin_used:
            out = dict(empty_resp)
            out["cabin_used"] = None
            out["success"] = False
            out["error"] = "fare_class_not_found"
            out["reason"] = "Reservation lacks cabin and none provided."
            return _json(out)

        if strategy != "match_bucket":
            out = dict(empty_resp)
            out["cabin_used"] = cabin_used
            out["success"] = False
            out["error"] = "unsupported_strategy"
            return _json(out)

        legs = res.get("flights") or []
        if not legs:
            out = dict(empty_resp)
            out["cabin_used"] = cabin_used
            out["success"] = False
            out["error"] = "no_flights_in_reservation"
            return _json(out)

        changes: list[dict[str, Any]] = []
        price_sources: list[dict[str, Any]] = []
        total_delta = 0.0
        legs_updated = 0

        for leg in legs:
            fn = leg.get("flight_number")
            iso_day = _to_iso_day(leg.get("date"))
            old_price = _as_float(leg.get("price"))
            new_price_report = old_price
            price_source = "reservation"

            if fn and iso_day:
                fdoc = _get_flight(data, fn)
                rec = _get_date_record(fdoc, iso_day) if fdoc else None
                if rec is None:
                    price_source = "reservation"
                else:
                    status_ok = (
                        (_norm_status(rec.get("status")) == "available")
                        if require_available
                        else True
                    )
                    bucket_p = (rec.get("prices") or {}).get(cabin_used)
                    bucket_price = _as_float(bucket_p)

                    if not status_ok:
                        price_source = "unavailable"
                    elif bucket_price is not None:
                        bucket_price = round(bucket_price, 2)
                        new_price_report = bucket_price
                        price_source = "flights_json"

                        if old_price is None or round(old_price, 2) != bucket_price:
                            leg["price"] = bucket_price
                            legs_updated += 1
                            delta = (
                                None
                                if old_price is None
                                else round(bucket_price - round(old_price, 2), 2)
                            )
                            if delta is not None:
                                total_delta = round(total_delta + delta, 2)
                            changes.append(
                                {
                                    "flight_number": fn,
                                    "date": iso_day,
                                    "old_price": (
                                        None
                                        if old_price is None
                                        else round(old_price, 2)
                                    ),
                                    "new_price": bucket_price,
                                    "delta": delta,
                                }
                            )
                    else:
                        price_source = "reservation"

            price_sources.append(
                {
                    "flight_number": fn,
                    "date": iso_day,
                    "cabin": cabin_used or None,
                    "old_price": None if old_price is None else round(old_price, 2),
                    "new_price": (
                        None if new_price_report is None else round(new_price_report, 2)
                    ),
                    "price_source": price_source,
                }
            )

        return _json(
            {
                "success": True,
                "reservation_id": reservation_id,
                "strategy": strategy,
                "require_available": require_available,
                "cabin_used": cabin_used or None,
                "legs_updated": legs_updated,
                "total_delta": round(total_delta, 2),
                "changes": changes,
                "price_sources": price_sources,
                "fallback_to_flights": empty_resp["fallback_to_flights"],
            }
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RepriceReservation",
                "description": (
                    "Reprice all legs in a reservation using a deterministic strategy "
                    "(currently 'match_bucket'). Returns legs_updated, changes, total_delta, "
                    "and per-leg price_sources (ISO dates; sources: flights_json/reservation/unavailable)."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string"},
                        "strategy": {"type": "string", "enum": ["match_bucket"]},
                        "require_available": {"type": "boolean"},
                        "cabin": {
                            "type": "string",
                            "enum": ["basic_economy", "economy", "business"],
                        },
                        "cabins_source": {
                            "type": "string",
                            "enum": ["reservation", "cabin"],
                            "description": "Use the reservation cabin (default) or an explicit 'cabin' argument.",
                        },
                        "fallback_to_flights": {
                            "type": "boolean",
                            "description": "Ignored; accepted for compatibility with some callers.",
                        },
                    },
                    "required": ["reservation_id", "strategy", "require_available"],
                    "additionalProperties": False,
                },
            },
        }
