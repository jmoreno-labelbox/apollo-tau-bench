from __future__ import annotations

import json
from datetime import date, datetime, timedelta  #required for fallback window enlargement
from decimal import ROUND_HALF_UP, Decimal
from typing import Any

from domains.dto import Tool


#--- auxiliary function that is optional
def _find_aircraft(
    data: dict[str, Any], aircraft_id: str | None, tail_number: str | None
) -> dict[str, Any] | None:
    pass
    for a in data.get("aircraft", []):
        if aircraft_id and a.get("aircraft_id") == aircraft_id:
            return a
        if tail_number and a.get("tail_number") == tail_number:
            return a
    return None


def _json(data: Any) -> str:
    pass
    payload = data
    out = json.dumps(payload, indent=2, sort_keys=True, default=str)
    return out


def _get_aircraft_model_by_id(
    data: dict[str, Any], model_id: str
) -> dict[str, Any] | None:
    pass
    mid = (model_id or "").upper()
    for m in data.get("aircraft_models", []):
        if (m.get("model_id") or "").upper() == mid:
            return m
    return None


def _get_flight(data: dict[str, Any], flight_number: str) -> dict[str, Any] | None:
    pass
    for f in data.get("flights", []):
        if f.get("flight_number") == flight_number:
            return f
    return None


def _round2(x) -> float:
    pass
    return float(Decimal(str(x)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def _load_flights(data: dict[str, Any]) -> list[dict[str, Any]]:
    pass
    return data.get("flights", [])


def _get_airport_by_iata(data: dict[str, Any], iata_code: str) -> dict[str, Any] | None:
    pass
    iata = (iata_code or "").upper()
    for a in data.get("airports", []):
        if a.get("iata_code") == iata:
            return a
    return None


def _next_change_id(data: dict[str, Any], prefix: str = "PC") -> str:
    pass
    seq = data.setdefault("_seq", {}).get("price_change_id", 0) + 1
    data["_seq"]["price_change_id"] = seq
    return f"{prefix}{seq:06d}"


def _get_date_record(flight: dict[str, Any], day: str) -> dict[str, Any] | None:
    pass
    return (flight or {}).get("dates", {}).get(day)


def _get_reservation(data, reservation_id):
    pass
    res = data.get("reservations")
    if isinstance(res, dict):
        rec = res.get(reservation_id)
        if isinstance(rec, dict):
            #make sure reservation_id is available for downstream processing
            return (
                rec
                if rec.get("reservation_id")
                else {**rec, "reservation_id": reservation_id}
            )
        #additional scan
        for r in res.values():
            if isinstance(r, dict) and r.get("reservation_id") == reservation_id:
                return r
        return None
    #fallback in list format
    for r in res or []:
        if isinstance(r, dict) and r.get("reservation_id") == reservation_id:
            return r
    return None


import re


def _get_cert_by_id(data: dict[str, Any], cert_id: str) -> dict[str, Any] | None:
    pass
    target = _norm(cert_id)
    for c in data.get("certifications", []):
        if _norm(c.get("certification_id")) == target:
            return c
    return None


def _norm(s: str) -> str:
    pass
    if s is None:
        return ""
    #trim, convert to lowercase, eliminate non-alphanumeric characters
    return re.sub(r"[^a-z0-9]", "", str(s).strip().lower())


def _find_crew_member(
    data: dict[str, Any], crew_member_id: str
) -> dict[str, Any] | None:
    pass
    target = _norm(crew_member_id)
    for cm in data.get("crew_members", []):
        if _norm(cm.get("crew_member_id")) == target:
            return cm
    return None


def _get_cert_by_code(data: dict[str, Any], code: str) -> dict[str, Any] | None:
    pass
    target = _norm(code)
    for c in data.get("certifications", []):
        c_code = _norm(c.get("certification_code"))
        if c_code == target:
            return c
    #fallback: attempt to use common alias field names if they exist (no operation if they do not)
    for c in data.get("certifications", []):
        #occasionally datasets include 'model_id' or 'code'
        for alt_key in ("model_id", "code", "name", "model"):
            if _norm(c.get(alt_key)) == target:
                return c
    return None


from datetime import date as _date


def _to_iso_day(v):
    pass
    if v in (None, "", "null"):
        return "9999-12-31"
    s = str(v)
    #Attempt strict ISO parsing (also accepts complete ISO datetimes)
    try:
        return datetime.fromisoformat(s).date().isoformat()
    except Exception:
        #Fallback: use the first 10 characters if they represent a valid YYYY-MM-DD
        day = s[:10]
        try:
            _date.fromisoformat(day)
            return day
        except Exception:
            return "9999-12-31"


#Standard status enumerations (in lowercase)
FLIGHT_STATUS = {"available", "cancelled", "delayed", "diverted", "landed"}
AIRCRAFT_STATUS = {
    "active",
    "maintenance",
    "stored",
    "in maintenance",
}  #expand as required
EVENT_STATUS = {"active", "resolved"}


def _norm_status(s: str) -> str:
    pass
    return (s or "").strip().lower()


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
        pass
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


class ListAllFaresByRoute(Tool):
    """Enumerate available fares (by flight/date) for a route, limited to a cap (default 5)."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        origin: str,
        destination: str,
        limit: int = 5,
        offset: int = 0
    ) -> str:
        # standardize inputs
        origin = (origin or "").upper()
        destination = (destination or "").upper()

        # page management
        try:
            limit = int(limit)
        except Exception:
            limit = 5
        if limit <= 0:
            limit = 5

        try:
            offset = int(offset)
        except Exception:
            offset = 0
        if offset < 0:
            offset = 0

        if not origin or not destination:
            return _json(
                {
                    "error": "missing_params",
                    "reason": "origin and destination are required.",
                }
            )

        flights = _load_flights(data)
        rows: list[dict[str, Any]] = []
        for f in flights:
            if f.get("origin") == origin and f.get("destination") == destination:
                for d, info in (f.get("dates") or {}).items():
                    if (
                        isinstance(info, dict)
                        and _norm_status(info.get("status")) == "available"
                        and "prices" in info
                    ):
                        rows.append(
                            {
                                "flight_number": f["flight_number"],
                                "date": d,
                                "prices": info["prices"],
                                "available_seats": info.get("available_seats"),
                            }
                        )

        # order by date followed by flight_number
        rows.sort(key=lambda x: (x["date"], x["flight_number"]))

        total = len(rows)
        sliced = rows[offset : offset + limit]

        return _json(
            {
                "route": {"origin": origin, "destination": destination},
                "total": total,
                "offset": offset,
                "limit": limit,
                "has_more": offset + limit < total,
                "fares": sliced,
            }
        )
        pass

        #standardize inputs
        origin = (origin or "").upper()
        destination = (destination or "").upper()

        #page management
        try:
            limit = int(limit)
        except Exception:
            limit = 5
        if limit <= 0:
            limit = 5

        try:
            offset = int(offset)
        except Exception:
            offset = 0
        if offset < 0:
            offset = 0

        if not origin or not destination:
            return _json(
                {
                    "error": "missing_params",
                    "reason": "origin and destination are required.",
                }
            )

        flights = _load_flights(data)
        rows: list[dict[str, Any]] = []
        for f in flights:
            if f.get("origin") == origin and f.get("destination") == destination:
                for d, info in (f.get("dates") or {}).items():
                    if (
                        isinstance(info, dict)
                        and _norm_status(info.get("status")) == "available"
                        and "prices" in info
                    ):
                        rows.append(
                            {
                                "flight_number": f["flight_number"],
                                "date": d,
                                "prices": info["prices"],
                                "available_seats": info.get("available_seats"),
                            }
                        )

        #order by date followed by flight_number
        rows.sort(key=lambda x: (x["date"], x["flight_number"]))

        total = len(rows)
        sliced = rows[offset : offset + limit]

        return _json(
            {
                "route": {"origin": origin, "destination": destination},
                "total": total,
                "offset": offset,
                "limit": limit,
                "has_more": offset + limit < total,
                "fares": sliced,
            }
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListAllFaresByRoute",
                "description": "List available fares for a given origin→destination route (paginated).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "origin": {"type": "string"},
                        "destination": {"type": "string"},
                        "limit": {
                            "type": "integer",
                            "minimum": 1,
                            "description": "Max items to return (default 5).",
                        },
                        "offset": {
                            "type": "integer",
                            "minimum": 0,
                            "description": "Items to skip (default 0).",
                        },
                    },
                    "required": ["origin", "destination"],
                },
            },
        }


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
        req_cabins = [c for c in cabins if c in CABINS]
        if not req_cabins:
            return _json({"error": "fare_class_not_found"})
        if price_component != "base_fare":
            return _json({"error": "invalid_price_component"})

        flights = data.get("flights", [])
        agg: dict[str, dict[str, tuple[float, str]]] = {}

        for f in flights:
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
                bucket = agg.setdefault(d, {})

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
        req_cabins = [c for c in cabins if c in CABINS]
        if not req_cabins:
            return _json({"error": "fare_class_not_found"})
        if price_component != "base_fare":
            return _json({"error": "invalid_price_component"})

        flights = data.get("flights", [])
        agg: dict[str, dict[str, tuple[float, str]]] = {}

        for f in flights:
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
                bucket = agg.setdefault(d, {})

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
        pass
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
        pass
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


class GetHistoricalTicketPrices(Tool):
    """Provide all available daily prices for a flight for the given fare_class."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        flight_number: str,
        fare_class: str,
        start_date: str | None = None,
        end_date: str | None = None,
        require_available: bool = True
    ) -> str:
        flight = _get_flight(data, flight_number)
        if not flight:
            return _json({"error": "flight_not_found"})

        out: list[dict[str, Any]] = []
        dates_map = flight.get("dates") or {}
        if not isinstance(dates_map, dict):
            return _json(
                {
                    "flight_number": flight_number,
                    "fare_class": fare_class,
                    "history": [],
                }
            )

        for d, rec in dates_map.items():
            # ISO date range safe for lexicographic ordering
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
        return _json(
            {
                "flight_number": flight_number,
                "fare_class": fare_class,
                "start_date": start_date,
                "end_date": end_date,
                "require_available": require_available,
                "history": out,
            }
        )
        pass

        flight = _get_flight(data, flight_number)
        if not flight:
            return _json({"error": "flight_not_found"})

        out: list[dict[str, Any]] = []
        dates_map = flight.get("dates") or {}
        if not isinstance(dates_map, dict):
            return _json(
                {
                    "flight_number": flight_number,
                    "fare_class": fare_class,
                    "history": [],
                }
            )

        for d, rec in dates_map.items():
            #ISO date range safe for lexicographic ordering
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
        return _json(
            {
                "flight_number": flight_number,
                "fare_class": fare_class,
                "start_date": start_date,
                "end_date": end_date,
                "require_available": require_available,
                "history": out,
            }
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetHistoricalTicketPrices",
                "description": "List daily prices for a flight and fare_class, optionally within a date window.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "fare_class": {
                            "type": "string",
                            "enum": ["basic_economy", "economy", "business"],
                        },
                        "start_date": {
                            "type": "string",
                            "description": "Inclusive YYYY-MM-DD",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "Inclusive YYYY-MM-DD",
                        },
                        "require_available": {
                            "type": "boolean",
                            "description": "Default true",
                        },
                    },
                    "required": ["flight_number", "fare_class"],
                    "additionalProperties": False,
                },
            },
        }


