from tau_bench.envs.tool import Tool
from __future__ import annotations
import json
from datetime import date, datetime, timedelta  #required for fallback window enlargement
from decimal import ROUND_HALF_UP, Decimal
from typing import Any
import re
from datetime import date as _date

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
