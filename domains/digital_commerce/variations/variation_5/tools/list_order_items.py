from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class ListOrderItems(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: Any, order_items: list[dict[str, Any]] = None) -> str:
        order_id = _as_id(order_id)
        order_items = order_items if order_items is not None else data.get("order_items", [])
        rows = [oi for oi in order_items if _as_id(oi.get("order_id")) == order_id]
        items = [
            {
                "product_id": r.get("product_id"),
                "qty": int(r.get("quantity", 0)),
                "unit_price": float(r.get("price", 0.0)),
                "line_subtotal": round(
                    float(r.get("price", 0.0)) * int(r.get("quantity", 0)), 2
                ),
            }
            for r in rows
        ]
        payload = {"order_id": order_id, "items": items}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListOrderItems",
                "description": "Return normalized order line items for an order.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }
