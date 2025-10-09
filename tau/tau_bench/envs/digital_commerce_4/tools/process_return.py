from tau_bench.envs.tool import Tool
import json
from typing import Any

class ProcessReturn(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: str, items: list[dict[str, Any]]) -> str:
        order_id = _sid(order_id)
        norm_items: list[dict[str, Any]] = []
        for it in items or []:
            pid = _sid(it.get("product_id"))
            qty = int(it.get("quantity", 1))
            reason = it.get("reason", "customer_request")
            norm_items.append({"product_id": pid, "quantity": qty, "reason": reason})
        orders = data.get("orders", [])
        order = next((o for o in orders if _eq(o.get("order_id"), order_id)), None)
        if not order:
            payload = {"error": f"order {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        if order.get("status") not in ("Delivered", "Return Pending"):
            payload = {"error": "return not allowed for this status"}
            out = json.dumps(payload, indent=2)
            return out
        order["status"] = "Delivered"
        _append_audit(data, "PROCESS_RETURN", order_id, {"items": norm_items})
        _ws_append(data, order_id, "PROCESS_RETURN", {"items": norm_items})
        payload = {"order_id": order_id, "order_status": order["status"]}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ProcessReturn",
                "description": "Process a return by incrementing product stock and normalizing order status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "items": {"type": "array", "items": {"type": "object"}},
                    },
                    "required": ["order_id", "items"],
                },
            },
        }