class GetAverageTicketPrice(Tool):
    """Calculate the average price for a flight across a date range for a fare_class."""

    @staticmethod
    def _median(vals):
        pass
        s = sorted(vals)
        n = len(s)
        if n == 0:
            return None
        mid = n // 2
        return s[mid] if n % 2 else (s[mid - 1] + s[mid]) / 2

    @staticmethod
    def _iqr_filter(vals, k=1.5):
        pass
        if len(vals) < 4:
            return vals
        s = sorted(vals)
        n = len(s)

        def q(p):
            pass
            if n == 1:
                return s[0]
            idx = (p / 100.0) * (n - 1)
            lo, hi = int(idx), min(int(idx) + 1, n - 1)
            frac = idx - lo
            return s[lo] * (1 - frac) + s[hi] * frac

        q1, q3 = q(25), q(75)
        iqr = q3 - q1
        lo, hi = q1 - k * iqr, q3 + k * iqr
        return [v for v in vals if lo <= v <= hi]

    @staticmethod
    def _collect_prices(flight, fare_class, start_date, end_date, exclude_dates):
        pass
        prices = []
        used_days = []
        for d, rec in (flight.get("dates") or {}).items():
            if not (start_date <= d <= end_date):
                continue
            if d in exclude_dates:
                continue
            if (
                _norm_status(rec.get("status")) == "available"
                and rec.get("prices")
                and fare_class in rec["prices"]
            ):
                prices.append(float(rec["prices"][fare_class]))
                used_days.append(d)
        return prices, used_days

    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        flight_number: str,
        fare_class: str,
        start_date: str,
        end_date: str,
        exclude_dates: list[str] | None = None,
        outlier_policy: dict[str, Any] | None = None,
        min_samples: int = 0,
        fallback: dict[str, Any] | None = None,
        include: dict[str, Any] | None = None,
        price_component: str = "base_fare"
    ) -> str:
        pass

        exclude_dates = set(exclude_dates or [])
        outlier_policy = outlier_policy or {}
        fallback = fallback or {}
        include = include or {}

        if price_component != "base_fare":
            return _json({"error": "invalid_price_component"})

        flight = _get_flight(data, flight_number)
        if not flight:
            return _json({"error": "flight_not_found"})

        # first iteration
        prices, used_days = GetAverageTicketPrice._collect_prices(
            flight, fare_class, start_date, end_date, exclude_dates
        )

        # optional filtering of outliers
        if outlier_policy.get("method") == "iqr":
            try:
                k = float(outlier_policy.get("k", 1.5))
            except Exception:
                k = 1.5
            prices = GetAverageTicketPrice._iqr_filter(prices, k)

        # one-time fallback expansion
        fallback_expand_window_days = fallback.get("expand_window_days", 0)
        fallback_max_expansions = fallback.get("max_expansions", 0)
        if min_samples and len(prices) < min_samples and fallback_expand_window_days > 0 and fallback_max_expansions > 0:
            try:
                exp = int(fallback_expand_window_days)
                max_exp = int(fallback_max_expansions)
            except Exception:
                exp, max_exp = 0, 0
            if exp > 0 and max_exp > 0:

                def shift(day_str, delta_days):
                    pass
                    dt = datetime.strptime(day_str, "%Y-%m-%d").date()
                    return (dt + timedelta(days=delta_days)).strftime("%Y-%m-%d")

                s2 = shift(start_date, -exp)
                e2 = shift(end_date, +exp)
                prices, used_days = GetAverageTicketPrice._collect_prices(
                    flight, fare_class, s2, e2, exclude_dates
                )
                if outlier_policy.get("method") == "iqr":
                    try:
                        k = float(outlier_policy.get("k", 1.5))
                    except Exception:
                        k = 1.5
                    prices = GetAverageTicketPrice._iqr_filter(prices, k)
                start_date, end_date = s2, e2  # document the enlarged window

        if not prices:
            return _json({"error": "no_prices_in_range"})

        avg_price = _round2(sum(prices) / len(prices))
        payload = {
            "flight_number": flight_number,
            "fare_class": fare_class,
            "start_date": start_date,
            "end_date": end_date,
            "average_price": avg_price,
        }
        if include.get("count"):
            payload["sample_size"] = len(prices)
        if include.get("median"):
            payload["median_price"] = _round2(GetAverageTicketPrice._median(prices))
        if include.get("excluded_dates"):
            payload["excluded_dates"] = sorted(list(exclude_dates))
        return _json(payload)

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetAverageTicketPrice",
                "description": (
                    "Average price over a date range with optional IQR outlier removal. "
                    "Supports optional fallback window expansion."
                ),
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
                        "exclude_dates": {"type": "array", "items": {"type": "string"}},
                        "outlier_policy": {
                            "type": "object",
                            "properties": {
                                "method": {"type": "string", "enum": ["iqr"]},
                                "k": {"type": "number"},
                            },
                        },
                        "min_samples": {"type": "integer"},
                        "fallback": {  #<- record fallback
                            "type": "object",
                            "properties": {
                                "expand_window_days": {"type": "integer"},
                                "max_expansions": {"type": "integer"},
                            },
                        },
                        "include": {
                            "type": "object",
                            "properties": {
                                "median": {"type": "boolean"},
                                "count": {"type": "boolean"},
                                "excluded_dates": {"type": "boolean"},
                            },
                        },
                        "price_component": {"type": "string", "enum": ["base_fare"]},
                    },
                    "required": [
                        "flight_number",
                        "fare_class",
                        "start_date",
                        "end_date",
                    ],
                    "additionalProperties": False,
                },
            },
        }


class GetOperationalEvents(Tool):
    """Enumerate operational events for a flight within a date range; optionally filter by types.
    Provides `excluded_dates` (unique YYYY-MM-DD) for use in pricing filters."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        start_date: str,
        end_date: str,
        flight_number: str | None = None,
        types: list[str] | None = None
    ) -> str:
        types = {_norm_status(t) for t in (types or [])}

        events_src = data.get("operational_events", [])
        out: list[dict[str, Any]] = []
        for ev in events_src:
            # be accommodating to schema: date / event_date / timestamp
            raw = ev.get("date") or ev.get("event_date") or ev.get("timestamp")
            if not raw:
                continue
            day = str(raw)[:10]  # YYYY-MM-DD also derived from ISO datetimes
            if not (start_date <= day <= end_date):
                continue
            if flight_number and ev.get("flight_number") != flight_number:
                continue
            ev_type = _norm_status(ev.get("type") or ev.get("status"))
            if types and ev_type not in types:
                continue
            out.append({"date": day, "type": ev_type, "raw": ev})

        excluded_dates = sorted({e["date"] for e in out})

        return _json(
            {"events": out, "excluded_dates": excluded_dates, "total": len(out)}
        )
        pass
        types = {_norm_status(t) for t in (types or [])}

        events_src = data.get("operational_events", [])
        out: list[dict[str, Any]] = []
        for ev in events_src:
            #be accommodating to schema: date / event_date / timestamp
            raw = ev.get("date") or ev.get("event_date") or ev.get("timestamp")
            if not raw:
                continue
            day = str(raw)[:10]  #YYYY-MM-DD also derived from ISO datetimes
            if not (start_date <= day <= end_date):
                continue
            if flight_number and ev.get("flight_number") != flight_number:
                continue
            ev_type = _norm_status(ev.get("type") or ev.get("status"))
            if types and ev_type not in types:
                continue
            out.append({"date": day, "type": ev_type, "raw": ev})

        excluded_dates = sorted({e["date"] for e in out})

        return _json(
            {"events": out, "excluded_dates": excluded_dates, "total": len(out)}
        )

    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetOperationalEvents",
                "description": "List operational events for flight/date range; returns excluded_dates and total.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"},
                        "types": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["start_date", "end_date"],
                },
            },
        }


class GetFlownRevenueForFlight(Tool):
    """
    Estimate the flown revenue for a flight over a date range, acknowledged on each leg's date.
    NOTE: The current dataset lacks taxes/fees/surcharges, thus 'total' equals 'base_fare'.
    """

    @staticmethod
    def _num(x):
        pass
        try:
            return float(x)
        except Exception:
            return None

    @staticmethod
    def _leg_amount(price_obj, price_component: str) -> float | None:
        pass

        if isinstance(price_obj, (int, float, str)):
            return GetFlownRevenueForFlight._num(price_obj)
        if isinstance(price_obj, dict):
            return GetFlownRevenueForFlight._num(price_obj.get("base_fare"))
        return None

    @staticmethod
    def _reservation_total(res, price_component: str) -> float | None:
        pass
        #Favor dictionary with base_fare; revert to scalar price if necessary
        if isinstance(res.get("price"), dict):
            return GetFlownRevenueForFlight._leg_amount(res["price"], price_component)
        if isinstance(res.get("total_price"), dict):
            return GetFlownRevenueForFlight._leg_amount(
                res["total_price"], price_component
            )
        if isinstance(res.get("price"), (int, float, str)):
            return GetFlownRevenueForFlight._num(res["price"])
        return None

    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        flight_number: str,
        start_date: str,
        end_date: str,
        price_component: str = "base_fare",  # retained for API structure; 'total' equals 'base_fare' in the current dataset
        require_available: bool = True,
        include_details: bool = False
    ) -> str:
        pass
        price_component = (price_component or "base_fare").lower()
        if price_component not in ("base_fare", "total"):
            return _json({"error": "invalid_price_component"})

        reservations = data.get("reservations", [])
        flights = data.get("flights", [])

        flight_date_status = {}
        if require_available:
            for f in flights if isinstance(flights, list) else []:
                if f.get("flight_number") == flight_number:
                    for d, rec in (f.get("dates") or {}).items():
                        flight_date_status[(flight_number, d)] = _norm_status(
                            (rec or {}).get("status")
                        )

        def operated(day: str) -> bool:
            pass
            return (not require_available) or (
                flight_date_status.get((flight_number, day)) == "available"
            )

        total = 0.0
        legs_recognized = 0
        reservations_scanned = 0
        details: list[dict[str, Any]] = []

        if isinstance(reservations, list):
            for res in reservations:
                reservations_scanned += 1
                legs = res.get("flights") or res.get("legs") or []
                if not legs:
                    continue

                # Attempt per-leg pricing initially
                leg_amts: list[float | None] = []
                has_leg_prices = False
                for leg in legs:
                    amt = GetFlownRevenueForFlight._leg_amount(
                        leg.get("price"), price_component
                    )
                    if amt is not None:
                        has_leg_prices = True
                    leg_amts.append(amt)

                # If leg prices are absent, divide reservation base_fare evenly
                if not has_leg_prices:
                    res_total = GetFlownRevenueForFlight._reservation_total(
                        res, price_component
                    )
                    if res_total is not None and len(legs) > 0:
                        equal_share = res_total / len(legs)
                        leg_amts = [equal_share for _ in legs]

                # Identify per corresponding leg/date
                for i, leg in enumerate(legs):
                    if leg.get("flight_number") != flight_number:
                        continue
                    day = str(leg.get("date") or "")[:10]
                    if not (start_date <= day <= end_date):
                        continue
                    if not operated(day):
                        continue

                    amt = leg_amts[i] if i < len(leg_amts) else None
                    if amt is None:
                        continue
                    amt = round(float(amt), 2)
                    total += amt
                    legs_recognized += 1
                    if include_details:
                        details.append(
                            {
                                "reservation_id": res.get("reservation_id")
                                or res.get("id"),
                                "flight_number": flight_number,
                                "date": day,
                                "amount": amt,
                            }
                        )

        payload: dict[str, Any] = {
            "flight_number": flight_number,
            "start_date": start_date,
            "end_date": end_date,
            "price_component": price_component,  # retained for compatibility
            "require_available": require_available,
            "reservations_scanned": reservations_scanned,
            "legs_recognized": legs_recognized,
            "recognized_revenue": round(total, 2),
        }
        if include_details:
            payload["details"] = details
        return _json(payload)
        pass
        price_component = (price_component or "base_fare").lower()
        if price_component not in ("base_fare", "total"):
            return _json({"error": "invalid_price_component"})

        reservations = data.get("reservations", [])
        flights = data.get("flights", [])

        flight_date_status = {}
        if require_available:
            for f in flights if isinstance(flights, list) else []:
                if f.get("flight_number") == flight_number:
                    for d, rec in (f.get("dates") or {}).items():
                        flight_date_status[(flight_number, d)] = _norm_status(
                            (rec or {}).get("status")
                        )

        def operated(day: str) -> bool:
            pass
            return (not require_available) or (
                flight_date_status.get((flight_number, day)) == "available"
            )

        total = 0.0
        legs_recognized = 0
        reservations_scanned = 0
        details: list[dict[str, Any]] = []

        if isinstance(reservations, list):
            for res in reservations:
                reservations_scanned += 1
                legs = res.get("flights") or res.get("legs") or []
                if not legs:
                    continue

                #Attempt per-leg pricing initially
                leg_amts: list[float | None] = []
                has_leg_prices = False
                for leg in legs:
                    amt = GetFlownRevenueForFlight._leg_amount(
                        leg.get("price"), price_component
                    )
                    if amt is not None:
                        has_leg_prices = True
                    leg_amts.append(amt)

                #If leg prices are absent, divide reservation base_fare evenly
                if not has_leg_prices:
                    res_total = GetFlownRevenueForFlight._reservation_total(
                        res, price_component
                    )
                    if res_total is not None and len(legs) > 0:
                        equal_share = res_total / len(legs)
                        leg_amts = [equal_share for _ in legs]

                #Identify per corresponding leg/date
                for i, leg in enumerate(legs):
                    if leg.get("flight_number") != flight_number:
                        continue
                    day = str(leg.get("date") or "")[:10]
                    if not (start_date <= day <= end_date):
                        continue
                    if not operated(day):
                        continue

                    amt = leg_amts[i] if i < len(leg_amts) else None
                    if amt is None:
                        continue
                    amt = round(float(amt), 2)
                    total += amt
                    legs_recognized += 1
                    if include_details:
                        details.append(
                            {
                                "reservation_id": res.get("reservation_id")
                                or res.get("id"),
                                "flight_number": flight_number,
                                "date": day,
                                "amount": amt,
                            }
                        )

        payload: dict[str, Any] = {
            "flight_number": flight_number,
            "start_date": start_date,
            "end_date": end_date,
            "price_component": price_component,  #retained for compatibility
            "require_available": require_available,
            "reservations_scanned": reservations_scanned,
            "legs_recognized": legs_recognized,
            "recognized_revenue": round(total, 2),
        }
        if include_details:
            payload["details"] = details
        return _json(payload)

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetFlownRevenueForFlight",
                "description": "Approximate flown revenue using base_fare only (dataset has no taxes/fees).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"},
                        "price_component": {
                            "type": "string",
                            "enum": ["base_fare", "total"],
                            "description": "Kept for compatibility; 'total' == 'base_fare' in current data.",
                        },
                        "require_available": {"type": "boolean"},
                        "include_details": {"type": "boolean"},
                    },
                    "required": ["flight_number", "start_date", "end_date"],
                },
            },
        }


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


class GetFlightStatusByDate(Tool):
    """Provide the status for a particular flight/date."""

    @staticmethod
    def invoke(data: dict[str, Any], flight_number: str, date: str) -> str:
        f = _get_flight(data, flight_number)
        if not f:
            return _json({"error": "flight_not_found"})
        rec = _get_date_record(f, date)
        if not rec:
            return _json({"error": "price_not_available_for_date"})
        return _json(
            {
                "flight_number": flight_number,
                "date": date,
                "flight_status": _norm_status(rec.get("status")),
            }
        )
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetFlightStatusByDate",
                "description": "Status for a flight on a given date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "date": {"type": "string"},
                    },
                    "required": ["flight_number", "date"],
                },
            },
        }


class GetAircraftByTailNumber(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], tail_number: str) -> str:
        aircraft_list = data.get("aircraft", [])
        for aircraft in aircraft_list:
            if aircraft.get("tail_number") == tail_number:
                #standardize status casing prior to returning
                out = dict(aircraft)
                if "status" in out:
                    out["status"] = _norm_status(out.get("status"))
                return _json(out)
        return _json({"error": "Aircraft not found", "tail_number": tail_number})
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetAircraftByTailNumber",
                "description": "Retrieves the full details of an aircraft using its unique tail number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tail_number": {
                            "type": "string",
                            "description": "The unique tail number of the aircraft (e.g., 'G-ZNKH').",
                        }
                    },
                    "required": ["tail_number"],
                },
            },
        }


class GetAvailableSeat(Tool):
    """Provide the available seats for a cabin on a flight/date (accesses available_seats[cabin])."""

    @staticmethod
    def invoke(
        data: dict[str, Any], flight_number: str, date: str, cabin: str
    ) -> str:
        f = _get_flight(data, flight_number)
        if not f:
            return _json({"error": "flight_not_found"})
        rec = _get_date_record(f, date)
        if not rec or _norm_status(rec.get("status")) != "available":
            return _json({"error": "price_not_available_for_date"})
        seats = (rec.get("available_seats") or {}).get(cabin)
        if seats is None:
            return _json({"error": "fare_class_not_found"})
        return _json(
            {
                "flight_number": flight_number,
                "date": date,
                "cabin": cabin,
                "available_seats": seats,
            }
        )
        pass
        f = _get_flight(data, flight_number)
        if not f:
            return _json({"error": "flight_not_found"})
        rec = _get_date_record(f, date)
        if not rec or _norm_status(rec.get("status")) != "available":
            return _json({"error": "price_not_available_for_date"})
        seats = (rec.get("available_seats") or {}).get(cabin)
        if seats is None:
            return _json({"error": "fare_class_not_found"})
        return _json(
            {
                "flight_number": flight_number,
                "date": date,
                "cabin": cabin,
                "available_seats": seats,
            }
        )

    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetAvailableSeat",
                "description": "Available seats for a cabin on a flight/date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "date": {"type": "string"},
                        "cabin": {
                            "type": "string",
                            "enum": ["basic_economy", "economy", "business"],
                        },
                    },
                    "required": ["flight_number", "date", "cabin"],
                },
            },
        }


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


class AdjustSeasonalPricing(Tool):
    """
    Predictable write: multiply prices in [start_date,end_date] by a constant multiplier,
    rounding to 2 decimal places. Optionally limit to one fare_class. Returns a preview of the first N changes.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        flight_number: str,
        start_date: str,
        end_date: str,
        multiplier: float = 1.0,
        max_preview: int = 0,
        fare_class: str | None = None
    ) -> str:
        # check dates for validity
        try:
            sd = date.fromisoformat(start_date)
            ed = date.fromisoformat(end_date)
        except Exception:
            return _json({"error": "invalid_date_format"})
        if sd > ed:
            return _json(
                {
                    "error": "invalid_date_range",
                    "start_date": start_date,
                    "end_date": end_date,
                }
            )

        # standardize cabin filter
        fare_class = (fare_class or "").strip().lower() or None

        f = _get_flight(data, flight_number)
        if not f:
            return _json({"error": "flight_not_found"})

        mult_dec = Decimal(str(multiplier))
        preview: list[dict[str, Any]] = []

        # loop in a deterministic manner by date
        for d in sorted((f.get("dates") or {}).keys()):
            if not (start_date <= d <= end_date):
                continue
            rec = (f.get("dates") or {}).get(d) or {}
            prices = rec.get("prices")
            if not isinstance(prices, dict):
                continue

            # select cabins for updating
            cabins = [fare_class] if fare_class else list(prices.keys())

            for cab in cabins:
                if cab not in prices:
                    continue
                try:
                    base = Decimal(str(prices[cab]))
                except Exception:
                    continue

                # predictable rounding half-up to 2 decimal places
                newp = float(
                    (base * mult_dec).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
                )
                oldp = float(base.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))

                if newp != oldp:
                    rec["prices"][cab] = newp
                    if len(preview) < max_preview:
                        preview.append(
                            {"date": d, "cabin": cab, "old": oldp, "new": newp}
                        )

        return _json(
            {
                "success": True,
                "flight_number": flight_number,
                "start_date": start_date,
                "end_date": end_date,
                "multiplier": float(mult_dec),
                "fare_class": fare_class,
                "preview": preview,
            }
        )
        pass
        #check dates for validity
        try:
            sd = date.fromisoformat(start_date)
            ed = date.fromisoformat(end_date)
        except Exception:
            return _json({"error": "invalid_date_format"})
        if sd > ed:
            return _json(
                {
                    "error": "invalid_date_range",
                    "start_date": start_date,
                    "end_date": end_date,
                }
            )

        #standardize cabin filter
        fare_class = (fare_class or "").strip().lower() or None

        f = _get_flight(data, flight_number)
        if not f:
            return _json({"error": "flight_not_found"})

        mult_dec = Decimal(str(multiplier))
        preview: list[dict[str, Any]] = []

        #loop in a deterministic manner by date
        for d in sorted((f.get("dates") or {}).keys()):
            if not (start_date <= d <= end_date):
                continue
            rec = (f.get("dates") or {}).get(d) or {}
            prices = rec.get("prices")
            if not isinstance(prices, dict):
                continue

            #select cabins for updating
            cabins = [fare_class] if fare_class else list(prices.keys())

            for cab in cabins:
                if cab not in prices:
                    continue
                try:
                    base = Decimal(str(prices[cab]))
                except Exception:
                    continue

                #predictable rounding half-up to 2 decimal places
                newp = float(
                    (base * mult_dec).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
                )
                oldp = float(base.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))

                if newp != oldp:
                    rec["prices"][cab] = newp
                    if len(preview) < max_preview:
                        preview.append(
                            {"date": d, "cabin": cab, "old": oldp, "new": newp}
                        )

        return _json(
            {
                "success": True,
                "flight_number": flight_number,
                "start_date": start_date,
                "end_date": end_date,
                "multiplier": float(mult_dec),
                "fare_class": fare_class,
                "preview": preview,
            }
        )

    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "AdjustSeasonalPricing",
                "description": "Deterministically scale prices over a window; optionally only a single fare_class.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"},
                        "multiplier": {"type": "number"},
                        "max_preview": {"type": "integer"},
                        "fare_class": {
                            "type": "string",
                            "enum": ["basic_economy", "economy", "business"],
                        },
                    },
                    "required": [
                        "flight_number",
                        "start_date",
                        "end_date",
                        "multiplier",
                    ],
                    "additionalProperties": False,
                },
            },
        }


