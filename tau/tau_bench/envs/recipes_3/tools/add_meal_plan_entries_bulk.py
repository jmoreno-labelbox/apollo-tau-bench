from tau_bench.envs.tool import Tool
import json
from typing import Any

class AddMealPlanEntriesBulk(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        meal_plan_id: int,
        week_start_date: str,
        recipe_ids: list[int],
        servings_adult: int,
        servings_child: int,
        child_notes_map: dict[str, str]
    ) -> str:
        from datetime import datetime, timedelta

        table = _get_table(data, "meal_plan_entries")
        # generate up to len(recipe_ids) entries for consecutive dates beginning from week_start_date
        try:
            start = datetime.strptime(week_start_date, "%Y-%m-%d")
        except Exception:
            return _error("invalid week_start_date")
        created_ids = []
        for idx, rid in enumerate(recipe_ids or []):
            plan_date = (start + timedelta(days=idx)).strftime("%Y-%m-%d")
            existing = next(
                (
                    e
                    for e in table
                    if e.get("meal_plan_id") == meal_plan_id
                    and e.get("plan_date") == plan_date
                    and e.get("meal_type") == "Dinner"
                ),
                None,
            )
            notes = child_notes_map.get(str(rid)) or "Child: low spice, small pieces"
            if existing:
                existing.update(
                    {
                        "recipe_id": rid,
                        "servings_adult": servings_adult,
                        "servings_child": servings_child,
                        "notes": notes,
                    }
                )
                created_ids.append(existing.get("entry_id"))
                continue
            next_id = _max_int(table, "entry_id", 0) + 1
            rec = {
                "entry_id": next_id,
                "meal_plan_id": meal_plan_id,
                "plan_date": plan_date,
                "meal_type": "Dinner",
                "recipe_id": rid,
                "servings_adult": servings_adult,
                "servings_child": servings_child,
                "notes": notes,
            }
            table.append(rec)
            created_ids.append(next_id)
        payload = {"entry_ids": created_ids}
        out = json.dumps(payload, indent=2)
        return out
        pass
        from datetime import datetime, timedelta

        table = _get_table(data, "meal_plan_entries")
        #generate up to len(recipe_ids) entries for consecutive dates beginning from week_start_date
        try:
            start = datetime.strptime(week_start_date, "%Y-%m-%d")
        except Exception:
            return _error("invalid week_start_date")
        created_ids = []
        for idx, rid in enumerate(recipe_ids or []):
            plan_date = (start + timedelta(days=idx)).strftime("%Y-%m-%d")
            existing = next(
                (
                    e
                    for e in table
                    if e.get("meal_plan_id") == meal_plan_id
                    and e.get("plan_date") == plan_date
                    and e.get("meal_type") == "Dinner"
                ),
                None,
            )
            notes = child_notes_map.get(str(rid)) or "Child: low spice, small pieces"
            if existing:
                existing.update(
                    {
                        "recipe_id": rid,
                        "servings_adult": servings_adult,
                        "servings_child": servings_child,
                        "notes": notes,
                    }
                )
                created_ids.append(existing.get("entry_id"))
                continue
            next_id = _max_int(table, "entry_id", 0) + 1
            rec = {
                "entry_id": next_id,
                "meal_plan_id": meal_plan_id,
                "plan_date": plan_date,
                "meal_type": "Dinner",
                "recipe_id": rid,
                "servings_adult": servings_adult,
                "servings_child": servings_child,
                "notes": notes,
            }
            table.append(rec)
            created_ids.append(next_id)
        payload = {"entry_ids": created_ids}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addMealPlanEntriesBulk",
                "description": "Adds or updates consecutive Dinner entries for a week for given recipe_ids.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_plan_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                        "recipe_ids": {"type": "array", "items": {"type": "integer"}},
                        "servings_adult": {"type": "integer"},
                        "servings_child": {"type": "integer"},
                        "child_notes_map": {"type": "object"},
                    },
                    "required": [
                        "meal_plan_id",
                        "week_start_date",
                        "recipe_ids",
                        "servings_adult",
                        "servings_child",
                        "child_notes_map",
                    ],
                },
            },
        }
