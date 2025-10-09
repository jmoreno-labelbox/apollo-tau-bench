from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal

class CalclulateDiscountFlat(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], subtotal: Any = None, discount_amount: Any = None) -> str:
        if subtotal is None or discount_amount is None:
            payload = {"error": "Missing required fields: subtotal and/or discount_amount"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        try:
            sub = _money(_dec(subtotal))
            disc = _money(_dec(discount_amount))
        except Exception:
            payload = {"error": "subtotal and discount_amount must be numeric"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        total = _money(max(sub - disc, Decimal("0")))
        payload = {"total": _to_number(total)}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateDiscountFlat",
                "description": "Apply a flat discount amount to a subtotal.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subtotal": {
                            "type": "number",
                            "description": "Original subtotal before discount.",
                        },
                        "discount_amount": {
                            "type": "number",
                            "description": "Flat discount amount to subtract.",
                        },
                    },
                    "required": ["subtotal", "discount_amount"],
                },
            },
        }