class SetTicketPrice(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        flight_number: str,
        date: str,
        fare_class: str,
        price: float,
        require_available: bool = False
    ) -> str:
        flights = data.get("flights", [])
        if isinstance(flights, dict):
            f = flights.get(flight_number)
        elif isinstance(flights, list):
            f = next(
                (row for row in flights if row.get("flight_number") == flight_number),
                None,
            )
        else:
            f = None

        if not f:
            return _json({"error": "flight_not_found", "flight_number": flight_number})

        d = f.get("dates", {}).get(date) if isinstance(f.get("dates"), dict) else None
        if not d:
            return _json({"error": "date_not_found", "date": date})

        #standardize status and enforce if necessary
        status = _norm_status(d.get("status"))
        if require_available and status != "available":
            return _json(
                {
                    "error": "invalid_status",
                    "reason": f"Flight {flight_number} on {date} has status '{status}', "
                    f"cannot set ticket price unless 'available'.",
                }
            )

        inv = d.setdefault("inventory", {}).setdefault(fare_class, {})
        inv["price"] = float(price)

        return _json(
            {
                "success": True,
                "flight_number": flight_number,
                "date": date,
                "fare_class": fare_class,
                "price": inv["price"],
                "status": status,
            }
        )
        pass
        flights = data.get("flights", [])
        if isinstance(flights, dict):
            f = flights.get(flight_number)
        elif isinstance(flights, list):
            f = next(
                (row for row in flights if row.get("flight_number") == flight_number),
                None,
            )
        else:
            f = None

        if not f:
            return _json({"error": "flight_not_found", "flight_number": flight_number})

        d = f.get("dates", {}).get(date) if isinstance(f.get("dates"), dict) else None
        if not d:
            return _json({"error": "date_not_found", "date": date})

        #standardize status and enforce if necessary
        status = _norm_status(d.get("status"))
        if require_available and status != "available":
            return _json(
                {
                    "error": "invalid_status",
                    "reason": f"Flight {flight_number} on {date} has status '{status}', "
                    f"cannot set ticket price unless 'available'.",
                }
            )

        inv = d.setdefault("inventory", {}).setdefault(fare_class, {})
        inv["price"] = float(price)

        return _json(
            {
                "success": True,
                "flight_number": flight_number,
                "date": date,
                "fare_class": fare_class,
                "price": inv["price"],
                "status": status,
            }
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "SetTicketPrice",
                "description": "Set the ticket price for a given fare_class on a flight date. "
                "Optionally enforce that the flight must be 'available'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "date": {"type": "string", "description": "YYYY-MM-DD"},
                        "fare_class": {"type": "string"},
                        "price": {"type": "number"},
                        "require_available": {
                            "type": "boolean",
                            "description": "If true, only allow when status=='available'. Default false.",
                        },
                    },
                    "required": ["flight_number", "date", "fare_class", "price"],
                },
            },
        }


