# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _money








def _to_number(d: Decimal) -> float:
    return float(d)

def _money(x: Decimal) -> Decimal:
    return x.quantize(_TWOPLACES, rounding=ROUND_HALF_UP)

def _dec(x) -> Decimal:
    return Decimal(str(x))

class ApplyOfferToSubtotal(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], subtotal: Any, offer_code: Any) -> str:
        if subtotal is None or not offer_code:
            return json.dumps(
                {"error": "Missing required fields: subtotal and/or offer_code"}, indent=2
            )
        try:
            sub = _money(_dec(subtotal))
        except Exception:
            return json.dumps({"error": "subtotal must be numeric"}, indent=2)

        offers = list(data.get("offers", {}).values())
        match = next((o for o in offers if o.get("offer_code") == offer_code), None)
        if not match:
            return json.dumps({"valid": False, "reason": "Offer not found"}, indent=2)
        if not match.get("is_active", False):
            return json.dumps({"valid": False, "reason": "Offer is inactive"}, indent=2)

        dtype = match.get("discount_type")
        dval = _dec(match.get("discount_value", 0))

        if dtype == "PERCENTAGE":
            disc = _money(sub * dval / Decimal("100"))
        elif dtype == "FIXED_AMOUNT":
            disc = _money(dval)
        else:
            return json.dumps({"error": f"Unknown discount_type '{dtype}'"}, indent=2)

        total = _money(max(sub - disc, Decimal("0")))
        return json.dumps(
            {
                "valid": True,
                "offer": match,
                "subtotal": _to_number(sub),
                "discount_amount": _to_number(disc),
                "total": _to_number(total),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "apply_offer_to_subtotal",
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