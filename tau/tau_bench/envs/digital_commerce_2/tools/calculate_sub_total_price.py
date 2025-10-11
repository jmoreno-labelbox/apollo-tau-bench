# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _money


class CalculateSubTotalPrice(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], items: Any) -> str:
        items: List[Dict[str, Any]] = items
        if not items or not isinstance(items, list):
            return json.dumps(
                {
                    "error": "Missing or invalid 'items'. Expected a list of {product_id, quantity, price}."
                },
                indent=2,
            )

        total = Decimal("0")
        for item in items:
            product_id = item.get("product_id")
            quantity = item.get("quantity")
            price = item.get("price")
            if product_id is None or quantity is None or price is None:
                return json.dumps(
                    {"error": "Each item must include product_id, quantity, price"}, indent=2
                )
            try:
                q = int(quantity)
                p = _money(_dec(price))
            except Exception:
                return json.dumps(
                    {"error": f"Invalid numeric values for product_id '{product_id}'"}, indent=2
                )
            line = _money(p * Decimal(q))
            total += line

        total = _money(total)
        return json.dumps({"subtotal": _to_number(total)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_sub_total_price",
                "description": "Calculate subtotal price from a list of products, their quantities, and prices.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "items": {
                            "type": "array",
                            "description": "List of products with quantity and price.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "product_id": {"type": "string"},
                                    "quantity": {"type": "integer"},
                                    "price": {"type": "number"},
                                },
                                "required": ["product_id", "quantity", "price"],
                            },
                        }
                    },
                    "required": ["items"],
                },
            },
        }
