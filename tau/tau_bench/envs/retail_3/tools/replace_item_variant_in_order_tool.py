# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReplaceItemVariantInOrderTool(Tool):
    """
    Replaces an item in an order, recalculates financials, and updates tracking,
    with all changes occurring in the shared in-memory state.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get("order_id")
        index = kwargs.get("index")
        product_id = kwargs.get("product_id")
        item_id = kwargs.get("item_id")

        orders = list(data.get("orders", {}).values())
        products = list(data.get("products", {}).values())
        tracking_data = data.get("tracking", [])

        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            return json.dumps({"error": f"Order '{order_id}' not found"}, indent=2)

        new_variant = None
        for p in products:
            if p.get("product_id") == product_id:
                variant_details = p.get("variants", {}).get(item_id)
                if variant_details:
                    new_variant = {
                        "name": p.get("name"),
                        "product_id": product_id,
                        "item_id": item_id,
                        "price": variant_details.get("price"),
                        "options": variant_details.get("options", {}),
                    }
                    break
        if not new_variant:
            return json.dumps(
                {"error": f"Variant '{item_id}' for product '{product_id}' not found"}, indent=2
            )

        items = order.get("items", [])
        if not 0 <= index < len(items):
            return json.dumps(
                {"error": f"Index {index} is out of bounds for the items in order '{order_id}'"},
                indent=2,
            )

        old_item = items[index]
        old_product_id = old_item.get("product_id")
        old_item_id = old_item.get("item_id")

        items[index] = new_variant

        if old_product_id and old_item_id:
            _adjust_stock(data, old_product_id, old_item_id, 1)

        _adjust_stock(data, product_id, item_id, -1)

        _recalculate_financials(order)

        tr = next((t for t in tracking_data if t.get("order_id") == order_id), None)
        if tr and old_item_id and "item_ids" in tr:
            try:
                id_index = tr["item_ids"].index(old_item_id)
                tr["item_ids"][id_index] = item_id
            except ValueError:
                pass

        return json.dumps(
            {
                "status": "success",
                "message": f"Order {order_id} was successfully modified in memory.",
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "replace_item_variant_in_order",
                "description": "Replaces an item in an order with a new variant and updates financials and tracking in memory.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "index": {"type": "integer"},
                        "product_id": {"type": "string"},
                        "item_id": {"type": "string"},
                    },
                    "required": ["order_id", "index", "product_id", "item_id"],
                },
            },
        }
