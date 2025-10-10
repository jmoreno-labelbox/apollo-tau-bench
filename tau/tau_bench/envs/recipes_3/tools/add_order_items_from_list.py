# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddOrderItemsFromList(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: int, store_id: int) -> str:
        order = _require(data, "orders", "order_id", int(order_id))
        if not order:
            return json.dumps({"error": f"order_id {order_id} not found"})
        list_id = int(order.get("list_id"))
        items = [i for i in data.get("grocery_list_items", []) if int(i.get("list_id")) == list_id]
        oi_tbl = _tbl(data, "order_items")
        next_oi = _max_id(oi_tbl, "order_item_id", 10100)
        subtotal = 0
        for it in items:
            ingr_id = int(it.get("ingredient_id"))
            prods = [
                p
                for p in data.get("store_products", [])
                if int(p.get("store_id")) == int(store_id)
                and int(p.get("ingredient_id")) == ingr_id
                and p.get("stock_status_enum") in ("in_stock", "low")
            ]
            prods = sorted(
                prods,
                key=lambda p: (int(p.get("price_cents", 10**9)), int(p.get("product_id", 10**9))),
            )
            if not prods:
                continue
            product = prods[0]
            next_oi += 1
            row = {
                "order_item_id": next_oi,
                "order_id": int(order_id),
                "product_id": int(product.get("product_id")),
                "requested_qty": 1,
                "fulfilled_qty": 1,
                "substitute_product_id": None,
            }
            oi_tbl.append(row)
            subtotal += int(product.get("price_cents", 0))
        order["subtotal_cents"] = subtotal
        order["total_cents"] = subtotal
        # Deterministic field to guarantee write behavior even when no items have been included.
        order["items_populated_at"] = "2025-01-02T11:00:00"
        return json.dumps({"subtotal_cents": subtotal, "total_cents": subtotal})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_order_items_from_list",
                "description": "Populate order_items by selecting lowest-price in-stock products.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "integer"},
                        "store_id": {"type": "integer"},
                    },
                    "required": ["order_id", "store_id"],
                },
            },
        }
