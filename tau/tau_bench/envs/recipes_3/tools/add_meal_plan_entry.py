from tau_bench.envs.tool import Tool
import json
from typing import Any

class AddMealPlanEntry(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        meal_plan_id: int,
        plan_date: str,
        meal_type: str,
        recipe_id: int,
        servings_adult: int,
        servings_child: int,
        notes: str
    ) -> str:
        table = _get_table(data, "meal_plan_entries")
        existing = next(
            (
                e
                for e in table
                if e.get("meal_plan_id") == meal_plan_id
                and e.get("plan_date") == plan_date
                and e.get("meal_type") == meal_type
            ),
            None,
        )
        if existing:
            # idempotent update to align with deterministic notes
            existing.update(
                {
                    "recipe_id": recipe_id,
                    "servings_adult": servings_adult,
                    "servings_child": servings_child,
                    "notes": notes,
                }
            )
            payload = {"entry_id": existing.get("entry_id"), "deduplicated": True}
            out = json.dumps(payload, indent=2)
            return out
        next_id = _max_int(table, "entry_id", 0) + 1
        rec = {
            "entry_id": next_id,
            "meal_plan_id": meal_plan_id,
            "plan_date": plan_date,
            "meal_type": meal_type,
            "recipe_id": recipe_id,
            "servings_adult": servings_adult,
            "servings_child": servings_child,
            "notes": notes,
        }
        table.append(rec)
        payload = {"entry_id": next_id, "deduplicated": False}
        out = json.dumps(payload, indent=2)
        return out
        pass
        table = _get_table(data, "meal_plan_entries")
        existing = next(
            (
                e
                for e in table
                if e.get("meal_plan_id") == meal_plan_id
                and e.get("plan_date") == plan_date
                and e.get("meal_type") == meal_type
            ),
            None,
        )
        if existing:
            #idempotent update to align with deterministic notes
            existing.update(
                {
                    "recipe_id": recipe_id,
                    "servings_adult": servings_adult,
                    "servings_child": servings_child,
                    "notes": notes,
                }
            )
            payload = {"entry_id": existing.get("entry_id"), "deduplicated": True}
            out = json.dumps(
                payload, indent=2
            )
            return out
        next_id = _max_int(table, "entry_id", 0) + 1
        rec = {
            "entry_id": next_id,
            "meal_plan_id": meal_plan_id,
            "plan_date": plan_date,
            "meal_type": meal_type,
            "recipe_id": recipe_id,
            "servings_adult": servings_adult,
            "servings_child": servings_child,
            "notes": notes,
        }
        table.append(rec)
        payload = {"entry_id": next_id, "deduplicated": False}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addMealPlanEntry",
                "description": "Adds or updates a meal plan entry deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_plan_id": {"type": "integer"},
                        "plan_date": {"type": "string"},
                        "meal_type": {"type": "string"},
                        "recipe_id": {"type": "integer"},
                        "servings_adult": {"type": "integer"},
                        "servings_child": {"type": "integer"},
                        "notes": {"type": "string"},
                    },
                    "required": [
                        "meal_plan_id",
                        "plan_date",
                        "meal_type",
                        "recipe_id",
                        "servings_adult",
                        "servings_child",
                        "notes",
                    ],
                },
            },
        }
