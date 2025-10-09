from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal

class CalculateDiscountPercent(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], subtotal: Any = None, discount_percent: Any = None) -> str:
        if subtotal is None or discount_percent is None:
            payload = {"error": "Missing required fields: subtotal and/or discount_percent"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        try:
            sub = _money(_dec(subtotal))
            pct = _dec(discount_percent) / Decimal("100")
        except Exception:
            payload = {"error": "subtotal and discount_percent must be numeric"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        disc = _money(sub * pct)
        total = _money(max(sub - disc, Decimal("0")))
        payload = {"discount_amount": _to_number(disc), "total": _to_number(total)}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateDiscountPercent",
                "description": "Apply a percentage discount to a subtotal.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subtotal": {
                            "type": "number",
                            "description": "Original subtotal before discount.",
                        },
                        "discount_percent": {
                            "type": "number",
                            "description": "Discount percentage to apply.",
                        },
                    },
                    "required": ["subtotal", "discount_percent"],
                },
            },
        }
