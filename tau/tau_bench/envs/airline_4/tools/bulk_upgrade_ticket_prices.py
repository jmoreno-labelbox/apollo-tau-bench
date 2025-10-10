from __future__ import annotations
from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, timedelta  #required for fallback window enlargement
from decimal import ROUND_HALF_UP, Decimal
from typing import Any
import re
from datetime import date as _date

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
