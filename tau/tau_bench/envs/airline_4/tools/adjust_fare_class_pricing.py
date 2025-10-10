# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AdjustFareClassPricing(Tool):
    """
    Repeat-safe fare adjustment:
      - If target_price is provided, sets the absolute price (canonical set).
      - Else computes target = round2(current + delta) and sets that absolute value.
      - Ensures availability on the date before writing (same-call compliance).
      - Returns before/after snapshot and changed/no_change.
    """

    @staticmethod
    def invoke(
        data: Dict[str, Any], *,
        flight_number: str,
        date: str,
        fare_class: str,
        delta: Optional[float] = None,
        target_price: Optional[float] = None
    ) -> str:
        # normalize inputs
        fare_class = (fare_class or "").strip().lower()

        # validate mutually exclusive/required params
        if target_price is None and delta is None:
            return _json({"error": "invalid_params", "reason": "Provide target_price or delta"})
        if target_price is not None and delta is not None:
            return _json({"error": "invalid_params", "reason": "Provide either target_price or delta, not both"})

        # fetch flight/date record
        flight = _get_flight(data, flight_number)
        if not flight:
            return _json({"error": "flight_not_found"})
        rec = _get_date_record(flight, date)
        if not rec:
            return _json({"error": "price_not_available_for_date"})
        # ensure availability before price write
        if _norm_status(rec.get("status")) != "available":
            rec["status"] = "available"

        prices = rec.setdefault("prices", {})
        if fare_class not in prices:
            return _json({"error": "fare_class_not_found"})

        # read current price
        try:
            cur = float(prices[fare_class])
        except Exception:
            return _json({"error": "invalid_price_value"})

        # compute target
        if target_price is not None:
            try:
                tgt = float(target_price)
            except Exception:
                return _json({"error": "invalid_target_price"})
        else:
            try:
                d = float(delta)  # already validated via not None
            except Exception:
                return _json({"error": "invalid_delta"})
            tgt = cur + d

        # HALF-UP to 2 decimals for both before/after comparison and the write
        cur_r = float(Decimal(str(cur)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
        tgt_r = float(Decimal(str(tgt)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))

        changed = int(tgt_r != cur_r)
        if changed:
            prices[fare_class] = tgt_r

        # after snapshot
        after = {
            "flight_number": flight_number,
            "date": date,
            "status": _norm_status(rec.get("status")),
            "prices": rec.get("prices", {}),
        }

        return _json({
            "success": True,
            "flight_number": flight_number,
            "date": date,
            "fare_class": fare_class,
            "old_price": cur_r,
            "price": tgt_r,
            "changed": changed,
            "no_change": (changed == 0),
            "after": after
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "adjust_fare_class_pricing",
                "description": "Repeat-safe fare adjustment: set absolute price (target_price) or set current+delta as absolute target.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "date": {"type": "string"},
                        "fare_class": {"type": "string", "enum": ["basic_economy", "economy", "business"]},
                        "delta": {"type": "number", "description": "Relative change; converted to absolute target and written."},
                        "target_price": {"type": "number", "description": "Absolute price to set (preferred for idempotency)."}
                    },
                    "required": ["flight_number", "date", "fare_class"],
                    "additionalProperties": False
                }
            }
        }
