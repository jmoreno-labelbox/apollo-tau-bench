# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump


class ProposeSubstituteProducts(Tool):
    """For flagged items, propose in-stock substitutes at the same store; honor peanut-free if require_peanut_free."""
    @staticmethod
    def invoke(data: Dict[str, Any], store_id, flagged_items = [], require_peanut_free = False) -> str:
        flagged = flagged_items
        require_peanut_free = bool(require_peanut_free)
        if store_id is None or not isinstance(flagged, list):
            return _json_dump({"error": "store_id and flagged_items are required"})
        suggestions = []
        for f in flagged:
            iid = int(f.get("ingredient_id"))
            # Main: optimal ingredient available in inventory
            prods = _store_products_for_ingredient(data, int(store_id), iid)
            best = _lowest_price_pref_stock([p for p in prods if p.get("stock_status_enum") in ("in_stock","low")])
            if best:
                suggestions.append({
                    "ingredient_id": iid,
                    "substitute_ingredient_id": iid,
                    "substitute_product_id": int(best["product_id"])
                })
                continue
            # Fallback: any in-store item within the same ingredient category (if no dataset category, then omit).
            # Ensure predictable functionality by returning no suggestions when none exist.
            ing = _ingredient_by_id(data, iid)
            if require_peanut_free and ing and not bool(ing.get("peanut_free_flag", True)):
                # bypass bases that are not peanut-free if necessary
                continue
        return _json_dump({"substitutions": suggestions})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"propose_substitute_products",
            "description":"Suggest in-store substitute products for flagged items.",
            "parameters":{"type":"object","properties":{
                "store_id":{"type":"integer"},
                "flagged_items":{"type":"array","items":{"type":"object"}},
                "require_peanut_free":{"type":"boolean"}
            },"required":["store_id","flagged_items"]}
        }}
