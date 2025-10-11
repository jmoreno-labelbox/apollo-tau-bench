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

def _get_flight(data: Dict[str, Any], flight_number: str) -> Optional[Dict[str, Any]]:
    for f in data.get("flights", []):
        if f.get("flight_number") == flight_number:
            return f
    return None

class UpdateFlightInventoryAndPrices(Tool):
    """
    Partially update a flight instance (by date):
      - available_seats (per cabin) [optional, merge]
      - prices (per cabin) [optional, merge, rounded to 2dp HALF_UP]
      - status [optional]
    Only provided fields/keys are updated; others remain unchanged.
    Creates the date record if missing (policy-allowed).
    Cabins are not hard-coded; keys come from existing flight data or the payload.
    Accepts one or multiple cabins per call for both available_seats and prices.
    Auto-sets status='available' before price/seat writes if date is not available.
    """

    @staticmethod
    def _existing_cabins(route: Dict[str, Any], date: str) -> Set[str]:
        cabins: Set[str] = set()
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
        data: Dict[str, Any], *,
        flight_number: str,
        date: str,
        available_seats: Optional[Dict[str, Any]] = None,
        prices: Optional[Dict[str, Any]] = None,
        status: Optional[str] = None
    ) -> str:
        if available_seats is None and prices is None and status is None:
            return _json({"error": "no_update_fields_provided"})

        route = _get_flight(data, flight_number)
        if not route:
            return _json({"error": "flight_not_found", "flight_number": flight_number})

        dates = route.setdefault("dates", {})
        date_info = dates.setdefault(date, {
            "status": "available",
            "available_seats": {},
            "prices": {}
        })

        # Optional state (check if enum enforcement is applied)
        status_updated = False
        if status is not None:
            s = _norm_status(status)
            if s and s not in FLIGHT_STATUS:
                return _json({
                    "error": "invalid_status",
                    "entity": "flight",
                    "provided": status,
                    "allowed": sorted(list(FLIGHT_STATUS))
                })
            if date_info.get("status") != s:
                date_info["status"] = s
                status_updated = True

        # When specifying seats/prices (regardless of cabin count), verify the availability condition (automatically set to 'available' if required).
        writing_inventory = isinstance(available_seats, dict) and len(available_seats) > 0
        writing_prices = isinstance(prices, dict) and len(prices) > 0
        if (writing_inventory or writing_prices) and _norm_status(date_info.get("status")) != "available":
            date_info["status"] = "available"
            status_updated = True

        # Optional logging of identified cabins (retained for future diagnostics)
        _ = UpdateFlightInventoryAndPrices._existing_cabins(route, date)

        changed = 0

        # Combine seats (using all supplied keys)
        if writing_inventory:
            seat_map = date_info.setdefault("available_seats", {})
            for cabin_key, v in available_seats.items():
                try:
                    iv = int(v)
                    if iv < 0:
                        return _json({"error": "available_seats_negative", "cabin": cabin_key})
                except Exception:
                    return _json({"error": "available_seats_not_int", "cabin": cabin_key, "value": v})
                if seat_map.get(cabin_key) != iv:
                    seat_map[cabin_key] = iv
                    changed += 1

        # Combine prices (using all specified keys) with rounding applied.
        if writing_prices:
            price_map = date_info.setdefault("prices", {})
            for cabin_key, v in prices.items():
                try:
                    fv = float(v)
                    if fv < 0:
                        return _json({"error": "prices_negative", "cabin": cabin_key})
                except Exception:
                    return _json({"error": "prices_not_number", "cabin": cabin_key, "value": v})
                rv = _round2(fv)
                if price_map.get(cabin_key) != rv:
                    price_map[cabin_key] = rv
                    changed += 1

        if status_updated:
            changed += 1

        updated = {
            "status_updated": bool(status_updated),
            "available_seats_keys": sorted(list(available_seats.keys())) if isinstance(available_seats, dict) else [],
            "prices_keys": sorted(list(prices.keys())) if isinstance(prices, dict) else []
        }

        # Provide a daily snapshot for prompt confirmation.
        return _json({
            "flight_number": flight_number,
            "date": date,
            "status": _norm_status(date_info.get("status")),
            "available_seats": date_info.get("available_seats", {}),
            "prices": date_info.get("prices", {}),
            "changed": int(changed > 0),
            "no_change": (changed == 0),
            "updated": updated
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_flight_inventory_and_prices",
                "description": (
                    "Partially updates a flight's per-date inventory/prices/status (verification-by-return). "
                    "Only provided cabins are changed; others remain untouched. "
                    "Creates the date record if missing (policy-allowed). Prices are rounded to 2 decimals. "
                    "Accepts multiple cabins in a single call and ensures availability before price/seat writes."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "date": {"type": "string", "description": "YYYY-MM-DD"},
                        "available_seats": {
                            "type": "object",
                            "description": "Per-cabin seat counts to update (merge). One or multiple keys.",
                            "additionalProperties": {"type": "integer"}
                        },
                        "prices": {
                            "type": "object",
                            "description": "Per-cabin prices to update (merge). One or multiple keys.",
                            "additionalProperties": {"type": "number"}
                        },
                        "status": {"type": "string"}
                    },
                    "required": ["flight_number", "date"],
                    "additionalProperties": False
                }
            }
        }