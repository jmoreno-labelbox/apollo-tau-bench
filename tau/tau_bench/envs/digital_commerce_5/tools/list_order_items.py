# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListOrderItems(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str) -> str:
        order_id = _as_id(order_id)
        order_items = data.get("order_items", [])
        rows = [oi for oi in order_items if _as_id(oi.get("order_id")) == order_id]
        items = [
            {
                "product_id": r.get("product_id"),
                "qty": int(r.get("quantity", 0)),
                "unit_price": float(r.get("price", 0.0)),
                "line_subtotal": round(float(r.get("price", 0.0)) * int(r.get("quantity", 0)), 2),
            }
            for r in rows
        ]
        return json.dumps({"order_id": order_id, "items": items}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_order_items",
                "description": "Return normalized order line items for an order.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }
