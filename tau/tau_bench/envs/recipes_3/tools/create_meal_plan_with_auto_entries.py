from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateMealPlanWithAutoEntries(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        household_id: int,
        week_start_date: str,
        created_by_user_id: int,
        servings_adult: int,
        servings_child: int,
        max_per_cuisine: int = 2,
        exclude_days_back: int = 14
    ) -> str:
        pass
        # Formulate plan in a deterministic manner
        mp_res = json.loads(
            CreateMealPlan.invoke(
                data,
                household_id=household_id,
                week_start_date=week_start_date,
                created_by_user_id=created_by_user_id,
            )
        )
        meal_plan_id = mp_res.get("meal_plan_id")
        # Choose seven dinner recipes in a deterministic way
        recipes = _get_table(data, "recipes")
        mh = _get_table(data, "meal_history")
        # Omit recent recipes within exclude_days_back days from week_start_date
        from datetime import datetime

        recent_set = set()
        try:
            ws_date = datetime.strptime(week_start_date, "%Y-%m-%d").date()
        except Exception:
            ws_date = None
        for row in mh:
            if row.get("household_id") != household_id or not ws_date:
                continue
            d_str = row.get("plan_date") or ""
            try:
                d_date = datetime.strptime(d_str, "%Y-%m-%d").date()
            except Exception:
                continue
            delta = (ws_date - d_date).days
            if delta >= 0 and delta < int(exclude_days_back or 14):
                recent_set.add(row.get("recipe_id"))
        dinner = [
            r
            for r in recipes
            if r.get("meal_type") == "Dinner" and r.get("is_peanut_free")
        ]
        # rank by protein in descending order, calories in ascending order, and id in ascending order
        ranked = sorted(
            dinner,
            key=lambda r: (
                -(r.get("protein_g_per_serving") or 0),
                (r.get("calories_per_serving") or 0),
                r.get("recipe_id"),
            ),
        )
        # impose cuisine limit and ease if necessary to achieve 7 entries
        cuisine_count: dict[str, int] = {}
        chosen: list[int] = []
        current_cap = (
            max_per_cuisine
            if isinstance(max_per_cuisine, int) and max_per_cuisine > 0
            else 2
        )

        def fill_with_cap(cap: int):
            pass
            nonlocal chosen, cuisine_count
            for rec in ranked:
                rid = rec.get("recipe_id")
                if rid in chosen or rid in recent_set:
                    continue
                cz = rec.get("cuisine")
                if cuisine_count.get(cz, 0) >= cap:
                    continue
                chosen.append(rid)
                cuisine_count[cz] = cuisine_count.get(cz, 0) + 1
                if len(chosen) == 7:
                    return True
            return False

        # attempt initial limit, then gradually ease up to unlimited
        if not fill_with_cap(current_cap):
            if not fill_with_cap(current_cap + 1):
                if not fill_with_cap(current_cap + 2):
                    # last review disregarding cuisine limit
                    for rec in ranked:
                        if len(chosen) == 7:
                            break
                        rid = rec.get("recipe_id")
                        if rid in chosen or rid in recent_set:
                            continue
                        chosen.append(rid)
                        cuisine_count[rec.get("cuisine")] = (
                            cuisine_count.get(rec.get("cuisine"), 0) + 1
                        )
        # generate notes for children
        notes_map = json.loads(
            DeriveChildModifications.invoke(
                data, recipe_ids=chosen, ruleset="low_spice mild_textures bite_size"
            )
        ).get("child_notes", {}).values()
        # generate entries from Mon to Sun beginning at week_start_date
        bulk_res = json.loads(
            AddMealPlanEntriesBulk.invoke(
                data,
                meal_plan_id=meal_plan_id,
                week_start_date=week_start_date,
                recipe_ids=chosen,
                servings_adult=servings_adult,
                servings_child=servings_child,
                child_notes_map=notes_map,
            )
        )
        payload = {
            "meal_plan_id": meal_plan_id,
            "entry_ids": bulk_res.get("entry_ids"),
            "selected_recipe_ids": chosen,
            "dinner_only": True,
            "child_notes_applied": True,
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        pass
        #Formulate plan in a deterministic manner
        mp_res = json.loads(
            CreateMealPlan.invoke(
                data,
                household_id=household_id,
                week_start_date=week_start_date,
                created_by_user_id=created_by_user_id,
            )
        )
        meal_plan_id = mp_res.get("meal_plan_id")
        #Choose seven dinner recipes in a deterministic way
        recipes = _get_table(data, "recipes")
        mh = _get_table(data, "meal_history")
        #Omit recent recipes within exclude_days_back days from week_start_date
        from datetime import datetime

        recent_set = set()
        try:
            ws_date = datetime.strptime(week_start_date, "%Y-%m-%d").date()
        except Exception:
            ws_date = None
        for row in mh:
            if row.get("household_id") != household_id or not ws_date:
                continue
            d_str = row.get("plan_date") or ""
            try:
                d_date = datetime.strptime(d_str, "%Y-%m-%d").date()
            except Exception:
                continue
            delta = (ws_date - d_date).days
            if delta >= 0 and delta < int(exclude_days_back or 14):
                recent_set.add(row.get("recipe_id"))
        dinner = [
            r
            for r in recipes
            if r.get("meal_type") == "Dinner" and r.get("is_peanut_free")
        ]
        #rank by protein in descending order, calories in ascending order, and id in ascending order
        ranked = sorted(
            dinner,
            key=lambda r: (
                -(r.get("protein_g_per_serving") or 0),
                (r.get("calories_per_serving") or 0),
                r.get("recipe_id"),
            ),
        )
        #impose cuisine limit and ease if necessary to achieve 7 entries
        cuisine_count: dict[str, int] = {}
        chosen: list[int] = []
        current_cap = (
            max_per_cuisine
            if isinstance(max_per_cuisine, int) and max_per_cuisine > 0
            else 2
        )

        def fill_with_cap(cap: int):
            pass
            nonlocal chosen, cuisine_count
            for rec in ranked:
                rid = rec.get("recipe_id")
                if rid in chosen or rid in recent_set:
                    continue
                cz = rec.get("cuisine")
                if cuisine_count.get(cz, 0) >= cap:
                    continue
                chosen.append(rid)
                cuisine_count[cz] = cuisine_count.get(cz, 0) + 1
                if len(chosen) == 7:
                    return True
            return False

        #attempt initial limit, then gradually ease up to unlimited
        if not fill_with_cap(current_cap):
            if not fill_with_cap(current_cap + 1):
                if not fill_with_cap(current_cap + 2):
                    #last review disregarding cuisine limit
                    for rec in ranked:
                        if len(chosen) == 7:
                            break
                        rid = rec.get("recipe_id")
                        if rid in chosen or rid in recent_set:
                            continue
                        chosen.append(rid)
                        cuisine_count[rec.get("cuisine")] = (
                            cuisine_count.get(rec.get("cuisine"), 0) + 1
                        )
        #generate notes for children
        notes_map = json.loads(
            DeriveChildModifications.invoke(
                data, recipe_ids=chosen, ruleset="low_spice mild_textures bite_size"
            )
        ).get("child_notes", {}).values()
        #generate entries from Mon to Sun beginning at week_start_date
        bulk_res = json.loads(
            AddMealPlanEntriesBulk.invoke(
                data,
                meal_plan_id=meal_plan_id,
                week_start_date=week_start_date,
                recipe_ids=chosen,
                servings_adult=servings_adult,
                servings_child=servings_child,
                child_notes_map=notes_map,
            )
        )
        payload = {
                "meal_plan_id": meal_plan_id,
                "entry_ids": bulk_res.get("entry_ids"),
                "selected_recipe_ids": chosen,
                "dinner_only": True,
                "child_notes_applied": True,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateMealPlanWithAutoEntries",
                "description": "Creates a meal plan and auto-populates 7 Dinner entries (max 2 per cuisine, exclude recent).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                        "created_by_user_id": {"type": "integer"},
                        "servings_adult": {"type": "integer"},
                        "servings_child": {"type": "integer"},
                        "max_per_cuisine": {"type": "integer"},
                        "exclude_days_back": {"type": "integer"},
                    },
                    "required": [
                        "household_id",
                        "week_start_date",
                        "created_by_user_id",
                        "servings_adult",
                        "servings_child",
                    ],
                },
            },
        }
