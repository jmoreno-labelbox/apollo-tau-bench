# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAverageTicketPrice(Tool):
    """Compute average price for a flight over a date range for a fare_class."""

    @staticmethod
    def _median(vals):
        s = sorted(vals); n = len(s)
        if n == 0: return None
        mid = n//2
        return (s[mid] if n%2 else (s[mid-1]+s[mid])/2)

    @staticmethod
    def _iqr_filter(vals, k=1.5):
        if len(vals) < 4:
            return vals
        s = sorted(vals); n = len(s)
        def q(p):
            if n == 1: return s[0]
            idx = (p/100.0)*(n-1)
            lo, hi = int(idx), min(int(idx)+1, n-1)
            frac = idx - lo
            return s[lo]*(1-frac) + s[hi]*frac
        q1, q3 = q(25), q(75)
        iqr = q3 - q1
        lo, hi = q1 - k*iqr, q3 + k*iqr
        return [v for v in vals if lo <= v <= hi]

    @staticmethod
    def _collect_prices(flight, fare_class, start_date, end_date, exclude_dates):
        prices = []
        used_days = []
        for d, rec in (flight.get("dates") or {}).items():
            if not (start_date <= d <= end_date):
                continue
            if d in exclude_dates:
                continue
            if _norm_status(rec.get("status")) == "available" and rec.get("prices") and fare_class in rec["prices"]:
                prices.append(float(rec["prices"][fare_class]))
                used_days.append(d)
        return prices, used_days

    @staticmethod
    def invoke(
        data: Dict[str, Any], *,
        flight_number: str,
        fare_class: str,
        start_date: str,
        end_date: str,
        exclude_dates: Optional[List[str]] = None,
        outlier_policy: Optional[Dict[str, Any]] = None,
        min_samples: int = 0,
        fallback: Optional[Dict[str, Any]] = None,   # <- permit fallback
        include: Optional[Dict[str, Any]] = None,
        price_component: str = "base_fare"
    ) -> str:

        exclude_dates = set(exclude_dates or [])
        outlier_policy = outlier_policy or {}
        fallback = fallback or {}
        include = include or {}

        if price_component != "base_fare":
            return _json({"error": "invalid_price_component"})

        flight = _get_flight(data, flight_number)
        if not flight:
            return _json({"error":"flight_not_found"})

        # initial attempt
        prices, used_days = GetAverageTicketPrice._collect_prices(
            flight, fare_class, start_date, end_date, exclude_dates
        )

        # conditional outlier removal
        if outlier_policy.get("method") == "iqr":
            try:
                k = float(outlier_policy.get("k", 1.5))
            except Exception:
                k = 1.5
            prices = GetAverageTicketPrice._iqr_filter(prices, k)

        # single attempt fallback expansion
        if min_samples and len(prices) < min_samples and fallback:
            try:
                exp = int(fallback.get("expand_window_days", 0))
                max_exp = int(fallback.get("max_expansions", 0))
            except Exception:
                exp, max_exp = 0, 0
            if exp > 0 and max_exp > 0:
                def shift(day_str, delta_days):
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
                start_date, end_date = s2, e2  # log the enlarged window

        if not prices:
            return _json({"error":"no_prices_in_range"})

        avg_price = _round2(sum(prices)/len(prices))
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
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_average_ticket_price",
                "description": (
                    "Average price over a date range with optional IQR outlier removal. "
                    "Supports optional fallback window expansion."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "fare_class": {"type": "string", "enum": ["basic_economy", "economy", "business"]},
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"},
                        "exclude_dates": {"type": "array", "items": {"type": "string"}},
                        "outlier_policy": {
                            "type": "object",
                            "properties": {
                                "method": {"type": "string", "enum": ["iqr"]},
                                "k": {"type": "number"}
                            }
                        },
                        "min_samples": {"type": "integer"},
                        "fallback": {  # <- fallback for document
                            "type": "object",
                            "properties": {
                                "expand_window_days": {"type": "integer"},
                                "max_expansions": {"type": "integer"}
                            }
                        },
                        "include": {
                            "type": "object",
                            "properties": {
                                "median": {"type": "boolean"},
                                "count": {"type": "boolean"},
                                "excluded_dates": {"type": "boolean"}
                            }
                        },
                        "price_component": {"type": "string", "enum": ["base_fare"]}
                    },
                    "required": ["flight_number", "fare_class", "start_date", "end_date"],
                    "additionalProperties": False
                }
            }
        }
