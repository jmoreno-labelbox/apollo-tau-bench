# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateOrderForPlanListByKeys(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        household_id: int,
        week_start_date: str,
        store_id: int,
        scheduled_slot_start_ts: str,
        scheduled_slot_end_ts: str,
    ) -> str:
        # Find list by plan keys
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
        tbl = _tbl(data, "orders")
        next_id = _max_id(tbl, "order_id", 10000) + 1
        row = {
            "order_id": next_id,
            "household_id": int(household_id),
            "store_id": int(store_id),
            "list_id": int(gl.get("list_id")),
            "status_enum": "initialized",
            "subtotal_cents": 0,
            "total_cents": 0,
            "placed_ts": "2025-01-02T10:00:00",
            "scheduled_slot_start_ts": str(scheduled_slot_start_ts),
            "scheduled_slot_end_ts": str(scheduled_slot_end_ts),
        }
        tbl.append(row)
        return _json({"order_id": next_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_order_for_plan_list_by_keys",
                "description": "Create order for the grocery list linked to (household_id, week_start_date).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                        "store_id": {"type": "integer"},
                        "scheduled_slot_start_ts": {"type": "string"},
                        "scheduled_slot_end_ts": {"type": "string"},
                    },
                    "required": [
                        "household_id",
                        "week_start_date",
                        "store_id",
                        "scheduled_slot_start_ts",
                        "scheduled_slot_end_ts",
                    ],
                },
            },
        }
