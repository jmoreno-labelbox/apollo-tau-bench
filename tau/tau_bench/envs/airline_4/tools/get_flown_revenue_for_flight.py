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

        reservations = data.get("reservations", {}).values()
        flights = data.get("flights", {}).values()

        flight_date_status = {}
        if require_available:
            for f in flights.values() if isinstance(flights, list) else []:
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
            for res in reservations.values():
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

        reservations = data.get("reservations", {}).values()
        flights = data.get("flights", {}).values()

        flight_date_status = {}
        if require_available:
            for f in flights.values() if isinstance(flights, list) else []:
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
            for res in reservations.values():
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
