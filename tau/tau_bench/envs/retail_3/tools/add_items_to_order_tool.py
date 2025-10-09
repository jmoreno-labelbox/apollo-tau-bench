from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AddItemsToOrderTool(Tool):
    """
    Add one or more items to an existing order by resolving variants from products.json.

    Behavior:
    - Confirms the order exists.
    - For each {product_id, item_id, quantity}, resolves the variant from products.json.
    - Adds one entry per unit to order["items"] (consistent with dataset structure).
    - Does not recalculate totals; this function only modifies the item list.

    Input (kwargs):
        order_id (str, required)
        items (List[dict], required) -> {product_id, item_id, quantity?}

    Output:
        JSON string with {"order_id","added_count","items_len"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, items: list = None) -> str:
        if not order_id or not isinstance(items, list) or not items:
            payload = {"error": "order_id and non-empty items are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        orders = data.get("orders", {}).values()
        products = data.get("products", {}).values()
        order = next((o for o in orders.values() if o.get("order_id") == order_id), None)

        if not order:
            payload = {"error": f"order_id '{order_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out

        added = 0
        for line in items:
            pid = line.get("product_id")
            iid = line.get("item_id")
            qty = int(line.get("quantity", 1) or 1)

            if not pid or not iid or qty < 1:
                payload = {
                        "error": "Each item must include product_id, item_id, and quantity>=1"
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out

            product = next((p for p in products.values() if p.get("product_id") == pid), None)
            variant = (product.get("variants") or {}).get(iid) if product else None

            if not variant:
                payload = {
                        "error": f"Variant not found for product_id='{pid}', item_id='{iid}'"
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out

            resolved_item = {
                "name": product.get("name"),
                "product_id": pid,
                "item_id": iid,
                "price": variant.get("price"),
                "options": list(variant.get("options", {}).values()),
            }

            for _ in range(qty):
                (order.setdefault("items", [])).append(resolved_item)
                added += 1

            _adjust_stock(data, pid, iid, -qty)
        payload = {
                "order_id": order_id,
                "added_count": added,
                "items_len": len(order.get("items", [])),
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
                "name": "AddItemsToOrder",
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
