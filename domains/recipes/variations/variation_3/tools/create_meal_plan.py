from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateMealPlan(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        household_id: int,
        week_start_date: str,
        created_by_user_id: int
    ) -> str:
        table = _get_table(data, "meal_plans")
        existing = next(
            (
                m
                for m in table
                if m.get("household_id") == household_id
                and m.get("week_start_date") == week_start_date
                and m.get("created_by_user_id") == created_by_user_id
            ),
            None,
        )
        if existing:
            payload = {"meal_plan_id": existing.get("meal_plan_id"), "deduplicated": True}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        next_id = _max_int(table, "meal_plan_id", 0) + 1
        rec = {
            "meal_plan_id": next_id,
            "household_id": household_id,
            "week_start_date": week_start_date,
            "created_by_user_id": created_by_user_id,
            "created_at": "FIXED",
        }
        table.append(rec)
        payload = {"meal_plan_id": next_id, "deduplicated": False}
        out = json.dumps(payload, indent=2)
        return out
        pass
        table = _get_table(data, "meal_plans")
        existing = next(
            (
                m
                for m in table
                if m.get("household_id") == household_id
                and m.get("week_start_date") == week_start_date
                and m.get("created_by_user_id") == created_by_user_id
            ),
            None,
        )
        if existing:
            payload = {"meal_plan_id": existing.get("meal_plan_id"), "deduplicated": True}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        next_id = _max_int(table, "meal_plan_id", 0) + 1
        rec = {
            "meal_plan_id": next_id,
            "household_id": household_id,
            "week_start_date": week_start_date,
            "created_by_user_id": created_by_user_id,
            "created_at": "FIXED",
        }
        table.append(rec)
        payload = {"meal_plan_id": next_id, "deduplicated": False}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createMealPlan",
                "description": "Creates or returns an existing meal_plan deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                        "created_by_user_id": {"type": "integer"},
                    },
                    "required": [
                        "household_id",
                        "week_start_date",
                        "created_by_user_id",
                    ],
                },
            },
        }
