# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddItemsToOrderTool(Tool):
    """
    Add one or more items to an existing order by resolving variants from products.json.

    Behavior:
    - Validates the order exists.
    - For each {product_id, item_id, quantity}, resolves the variant from products.json.
    - Appends one entry per unit to order["items"] (consistent with dataset structure).
    - Does not recalculate totals; this tool only amends the item list.

    Input (kwargs):
        order_id (str, required)
        items (List[dict], required) -> {product_id, item_id, quantity?}

    Output:
        JSON string with {"order_id","added_count","items_len"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get("order_id")
        items_spec = kwargs.get("items")

        if not order_id or not isinstance(items_spec, list) or not items_spec:
            return json.dumps({"error": "order_id and non-empty items are required"}, indent=2)

        orders = list(data.get("orders", {}).values())
        products = list(data.get("products", {}).values())
        order = next((o for o in orders if o.get("order_id") == order_id), None)

        if not order:
            return json.dumps({"error": f"order_id '{order_id}' not found"}, indent=2)

        added = 0
        for line in items_spec:
            pid = line.get("product_id")
            iid = line.get("item_id")
            qty = int(line.get("quantity", 1) or 1)

            if not pid or not iid or qty < 1:
                return json.dumps(
                    {"error": "Each item must include product_id, item_id, and quantity>=1"},
                    indent=2,
                )

            product = next((p for p in products if p.get("product_id") == pid), None)
            variant = (product.get("variants") or {}).get(iid) if product else None

            if not variant:
                return json.dumps(
                    {"error": f"Variant not found for product_id='{pid}', item_id='{iid}'"},
                    indent=2,
                )

            resolved_item = {
                "name": product.get("name"),
                "product_id": pid,
                "item_id": iid,
                "price": variant.get("price"),
                "options": variant.get("options", {}),
            }

            for _ in range(qty):
                (order.setdefault("items", [])).append(resolved_item)
                added += 1

            _adjust_stock(data, pid, iid, -qty)

        return json.dumps(
            {
                "order_id": order_id,
                "added_count": added,
                "items_len": len(order.get("items", [])),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_items_to_order",
                "description": "Add one or more resolved product variants into an existing order (orders.json).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "items": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "product_id": {"type": "string"},
                                    "item_id": {"type": "string"},
                                    "quantity": {
                                        "type": "integer",
                                        "minimum": 1,
                                        "default": 1,
                                    },
                                },
                                "required": ["product_id", "item_id"],
                            },
                        },
                    },
                    "required": ["order_id", "items"],
                },
            },
        }
