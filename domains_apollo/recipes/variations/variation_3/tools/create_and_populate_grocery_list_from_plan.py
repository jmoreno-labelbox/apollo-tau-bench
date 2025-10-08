from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateAndPopulateGroceryListFromPlan(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        meal_plan_id: int,
        created_by_user_id: int,
        household_id: int = None,
        week_start_date: str = None,
        list_id: int = None,
        recipe_ids: list[int] = None,
        categorized_items: list[dict] = None
    ) -> str:
        pass
        # Extract household and week_start_date from the plan
        plans = _get_table(data, "meal_plans")
        entries = _get_table(data, "meal_plan_entries")
        mh = _get_table(data, "meal_history")
        mp = next((p for p in plans if p.get("meal_plan_id") == meal_plan_id), None)
        if not mp:
            return _error("meal_plan not found")
        household_id = mp.get("household_id")
        week_start_date = mp.get("week_start_date") or ""
        # Form or utilize list in a deterministic manner
        list_res = json.loads(
            CreateGroceryList.invoke(
                data,
                household_id=household_id,
                source_meal_plan_id=meal_plan_id,
                created_by_user_id=created_by_user_id,
            )
        )
        list_id = list_res.get("list_id")
        # If the list contains items, avoid duplication
        gli = _get_table(data, "grocery_list_items")
        if any(i.get("list_id") == list_id for i in gli):
            payload = {"list_id": list_id, "added": 0, "deduplicated_items": True}
            out = json.dumps(
                payload, indent=2
            )
            return out
        # Gather Dinner recipe_ids from entries for this plan, sorted by plan_date
        dinner_entries = [
            e
            for e in entries
            if e.get("meal_plan_id") == meal_plan_id and e.get("meal_type") == "Dinner"
        ]
        dinner_entries = sorted(dinner_entries, key=lambda e: e.get("plan_date") or "")
        recipe_ids = [e.get("recipe_id") for e in dinner_entries]
        # Merge ingredients from selected recipes
        cons = json.loads(
            ConsolidateIngredients.invoke(data, recipe_ids=recipe_ids)
        ).get("items", [])
        # Calculate the recent 30-day period concluding at week_start_date for overlap flagging
        from datetime import datetime, timedelta

        recent_30 = []
        try:
            ws_date = datetime.strptime(week_start_date, "%Y-%m-%d").date()
            start_30 = (ws_date - timedelta(days=30)).strftime("%Y-%m-%d")
            end_30 = ws_date.strftime("%Y-%m-%d")
            recent_30 = [
                h
                for h in mh
                if h.get("household_id") == household_id
                and start_30 <= (h.get("plan_date") or "") <= end_30
            ]
        except Exception:
            recent_30 = []
        # Classify and append flags
        categorized = json.loads(
            CategorizeAndFlag.invoke(
                data, items=cons, household_id=household_id, recent_30d=recent_30
            )
        ).get("categorized_items", [])
        # Add items in a deterministic manner
        add_res = json.loads(
            AddGroceryListItems.invoke(data, list_id=list_id, items=categorized)
        )
        payload = {"list_id": list_id, "added": add_res.get("count")}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAndPopulateGroceryListFromPlan",
                "description": "Creates a grocery list for a meal plan and populates it with consolidated, categorized items for Dinner entries.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_plan_id": {"type": "integer"},
                        "created_by_user_id": {"type": "integer"},
                    },
                    "required": ["meal_plan_id", "created_by_user_id"],
                },
            },
        }
