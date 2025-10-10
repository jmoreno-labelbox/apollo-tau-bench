# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ProposeSubstituteProducts(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        store_id: int,
        flagged_items: List[Dict[str, Any]],
        require_peanut_free: bool = False,
    ) -> str:
        suggestions = []
        for f in flagged_items or []:
            iid = int(f.get("ingredient_id"))
            ing = _ingredient_by_id(data, iid)
            if require_peanut_free and ing and not bool(ing.get("peanut_free_flag", True)):
                continue
            prods = [
                p
                for p in data.get("store_products", [])
                if int(p.get("store_id")) == int(store_id)
                and int(p.get("ingredient_id")) == iid
                and p.get("stock_status_enum") in ("in_stock", "low")
            ]
            prods = sorted(
                prods,
                key=lambda p: (int(p.get("price_cents", 10**9)), int(p.get("product_id", 10**9))),
            )
            best = prods[0] if prods else None
            if best:
                suggestions.append(
                    {
                        "ingredient_id": iid,
                        "substitute_ingredient_id": iid,
                        "substitute_product_id": int(best.get("product_id")),
                    }
                )
        return json.dumps({"substitutions": suggestions})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "propose_substitute_products",
                "description": "Suggest in-store substitute products for flagged items.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {"type": "integer"},
                        "flagged_items": {"type": "array", "items": {"type": "object"}},
                        "require_peanut_free": {"type": "boolean"},
                    },
                    "required": ["store_id", "flagged_items"],
                },
            },
        }
