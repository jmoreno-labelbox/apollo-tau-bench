# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RemovePaymentByIndexTool(Tool):
    """
    Remove a payment/refund entry from an order's payment_history by index.

    Behavior:
    - Validates the order exists and index is within range.
    - Removes payment_history[index].

    Input (kwargs):
        order_id (str, required)
        index (int, required)   # Zero-indexed

    Output:
        JSON string with {"order_id","removed":true,"payment_history_len"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], index, order_id) -> str:

        if not order_id or index is None:
            return json.dumps({"error": "order_id and index are required"}, indent=2)

        try:
            idx = int(index)
        except Exception:
            return json.dumps({"error": "index must be an integer"}, indent=2)

        orders = list(data.get("orders", {}).values())
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            return json.dumps({"error": f"order_id '{order_id}' not found"}, indent=2)

        history = order.get("payment_history", [])
        if not (0 <= idx < len(history)):
            return json.dumps(
                {"error": f"index out of range 0..{max(0, len(history)-1)}"}, indent=2
            )

        history.pop(idx)
        order["payment_history"] = history

        return json.dumps(
            {
                "order_id": order_id,
                "removed": True,
                "payment_history_len": len(history),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_payment_by_index",
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