class ApplyDiscountToFlight(Tool):
    """Implement a percentage discount on a flight/date/fare_class (modifies price directly).
    Additionally, logs a predictable audit record to data["price_changes"] with a sequential id (no timestamps).
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        flight_number: str,
        fare_class: str,
        date: str,
        percent: float
    ) -> str:
        # percentage parsing and verification
        try:
            percent = float(percent)
        except Exception:
            return _json({"error": "invalid_percent"})

        if percent < 0 or percent > 100:
            return _json({"error": "invalid_percent"})

        flight = _get_flight(data, flight_number)
        if not flight:
            return _json({"error": "flight_not_found"})

        rec = _get_date_record(flight, date)
        if not rec or _norm_status(rec.get("status")) != "available":
            return _json({"error": "price_not_available_for_date"})

        prices = rec.get("prices")
        if not isinstance(prices, dict):
            return _json({"error": "fare_class_not_found"})

        if fare_class not in prices:
            return _json({"error": "fare_class_not_found"})

        try:
            old_price = float(prices[fare_class])
        except Exception:
            return _json({"error": "fare_class_not_found"})

        # apply discount to BASE FARE; leave taxes/fees unchanged
        new_price = round(old_price * (1 - percent / 100.0), 2)
        if new_price < 0:
            new_price = 0.0

        prices[fare_class] = new_price

        # --- predictable audit record (NO timestamp) ---
        change_id = _next_change_id(data, prefix="PC")
        (data.setdefault("price_changes", [])).append(
            {
                "id": change_id,
                "type": "discount",
                "flight_number": flight_number,
                "date": date,
                "fare_class": fare_class,
                "old": round(old_price, 2),
                "new": new_price,
                # no timestamp to ensure determinism as per policy
            }
        )

        return _json(
            {
                "success": True,
                "audit_id": change_id,
                "flight_number": flight_number,
                "date": date,
                "fare_class": fare_class,
                "discount_percent": percent,
                "old_price": round(old_price, 2),
                "new_price": new_price,
            }
        )
        pass
        #percentage parsing and verification
        try:
            percent = float(percent)
        except Exception:
            return _json({"error": "invalid_percent"})

        if percent < 0 or percent > 100:
            return _json({"error": "invalid_percent"})

        flight = _get_flight(data, flight_number)
        if not flight:
            return _json({"error": "flight_not_found"})

        rec = _get_date_record(flight, date)
        if not rec or _norm_status(rec.get("status")) != "available":
            return _json({"error": "price_not_available_for_date"})

        prices = rec.get("prices")
        if not isinstance(prices, dict):
            return _json({"error": "fare_class_not_found"})

        if fare_class not in prices:
            return _json({"error": "fare_class_not_found"})

        try:
            old_price = float(prices[fare_class])
        except Exception:
            return _json({"error": "fare_class_not_found"})

        #apply discount to BASE FARE; leave taxes/fees unchanged
        new_price = round(old_price * (1 - percent / 100.0), 2)
        if new_price < 0:
            new_price = 0.0

        prices[fare_class] = new_price

        #--- predictable audit record (NO timestamp) ---
        change_id = _next_change_id(data, prefix="PC")
        (data.setdefault("price_changes", [])).append(
            {
                "id": change_id,
                "type": "discount",
                "flight_number": flight_number,
                "date": date,
                "fare_class": fare_class,
                "old": round(old_price, 2),
                "new": new_price,
                #no timestamp to ensure determinism as per policy
            }
        )

        return _json(
            {
                "success": True,
                "audit_id": change_id,
                "flight_number": flight_number,
                "date": date,
                "fare_class": fare_class,
                "discount_percent": percent,
                "old_price": round(old_price, 2),
                "new_price": new_price,
            }
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "ApplyDiscountToFlight",
                "description": (
                    "Apply a percent discount to the BASE FARE for a given flight/date/fare_class. "
                    "Creates an audit record in data['price_changes'] and returns its audit_id."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "date": {"type": "string"},
                        "fare_class": {
                            "type": "string",
                            "enum": ["basic_economy", "economy", "business"],
                        },
                        "percent": {"type": "number"},
                    },
                    "required": ["flight_number", "date", "fare_class", "percent"],
                },
            },
        }


class RemoveDiscountFromFlight(Tool):
    """
    Undo a discount applied to a flight/date/fare_class.

    Order of strategies:
      1) Revert based on audit (preferred)
      2) Revert to specified 'original_price'
      3) Revert to 'percent' inversion
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        flight_number: str,
        date: str,
        fare_class: str,
        discount_id: str | None = None,
        original_price: float | None = None,
        percent: float | None = None,
        strict: bool = False
    ) -> str:
        pass
        fare_class_req = (fare_class or "").lower().strip()

        flight = _get_flight(data, flight_number)
        if not flight:
            return _json({"error": "flight_not_found"})

        rec = _get_date_record(flight, date)
        if not rec or _norm_status(rec.get("status")) != "available":
            return _json({"error": "price_not_available_for_date"})

        prices = rec.get("prices") or {}
        if not isinstance(prices, dict) or fare_class_req not in prices:
            return _json({"error": "fare_class_not_found"})

        resolved_cabin = fare_class_req
        override_used = False

        #--- Approach 1: revert based on audit ---
        audits = [
            a
            for a in data.get("price_changes", [])
            if isinstance(a, dict) and a.get("type") == "discount"
        ]

        def id_seq(aid: str) -> int:
            pass
            try:
                return int(str(aid)[2:])
            except Exception:
                return -1

        def match_base(a):
            pass
            return a.get("flight_number") == flight_number and a.get("date") == date

        audit_row = None
        if discount_id:
            audit_row = next(
                (a for a in audits if a.get("id") == discount_id and match_base(a)),
                None,
            )
            if not audit_row and strict:
                return _json({"error": "discount_not_found"})
        else:
            candidates = [
                a
                for a in audits
                if match_base(a) and a.get("fare_class") == resolved_cabin
            ] or [a for a in audits if match_base(a)]
            candidates.sort(key=lambda x: id_seq(x.get("id")), reverse=True)
            audit_row = candidates[0] if candidates else None

        if audit_row:
            audit_cab = (audit_row.get("fare_class") or "").lower().strip()
            if audit_cab and audit_cab != resolved_cabin:
                if strict:
                    return _json(
                        {
                            "error": "fare_class_mismatch",
                            "expected": audit_cab,
                            "provided": resolved_cabin,
                        }
                    )
                resolved_cabin = audit_cab
                override_used = True

            if resolved_cabin not in prices:
                return _json({"error": "fare_class_not_found"})

            try:
                current_f = float(prices[resolved_cabin])
                old_f = float(audit_row.get("old"))
                new_f = float(audit_row.get("new"))
            except Exception:
                if strict:
                    return _json({"error": "discount_not_found"})
                audit_row = None
            else:
                if strict and round(current_f, 2) != round(new_f, 2):
                    return _json(
                        {
                            "error": "price_mismatch",
                            "expected_current": round(new_f, 2),
                            "found_current": round(current_f, 2),
                        }
                    )
                prices[resolved_cabin] = round(old_f, 2)
                revert_id = _next_change_id(data, prefix="PC")
                (data.setdefault("price_changes", [])).append(
                    {
                        "id": revert_id,
                        "type": "revert_discount",
                        "flight_number": flight_number,
                        "date": date,
                        "fare_class": resolved_cabin,
                        "old": round(current_f, 2),
                        "new": round(old_f, 2),
                        "reverts_audit_id": audit_row.get("id"),
                    }
                )
                return _json(
                    {
                        "success": True,
                        "strategy": "audit",
                        "audit_id": revert_id,
                        "reverted_from_audit": True,
                        "discount_id_used": audit_row.get("id"),
                        "flight_number": flight_number,
                        "date": date,
                        "fare_class": resolved_cabin,
                        "fare_class_overridden_from_audit": override_used or None,
                        "previous_price": round(current_f, 2),
                        "restored_price": round(old_f, 2),
                    }
                )

        #--- Approach 2: specific original_price ---
        if original_price is not None:
            try:
                orig_f = round(float(original_price), 2)
            except Exception:
                return _json({"error": "invalid_original_price"})
            try:
                current_f = round(float(prices[resolved_cabin]), 2)
            except Exception:
                return _json({"error": "fare_class_not_found"})

            prices[resolved_cabin] = orig_f
            revert_id = _next_change_id(data, prefix="PC")
            (data.setdefault("price_changes", [])).append(
                {
                    "id": revert_id,
                    "type": "revert_discount",
                    "flight_number": flight_number,
                    "date": date,
                    "fare_class": resolved_cabin,
                    "old": current_f,
                    "new": orig_f,
                    "reverts_audit_id": discount_id,
                }
            )
            return _json(
                {
                    "success": True,
                    "strategy": "original_price",
                    "audit_id": revert_id,
                    "reverted_from_audit": False,
                    "discount_id_used": discount_id,
                    "flight_number": flight_number,
                    "date": date,
                    "fare_class": resolved_cabin,
                    "previous_price": current_f,
                    "restored_price": orig_f,
                }
            )

        #--- Approach 3: reverse by percentage ---
        if percent is not None:
            try:
                pct = float(percent)
            except Exception:
                return _json({"error": "invalid_percent"})
            if pct <= 0 or pct > 100:
                return _json({"error": "invalid_percent"})

            try:
                current_f = float(prices[resolved_cabin])
            except Exception:
                return _json({"error": "fare_class_not_found"})

            denom = 1 - pct / 100.0
            if denom <= 0:
                return _json({"error": "invalid_percent"})
            restored = round(current_f / denom, 2)

            prices[resolved_cabin] = restored
            revert_id = _next_change_id(data, prefix="PC")
            (data.setdefault("price_changes", [])).append(
                {
                    "id": revert_id,
                    "type": "revert_discount",
                    "flight_number": flight_number,
                    "date": date,
                    "fare_class": resolved_cabin,
                    "old": round(current_f, 2),
                    "new": restored,
                    "reverts_percent": pct,
                    "reverts_audit_id": discount_id,
                }
            )
            return _json(
                {
                    "success": True,
                    "strategy": "percent",
                    "audit_id": revert_id,
                    "reverted_from_audit": False,
                    "discount_id_used": discount_id,
                    "flight_number": flight_number,
                    "date": date,
                    "fare_class": resolved_cabin,
                    "previous_price": round(current_f, 2),
                    "restored_price": restored,
                }
            )

        #No valid audit and no fallback data
        return _json(
            {
                "error": "missing_params",
                "reason": "Provide discount_id (preferred) or original_price/percent.",
            }
        )
        pass
        fare_class_req = (fare_class or "").lower().strip()

        flight = _get_flight(data, flight_number)
        if not flight:
            return _json({"error": "flight_not_found"})

        rec = _get_date_record(flight, date)
        if not rec or _norm_status(rec.get("status")) != "available":
            return _json({"error": "price_not_available_for_date"})

        prices = rec.get("prices") or {}
        if not isinstance(prices, dict) or fare_class_req not in prices:
            return _json({"error": "fare_class_not_found"})

        resolved_cabin = fare_class_req
        override_used = False

        #--- Approach 1: revert based on audit ---
        audits = [
            a
            for a in data.get("price_changes", [])
            if isinstance(a, dict) and a.get("type") == "discount"
        ]

        def id_seq(aid: str) -> int:
            pass
            try:
                return int(str(aid)[2:])
            except Exception:
                return -1

        def match_base(a):
            pass
            return a.get("flight_number") == flight_number and a.get("date") == date

        audit_row = None
        if discount_id:
            audit_row = next(
                (a for a in audits if a.get("id") == discount_id and match_base(a)),
                None,
            )
            if not audit_row and strict:
                return _json({"error": "discount_not_found"})
        else:
            candidates = [
                a
                for a in audits
                if match_base(a) and a.get("fare_class") == resolved_cabin
            ] or [a for a in audits if match_base(a)]
            candidates.sort(key=lambda x: id_seq(x.get("id")), reverse=True)
            audit_row = candidates[0] if candidates else None

        if audit_row:
            audit_cab = (audit_row.get("fare_class") or "").lower().strip()
            if audit_cab and audit_cab != resolved_cabin:
                if strict:
                    return _json(
                        {
                            "error": "fare_class_mismatch",
                            "expected": audit_cab,
                            "provided": resolved_cabin,
                        }
                    )
                resolved_cabin = audit_cab
                override_used = True

            if resolved_cabin not in prices:
                return _json({"error": "fare_class_not_found"})

            try:
                current_f = float(prices[resolved_cabin])
                old_f = float(audit_row.get("old"))
                new_f = float(audit_row.get("new"))
            except Exception:
                if strict:
                    return _json({"error": "discount_not_found"})
                audit_row = None
            else:
                if strict and round(current_f, 2) != round(new_f, 2):
                    return _json(
                        {
                            "error": "price_mismatch",
                            "expected_current": round(new_f, 2),
                            "found_current": round(current_f, 2),
                        }
                    )
                prices[resolved_cabin] = round(old_f, 2)
                revert_id = _next_change_id(data, prefix="PC")
                (data.setdefault("price_changes", [])).append(
                    {
                        "id": revert_id,
                        "type": "revert_discount",
                        "flight_number": flight_number,
                        "date": date,
                        "fare_class": resolved_cabin,
                        "old": round(current_f, 2),
                        "new": round(old_f, 2),
                        "reverts_audit_id": audit_row.get("id"),
                    }
                )
                return _json(
                    {
                        "success": True,
                        "strategy": "audit",
                        "audit_id": revert_id,
                        "reverted_from_audit": True,
                        "discount_id_used": audit_row.get("id"),
                        "flight_number": flight_number,
                        "date": date,
                        "fare_class": resolved_cabin,
                        "fare_class_overridden_from_audit": override_used or None,
                        "previous_price": round(current_f, 2),
                        "restored_price": round(old_f, 2),
                    }
                )

        #--- Approach 2: specific original_price ---
        if original_price is not None:
            try:
                orig_f = round(float(original_price), 2)
            except Exception:
                return _json({"error": "invalid_original_price"})
            try:
                current_f = round(float(prices[resolved_cabin]), 2)
            except Exception:
                return _json({"error": "fare_class_not_found"})

            prices[resolved_cabin] = orig_f
            revert_id = _next_change_id(data, prefix="PC")
            (data.setdefault("price_changes", [])).append(
                {
                    "id": revert_id,
                    "type": "revert_discount",
                    "flight_number": flight_number,
                    "date": date,
                    "fare_class": resolved_cabin,
                    "old": current_f,
                    "new": orig_f,
                    "reverts_audit_id": discount_id,
                }
            )
            return _json(
                {
                    "success": True,
                    "strategy": "original_price",
                    "audit_id": revert_id,
                    "reverted_from_audit": False,
                    "discount_id_used": discount_id,
                    "flight_number": flight_number,
                    "date": date,
                    "fare_class": resolved_cabin,
                    "previous_price": current_f,
                    "restored_price": orig_f,
                }
            )

        #--- Approach 3: reverse by percentage ---
        if percent is not None:
            try:
                pct = float(percent)
            except Exception:
                return _json({"error": "invalid_percent"})
            if pct <= 0 or pct > 100:
                return _json({"error": "invalid_percent"})

            try:
                current_f = float(prices[resolved_cabin])
            except Exception:
                return _json({"error": "fare_class_not_found"})

            denom = 1 - pct / 100.0
            if denom <= 0:
                return _json({"error": "invalid_percent"})
            restored = round(current_f / denom, 2)

            prices[resolved_cabin] = restored
            revert_id = _next_change_id(data, prefix="PC")
            (data.setdefault("price_changes", [])).append(
                {
                    "id": revert_id,
                    "type": "revert_discount",
                    "flight_number": flight_number,
                    "date": date,
                    "fare_class": resolved_cabin,
                    "old": round(current_f, 2),
                    "new": restored,
                    "reverts_percent": pct,
                    "reverts_audit_id": discount_id,
                }
            )
            return _json(
                {
                    "success": True,
                    "strategy": "percent",
                    "audit_id": revert_id,
                    "reverted_from_audit": False,
                    "discount_id_used": discount_id,
                    "flight_number": flight_number,
                    "date": date,
                    "fare_class": resolved_cabin,
                    "previous_price": round(current_f, 2),
                    "restored_price": restored,
                }
            )

        #No valid audit and no fallback data
        return _json(
            {
                "error": "missing_params",
                "reason": "Provide discount_id (preferred) or original_price/percent.",
            }
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "RemoveDiscountFromFlight",
                "description": "Revert a discount; prefer audit, else original_price, else percent.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "date": {"type": "string"},
                        "fare_class": {
                            "type": "string",
                            "enum": ["basic_economy", "economy", "business"],
                        },
                        "discount_id": {"type": "string"},
                        "original_price": {"type": "number"},
                        "percent": {"type": "number"},
                        "strict": {"type": "boolean"},
                    },
                    "required": ["flight_number", "date", "fare_class"],
                    "additionalProperties": False,
                },
            },
        }


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
        pass
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


