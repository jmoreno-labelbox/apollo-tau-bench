# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool








def _round2(x) -> float:
    return float(Decimal(str(x)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))

def _norm_status(s: str) -> str:
    return (s or "").strip().lower()

def _json(data: Any) -> str:
    return json.dumps(data, indent=2, sort_keys=True, default=str)

class SetTicketPrice(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], *,
        flight_number: str,
        date: str,
        fare_class: str,
        price: float,
        require_available: bool = False,
    ) -> str:
        flights = list(data.get("flights", {}).values())
        if isinstance(flights, dict):
            f = flights.get(flight_number)
        elif isinstance(flights, list):
            f = next((row for row in flights if row.get("flight_number") == flight_number), None)
        else:
            f = None

        if not f:
            return _json({"error": "flight_not_found", "flight_number": flight_number})

        if not isinstance(f.get("dates"), dict):
            return _json({"error": "date_not_found", "date": date})
        d = f["dates"].get(date)
        if not d:
            return _json({"error": "date_not_found", "date": date})

        # standardize status and apply enforcement if necessary
        status = _norm_status(d.get("status"))
        if require_available and status != "available":
            return _json({
                "error": "invalid_status",
                "reason": f"Flight {flight_number} on {date} has status '{status}', "
                          f"cannot set ticket price unless 'available'."
            })

        # --- Canonical write: prices are stored in the 'prices' bucket for dated flights ---
        prices = d.setdefault("prices", {})
        new_price = _round2(float(price))
        changed = int(prices.get(fare_class) != new_price)
        prices[fare_class] = new_price

        # Post-snapshot for validation
        after = {
            "flight_number": flight_number,
            "date": date,
            "status": status,
            "available_seats": d.get("available_seats", {}),
            "prices": d.get("prices", {}),
        }

        return _json({
            "success": True,
            "flight_number": flight_number,
            "date": date,
            "fare_class": fare_class,
            "price": new_price,
            "status": status,
            "changed": changed,
            "no_change": (changed == 0),
            "after": after
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_ticket_price",
                "description": "Set the ticket price for a given fare_class on a flight date (writes to canonical 'prices'). Optionally enforce that the flight must be 'available'. Returns a verification snapshot.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "date": {"type": "string", "description": "YYYY-MM-DD"},
                        "fare_class": {"type": "string"},
                        "price": {"type": "number"},
                        "require_available": {
                            "type": "boolean",
                            "description": "If true, only allow when status=='available'. Default false."
                        }
                    },
                    "required": ["flight_number", "date", "fare_class", "price"]
                }
            }
        }