# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateDiscountPercent(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], subtotal: Any, discount_percent: Any) -> str:
        if subtotal is None or discount_percent is None:
            return json.dumps(
                {"error": "Missing required fields: subtotal and/or discount_percent"}, indent=2
            )
        try:
            sub = _money(_dec(subtotal))
            pct = _dec(discount_percent) / Decimal("100")
        except Exception:
            return json.dumps({"error": "subtotal and discount_percent must be numeric"}, indent=2)

        disc = _money(sub * pct)
        total = _money(max(sub - disc, Decimal("0")))
        return json.dumps(
            {"discount_amount": _to_number(disc), "total": _to_number(total)}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_discount_percent",
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
