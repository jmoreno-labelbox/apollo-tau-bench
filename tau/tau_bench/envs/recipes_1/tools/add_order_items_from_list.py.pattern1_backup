# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddOrderItemsFromList(Tool):
    """Populate order_items from a list by choosing the lowest-price in-stock product for each ingredient."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get("order_id")
        store_id = kwargs.get("store_id")
        product_overrides = kwargs.get("product_overrides", {})  # optional {ingredient_id: product_id}
        if order_id is None or store_id is None:
            return _json_dump({"error": "order_id and store_id are required"})
        order = _require(data, "orders", "order_id", int(order_id))
        if not order:
            return _json_dump({"error": f"order_id {order_id} not found"})
        list_id = int(order["list_id"])
        items = [i for i in data.get("grocery_list_items", []) if int(i.get("list_id")) == list_id]
        oi_tbl = data.setdefault("order_items", [])
        next_oi = _max_id(oi_tbl, "order_item_id", 10100)
        subtotal = 0
        created_ids: List[int] = []
        for it in items:
            ingr_id = int(it["ingredient_id"])
            override_pid = product_overrides.get(str(ingr_id)) or product_overrides.get(ingr_id)
            product = None
            if override_pid is not None:
                product = next((p for p in data.get("store_products", []) if int(p.get("product_id")) == int(override_pid)), None)
            if product is None:
                prods = _store_products_for_ingredient(data, int(store_id), ingr_id)
                prods = [p for p in prods if p.get("stock_status_enum") in ("in_stock","low")]
                product = _lowest_price_pref_stock(prods)
            if product is None:
                continue
            next_oi += 1
            row = {
                "order_item_id": next_oi,
                "order_id": int(order_id),
                "product_id": int(product.get("product_id")),
                "requested_qty": 1,
                "fulfilled_qty": 1,
                "substitute_product_id": None
            }
            oi_tbl.append(row)
            created_ids.append(next_oi)
            subtotal += int(product.get("price_cents", 0))
        order["subtotal_cents"] = subtotal
        order["total_cents"] = subtotal  # deterministic (no implicit fees)
        return _json_dump({"created_order_item_ids": created_ids, "subtotal_cents": order["subtotal_cents"], "total_cents": order["total_cents"]})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"add_order_items_from_list",
            "description":"Populate order_items by selecting lowest-price in-stock products for each ingredient.",
            "parameters":{"type":"object","properties":{
                "order_id":{"type":"integer"},
                "store_id":{"type":"integer"},
                "product_overrides":{"type":"object"}
            },"required":["order_id","store_id"]}
        }}
