from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ApplyOfferToSubtotal(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], subtotal: Any, offer_code: Any) -> str:
        if subtotal is None or not offer_code:
            payload = {"error": "Missing required fields: subtotal and/or offer_code"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        try:
            sub = _money(_dec(subtotal))
        except Exception:
            payload = {"error": "subtotal must be numeric"}
            out = json.dumps(payload, indent=2)
            return out

        offers = data.get("offers", {}).values()
        match = next((o for o in offers.values() if o.get("offer_code") == offer_code), None)
        if not match:
            payload = {"valid": False, "reason": "Offer not found"}
            out = json.dumps(payload, indent=2)
            return out
        if not match.get("is_active", False):
            payload = {"valid": False, "reason": "Offer is inactive"}
            out = json.dumps(payload, indent=2)
            return out

        dtype = match.get("discount_type")
        dval = _dec(match.get("discount_value", 0))

        if dtype == "PERCENTAGE":
            disc = _money(sub * dval / Decimal("100"))
        elif dtype == "FIXED_AMOUNT":
            disc = _money(dval)
        else:
            payload = {"error": f"Unknown discount_type '{dtype}'"}
            out = json.dumps(payload, indent=2)
            return out

        total = _money(max(sub - disc, Decimal("0")))
        payload = {
                "valid": True,
                "offer": match,
                "subtotal": _to_number(sub),
                "discount_amount": _to_number(disc),
                "total": _to_number(total),
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ApplyOfferToSubtotal",
                "description": "Validate an offer and compute discount+total for a subtotal.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subtotal": {"type": "number"},
                        "offer_code": {"type": "string"},
                    },
                    "required": ["subtotal", "offer_code"],
                },
            },
        }