class BulkUpgradeTicketPrices(Tool):
    """
    Establish upgrade as no-charge by transferring from_cabin price to to_cabin across a date range
    for a specified flight. Only dates with status == 'available' will be modified.
    Predictable (no randomness). Returns counts and a preview of the first N changes.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        flight_number: str,
        start_date: str,
        end_date: str,
        from_cabin: str,
        to_cabin: str,
        max_preview: int = 0,
        no_charge: bool | None = None,
        # Optional: ensure that only no-charge upgrades are permitted
    ) -> str:
        if no_charge is not None and no_charge is False:
            return _json(
                {
                    "error": "unsupported_mode",
                    "reason": "Only no-charge upgrades are supported",
                }
            )

        # Check dates (ISO) and the order of the window
        try:
            sd = date.fromisoformat(start_date)
            ed = date.fromisoformat(end_date)
        except Exception:
            return _json({"error": "invalid_date_format"})
        if sd > ed:
            return _json(
                {
                    "error": "invalid_date_range",
                    "start_date": start_date,
                    "end_date": end_date,
                }
            )

        # Standardize cabins
        from_cabin = (from_cabin or "").strip().lower()
        to_cabin = (to_cabin or "").strip().lower()
        if from_cabin == to_cabin:
            return _json(
                {
                    "error": "invalid_cabins",
                    "reason": "from_cabin and to_cabin must differ",
                }
            )

        f = _get_flight(data, flight_number)
        if not f:
            return _json({"error": "flight_not_found"})

        changed = 0
        preview: list[dict[str, Any]] = []

        # Loop in a predictable manner
        for d in sorted((f.get("dates") or {}).keys()):
            if not (start_date <= d <= end_date):
                continue
            rec = (f.get("dates") or {}).get(d) or {}
            if _norm_status(rec.get("status")) != "available":
                continue
            prices = rec.get("prices") or {}
            if from_cabin not in prices or to_cabin not in prices:
                continue
            try:
                src = round(float(prices[from_cabin]), 2)
                dst = round(float(prices[to_cabin]), 2)
            except Exception:
                continue
            if dst != src:
                rec["prices"][to_cabin] = src
                changed += 1
                if len(preview) < max_preview:
                    preview.append(
                        {
                            "date": d,
                            "from_cabin": from_cabin,
                            "to_cabin": to_cabin,
                            "old_to_cabin": dst,
                            "new_to_cabin": src,
                        }
                    )

        return _json(
            {
                "success": True,
                "flight_number": flight_number,
                "start_date": start_date,
                "end_date": end_date,
                "from_cabin": from_cabin,
                "to_cabin": to_cabin,
                "changed": changed,
                "preview": preview,
            }
        )
        pass
        #Optional: ensure that only no-charge upgrades are permitted
        if no_charge is not None and no_charge is False:
            return _json(
                {
                    "error": "unsupported_mode",
                    "reason": "Only no-charge upgrades are supported",
                }
            )

        #Check dates (ISO) and the order of the window
        try:
            sd = date.fromisoformat(start_date)
            ed = date.fromisoformat(end_date)
        except Exception:
            return _json({"error": "invalid_date_format"})
        if sd > ed:
            return _json(
                {
                    "error": "invalid_date_range",
                    "start_date": start_date,
                    "end_date": end_date,
                }
            )

        #Standardize cabins
        from_cabin = (from_cabin or "").strip().lower()
        to_cabin = (to_cabin or "").strip().lower()
        if from_cabin == to_cabin:
            return _json(
                {
                    "error": "invalid_cabins",
                    "reason": "from_cabin and to_cabin must differ",
                }
            )

        f = _get_flight(data, flight_number)
        if not f:
            return _json({"error": "flight_not_found"})

        changed = 0
        preview: list[dict[str, Any]] = []

        #Loop in a predictable manner
        for d in sorted((f.get("dates") or {}).keys()):
            if not (start_date <= d <= end_date):
                continue
            rec = (f.get("dates") or {}).get(d) or {}
            if _norm_status(rec.get("status")) != "available":
                continue
            prices = rec.get("prices") or {}
            if from_cabin not in prices or to_cabin not in prices:
                continue
            try:
                src = round(float(prices[from_cabin]), 2)
                dst = round(float(prices[to_cabin]), 2)
            except Exception:
                continue
            if dst != src:
                rec["prices"][to_cabin] = src
                changed += 1
                if len(preview) < max_preview:
                    preview.append(
                        {
                            "date": d,
                            "from_cabin": from_cabin,
                            "to_cabin": to_cabin,
                            "old_to_cabin": dst,
                            "new_to_cabin": src,
                        }
                    )

        return _json(
            {
                "success": True,
                "flight_number": flight_number,
                "start_date": start_date,
                "end_date": end_date,
                "from_cabin": from_cabin,
                "to_cabin": to_cabin,
                "changed": changed,
                "preview": preview,
            }
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "BulkUpgradeTicketPrices",
                "description": "Copy from_cabin price to to_cabin (no-charge upgrades) for a flight over a date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"},
                        "from_cabin": {
                            "type": "string",
                            "enum": ["basic_economy", "economy", "business"],
                        },
                        "to_cabin": {
                            "type": "string",
                            "enum": ["basic_economy", "economy", "business"],
                        },
                        "max_preview": {"type": "integer"},
                        "no_charge": {
                            "type": "boolean",
                            "description": "If false, returns error (tool only supports free upgrades).",
                        },
                    },
                    "required": [
                        "flight_number",
                        "start_date",
                        "end_date",
                        "from_cabin",
                        "to_cabin",
                    ],
                    "additionalProperties": False,
                },
            },
        }


class UpdateFlightSchedule(Tool):
    """
    Modify schedule fields for a flight based on either:
      - an explicit 'dates' list (takes priority), or
      - an inclusive [start_date, end_date] range.
    Fields that can be updated: status, aircraft, crew (list).
    Generates missing date records under the flight if necessary (permitted by policy).
    Predictable; returns a summary and preview (first N).
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        flight_number: str,
        dates: list[str] | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        status: str | None = None,
        aircraft: str | None = None,
        crew: list[str] | None = None,
        max_preview: int = 0
    ) -> str:
        dates_list = dates or []
        #🔹 Standardize and verify right away when status is given
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
            status = s  #replace with standardized lowercase

        #fundamental verification
        if not isinstance(dates_list, list):
            return _json({"error": "invalid_dates_param"})
        if not dates_list and not (start_date and end_date):
            return _json(
                {
                    "error": "missing_date_selector",
                    "reason": "Provide 'dates' or 'start_date'+'end_date'.",
                }
            )
        if crew is not None and not isinstance(crew, list):
            return _json(
                {"error": "invalid_crew", "reason": "crew must be a list of strings"}
            )

        f = _get_flight(data, flight_number)
        if not f:
            return _json(
                {
                    "error": "not_found",
                    "entity": "flight",
                    "flight_number": flight_number,
                }
            )

        #Construct target date set in a predictable manner
        targets: set[str] = set()
        if dates_list:
            for d in dates_list:
                if isinstance(d, str):
                    targets.add(d)
        else:
            for d in f.get("dates") or {}:
                if start_date <= d <= end_date:
                    targets.add(d)
            #generate absent dates within the range
            from datetime import datetime, timedelta

            def iter_days(s: str, e: str):
                ds = datetime.strptime(s, "%Y-%m-%d").date()
                de = datetime.strptime(e, "%Y-%m-%d").date()
                cur = ds
                while cur <= de:
                    yield cur.strftime("%Y-%m-%d")
                    cur = cur + timedelta(days=1)

            for d in iter_days(start_date, end_date):
                targets.add(d)

        changed = 0
        preview = []
        f.setdefault("dates", {})

        for d in sorted(targets):
            rec = f["dates"].setdefault(d, {})
            before = {
                "status": _norm_status(rec.get("status")),
                "aircraft": rec.get("aircraft"),
                "crew": rec.get("crew"),
            }
            if status is not None:
                rec["status"] = status
            if aircraft is not None:
                rec["aircraft"] = aircraft
            if crew is not None:
                rec["crew"] = crew

            after = {
                "status": _norm_status(rec.get("status")),
                "aircraft": rec.get("aircraft"),
                "crew": rec.get("crew"),
            }
            if before != after:
                changed += 1
                if len(preview) < max_preview:
                    preview.append({"date": d, "before": before, "after": after})

        return _json(
            {
                "success": True,
                "flight_number": flight_number,
                "changed": changed,
                "preview": preview,
            }
        )
        pass
        dates_list = dates or []
        #🔹 Standardize and verify right away when status is given
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
            status = s  #replace with standardized lowercase

        #fundamental verification
        if not isinstance(dates_list, list):
            return _json({"error": "invalid_dates_param"})
        if not dates_list and not (start_date and end_date):
            return _json(
                {
                    "error": "missing_date_selector",
                    "reason": "Provide 'dates' or 'start_date'+'end_date'.",
                }
            )
        if crew is not None and not isinstance(crew, list):
            return _json(
                {"error": "invalid_crew", "reason": "crew must be a list of strings"}
            )

        f = _get_flight(data, flight_number)
        if not f:
            return _json(
                {
                    "error": "not_found",
                    "entity": "flight",
                    "flight_number": flight_number,
                }
            )

        #Construct target date set in a predictable manner
        targets: set[str] = set()
        if dates_list:
            for d in dates_list:
                if isinstance(d, str):
                    targets.add(d)
        else:
            for d in f.get("dates") or {}:
                if start_date <= d <= end_date:
                    targets.add(d)
            #generate absent dates within the range
            from datetime import datetime, timedelta

            def iter_days(s: str, e: str):
                pass
                ds = datetime.strptime(s, "%Y-%m-%d").date()
                de = datetime.strptime(e, "%Y-%m-%d").date()
                cur = ds
                while cur <= de:
                    yield cur.strftime("%Y-%m-%d")
                    cur = cur + timedelta(days=1)

            for d in iter_days(start_date, end_date):
                targets.add(d)

        changed = 0
        preview = []
        f.setdefault("dates", {})

        for d in sorted(targets):
            rec = f["dates"].setdefault(d, {})
            before = {
                "status": _norm_status(rec.get("status")),
                "aircraft": rec.get("aircraft"),
                "crew": rec.get("crew"),
            }
            if status is not None:
                rec["status"] = status
            if aircraft is not None:
                rec["aircraft"] = aircraft
            if crew is not None:
                rec["crew"] = crew

            after = {
                "status": _norm_status(rec.get("status")),
                "aircraft": rec.get("aircraft"),
                "crew": rec.get("crew"),
            }
            if before != after:
                changed += 1
                if len(preview) < max_preview:
                    preview.append({"date": d, "before": before, "after": after})

        return _json(
            {
                "success": True,
                "flight_number": flight_number,
                "changed": changed,
                "preview": preview,
            }
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "UpdateFlightSchedule",
                "description": "Update per-date schedule (status/aircraft/crew) for a flight by dates or by range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "dates": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Specific dates to update (YYYY-MM-DD).",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "Inclusive start if using a range.",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "Inclusive end if using a range.",
                        },
                        "status": {
                            "type": "string",
                            "description": "e.g. 'available', 'cancelled', 'diverted'",
                        },
                        "aircraft": {"type": "string"},
                        "crew": {"type": "array", "items": {"type": "string"}},
                        "max_preview": {"type": "integer"},
                    },
                    "required": ["flight_number"],
                },
            },
        }


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
        pass
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


