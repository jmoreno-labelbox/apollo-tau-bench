from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime
from typing import Any

class RemovePaymentByIndexTool(Tool):
    """
    Delete a payment/refund entry from an order's payment_history by index.

    Behavior:
    - Confirms the order exists and the index is within range.
    - Deletes payment_history[index].

    Input (kwargs):
        order_id (str, required)
        index (int, required)   # 0-based

    Output:
        JSON string with {"order_id","removed":true,"payment_history_len"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, index: int = None) -> str:
        if not order_id or index is None:
            payload = {"error": "order_id and index are required"}
            out = json.dumps(payload, indent=2)
            return out

        try:
            idx = int(index)
        except Exception:
            payload = {"error": "index must be an integer"}
            out = json.dumps(payload, indent=2)
            return out

        orders = data.get("orders", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"order_id '{order_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out

        history = order.get("payment_history", [])
        if not (0 <= idx < len(history)):
            payload = {"error": f"index out of range 0..{max(0, len(history)-1)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        history.pop(idx)
        order["payment_history"] = history
        payload = {
                "order_id": order_id,
                "removed": True,
                "payment_history_len": len(history),
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RemovePaymentByIndex",
                "description": "Remove a payment/refund entry at a given index from an order's payment_history.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "index": {"type": "integer", "minimum": 0},
                    },
                    "required": ["order_id", "index"],
                },
            },
        }
