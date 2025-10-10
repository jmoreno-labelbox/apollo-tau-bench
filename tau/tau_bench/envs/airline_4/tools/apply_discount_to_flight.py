# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ApplyDiscountToFlight(Tool):
    """Apply a percentage discount to a flight/date/fare_class (modifies price in-place).
    Also logs a deterministic audit record to data["price_changes"] with an incrementing id (no timestamps).
    """
    @staticmethod
    def invoke(
        data: Dict[str, Any], *,
        flight_number: str,
        fare_class: str,
        date: str,
        percent: float
    ) -> str:
        # percent parsing & validation
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

        # apply discount to BASE FARE; taxes/fees untouched
        new_price = round(old_price * (1 - percent / 100.0), 2)
        if new_price < 0:
            new_price = 0.0

        prices[fare_class] = new_price

        # --- deterministic audit record (NO timestamp) ---
        change_id = _next_change_id(data, prefix="PC")
        (data.setdefault("price_changes", [])).append({
            "id": change_id,
            "type": "discount",
            "flight_number": flight_number,
            "date": date,
            "fare_class": fare_class,
            "old": round(old_price, 2),
            "new": new_price
            # no timestamp for determinism per policy
        })

        return _json({
            "success": True,
            "audit_id": change_id,
            "flight_number": flight_number,
            "date": date,
            "fare_class": fare_class,
            "discount_percent": percent,
            "old_price": round(old_price, 2),
            "new_price": new_price
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "apply_discount_to_flight",
                "description": (
                    "Apply a percent discount to the BASE FARE for a given flight/date/fare_class. "
                    "Creates an audit record in data['price_changes'] and returns its audit_id."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "date": {"type": "string"},
                        "fare_class": {"type": "string", "enum": ["basic_economy", "economy", "business"]},
                        "percent": {"type": "number"}
                    },
                    "required": ["flight_number", "date", "fare_class", "percent"]
                }
            }
        }