class LogUpgradeNoCharge(Tool):
    """
    Create a predictable audit entry for a no-charge upgrade in price_changes.
    Returns audit_id. The timestamp is derived predictably from 'date' (T00:00:00Z) if supplied.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        reservation_id: str | None = None,
        flight_number: str | None = None,
        date: str | None = None,
        from_cabin: str,
        to_cabin: str,
        reason: str | None = None
    ) -> str:
        pass
        date_str = date  # YYYY-MM-DD (optional yet advisable)
        from_cabin = (from_cabin or "").lower()
        to_cabin = (to_cabin or "").lower()
        reason = reason or "no_charge_upgrade"

        if not reservation_id and not (flight_number and date_str):
            return _json(
                {
                    "error": "missing_params",
                    "reason": "Provide reservation_id or (flight_number and date).",
                }
            )
        if not from_cabin or not to_cabin or from_cabin == to_cabin:
            return _json({"error": "invalid_cabins"})

        # Predictable id and timestamp
        change_id = _next_change_id(data, prefix="PC")
        det_ts = f"{str(date_str)[:10]}T00:00:00Z" if date_str else None

        entry = {
            "id": change_id,
            "type": "upgrade_no_charge",
            "reservation_id": reservation_id,
            "flight_number": flight_number,
            "date": date_str,
            "from_cabin": from_cabin,
            "to_cabin": to_cabin,
            "reason": reason,
        }
        if det_ts is not None:
            entry["timestamp"] = det_ts

        (data.setdefault("price_changes", [])).append(entry)

        return _json({"success": True, "audit_id": change_id, "logged": entry})
        pass
        date_str = date  #YYYY-MM-DD (optional yet advisable)
        from_cabin = (from_cabin or "").lower()
        to_cabin = (to_cabin or "").lower()
        reason = reason or "no_charge_upgrade"

        if not reservation_id and not (flight_number and date_str):
            return _json(
                {
                    "error": "missing_params",
                    "reason": "Provide reservation_id or (flight_number and date).",
                }
            )
        if not from_cabin or not to_cabin or from_cabin == to_cabin:
            return _json({"error": "invalid_cabins"})

        #Predictable id and timestamp
        change_id = _next_change_id(data, prefix="PC")
        det_ts = f"{str(date_str)[:10]}T00:00:00Z" if date_str else None

        entry = {
            "id": change_id,
            "type": "upgrade_no_charge",
            "reservation_id": reservation_id,
            "flight_number": flight_number,
            "date": date_str,
            "from_cabin": from_cabin,
            "to_cabin": to_cabin,
            "reason": reason,
        }
        if det_ts is not None:
            entry["timestamp"] = det_ts

        (data.setdefault("price_changes", [])).append(entry)

        return _json({"success": True, "audit_id": change_id, "logged": entry})

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "LogUpgradeNoCharge",
                "description": "Write an audit entry for a no-charge upgrade to the price_changes log.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string"},
                        "flight_number": {"type": "string"},
                        "date": {"type": "string"},
                        "from_cabin": {
                            "type": "string",
                            "enum": ["basic_economy", "economy", "business"],
                        },
                        "to_cabin": {
                            "type": "string",
                            "enum": ["basic_economy", "economy", "business"],
                        },
                        "reason": {"type": "string"},
                    },
                    "required": ["from_cabin", "to_cabin"],
                },
            },
        }


class GetAircraftProfile(Tool):
    """
    Provide a single aircraft enhanced with model specifications and airport information.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        aircraft_id: str | None = None,
        tail_number: str | None = None
    ) -> str:
        pass
        # demand precisely one selector
        if bool(aircraft_id) == bool(tail_number):
            return _json(
                {
                    "error": "invalid_params",
                    "reason": "Provide exactly one of aircraft_id or tail_number.",
                }
            )

        # locate aircraft
        ac = None
        for a in data.get("aircraft", []):
            if aircraft_id and a.get("aircraft_id") == aircraft_id:
                ac = a
                break
            if tail_number and a.get("tail_number") == tail_number:
                ac = a
                break
        if not ac:
            return _json({"error": "aircraft_not_found"})

        # enhance model
        model_id = ((ac.get("model") or {}).get("model_id") or "").upper()
        model = _get_aircraft_model_by_id(data, model_id) if model_id else None

        # enhance airport
        iata = ((ac.get("location") or {}).get("iata_code") or "").upper()
        apt = _get_airport_by_iata(data, iata) if iata else None

        out = {
            "aircraft_id": ac.get("aircraft_id"),
            "tail_number": ac.get("tail_number"),
            "status": _norm_status(ac.get("status")),
            "location": {
                "iata_code": iata or None,
                "airport_name": (apt or {}).get("airport_name"),
                "icao_code": (apt or {}).get("icao_code"),
                "timezone": (apt or {}).get("timezone"),
            },
            "model": {
                "model_id": model_id or None,
                "model_name": (ac.get("model") or {}).get("model_name"),
                "manufacturer": (model or {}).get("manufacturer"),
                "passenger_capacity": (model or {}).get("passenger_capacity"),
                "cargo_capacity_kg": (model or {}).get("cargo_capacity_kg"),
                "maximum_takeoff_weight_kg": (model or {}).get(
                    "maximum_takeoff_weight_kg"
                ),
                "range_km": (model or {}).get("range_km"),
                "engine_type": (model or {}).get("engine_type"),
            },
        }
        return _json(out)
        pass
        #demand precisely one selector
        if bool(aircraft_id) == bool(tail_number):
            return _json(
                {
                    "error": "invalid_params",
                    "reason": "Provide exactly one of aircraft_id or tail_number.",
                }
            )

        #locate aircraft
        ac = None
        for a in data.get("aircraft", []):
            if aircraft_id and a.get("aircraft_id") == aircraft_id:
                ac = a
                break
            if tail_number and a.get("tail_number") == tail_number:
                ac = a
                break
        if not ac:
            return _json({"error": "aircraft_not_found"})

        #enhance model
        model_id = ((ac.get("model") or {}).get("model_id") or "").upper()
        model = _get_aircraft_model_by_id(data, model_id) if model_id else None

        #enhance airport
        iata = ((ac.get("location") or {}).get("iata_code") or "").upper()
        apt = _get_airport_by_iata(data, iata) if iata else None

        out = {
            "aircraft_id": ac.get("aircraft_id"),
            "tail_number": ac.get("tail_number"),
            "status": _norm_status(ac.get("status")),
            "location": {
                "iata_code": iata or None,
                "airport_name": (apt or {}).get("airport_name"),
                "icao_code": (apt or {}).get("icao_code"),
                "timezone": (apt or {}).get("timezone"),
            },
            "model": {
                "model_id": model_id or None,
                "model_name": (ac.get("model") or {}).get("model_name"),
                "manufacturer": (model or {}).get("manufacturer"),
                "passenger_capacity": (model or {}).get("passenger_capacity"),
                "cargo_capacity_kg": (model or {}).get("cargo_capacity_kg"),
                "maximum_takeoff_weight_kg": (model or {}).get(
                    "maximum_takeoff_weight_kg"
                ),
                "range_km": (model or {}).get("range_km"),
                "engine_type": (model or {}).get("engine_type"),
            },
        }
        return _json(out)

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetAircraftProfile",
                "description": "Lookup an aircraft by ID or tail number, enriched with model specs and airport details.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {"type": "string", "description": "e.g., AC001"},
                        "tail_number": {
                            "type": "string",
                            "description": "e.g., PR-GOL",
                        },
                    },
                    "oneOf": [
                        {"required": ["aircraft_id"]},
                        {"required": ["tail_number"]},
                    ],
                    "additionalProperties": False,
                },
            },
        }


