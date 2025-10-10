# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CheckStoreInventoryForList(Tool):
    """Flag low/out_of_stock items for a list at a given store; attach best in-store option if available."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        list_id = kwargs.get("list_id")
        store_id = kwargs.get("store_id")
        if list_id is None or store_id is None:
            return _json_dump({"error": "list_id and store_id are required"})
        gl_items = [i for i in list(data.get("grocery_list_items", {}).values()) if int(i.get("list_id")) == int(list_id)]
        results = []
        for it in gl_items:
            iid = int(it["ingredient_id"])
            prods = _store_products_for_ingredient(data, int(store_id), iid)
            best = _lowest_price_pref_stock(prods)
            status = best.get("stock_status_enum") if best else "out_of_catalog"
            results.append({
                "item_id": int(it["item_id"]),
                "ingredient_id": iid,
                "matched_product_id": int(best["product_id"]) if best else None,
                "stock_status_enum": status,
                "price_cents": int(best.get("price_cents", 0)) if best else None
            })
        return _json_dump({"store_check": results})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"check_store_inventory_for_list",
            "description":"Check availability for each list item at a store and return best options.",
            "parameters":{"type":"object","properties":{
                "list_id":{"type":"integer"},
                "store_id":{"type":"integer"}
            },"required":["list_id","store_id"]}
        }}
