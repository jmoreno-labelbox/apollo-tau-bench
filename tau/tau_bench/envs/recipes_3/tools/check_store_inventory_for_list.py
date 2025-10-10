# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CheckStoreInventoryForList(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], list_id: int, store_id: int) -> str:
        items = [
            i for i in data.get("grocery_list_items", []) if int(i.get("list_id")) == int(list_id)
        ]
        results: List[Dict[str, Any]] = []
        rank = {"in_stock": 0, "low": 1, "out_of_stock": 2}
        for it in items:
            iid = int(it.get("ingredient_id"))
            prods = [
                p
                for p in data.get("store_products", [])
                if int(p.get("store_id")) == int(store_id) and int(p.get("ingredient_id")) == iid
            ]
            prods_sorted = sorted(
                prods,
                key=lambda p: (
                    rank.get(p.get("stock_status_enum"), 3),
                    int(p.get("price_cents", 10**9)),
                    int(p.get("product_id", 10**9)),
                ),
            )
            best = prods_sorted[0] if prods_sorted else None
            results.append(
                {
                    "item_id": int(it.get("item_id")),
                    "ingredient_id": iid,
                    "matched_product_id": int(best.get("product_id")) if best else None,
                    "stock_status_enum": (
                        best.get("stock_status_enum") if best else "out_of_catalog"
                    ),
                    "price_cents": int(best.get("price_cents", 0)) if best else None,
                }
            )
        return _json({"store_check": results})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_store_inventory_for_list",
                "description": "Check availability for list items at a store and choose best deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {"list_id": {"type": "integer"}, "store_id": {"type": "integer"}},
                    "required": ["list_id", "store_id"],
                },
            },
        }