class ListAircraftAtAirport(Tool):
    """
    Enumerate aircraft currently stationed at a specified IATA airport, with optional filters.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        iata_code: str,
        status: str | None = None,
        model_id: str | None = None
    ) -> str:
        iata = (iata_code or "").upper()
        if not iata:
            return _json({"error": "missing_params", "reason": "iata_code is required"})

        status = status.strip() if isinstance(status, str) else None
        model_id = (model_id or "").upper() if model_id else None

        airport = _get_airport_by_iata(data, iata)

        rows: list[dict[str, Any]] = []
        for a in data.get("aircraft", []):
            loc = (a.get("location") or {}).get("iata_code")
            if (loc or "").upper() != iata:
                continue

            if status and _norm_status(a.get("status")) != status:
                continue

            ac_model_id = ((a.get("model") or {}).get("model_id") or "").upper()
            if model_id and ac_model_id != model_id:
                continue

            rows.append(
                {
                    "aircraft_id": a.get("aircraft_id"),
                    "tail_number": a.get("tail_number"),
                    "status": _norm_status(a.get("status")),
                    "model_id": ac_model_id or None,
                    "model_name": (a.get("model") or {}).get("model_name"),
                }
            )

        rows.sort(key=lambda r: (r.get("tail_number") or ""))

        return _json(
            {
                "airport": {
                    "iata_code": iata,
                    "airport_name": (airport or {}).get("airport_name"),
                    "icao_code": (airport or {}).get("icao_code"),
                    "timezone": (airport or {}).get("timezone"),
                },
                "total": len(rows),
                "aircraft": rows,
            }
        )
        pass
        iata = (iata_code or "").upper()
        if not iata:
            return _json({"error": "missing_params", "reason": "iata_code is required"})

        status = status.strip() if isinstance(status, str) else None
        model_id = (model_id or "").upper() if model_id else None

        airport = _get_airport_by_iata(data, iata)

        rows: list[dict[str, Any]] = []
        for a in data.get("aircraft", []):
            loc = (a.get("location") or {}).get("iata_code")
            if (loc or "").upper() != iata:
                continue

            if status and _norm_status(a.get("status")) != status:
                continue

            ac_model_id = ((a.get("model") or {}).get("model_id") or "").upper()
            if model_id and ac_model_id != model_id:
                continue

            rows.append(
                {
                    "aircraft_id": a.get("aircraft_id"),
                    "tail_number": a.get("tail_number"),
                    "status": _norm_status(a.get("status")),
                    "model_id": ac_model_id or None,
                    "model_name": (a.get("model") or {}).get("model_name"),
                }
            )

        rows.sort(key=lambda r: (r.get("tail_number") or ""))

        return _json(
            {
                "airport": {
                    "iata_code": iata,
                    "airport_name": (airport or {}).get("airport_name"),
                    "icao_code": (airport or {}).get("icao_code"),
                    "timezone": (airport or {}).get("timezone"),
                },
                "total": len(rows),
                "aircraft": rows,
            }
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListAircraftAtAirport",
                "description": "List aircraft currently located at a given IATA airport with optional status/model filters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "iata_code": {
                            "type": "string",
                            "description": "Airport IATA code, e.g., ATL",
                        },
                        "status": {
                            "type": "string",
                            "description": "Filter by aircraft status, e.g., Active",
                        },
                        "model_id": {
                            "type": "string",
                            "description": "Filter by model_id, e.g., B737-800",
                        },
                    },
                    "required": ["iata_code"],
                    "additionalProperties": False,
                },
            },
        }


class RepositionAircraft(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        aircraft_id: str | None = None,
        tail_number: str | None = None,
        to_iata: str = "",
        reason: str | None = None
    ) -> str:
        to_iata = (to_iata or "").upper()

        if bool(aircraft_id) == bool(tail_number):
            return _json(
                {
                    "error": "invalid_params",
                    "reason": "Provide exactly one of aircraft_id or tail_number.",
                }
            )
        if not to_iata:
            return _json({"error": "missing_params", "reason": "to_iata is required"})

        apt = _get_airport_by_iata(data, to_iata)
        if not apt:
            return _json({"error": "airport_not_found", "iata_code": to_iata})

        ac = _find_aircraft(data, aircraft_id, tail_number)
        if not ac:
            return _json({"error": "aircraft_not_found"})

        cur_iata = ((ac.get("location") or {}).get("iata_code") or "").upper()
        if cur_iata == to_iata:
            return _json(
                {
                    "success": True,
                    "aircraft_id": ac.get("aircraft_id"),
                    "tail_number": ac.get("tail_number"),
                    "from_iata": cur_iata or None,
                    "to_iata": to_iata,
                    "no_change": True,
                }
            )

        ac.setdefault("location", {})
        ac["location"]["iata_code"] = to_iata

        audit_id = _next_change_id(data, prefix="AM")
        (data.setdefault("aircraft_movements", [])).append(
            {
                "id": audit_id,
                "type": "RepositionAircraft",
                "aircraft_id": ac.get("aircraft_id"),
                "tail_number": ac.get("tail_number"),
                "from_iata": cur_iata or None,
                "to_iata": to_iata,
                "reason": reason,
            }
        )

        return _json(
            {
                "success": True,
                "aircraft_id": ac.get("aircraft_id"),
                "tail_number": ac.get("tail_number"),
                "from_iata": cur_iata or None,
                "to_iata": to_iata,
                "no_change": False,
                "audit_id": audit_id,
            }
        )
        pass
        to_iata = (to_iata or "").upper()

        if bool(aircraft_id) == bool(tail_number):
            return _json(
                {
                    "error": "invalid_params",
                    "reason": "Provide exactly one of aircraft_id or tail_number.",
                }
            )
        if not to_iata:
            return _json({"error": "missing_params", "reason": "to_iata is required"})

        apt = _get_airport_by_iata(data, to_iata)
        if not apt:
            return _json({"error": "airport_not_found", "iata_code": to_iata})

        ac = _find_aircraft(data, aircraft_id, tail_number)
        if not ac:
            return _json({"error": "aircraft_not_found"})

        cur_iata = ((ac.get("location") or {}).get("iata_code") or "").upper()
        if cur_iata == to_iata:
            return _json(
                {
                    "success": True,
                    "aircraft_id": ac.get("aircraft_id"),
                    "tail_number": ac.get("tail_number"),
                    "from_iata": cur_iata or None,
                    "to_iata": to_iata,
                    "no_change": True,
                }
            )

        ac.setdefault("location", {})
        ac["location"]["iata_code"] = to_iata

        audit_id = _next_change_id(data, prefix="AM")
        (data.setdefault("aircraft_movements", [])).append(
            {
                "id": audit_id,
                "type": "RepositionAircraft",
                "aircraft_id": ac.get("aircraft_id"),
                "tail_number": ac.get("tail_number"),
                "from_iata": cur_iata or None,
                "to_iata": to_iata,
                "reason": reason,
            }
        )

        return _json(
            {
                "success": True,
                "aircraft_id": ac.get("aircraft_id"),
                "tail_number": ac.get("tail_number"),
                "from_iata": cur_iata or None,
                "to_iata": to_iata,
                "no_change": False,
                "audit_id": audit_id,
            }
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "RepositionAircraft",
                "description": "Move an aircraft to a new IATA airport with validation and deterministic audit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {"type": "string", "description": "e.g., AC001"},
                        "tail_number": {
                            "type": "string",
                            "description": "e.g., N123AB",
                        },
                        "to_iata": {
                            "type": "string",
                            "description": "Target IATA, e.g., ATL",
                        },
                        "reason": {
                            "type": "string",
                            "description": "Audit text (optional)",
                        },
                    },
                    "oneOf": [
                        {"required": ["aircraft_id", "to_iata"]},
                        {"required": ["tail_number", "to_iata"]},
                    ],
                },
            },
        }


class UpdateAircraftStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        aircraft_id: str | None = None,
        tail_number: str | None = None,
        status: str,
        reason: str | None = None
    ) -> str:
        new_status = _norm_status(status) if isinstance(status, str) else ""
        if not new_status:
            return _json({"error": "missing_params", "reason": "status is required"})
        if new_status not in AIRCRAFT_STATUS:
            return _json(
                {
                    "error": "invalid_status",
                    "entity": "aircraft",
                    "provided": status,
                    "allowed": sorted(list(AIRCRAFT_STATUS)),
                }
            )

        if bool(aircraft_id) == bool(tail_number):
            return _json(
                {
                    "error": "invalid_params",
                    "reason": "Provide exactly one of aircraft_id or tail_number.",
                }
            )

        ac = _find_aircraft(data, aircraft_id, tail_number)
        if not ac:
            return _json({"error": "aircraft_not_found"})

        old_status = _norm_status(ac.get("status"))
        if old_status == new_status:
            return _json(
                {
                    "success": True,
                    "aircraft_id": ac.get("aircraft_id"),
                    "tail_number": ac.get("tail_number"),
                    "old_status": old_status,
                    "new_status": new_status,
                    "no_change": True,
                }
            )

        ac["status"] = new_status

        audit_id = _next_change_id(data, prefix="AS")
        (data.setdefault("aircraft_status_changes", [])).append(
            {
                "id": audit_id,
                "type": "UpdateAircraftStatus",
                "aircraft_id": ac.get("aircraft_id"),
                "tail_number": ac.get("tail_number"),
                "old_status": old_status,
                "new_status": new_status,
                "reason": reason,
            }
        )

        return _json(
            {
                "success": True,
                "aircraft_id": ac.get("aircraft_id"),
                "tail_number": ac.get("tail_number"),
                "old_status": old_status,
                "new_status": new_status,
                "no_change": False,
                "audit_id": audit_id,
            }
        )
        pass
        new_status = _norm_status(status) if isinstance(status, str) else ""
        if not new_status:
            return _json({"error": "missing_params", "reason": "status is required"})
        if new_status not in AIRCRAFT_STATUS:
            return _json(
                {
                    "error": "invalid_status",
                    "entity": "aircraft",
                    "provided": status,
                    "allowed": sorted(list(AIRCRAFT_STATUS)),
                }
            )

        if bool(aircraft_id) == bool(tail_number):
            return _json(
                {
                    "error": "invalid_params",
                    "reason": "Provide exactly one of aircraft_id or tail_number.",
                }
            )

        ac = _find_aircraft(data, aircraft_id, tail_number)
        if not ac:
            return _json({"error": "aircraft_not_found"})

        old_status = _norm_status(ac.get("status"))
        if old_status == new_status:
            return _json(
                {
                    "success": True,
                    "aircraft_id": ac.get("aircraft_id"),
                    "tail_number": ac.get("tail_number"),
                    "old_status": old_status,
                    "new_status": new_status,
                    "no_change": True,
                }
            )

        ac["status"] = new_status

        audit_id = _next_change_id(data, prefix="AS")
        (data.setdefault("aircraft_status_changes", [])).append(
            {
                "id": audit_id,
                "type": "UpdateAircraftStatus",
                "aircraft_id": ac.get("aircraft_id"),
                "tail_number": ac.get("tail_number"),
                "old_status": old_status,
                "new_status": new_status,
                "reason": reason,
            }
        )

        return _json(
            {
                "success": True,
                "aircraft_id": ac.get("aircraft_id"),
                "tail_number": ac.get("tail_number"),
                "old_status": old_status,
                "new_status": new_status,
                "no_change": False,
                "audit_id": audit_id,
            }
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "UpdateAircraftStatus",
                "description": "Update an aircraft's status with a deterministic audit record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {"type": "string", "description": "e.g., AC001"},
                        "tail_number": {
                            "type": "string",
                            "description": "e.g., N123AB",
                        },
                        "status": {
                            "type": "string",
                            "description": "New status, e.g., active",
                        },
                        "reason": {
                            "type": "string",
                            "description": "Audit text (optional)",
                        },
                    },
                    "oneOf": [
                        {"required": ["aircraft_id", "status"]},
                        {"required": ["tail_number", "status"]},
                    ],
                },
            },
        }


class GetCrewCertifications(Tool):
    """
    Read-only access to a crew member's certifications with optional filters.

    Filtering:
      • certification_code (exact match against the standard code in data['certifications'])
      • active_on (YYYY-MM-DD): returns records whose [issue_date .. expiry_date] encompasses this day.
        - expiry_date None/''/'null' is considered open-ended.
      • include_history: if True with active_on, include both active and inactive; if False, only active.

    Predictable:
      • Output is sorted by (certification_code, issue_date ASC).
      • No modifications; consistent formatting/keys.
    """

    @staticmethod
    def _is_active_on(
        issue_date: str | None, expiry_date: str | None, day: str
    ) -> bool:
        pass
        #Accept None/''/'null' as indefinite; all dates are ISO by the nature of upsert.
        from datetime import date

        d = date.fromisoformat(day)
        start = date.fromisoformat(issue_date) if issue_date else date.min
        end = (
            date.max
            if expiry_date in (None, "", "null")
            else date.fromisoformat(expiry_date)
        )
        return start <= d <= end

    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        crew_member_id: str,
        certification_code: str | None = None,
        active_on: str | None = None,
        include_history: bool = False
    ) -> str:
        # Check crew for validity
        if not crew_member_id:
            return _json(
                {"error": "missing_params", "reason": "crew_member_id is required"}
            )
        crew = _find_crew_member(data, crew_member_id)
        if not crew:
            return _json(
                {"error": "crew_member_not_found", "crew_member_id": crew_member_id}
            )

        # Translate certification_code (if given) to the standard one in the master list
        resolved_code = None
        if certification_code:
            cert = _get_cert_by_code(data, certification_code)
            if not cert:
                return _json(
                    {
                        "error": "certification_not_found",
                        "certification_code": certification_code,
                    }
                )
            resolved_code = cert.get("certification_code")

        # Standardize active_on if supplied
        day = None
        if active_on not in (None, "", "null"):
            try:
                # strict ISO; accept complete ISO datetime by utilizing a helper if needed
                day = _to_iso_day(active_on)
                from datetime import date as _date

                _date.fromisoformat(day)
            except Exception:
                return _json(
                    {
                        "error": "invalid_date_format",
                        "reason": "active_on must be YYYY-MM-DD",
                    }
                )

        # Gather and filter
        rows = []
        for cc in data.get("crew_certifications", []):
            cm = (cc.get("crew_member") or {}).get("crew_member_id")
            cert = cc.get("certification") or {}
            code = cert.get("certification_code")

            if cm != crew_member_id:
                continue
            if resolved_code and code != resolved_code:
                continue

            i_date = cc.get("issue_date")
            e_date = cc.get("expiry_date")

            # Implement active_on filter
            active_flag = None
            if day:
                active_flag = GetCrewCertifications._is_active_on(i_date, e_date, day)
                if not active_flag and not include_history:
                    continue

            rows.append(
                {
                    "crew_certification_id": cc.get("crew_certification_id"),
                    "crew_member_id": crew_member_id,
                    "certification_code": code,
                    "issue_date": i_date,
                    "expiry_date": e_date,
                    "active_on": active_flag,  # None if active_on is not supplied
                }
            )

        # Predictable sorting
        rows.sort(
            key=lambda r: (
                (r.get("certification_code") or ""),
                (r.get("issue_date") or ""),
            )
        )

        return _json(
            {
                "success": True,
                "crew_member_id": crew_member_id,
                "certification_code_filter": resolved_code,
                "active_on": day,
                "include_history": include_history,
                "count": len(rows),
                "results": rows,
            }
        )
        pass
        #Check crew for validity
        if not crew_member_id:
            return _json(
                {"error": "missing_params", "reason": "crew_member_id is required"}
            )
        crew = _find_crew_member(data, crew_member_id)
        if not crew:
            return _json(
                {"error": "crew_member_not_found", "crew_member_id": crew_member_id}
            )

        #Translate certification_code (if given) to the standard one in the master list
        resolved_code = None
        if certification_code:
            cert = _get_cert_by_code(data, certification_code)
            if not cert:
                return _json(
                    {
                        "error": "certification_not_found",
                        "certification_code": certification_code,
                    }
                )
            resolved_code = cert.get("certification_code")

        #Standardize active_on if supplied
        day = None
        if active_on not in (None, "", "null"):
            try:
                #strict ISO; accept complete ISO datetime by utilizing a helper if needed
                day = _to_iso_day(active_on)
                from datetime import date as _date

                _date.fromisoformat(day)
            except Exception:
                return _json(
                    {
                        "error": "invalid_date_format",
                        "reason": "active_on must be YYYY-MM-DD",
                    }
                )

        #Gather and filter
        rows = []
        for cc in data.get("crew_certifications", []):
            cm = (cc.get("crew_member") or {}).get("crew_member_id")
            cert = cc.get("certification") or {}
            code = cert.get("certification_code")

            if cm != crew_member_id:
                continue
            if resolved_code and code != resolved_code:
                continue

            i_date = cc.get("issue_date")
            e_date = cc.get("expiry_date")

            #Implement active_on filter
            active_flag = None
            if day:
                active_flag = GetCrewCertifications._is_active_on(i_date, e_date, day)
                if not active_flag and not include_history:
                    continue

            rows.append(
                {
                    "crew_certification_id": cc.get("crew_certification_id"),
                    "crew_member_id": crew_member_id,
                    "certification_code": code,
                    "issue_date": i_date,
                    "expiry_date": e_date,
                    "active_on": active_flag,  #None if active_on is not supplied
                }
            )

        #Predictable sorting
        rows.sort(
            key=lambda r: (
                (r.get("certification_code") or ""),
                (r.get("issue_date") or ""),
            )
        )

        return _json(
            {
                "success": True,
                "crew_member_id": crew_member_id,
                "certification_code_filter": resolved_code,
                "active_on": day,
                "include_history": include_history,
                "count": len(rows),
                "results": rows,
            }
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetCrewCertifications",
                "description": (
                    "List certifications for a crew member with optional filters: certification_code, "
                    "active_on (YYYY-MM-DD), include_history. Read-only, deterministic, sorted."
                ),
                "parameters": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "crew_member_id": {
                            "type": "string",
                            "description": "e.g. CM001",
                        },
                        "certification_code": {
                            "type": "string",
                            "description": "Filter to a specific code (e.g. A320neo)",
                        },
                        "active_on": {
                            "type": "string",
                            "description": "YYYY-MM-DD; return records active on this date",
                        },
                        "include_history": {
                            "type": "boolean",
                            "description": "When active_on is given, include inactive too",
                            "default": False,
                        },
                    },
                    "required": ["crew_member_id"],
                },
            },
        }


class UpsertCrewCertification(Tool):
    """
    Create or modify a crew member's certification with validation and predictable IDs/audit.
    """

    @staticmethod
    def _normalize_date_str(d):
        """Standardize incoming date-like values to ISO 'YYYY-MM-DD' or None (accepts None, '', 'null')."""
        pass
        if d in (None, "", "null"):
            return None
        date.fromisoformat(d)  #throws an error if invalid
        return d

    @staticmethod
    def _overlaps(a_start, a_end, b_start, b_end):
        """Inclusive day-level overlap; None/''/'null' expiry is considered open-ended."""
        pass
        a_s = date.fromisoformat(a_start)
        a_e = date.max if a_end in (None, "", "null") else date.fromisoformat(a_end)
        b_s = date.fromisoformat(b_start)
        b_e = date.max if b_end in (None, "", "null") else date.fromisoformat(b_end)
        return not (a_e < b_s or b_e < a_s)

    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        crew_member_id: str,
        certification_code: str | None = None,
        certification_id: str | None = None,
        issue_date: str,
        expiry_date: str | None = None,
        upsert_strategy: str = "create_new",
        reason: str | None = None
    ) -> str:
        pass
        cert_id = certification_id
        strategy = upsert_strategy

        #check crew for validity
        if not crew_member_id:
            return _json(
                {"error": "missing_params", "reason": "crew_member_id is required"}
            )
        crew = _find_crew_member(data, crew_member_id)
        if not crew:
            return _json(
                {"error": "crew_member_not_found", "crew_member_id": crew_member_id}
            )

        #precisely one of code or id
        if bool(certification_code) == bool(cert_id):
            return _json(
                {
                    "error": "invalid_params",
                    "reason": "Provide exactly one of certification_code or certification_id.",
                }
            )

        #determine certification
        cert = (
            _get_cert_by_code(data, certification_code)
            if certification_code
            else _get_cert_by_id(data, cert_id)
        )
        if not cert:
            return _json(
                {
                    "error": "certification_not_found",
                    "certification_code": certification_code,
                    "certification_id": cert_id,
                }
            )

        resolved_code = cert.get("certification_code")
        resolved_id = cert.get("certification_id")

        #standardize and verify strategy
        strategy = (
            strategy.strip().lower() if isinstance(strategy, str) else "create_new"
        )
        if strategy not in ("create_new", "replace_if_overlap"):
            return _json(
                {
                    "error": "invalid_params",
                    "reason": "upsert_strategy must be 'create_new' or 'replace_if_overlap'.",
                }
            )

        #date verification and standardization
        if not issue_date:
            return _json(
                {"error": "missing_params", "reason": "issue_date is required"}
            )
        try:
            issue_date = UpsertCrewCertification._normalize_date_str(issue_date)
            expiry_date = UpsertCrewCertification._normalize_date_str(expiry_date)
        except Exception:
            return _json(
                {
                    "error": "invalid_date_format",
                    "reason": "Dates must be YYYY-MM-DD or null",
                }
            )

        #groups
        existing_list = data.setdefault("crew_certifications", [])
        audits = data.setdefault("crew_cert_audits", [])

        #correspondences for this crew and cert_code
        matches = [
            cc
            for cc in existing_list
            if ((cc.get("crew_member") or {}).get("crew_member_id") == crew_member_id)
            and (
                (cc.get("certification") or {}).get("certification_code")
                == resolved_code
            )
        ]

        #predictable IDs
        det_cc_id = f"CC-{crew_member_id}-{resolved_code}-{issue_date}"
        audit_id = f"CA-{crew_member_id}-{issue_date}"

        def _make_record():
            pass
            return {
                "crew_certification_id": det_cc_id,
                "crew_member": {
                    "crew_member_id": crew_member_id,
                    "employee_code": crew.get("employee_code"),
                    "full_name": (
                        crew.get("first_name", "") + " " + crew.get("last_name", "")
                    ).strip(),
                },
                "certification": {
                    "certification_id": resolved_id,
                    "certification_code": resolved_code,
                },
                "issue_date": issue_date,
                "expiry_date": expiry_date,
            }

        existing_by_id = next(
            (
                cc
                for cc in existing_list
                if cc.get("crew_certification_id") == det_cc_id
            ),
            None,
        )

        if matches:
            overlapping = None
            for cc in matches:
                if UpsertCrewCertification._overlaps(
                    cc.get("issue_date"), cc.get("expiry_date"), issue_date, expiry_date
                ):
                    overlapping = cc
                    break

            if overlapping and strategy == "replace_if_overlap":
                overlapping["certification"] = {
                    "certification_id": resolved_id,
                    "certification_code": resolved_code,
                }
                overlapping["issue_date"] = issue_date
                overlapping["expiry_date"] = expiry_date
                overlapping["crew_certification_id"] = det_cc_id
                new_cc_id = det_cc_id
                action = "replaced"
            else:
                if existing_by_id:
                    new_cc_id = det_cc_id
                    action = "noop_exists"
                else:
                    existing_list.append(_make_record())
                    new_cc_id = det_cc_id
                    action = "created"
        else:
            if existing_by_id:
                new_cc_id = det_cc_id
                action = "noop_exists"
            else:
                existing_list.append(_make_record())
                new_cc_id = det_cc_id
                action = "created"

        #predictable audit (prevent duplicate audits with the same id)
        if not any(a.get("id") == audit_id for a in audits):
            audits.append(
                {
                    "id": audit_id,
                    "type": "UpsertCrewCertification",
                    "crew_member_id": crew_member_id,
                    "certification_code": resolved_code,
                    "issue_date": issue_date,
                    "expiry_date": expiry_date,
                    "strategy": strategy,
                    "reason": reason,
                }
            )

        return _json(
            {
                "success": True,
                "action": action,
                "crew_certification_id": new_cc_id,
                "crew_member_id": crew_member_id,
                "certification_code": resolved_code,
                "issue_date": issue_date,
                "expiry_date": expiry_date,
                "audit_id": audit_id,
            }
        )
        pass
        cert_id = certification_id
        strategy = upsert_strategy

        #check crew for validity
        if not crew_member_id:
            return _json(
                {"error": "missing_params", "reason": "crew_member_id is required"}
            )
        crew = _find_crew_member(data, crew_member_id)
        if not crew:
            return _json(
                {"error": "crew_member_not_found", "crew_member_id": crew_member_id}
            )

        #precisely one of code or id
        if bool(certification_code) == bool(cert_id):
            return _json(
                {
                    "error": "invalid_params",
                    "reason": "Provide exactly one of certification_code or certification_id.",
                }
            )

        #determine certification
        cert = (
            _get_cert_by_code(data, certification_code)
            if certification_code
            else _get_cert_by_id(data, cert_id)
        )
        if not cert:
            return _json(
                {
                    "error": "certification_not_found",
                    "certification_code": certification_code,
                    "certification_id": cert_id,
                }
            )

        resolved_code = cert.get("certification_code")
        resolved_id = cert.get("certification_id")

        #standardize and verify strategy
        strategy = (
            strategy.strip().lower() if isinstance(strategy, str) else "create_new"
        )
        if strategy not in ("create_new", "replace_if_overlap"):
            return _json(
                {
                    "error": "invalid_params",
                    "reason": "upsert_strategy must be 'create_new' or 'replace_if_overlap'.",
                }
            )

        #date verification and standardization
        if not issue_date:
            return _json(
                {"error": "missing_params", "reason": "issue_date is required"}
            )
        try:
            issue_date = UpsertCrewCertification._normalize_date_str(issue_date)
            expiry_date = UpsertCrewCertification._normalize_date_str(expiry_date)
        except Exception:
            return _json(
                {
                    "error": "invalid_date_format",
                    "reason": "Dates must be YYYY-MM-DD or null",
                }
            )

        #groups
        existing_list = data.setdefault("crew_certifications", [])
        audits = data.setdefault("crew_cert_audits", [])

        #correspondences for this crew and cert_code
        matches = [
            cc
            for cc in existing_list
            if ((cc.get("crew_member") or {}).get("crew_member_id") == crew_member_id)
            and (
                (cc.get("certification") or {}).get("certification_code")
                == resolved_code
            )
        ]

        #predictable IDs
        det_cc_id = f"CC-{crew_member_id}-{resolved_code}-{issue_date}"
        audit_id = f"CA-{crew_member_id}-{issue_date}"

        def _make_record():
            pass
            return {
                "crew_certification_id": det_cc_id,
                "crew_member": {
                    "crew_member_id": crew_member_id,
                    "employee_code": crew.get("employee_code"),
                    "full_name": (
                        crew.get("first_name", "") + " " + crew.get("last_name", "")
                    ).strip(),
                },
                "certification": {
                    "certification_id": resolved_id,
                    "certification_code": resolved_code,
                },
                "issue_date": issue_date,
                "expiry_date": expiry_date,
            }

        existing_by_id = next(
            (
                cc
                for cc in existing_list
                if cc.get("crew_certification_id") == det_cc_id
            ),
            None,
        )

        if matches:
            overlapping = None
            for cc in matches:
                if UpsertCrewCertification._overlaps(
                    cc.get("issue_date"), cc.get("expiry_date"), issue_date, expiry_date
                ):
                    overlapping = cc
                    break

            if overlapping and strategy == "replace_if_overlap":
                overlapping["certification"] = {
                    "certification_id": resolved_id,
                    "certification_code": resolved_code,
                }
                overlapping["issue_date"] = issue_date
                overlapping["expiry_date"] = expiry_date
                overlapping["crew_certification_id"] = det_cc_id
                new_cc_id = det_cc_id
                action = "replaced"
            else:
                if existing_by_id:
                    new_cc_id = det_cc_id
                    action = "noop_exists"
                else:
                    existing_list.append(_make_record())
                    new_cc_id = det_cc_id
                    action = "created"
        else:
            if existing_by_id:
                new_cc_id = det_cc_id
                action = "noop_exists"
            else:
                existing_list.append(_make_record())
                new_cc_id = det_cc_id
                action = "created"

        #predictable audit (prevent duplicate audits with the same id)
        if not any(a.get("id") == audit_id for a in audits):
            audits.append(
                {
                    "id": audit_id,
                    "type": "UpsertCrewCertification",
                    "crew_member_id": crew_member_id,
                    "certification_code": resolved_code,
                    "issue_date": issue_date,
                    "expiry_date": expiry_date,
                    "strategy": strategy,
                    "reason": reason,
                }
            )

        return _json(
            {
                "success": True,
                "action": action,
                "crew_certification_id": new_cc_id,
                "crew_member_id": crew_member_id,
                "certification_code": resolved_code,
                "issue_date": issue_date,
                "expiry_date": expiry_date,
                "audit_id": audit_id,
            }
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "UpsertCrewCertification",
                "description": (
                    "Create or update a crew member's certification with overlap handling and deterministic IDs. "
                    "crew_certification_id = 'CC-{crew_member_id}-{certification_code}-{issue_date}', "
                    "audit_id = 'CA-{crew_member_id}-{issue_date}'. Dates are ISO (YYYY-MM-DD) or null."
                ),
                "parameters": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "crew_member_id": {
                            "type": "string",
                            "description": "Crew member ID, e.g., CM001",
                        },
                        "certification_code": {
                            "type": "string",
                            "description": "e.g., B737-800, A320neo",
                        },
                        "certification_id": {
                            "type": "string",
                            "description": "e.g., CERT_B738",
                        },
                        "issue_date": {"type": "string", "description": "YYYY-MM-DD"},
                        "expiry_date": {
                            "type": ["string", "null"],
                            "description": "YYYY-MM-DD or null",
                        },
                        "upsert_strategy": {
                            "type": "string",
                            "enum": ["create_new", "replace_if_overlap"],
                            "default": "create_new",
                        },
                        "reason": {
                            "type": "string",
                            "description": "Audit text (optional)",
                        },
                    },
                    "oneOf": [
                        {
                            "required": [
                                "crew_member_id",
                                "certification_code",
                                "issue_date",
                            ]
                        },
                        {
                            "required": [
                                "crew_member_id",
                                "certification_id",
                                "issue_date",
                            ]
                        },
                    ],
                },
            },
        }


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
        dates = route.get("dates", {})
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

        dates = route.setdefault("dates", {})
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
            seat_map = date_info.setdefault("available_seats", {})
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
            price_map = date_info.setdefault("prices", {})
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
                "available_seats": date_info.get("available_seats", {}),
                "prices": date_info.get("prices", {}),
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

        dates = route.setdefault("dates", {})
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
            seat_map = date_info.setdefault("available_seats", {})
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
            price_map = date_info.setdefault("prices", {})
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
                "available_seats": date_info.get("available_seats", {}),
                "prices": date_info.get("prices", {}),
                "updated": updated,
                #"existing_cabins": sorted(list(_cabins_existing))  # uncomment if beneficial
            }
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
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


class AssignAircraftToFlight(Tool):
    """
    A utility to allocate a specific aircraft to a flight on a specified date.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any], flight_number: str, date: str, new_aircraft_id: str
    ) -> str:
        flights_data = data.get("flights", [])
        for flight in flights_data:
            if flight.get("flight_number") == flight_number:
                if date in flight.get("dates", {}):
                    flight["dates"][date][
                        "notes"
                    ] = f"Aircraft reassigned to {new_aircraft_id}"
                    payload = {
                        "status": "success",
                        "flight_number": flight_number,
                        "date": date,
                        "new_aircraft_id": new_aircraft_id,
                    }
                    out = json.dumps(payload)
                    return out
        payload = {"error": "Flight not found on the specified date."}
        out = json.dumps(payload)
        return out
        pass
        flights_data = data.get("flights", [])
        for flight in flights_data:
            if flight.get("flight_number") == flight_number:
                if date in flight.get("dates", {}):
                    flight["dates"][date][
                        "notes"
                    ] = f"Aircraft reassigned to {new_aircraft_id}"
                    payload = {
                            "status": "success",
                            "flight_number": flight_number,
                            "date": date,
                            "new_aircraft_id": new_aircraft_id,
                        }
                    out = json.dumps(
                        payload)
                    return out
        payload = {"error": "Flight not found on the specified date."}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "AssignAircraftToFlight",
                "description": "Assigns a new aircraft to a specific flight instance.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "date": {
                            "type": "string",
                            "description": "Date in YYYY-MM-DD format.",
                        },
                        "new_aircraft_id": {
                            "type": "string",
                            "description": "The ID of the new aircraft.",
                        },
                    },
                    "required": ["flight_number", "date", "new_aircraft_id"],
                },
            },
        }


TOOLS = [
    GetCurrentTicketPrice(),
    GetHistoricalTicketPrices(),
    GetAverageTicketPrice(),
    GetOperationalEvents(),
    GetFlownRevenueForFlight(),
    GetPriceChangeHistory(),
    ListOperatingDates(),
    ListAllFaresByRoute(),
    GetCheapestFlightFromReservation(),
    ComputeCheapestByDateForRoute(),
    GetFlightSchedule(),
    GetFlightStatusByDate(),
    GetAircraftByTailNumber(),
    GetAvailableSeat(),
    GetCrewCertifications(),
    #WRITE
    SetTicketPrice(),
    ApplyDiscountToFlight(),
    RemoveDiscountFromFlight(),
    AdjustFareClassPricing(),
    AdjustSeasonalPricing(),
    BulkUpgradeTicketPrices(),
    UpdateFlightSchedule(),
    RepriceReservation(),
    LogUpgradeNoCharge(),
    ListAircraftAtAirport(),
    GetAircraftProfile(),
    RepositionAircraft(),
    UpdateAircraftStatus(),
    UpsertCrewCertification(),
    UpdateFlightInventoryAndPrices(),
    AssignAircraftToFlight(),
]
