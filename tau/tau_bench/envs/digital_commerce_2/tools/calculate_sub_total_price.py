from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal

class CalculateSubTotalPrice(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], items: list[dict[str, Any]]) -> str:
        if not items or not isinstance(items, list):
            payload = {
                    "error": "Missing or invalid 'items'. Expected a list of {product_id, quantity, price}."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        total = Decimal("0")
        for item in items:
            product_id = item.get("product_id")
            quantity = item.get("quantity")
            price = item.get("price")
            if product_id is None or quantity is None or price is None:
                payload = {"error": "Each item must include product_id, quantity, price"}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            try:
                q = int(quantity)
                p = _money(_dec(price))
            except Exception:
                payload = {"error": f"Invalid numeric values for product_id '{product_id}'"}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            line = _money(p * Decimal(q))
            total += line

        total = _money(total)
        payload = {"subtotal": _to_number(total)}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateSubTotalPrice",
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
