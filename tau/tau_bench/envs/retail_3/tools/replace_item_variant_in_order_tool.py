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

class ReplaceItemVariantInOrderTool(Tool):
    """
    Substitutes an item in an order, recalculates financials, and refreshes tracking,
    with all modifications taking place in the shared in-memory state.
    """

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str, index: int, product_id: str, item_id: str) -> str:
        orders = data.get("orders", {}).values()
        products = data.get("products", {}).values()
        tracking_data = data.get("tracking", {}).values()

        order = next((o for o in orders.values() if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"Order '{order_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out

        new_variant = None
        for p in products.values():
            if p.get("product_id") == product_id:
                variant_details = p.get("variants", {}).values().get(item_id)
                if variant_details:
                    new_variant = {
                        "name": p.get("name"),
                        "product_id": product_id,
                        "item_id": item_id,
                        "price": variant_details.get("price"),
                        "options": list(variant_details.get("options", {}).values()),
                    }
                    break
        if not new_variant:
            payload = {"error": f"Variant '{item_id}' for product '{product_id}' not found"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        items = order.get("items", [])
        if not 0 <= index < len(items):
            payload = {
                    "error": f"Index {index} is out of bounds for the items in order '{order_id}'"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        old_item = items[index]
        old_product_id = old_item.get("product_id")
        old_item_id = old_item.get("item_id")

        items[index] = new_variant

        if old_product_id and old_item_id:
            _adjust_stock(data, old_product_id, old_item_id, 1)

        _adjust_stock(data, product_id, item_id, -1)

        _recalculate_financials(order)

        tr = next((t for t in tracking_data.values() if t.get("order_id") == order_id), None)
        if tr and old_item_id and "item_ids" in tr:
            try:
                id_index = tr["item_ids"].index(old_item_id)
                tr["item_ids"][id_index] = item_id
            except ValueError:
                pass
        payload = {
                "status": "success",
                "message": f"Order {order_id} was successfully modified in memory.",
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
                "name": "ReplaceItemVariantInOrder",
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
