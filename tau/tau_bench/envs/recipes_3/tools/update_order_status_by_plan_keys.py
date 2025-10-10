# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateOrderStatusByPlanKeys(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        household_id: int,
        week_start_date: str,
        store_id: int,
        new_status: str,
    ) -> str:
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
            return json({"error": "meal_plan not found for keys"})
        gl = next(
            (
                lt
                for lt in data.get("grocery_lists", [])
                if int(lt.get("source_meal_plan_id")) == int(plan.get("meal_plan_id"))
            ),
            None,
        )
        if not gl:
            return json({"error": "grocery_list not found for plan"})
        orders = [
            o
            for o in list(data.get("orders", {}).values())
            if int(o.get("household_id")) == int(household_id)
            and int(o.get("store_id")) == int(store_id)
            and int(o.get("list_id")) == int(gl.get("list_id"))
        ]
        if not orders:
            return json({"error": "order not found for keys"})
        order = sorted(orders, key=lambda o: int(o.get("order_id", 0)), reverse=True)[0]
        order["status_enum"] = str(new_status)
        order["last_status_update_at"] = "2025-01-02T11:05:00"
        return json({"order": order})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_order_status_by_plan_keys",
                "description": "Update order status by (household_id, week_start_date, store_id).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                        "store_id": {"type": "integer"},
                        "new_status": {"type": "string"},
                    },
                    "required": ["household_id", "week_start_date", "store_id", "new_status"],
                },
            },
        }
