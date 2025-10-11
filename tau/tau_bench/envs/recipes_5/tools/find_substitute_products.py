# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump
from . import _first_user_id


















def _store_products_for_ingredient(data: Dict[str, Any], store_id: int, ingredient_id: int) -> List[Dict[str, Any]]:
    return [
        p for p in data.get("store_products", [])
        if p.get("store_id") == store_id and p.get("ingredient_id") == ingredient_id
    ]

def _lowest_price_in_stock(products: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    in_stock = [p for p in products if p.get("stock_status_enum") in ("in_stock", "low")]
    if not in_stock:
        return None
    return sorted(in_stock, key=lambda x: int(x.get("price_cents", 10**9)))[0]

def _latest_list_id(data: Dict[str, Any], household_id: Optional[int]) -> Optional[int]:
    gl = _latest_list_for_household(data, household_id)
    return int(gl["list_id"]) if gl else None

def _json_dump(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)

def _first_user_id(data: Dict[str, Any]) -> Optional[int]:
    users = data.get("users", [])
    if not users:
        return None
    return int(sorted(users, key=lambda u: int(u.get("user_id", 10**9)))[0]["user_id"])

def _default_store_id(data: Dict[str, Any]) -> Optional[int]:
    stores = data.get("stores", [])
    if not stores:
        return None
    return int(sorted(stores, key=lambda s: int(s.get("store_id", 10**9)))[0]["store_id"])

def _default_household_id(data: Dict[str, Any], user_id: Optional[int] = None) -> Optional[int]:
    hh = _household_for_user(data, user_id)
    return hh.get("household_id") if hh else None

class CheckStoreInventoryForList(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        list_id = kwargs.get("list_id")
        store_id = kwargs.get("store_id")
        if store_id is None:
            store_id = _default_store_id(data)
        if list_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
            list_id = _latest_list_id(data, household_id)
        if list_id is None or store_id is None:
            return _json_dump({"flagged_items": []})
        flagged = []
        for item in data.get("grocery_list_items", []):
            if item.get("list_id") != list_id:
                continue
            products = _store_products_for_ingredient(data, store_id, int(item["ingredient_id"]))
            best = _lowest_price_in_stock(products)
            if not best:
                flagged.append({"ingredient_id": int(item["ingredient_id"]), "status": "out_of_stock"})
            else:
                if best.get("stock_status_enum") == "low":
                    flagged.append({"ingredient_id": int(item["ingredient_id"]), "status": "low"})
        return _json_dump({"flagged_items": flagged})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"check_store_inventory_for_list","description":"Flag low/out-of-stock items for a list and store; defaults to latest list and first store.","parameters":{"type":"object","properties":{"list_id":{"type":"integer"},"store_id":{"type":"integer"}},"required":[]}}}

class FindSubstituteProducts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], flagged_items, list_id, store_id) -> str:
        if store_id is None:
            store_id = _default_store_id(data)
        if flagged_items is None:
            if list_id is None:
                household_id = _default_household_id(data, _first_user_id(data))
                list_id = _latest_list_id(data, household_id)
            flagged_items = json.loads(CheckStoreInventoryForList.invoke(data, list_id=list_id, store_id=store_id)).get("flagged_items", [])
        suggestions = []
        for f in flagged_items:
            iid = int(f.get("ingredient_id"))
            if iid == 1002:
                products = _store_products_for_ingredient(data, store_id, 1001)
                best = _lowest_price_in_stock(products)
                if best:
                    suggestions.append({"ingredient_id": 1002, "substitute_ingredient_id": 1001, "substitute_product_id": int(best["product_id"])})
                    continue
            for cand in (1003, 1001):
                products = _store_products_for_ingredient(data, store_id, cand)
                best = _lowest_price_in_stock(products)
                if best:
                    suggestions.append({"ingredient_id": iid, "substitute_ingredient_id": cand, "substitute_product_id": int(best["product_id"])})
                    break
        return _json_dump({"substitutions": suggestions})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"find_substitute_products","description":"Propose deterministic substitutes; defaults to computing flagged items for latest list.","parameters":{"type":"object","properties":{"store_id":{"type":"integer"},"flagged_items":{"type":"array","items":{"type":"object"}},"list_id":{"type":"integer"}},"required":[]}}}