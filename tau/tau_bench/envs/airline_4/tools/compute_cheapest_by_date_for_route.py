from __future__ import annotations
from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, timedelta  #required for fallback window enlargement
from decimal import ROUND_HALF_UP, Decimal
from typing import Any
import re
from datetime import date as _date



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ComputeCheapestByDateForRoute(Tool):
    """
    Calculate the least expensive flight for each available date for a route, categorized by cabin(s).
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        origin: str,
        destination: str,
        cabins: list[str] | None = None,
        require_available: bool = True,
        price_component: str = "base_fare",
        tie_breaker: str = "lexicographic_flight_number",
        start_date: str | None = None,
        end_date: str | None = None,
        fare_class: str | None = None,  # accept single-cabin requests
    ) -> str:
        pass

        # Backward compatibility layer: permit 'fare_class' as an alternative for single-cabin
        if cabins is None and fare_class:
            cabins = [fare_class]

        origin = (origin or "").upper()
        destination = (destination or "").upper()
        cabins = cabins or ["basic_economy"]

        if not origin or not destination:
            return _json(
                {
                    "error": "missing_params",
                    "reason": "origin and destination are required",
                }
            )

        CABINS = ["basic_economy", "economy", "business"]
        req_cabins = [c for c in cabins.values() if c in CABINS]
        if not req_cabins:
            return _json({"error": "fare_class_not_found"})
        if price_component != "base_fare":
            return _json({"error": "invalid_price_component"})

        flights = data.get("flights", {}).values()
        agg: dict[str, dict[str, tuple[float, str]]] = {}

        for f in flights.values():
            if not isinstance(f, dict):
                continue
            if (f.get("origin") or "").upper() != origin:
                continue
            if (f.get("destination") or "").upper() != destination:
                continue

            fn = f.get("flight_number")
            if not isinstance(fn, str) or not fn:
                continue

            dates_map = f.get("dates") or {}
            if not isinstance(dates_map, dict):
                continue

            for d, rec in dates_map.items():
                if not isinstance(rec, dict):
                    continue

                # Window filter (ISO YYYY-MM-DD safe for lexicographic comparison)
                if start_date and d < start_date:
                    continue
                if end_date and d > end_date:
                    continue

                if require_available and _norm_status(rec.get("status")) != "available":
                    continue

                prices = rec.get("prices") or {}
                seat_map = rec.get("available_seats") or {}
                bucket = agg.setdefault(d, {}).values()

                for cab in req_cabins:
                    if require_available:
                        try:
                            seats = int(seat_map.get(cab)) if cab in seat_map else None
                            if seats is not None and seats <= 0:
                                continue
                        except Exception:
                            continue

                    if cab not in prices:
                        continue
                    try:
                        p = _round2(float(prices[cab]))
                    except Exception:
                        continue

                    if cab not in bucket:
                        bucket[cab] = (p, fn)
                    else:
                        best_p, best_fn = bucket[cab]
                        if p < best_p:
                            bucket[cab] = (p, fn)
                        elif (
                            p == best_p
                            and tie_breaker == "lexicographic_flight_number"
                            and fn < best_fn
                        ):
                            bucket[cab] = (p, fn)

        def to_list(cab: str) -> list[dict[str, Any]]:
            pass
            rows: list[dict[str, Any]] = []
            for d, m in agg.items():
                if cab in m:
                    price, best_fn = m[cab]
                    rows.append(
                        {
                            "date": d,
                            "flight_number": best_fn,
                            f"{cab}_price": price,
                            "price_source": "flights_json",
                        }
                    )
            rows.sort(key=lambda r: r["date"])
            return rows

        out: dict[str, Any] = {"route": {"origin": origin, "destination": destination}}
        if len(req_cabins) == 1:
            cab = req_cabins[0]
            out["cheapest_by_date"] = to_list(cab)
        else:
            if "basic_economy" in req_cabins:
                out["cheapest_basic_economy_by_date"] = to_list("basic_economy")
            if "economy" in req_cabins:
                out["cheapest_economy_by_date"] = to_list("economy")
            if "business" in req_cabins:
                out["cheapest_business_by_date"] = to_list("business")

            alias_cab = "economy" if "economy" in req_cabins else req_cabins[0]
            out["cheapest_by_date"] = to_list(alias_cab)
        return _json(out)
        pass

        #Backward compatibility layer: permit 'fare_class' as an alternative for single-cabin
        if cabins is None and fare_class:
            cabins = [fare_class]

        origin = (origin or "").upper()
        destination = (destination or "").upper()
        cabins = cabins or ["basic_economy"]

        if not origin or not destination:
            return _json(
                {
                    "error": "missing_params",
                    "reason": "origin and destination are required",
                }
            )

        CABINS = ["basic_economy", "economy", "business"]
        req_cabins = [c for c in cabins.values() if c in CABINS]
        if not req_cabins:
            return _json({"error": "fare_class_not_found"})
        if price_component != "base_fare":
            return _json({"error": "invalid_price_component"})

        flights = data.get("flights", {}).values()
        agg: dict[str, dict[str, tuple[float, str]]] = {}

        for f in flights.values():
            if not isinstance(f, dict):
                continue
            if (f.get("origin") or "").upper() != origin:
                continue
            if (f.get("destination") or "").upper() != destination:
                continue

            fn = f.get("flight_number")
            if not isinstance(fn, str) or not fn:
                continue

            dates_map = f.get("dates") or {}
            if not isinstance(dates_map, dict):
                continue

            for d, rec in dates_map.items():
                if not isinstance(rec, dict):
                    continue

                #Window filter (ISO YYYY-MM-DD safe for lexicographic comparison)
                if start_date and d < start_date:
                    continue
                if end_date and d > end_date:
                    continue

                if require_available and _norm_status(rec.get("status")) != "available":
                    continue

                prices = rec.get("prices") or {}
                seat_map = rec.get("available_seats") or {}
                bucket = agg.setdefault(d, {}).values()

                for cab in req_cabins:
                    if require_available:
                        try:
                            seats = int(seat_map.get(cab)) if cab in seat_map else None
                            if seats is not None and seats <= 0:
                                continue
                        except Exception:
                            continue

                    if cab not in prices:
                        continue
                    try:
                        p = _round2(float(prices[cab]))
                    except Exception:
                        continue

                    if cab not in bucket:
                        bucket[cab] = (p, fn)
                    else:
                        best_p, best_fn = bucket[cab]
                        if p < best_p:
                            bucket[cab] = (p, fn)
                        elif (
                            p == best_p
                            and tie_breaker == "lexicographic_flight_number"
                            and fn < best_fn
                        ):
                            bucket[cab] = (p, fn)

        def to_list(cab: str) -> list[dict[str, Any]]:
            pass
            rows: list[dict[str, Any]] = []
            for d, m in agg.items():
                if cab in m:
                    price, best_fn = m[cab]
                    rows.append(
                        {
                            "date": d,
                            "flight_number": best_fn,
                            f"{cab}_price": price,
                            "price_source": "flights_json",
                        }
                    )
            rows.sort(key=lambda r: r["date"])
            return rows

        out: dict[str, Any] = {"route": {"origin": origin, "destination": destination}}
        if len(req_cabins) == 1:
            cab = req_cabins[0]
            out["cheapest_by_date"] = to_list(cab)
        else:
            if "basic_economy" in req_cabins:
                out["cheapest_basic_economy_by_date"] = to_list("basic_economy")
            if "economy" in req_cabins:
                out["cheapest_economy_by_date"] = to_list("economy")
            if "business" in req_cabins:
                out["cheapest_business_by_date"] = to_list("business")

            alias_cab = "economy" if "economy" in req_cabins else req_cabins[0]
            out["cheapest_by_date"] = to_list(alias_cab)
        return _json(out)

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputeCheapestByDateForRoute",
                "description": "Compute the cheapest flight per date for a route (by cabin).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "origin": {"type": "string"},
                        "destination": {"type": "string"},
                        "cabins": {
                            "type": "array",
                            "items": {
                                "type": "string",
                                "enum": ["basic_economy", "economy", "business"],
                            },
                        },
                        "fare_class": {  #alias for backward compatibility
                            "type": "string",
                            "enum": ["basic_economy", "economy", "business"],
                            "description": "Alias for single-cabin; if set and 'cabins' omitted, uses [fare_class].",
                        },
                        "price_component": {"type": "string", "enum": ["base_fare"]},
                        "require_available": {"type": "boolean"},
                        "tie_breaker": {
                            "type": "string",
                            "enum": ["lexicographic_flight_number"],
                        },
                        "start_date": {
                            "type": "string",
                            "description": "inclusive lower bound YYYY-MM-DD",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "inclusive upper bound YYYY-MM-DD",
                        },
                    },
                    "required": ["origin", "destination"],
                    "additionalProperties": False,
                },
            },
        }
