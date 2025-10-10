# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _first_user_id


class FindSubstituteProducts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        store_id = kwargs.get("store_id")
        flagged_items = kwargs.get("flagged_items")
        list_id = kwargs.get("list_id")
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
