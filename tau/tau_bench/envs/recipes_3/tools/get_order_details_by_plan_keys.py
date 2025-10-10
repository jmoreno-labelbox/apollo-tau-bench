# Copyright Sierra Corporation

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetOrderDetailsByPlanKeys(Tool):
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
            return json.dumps({"order": None, "items": []})
        gl = next(
            (
                lt
                for lt in data.get("grocery_lists", [])
                if int(lt.get("source_meal_plan_id")) == int(plan.get("meal_plan_id"))
            ),
            None,
        )
        if not gl:
            return json.dumps({"order": None, "items": []})
        orders = [
            o
            for o in list(data.get("orders", {}).values())
            if int(o.get("household_id")) == int(household_id)
            and int(o.get("store_id")) == int(store_id)
            and int(o.get("list_id")) == int(gl.get("list_id"))
        ]
        if not orders:
            return json.dumps({"order": None, "items": []})
        order = sorted(orders, key=lambda o: int(o.get("order_id", 0)), reverse=True)[0]
        items = [
            i
            for i in data.get("order_items", [])
            if int(i.get("order_id")) == int(order.get("order_id"))
        ]
        return json.dumps({"order": order, "items": items})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_order_details_by_plan_keys",
                "description": "Get order header and items by (household_id, week_start_date, store_id).",
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
