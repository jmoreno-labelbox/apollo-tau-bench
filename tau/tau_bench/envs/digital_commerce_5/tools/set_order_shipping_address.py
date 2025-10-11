# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _err(msg: str) -> str:
    return json.dumps({"error": msg}, indent=2)

def _as_id(x: Any) -> str:
    if x is None:
        return x
    if isinstance(x, str):
        return x
    if isinstance(x, int):
        return str(x)
    if isinstance(x, float) and x.is_integer():
        return str(int(x))
    return str(x)

class SetOrderShippingAddress(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, address: str) -> str:
        order_id = _as_id(order_id)
        if not order_id or address is None:
            return _err("order_id and address are required.")
        orders = list(data.get("orders", {}).values())
        order = next((o for o in orders if _as_id(o.get("order_id")) == order_id), None)
        if not order:
            return _err("Order not found.")
        order["shipping_address_used"] = address
        return json.dumps({"order_id": order_id, "shipping_address_used": address}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_order_shipping_address",
                "description": "Attach a shipping address to an order (explicit object).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "address": {"type": "object"},
                    },
                    "required": ["order_id", "address"],
                },
            },
        }