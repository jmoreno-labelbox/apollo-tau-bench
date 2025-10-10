# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CheckStoreInventoryForPlanByKeys(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int, week_start_date: str, store_id: int) -> str:
        plan = next(
            (
                p
                for p in data.get("meal_plans", [])
                if int(p.get("household_id")) == int(household_id)
                and str(p.get("week_start_date")) == str(week_start_date)
            ),
            None,
        )
        if not plan:
            return json({"store_check": []})
        gl = next(
            (
                lt
                for lt in data.get("grocery_lists", [])
                if int(lt.get("source_meal_plan_id")) == int(plan.get("meal_plan_id"))
            ),
            None,
        )
        if not gl:
            return json({"store_check": []})
        items = [
            i
            for i in data.get("grocery_list_items", [])
            if int(i.get("list_id")) == int(gl.get("list_id"))
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
        return json({"store_check": results})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_store_inventory_for_plan_by_keys",
                "description": "Check availability for list items linked to (household_id, week_start_date) at a store.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                        "store_id": {"type": "integer"},
                    },
                    "required": ["household_id", "week_start_date", "store_id"],
                },
            },
        }
