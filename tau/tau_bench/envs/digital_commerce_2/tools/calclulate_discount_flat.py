# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _money


class CalclulateDiscountFlat(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], subtotal: Any, discount_amount: Any) -> str:
        if subtotal is None or discount_amount is None:
            return json.dumps(
                {"error": "Missing required fields: subtotal and/or discount_amount"}, indent=2
            )
        try:
            sub = _money(_dec(subtotal))
            disc = _money(_dec(discount_amount))
        except Exception:
            return json.dumps({"error": "subtotal and discount_amount must be numeric"}, indent=2)
        total = _money(max(sub - disc, Decimal("0")))
        return json.dumps({"total": _to_number(total)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_discount_flat",
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
