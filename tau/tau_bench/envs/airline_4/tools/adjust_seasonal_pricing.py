# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AdjustSeasonalPricing(Tool):
    """
    Repeat-safe seasonal multiplier:
      - Multiplies prices in [start_date, end_date] by `multiplier`, HALF-UP to 2dp.
      - Optional `fare_class` restricts the change to a single cabin; otherwise all cabins present are changed.
      - Dedupe via a deterministic audit keyed by (flight_number, date, cabin, multiplier): if the same audit exists,
        the call no-ops for that (date, cabin).
      - If a target date's status != 'available', set it to 'available' before writing (compliant same-call availability).
      - Returns a capped preview of first N changes.
    """
    @staticmethod
    def invoke(
        data: Dict[str, Any], *,
        flight_number: str,
        start_date: str,
        end_date: str,
        multiplier: float = 1.0,
        max_preview: int = 0,
        fare_class: Optional[str] = None,
        dedupe: bool = True,  # repeat-safe by default
    ) -> str:
        # validate dates/window
        try:
            sd = date.fromisoformat(start_date)
            ed = date.fromisoformat(end_date)
        except Exception:
            return _json({"error": "invalid_date_format"})
        if sd > ed:
            return _json({"error": "invalid_date_range", "start_date": start_date, "end_date": end_date})

        # normalize inputs
        fare_class = (fare_class or "").strip().lower() or None
        mult_dec = Decimal(str(multiplier))
        f = _get_flight(data, flight_number)
        if not f:
            return _json({"error": "flight_not_found"})

        # audit store + deterministic id generator
        audits = data.setdefault("seasonal_multiplier_audits", [])  # list of dict
        preview: List[Dict[str, Any]] = []
        changed = 0

        # iterate deterministically by date
        for d in sorted((f.get("dates") or {}).keys()):
            if not (start_date <= d <= end_date):
                continue
            rec = (f.get("dates") or {}).get(d) or {}
            # ensure availability for price writes
            if _norm_status(rec.get("status")) != "available":
                rec["status"] = "available"

            prices = rec.get("prices")
            if not isinstance(prices, dict):
                continue

            # cabins to consider
            cabins = [fare_class] if fare_class else list(prices.keys())

            for cab in cabins:
                if cab not in prices:
                    continue

                # dedupe check per (flight, date, cabin, multiplier)
                if dedupe:
                    exists = next((
                        a for a in audits
                        if a.get("flight_number") == flight_number
                        and a.get("date") == d
                        and a.get("cabin") == cab
                        and float(a.get("multiplier")) == float(multiplier)
                    ), None)
                    if exists:
                        # already applied; skip
                        continue

                try:
                    base = Decimal(str(prices[cab]))
                except Exception:
                    continue

                oldp = float(base.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
                newp = float((base * mult_dec).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
                if newp != oldp:
                    rec["prices"][cab] = newp
                    changed += 1
                    if len(preview) < max_preview:
                        preview.append({"date": d, "cabin": cab, "old": oldp, "new": newp})

                # record audit (even if no change, we can still log intent; keeping it to changed-only reduces noise)
                audit_id = _next_change_id(data, prefix="SM")
                audits.append({
                    "id": audit_id,
                    "type": "seasonal_multiplier",
                    "flight_number": flight_number,
                    "date": d,
                    "cabin": cab,
                    "multiplier": float(multiplier),
                })

        return _json({
            "success": True,
            "flight_number": flight_number,
            "start_date": start_date,
            "end_date": end_date,
            "multiplier": float(mult_dec),
            "fare_class": fare_class,
            "dedupe": bool(dedupe),
            "changed": changed,
            "preview": preview
        })

    @staticmethod
    def get_info():
        return {
            "type":"function",
            "function": {
                "name": "adjust_seasonal_pricing",
                "description": "Repeat-safe seasonal multiplier over a date window with audit dedupe.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"},
                        "multiplier": {"type": "number"},
                        "max_preview": {"type": "integer"},
                        "fare_class": {"type": "string", "enum": ["basic_economy", "economy", "business"]},
                        "dedupe": {"type": "boolean", "description": "Default true; If true, skip when identical multiplier audit exists."},
                    },
                    "required": ["flight_number", "start_date", "end_date", "multiplier"],
                    "additionalProperties": False
                }
            }
        }
