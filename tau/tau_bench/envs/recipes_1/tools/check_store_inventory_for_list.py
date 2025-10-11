# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump








def _store_products_for_ingredient(data: Dict[str, Any], store_id: int, ingredient_id: int) -> List[Dict[str, Any]]:
    return [
        p for p in data.get("store_products", [])
        if int(p.get("store_id")) == store_id and int(p.get("ingredient_id")) == ingredient_id
    ]

def _lowest_price_pref_stock(products: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    # Order by stock preference then price, deterministically
    rank = {"in_stock": 0, "low": 1, "out_of_stock": 2}
    def keyer(p: Dict[str, Any]):
        return (
            rank.get(p.get("stock_status_enum"), 3),
            int(p.get("price_cents", 10**9)),
            int(p.get("product_id", 10**9))
        )
    return sorted(products, key=keyer)[0] if products else None

def _json_dump(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)

class CheckStoreInventoryForList(Tool):
    """Flag low/out_of_stock items for a list at a given store; attach best in-store option if available."""
    @staticmethod
    def invoke(data: Dict[str, Any], list_id, store_id) -> str:
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