from tau_bench.envs.tool import Tool
import json
from typing import Any

class SelectInventoryDinnerAndLog(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        household_id: int,
        date_today: str,
        min_protein_g: int,
        exclude_days_back: int = 7,
        rating_int: int = 5,
        allow_pantry_staples: bool = True,
        max_missing_ingredients: int = 1
    ) -> str:
        pass
        from datetime import datetime, timedelta

        recipes = _get_table(data, "recipes")
        ri = _get_table(data, "recipe_ingredients")
        ingredients = _get_table(data, "ingredients")
        inv = _get_table(data, "inventory_items")
        mh = _get_table(data, "meal_history")
        #Construct sets
        inv_ids = {
            row.get("ingredient_id")
            for row in inv
            if row.get("household_id") == household_id
            and float(row.get("quantity") or 0) > 0
        }
        ing_map = {i.get("ingredient_id"): i for i in ingredients}
        #Recent timeframe
        recent_set = set()
        try:
            today = datetime.strptime(date_today, "%Y-%m-%d").date()
        except Exception:
            today = None
        if today:
            start = today - timedelta(days=int(exclude_days_back or 7))
            for row in mh:
                if row.get("household_id") != household_id:
                    continue
                d = row.get("plan_date") or ""
                try:
                    dd = datetime.strptime(d, "%Y-%m-%d").date()
                except Exception:
                    continue
                if start <= dd <= today:
                    recent_set.add(row.get("recipe_id"))
        #Potential dinner recipes that satisfy protein criteria and are not recent
        dinners = [
            r
            for r in recipes
            if r.get("meal_type") == "Dinner"
            and (r.get("protein_g_per_serving") or 0) >= int(min_protein_g or 0)
            and r.get("recipe_id") not in recent_set
        ]

        #Screen based on inventory availability
        def available_for_recipe(rid: int) -> tuple[bool, int]:
            pass
            rows = [x for x in ri if x.get("recipe_id") == rid]
            missing = 0
            for x in rows:
                ing_id = x.get("ingredient_id")
                if ing_id in inv_ids:
                    continue
                if allow_pantry_staples and bool(
                    (ing_map.get(ing_id) or {}).get("pantry_staple_flag")
                ):
                    continue
                missing += 1
                if missing > max_missing_ingredients:
                    return False, missing
            return True, missing

        def collect_feasible(max_missing: int) -> list[dict[str, Any]]:
            pass
            feasible_local: list[dict[str, Any]] = []
            for r in dinners:
                rid = r.get("recipe_id")
                #Temporarily assess using the given max_missing
                rows_local = [x for x in ri if x.get("recipe_id") == rid]
                missing_local = 0
                for x in rows_local:
                    ing_id = x.get("ingredient_id")
                    if ing_id in inv_ids:
                        continue
                    if allow_pantry_staples and bool(
                        (ing_map.get(ing_id) or {}).get("pantry_staple_flag")
                    ):
                        continue
                    missing_local += 1
                    if missing_local > max_missing:
                        missing_local = 999
                        break
                if missing_local != 999:
                    feasible_local.append(r)
            return feasible_local

        feasible: list[dict[str, Any]] = collect_feasible(
            int(max_missing_ingredients or 0)
        )
        if not feasible:
            feasible = collect_feasible(int(max_missing_ingredients or 0) + 1)
        if not feasible:
            feasible = collect_feasible(int(max_missing_ingredients or 0) + 2)
        #Rank in a deterministic manner: protein descending, calories ascending, recipe_id ascending
        ranked = sorted(
            feasible,
            key=lambda r: (
                -(r.get("protein_g_per_serving") or 0),
                (r.get("calories_per_serving") or 0),
                r.get("recipe_id"),
            ),
        )
        if not ranked:
            return _error("no_feasible_recipe")
        chosen = ranked[0]
        #Record to meal_history in a deterministic way
        next_id = _max_int(mh, "history_id", 0) + 1
        rec = {
            "history_id": next_id,
            "household_id": household_id,
            "plan_date": date_today,
            "recipe_id": chosen.get("recipe_id"),
            "was_prepared": True,
            "rating_int": int(rating_int),
        }
        mh.append(rec)
        payload = {"recipe_id": chosen.get("recipe_id"), "history_id": next_id}
        out = json.dumps(
            payload, indent=2
        )
        return out
        pass
        from datetime import datetime, timedelta

        recipes = _get_table(data, "recipes")
        ri = _get_table(data, "recipe_ingredients")
        ingredients = _get_table(data, "ingredients")
        inv = _get_table(data, "inventory_items")
        mh = _get_table(data, "meal_history")
        #Construct sets
        inv_ids = {
            row.get("ingredient_id")
            for row in inv
            if row.get("household_id") == household_id
            and float(row.get("quantity") or 0) > 0
        }
        ing_map = {i.get("ingredient_id"): i for i in ingredients}
        #Recent timeframe
        recent_set = set()
        try:
            today = datetime.strptime(date_today, "%Y-%m-%d").date()
        except Exception:
            today = None
        if today:
            start = today - timedelta(days=int(exclude_days_back or 7))
            for row in mh:
                if row.get("household_id") != household_id:
                    continue
                d = row.get("plan_date") or ""
                try:
                    dd = datetime.strptime(d, "%Y-%m-%d").date()
                except Exception:
                    continue
                if start <= dd <= today:
                    recent_set.add(row.get("recipe_id"))
        #Potential dinner recipes that satisfy protein criteria and are not recent
        dinners = [
            r
            for r in recipes
            if r.get("meal_type") == "Dinner"
            and (r.get("protein_g_per_serving") or 0) >= int(min_protein_g or 0)
            and r.get("recipe_id") not in recent_set
        ]

        #Screen based on inventory availability
        def available_for_recipe(rid: int) -> tuple[bool, int]:
            pass
            rows = [x for x in ri if x.get("recipe_id") == rid]
            missing = 0
            for x in rows:
                ing_id = x.get("ingredient_id")
                if ing_id in inv_ids:
                    continue
                if allow_pantry_staples and bool(
                    (ing_map.get(ing_id) or {}).get("pantry_staple_flag")
                ):
                    continue
                missing += 1
                if missing > max_missing_ingredients:
                    return False, missing
            return True, missing

        def collect_feasible(max_missing: int) -> list[dict[str, Any]]:
            pass
            feasible_local: list[dict[str, Any]] = []
            for r in dinners:
                rid = r.get("recipe_id")
                #Temporarily assess using the given max_missing
                rows_local = [x for x in ri if x.get("recipe_id") == rid]
                missing_local = 0
                for x in rows_local:
                    ing_id = x.get("ingredient_id")
                    if ing_id in inv_ids:
                        continue
                    if allow_pantry_staples and bool(
                        (ing_map.get(ing_id) or {}).get("pantry_staple_flag")
                    ):
                        continue
                    missing_local += 1
                    if missing_local > max_missing:
                        missing_local = 999
                        break
                if missing_local != 999:
                    feasible_local.append(r)
            return feasible_local

        feasible: list[dict[str, Any]] = collect_feasible(
            int(max_missing_ingredients or 0)
        )
        if not feasible:
            feasible = collect_feasible(int(max_missing_ingredients or 0) + 1)
        if not feasible:
            feasible = collect_feasible(int(max_missing_ingredients or 0) + 2)
        #Rank in a deterministic manner: protein descending, calories ascending, recipe_id ascending
        ranked = sorted(
            feasible,
            key=lambda r: (
                -(r.get("protein_g_per_serving") or 0),
                (r.get("calories_per_serving") or 0),
                r.get("recipe_id"),
            ),
        )
        if not ranked:
            return _error("no_feasible_recipe")
        chosen = ranked[0]
        #Record to meal_history in a deterministic way
        next_id = _max_int(mh, "history_id", 0) + 1
        rec = {
            "history_id": next_id,
            "household_id": household_id,
            "plan_date": date_today,
            "recipe_id": chosen.get("recipe_id"),
            "was_prepared": True,
            "rating_int": int(rating_int),
        }
        mh.append(rec)
        payload = {"recipe_id": chosen.get("recipe_id"), "history_id": next_id}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SelectInventoryDinnerAndLog",
                "description": "Selects a Dinner using inventory (optionally allowing pantry staples) with >= min protein, excluding recent meals, and logs it to meal_history.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "date_today": {"type": "string"},
                        "min_protein_g": {"type": "integer"},
                        "exclude_days_back": {"type": "integer"},
                        "rating_int": {"type": "integer"},
                        "allow_pantry_staples": {"type": "boolean"},
                        "max_missing_ingredients": {"type": "integer"},
                    },
                    "required": ["household_id", "date_today", "min_protein_g"],
                },
            },
        }
