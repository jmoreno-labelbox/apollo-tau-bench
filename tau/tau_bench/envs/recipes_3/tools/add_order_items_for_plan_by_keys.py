# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddOrderItemsForPlanByKeys(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int, week_start_date: str, store_id: int) -> str:
        # Resolve order by keys (choose highest order_id for determinism if multiple)
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
            return _json({"error": "meal_plan not found for keys"})
        gl = next(
            (
                lt
                for lt in data.get("grocery_lists", [])
                if int(lt.get("source_meal_plan_id")) == int(plan.get("meal_plan_id"))
            ),
            None,
        )
        if not gl:
            return _json({"error": "grocery_list not found for plan"})
        orders = [
            o
            for o in list(data.get("orders", {}).values())
            if int(o.get("household_id")) == int(household_id)
            and int(o.get("store_id")) == int(store_id)
            and int(o.get("list_id")) == int(gl.get("list_id"))
        ]
        if not orders:
            return _json({"error": "order not found for keys"})
        order = sorted(orders, key=lambda o: int(o.get("order_id", 0)), reverse=True)[0]
        # Reuse AddOrderItemsFromList logic deterministically
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
                "order_id": int(order.get("order_id")),
                "product_id": int(product.get("product_id")),
                "requested_qty": 1,
                "fulfilled_qty": 1,
                "substitute_product_id": None,
            }
            oi_tbl.append(row)
            subtotal += int(product.get("price_cents", 0))
        order["subtotal_cents"] = subtotal
        order["total_cents"] = subtotal
        order["items_populated_at"] = "2025-01-02T11:00:00"
        return _json({"subtotal_cents": subtotal, "total_cents": subtotal})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_order_items_for_plan_by_keys",
                "description": "Populate order_items by plan keys (household_id, week_start_date, store_id).",
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
