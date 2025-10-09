from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime
from typing import Any

class RemoveItemsByIndexTool(Tool):
    """
    Remove items from an order based on index positions within order['items'].

    Behavior:
    - Confirms the order exists and 'indices' is a list of unique integers.
    - Deletes items at the specified indices (0-based) that are present in the current list.
    - Silently ignores out-of-range indices to ensure robustness.

    Input (kwargs):
        order_id (str, required)
        indices (List[int], required)

    Output:
        JSON string with {"order_id","removed_count","items_len"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, indices: list = None) -> str:
        if not order_id or not isinstance(indices, list) or not indices:
            payload = {"error": "order_id and non-empty indices are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        try:
            idxs = sorted({int(i) for i in indices if int(i) >= 0}, reverse=True)
        except Exception:
            payload = {"error": "indices must be a list of integers >= 0"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        orders = data.get("orders", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"order_id '{order_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out

        items = order.get("items", [])
        removed_count = 0
        for i in idxs:
            if 0 <= i < len(items):
                removed_item = items.pop(i)

                product_id = removed_item.get("product_id")
                item_id = removed_item.get("item_id")

                if product_id and item_id:
                    _adjust_stock(data, product_id, item_id, 1)

                removed_count += 1

        order["items"] = items
        payload = {
                "order_id": order_id,
                "removed_count": removed_count,
                "items_len": len(items),
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
                "name": "RemoveItemsByIndex",
                "description": "Remove items from an order by zero-based indices within order['items'].",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "indices": {
                            "type": "array",
                            "items": {"type": "integer", "minimum": 0},
                        },
                    },
                    "required": ["order_id", "indices"],
                },
            },
        }
