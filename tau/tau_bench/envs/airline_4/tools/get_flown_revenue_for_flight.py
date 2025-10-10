# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetFlownRevenueForFlight(Tool):
    """
    Approximate flown revenue for a flight over a date range, recognized on each leg's date.
    NOTE: Current dataset has no taxes/fees/surcharges, so 'total' == 'base_fare'.
    """

    @staticmethod
    def _num(x):
        try:
            return float(x)
        except Exception:
            return None

    @staticmethod
    def _leg_amount(price_obj, price_component: str) -> float | None:

        if isinstance(price_obj, (int, float, str)):
            return GetFlownRevenueForFlight._num(price_obj)
        if isinstance(price_obj, dict):
            return GetFlownRevenueForFlight._num(price_obj.get("base_fare"))
        return None

    @staticmethod
    def _reservation_total(res, price_component: str) -> float | None:
        # Use a dictionary with base_fare as the primary option; revert to a scalar price if unavailable.
        if isinstance(res.get("price"), dict):
            return GetFlownRevenueForFlight._leg_amount(res["price"], price_component)
        if isinstance(res.get("total_price"), dict):
            return GetFlownRevenueForFlight._leg_amount(res["total_price"], price_component)
        if isinstance(res.get("price"), (int, float, str)):
            return GetFlownRevenueForFlight._num(res["price"])
        return None

    @staticmethod
    def invoke(
        data: Dict[str, Any], *,
        flight_number: str,
        start_date: str,
        end_date: str,
        price_component: str = "base_fare",  # retained for API structure; 'total' is equivalent to 'base_fare' in the existing dataset
        require_available: bool = True,
        include_details: bool = False
    ) -> str:
        price_component = (price_component or "base_fare").lower()
        if price_component not in ("base_fare", "total"):
            return _json({"error": "invalid_price_component"})

        reservations = list(data.get("reservations", {}).values())
        flights      = list(data.get("flights", {}).values())

        flight_date_status = {}
        if require_available:
            for f in flights if isinstance(flights, list) else []:
                if f.get("flight_number") == flight_number:
                    for d, rec in (f.get("dates") or {}).items():
                        flight_date_status[(flight_number, d)] = _norm_status((rec or {}).get("status"))

        def operated(day: str) -> bool:
            return (not require_available) or (flight_date_status.get((flight_number, day)) == "available")

        total = 0.0
        legs_recognized = 0
        reservations_scanned = 0
        details: List[Dict[str, Any]] = []

        if isinstance(reservations, list):
            for res in reservations:
                reservations_scanned += 1
                legs = res.get("flights") or res.get("legs") or []
                if not legs:
                    continue

                # Start with prices on a per-leg basis.
                leg_amts: List[Optional[float]] = []
                has_leg_prices = False
                for leg in legs:
                    amt = GetFlownRevenueForFlight._leg_amount(leg.get("price"), price_component)
                    if amt is not None:
                        has_leg_prices = True
                    leg_amts.append(amt)

                # In the absence of leg prices, divide the reservation base fare evenly.
                if not has_leg_prices:
                    res_total = GetFlownRevenueForFlight._reservation_total(res, price_component)
                    if res_total is not None and len(legs) > 0:
                        equal_share = res_total / len(legs)
                        leg_amts = [equal_share for _ in legs]

                # Identify based on corresponding leg/date.
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
                        details.append({
                            "reservation_id": res.get("reservation_id") or res.get("id"),
                            "flight_number": flight_number,
                            "date": day,
                            "amount": amt
                        })

        payload: Dict[str, Any] = {
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

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_flown_revenue_for_flight",
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
                            "description": "Kept for compatibility; 'total' == 'base_fare' in current data."
                        },
                        "require_available": {"type": "boolean"},
                        "include_details": {"type": "boolean"}
                    },
                    "required": ["flight_number", "start_date", "end_date"]
                }
            }
        }
