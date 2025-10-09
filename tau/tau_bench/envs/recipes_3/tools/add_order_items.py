from tau_bench.envs.tool import Tool
import json
from typing import Any

class AddOrderItems(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: int, items: list[dict[str, Any]]) -> str:
        table = _get_table(data, "order_items")
        next_id = _max_int(table, "order_item_id", 0)
        count = 0
        for it in items or []:
            next_id += 1
            rec = {
                "order_item_id": next_id,
                "order_id": order_id,
                "product_id": it.get("product_id"),
                "requested_qty": it.get("requested_qty"),
                "fulfilled_qty": it.get("fulfilled_qty"),
                "substitute_product_id": it.get("substitute_product_id"),
            }
            table.append(rec)
            count += 1
        payload = {"count": count}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddOrderItems",
                "description": "Appends order_items for an order with deterministic order_item_ids.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "integer"},
                        "items": {"type": "array"},
                    },
                    "required": ["order_id", "items"],
                },
            },
        }
