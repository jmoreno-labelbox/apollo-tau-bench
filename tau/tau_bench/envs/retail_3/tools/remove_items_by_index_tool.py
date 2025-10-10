# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RemoveItemsByIndexTool(Tool):
    """
    Remove items from an order by index positions within order['items'].

    Behavior:
    - Validates the order exists and 'indices' is a list of distinct integers.
    - Removes items at the provided indices (0-based) present in the current list.
    - Ignores out-of-range indices silently to be robust.

    Input (kwargs):
        order_id (str, required)
        indices (List[int], required)

    Output:
        JSON string with {"order_id","removed_count","items_len"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], indices, order_id) -> str:

        if not order_id or not isinstance(indices, list) or not indices:
            return json.dumps({"error": "order_id and non-empty indices are required"}, indent=2)

        try:
            idxs = sorted({int(i) for i in indices if int(i) >= 0}, reverse=True)
        except Exception:
            return json.dumps({"error": "indices must be a list of integers >= 0"}, indent=2)

        orders = list(data.get("orders", {}).values())
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            return json.dumps({"error": f"order_id '{order_id}' not found"}, indent=2)

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
        return json.dumps(
            {"order_id": order_id, "removed_count": removed_count, "items_len": len(items)},
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_items_by_index",
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
