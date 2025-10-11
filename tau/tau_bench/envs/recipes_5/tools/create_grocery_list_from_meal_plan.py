# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump
from . import _first_user_id
def _collect_recipe_ingredients(data: Dict[str, Any], recipe_ids: List[int]) -> List[Dict[str, Any]]:
    ri = data.get("recipe_ingredients", [])
    ridset = set(recipe_ids)
    return [row for row in ri if int(row.get("recipe_id")) in ridset]

def _household_for_user(data: Dict[str, Any], user_id: Optional[int]) -> Optional[Dict[str, Any]]:
    if user_id is not None:
        h = next((h for h in data.get("households", []) if h.get("primary_user_id") == user_id), None)
        if h:
            return h
    households = data.get("households", [])
    if not households:
        return None
    return sorted(households, key=lambda h: int(h.get("household_id", 10**9)))[0]

def _plan_week_dates(week_start_date: str) -> List[str]:
    # Deterministic: generate 7 consecutive ISO dates from a start date YYYY-MM-DD
    from datetime import date, timedelta
    y, m, d = [int(x) for x in str(week_start_date).split("-")]
    start = date(y, m, d)
    return [(start + timedelta(days=i)).isoformat() for i in range(7)]

def _parse_json_list_ids(json_str: str) -> List[int]:
    try:
        arr = json.loads(json_str)
        if isinstance(arr, list):
            return [int(x) for x in arr]
    except Exception:
        pass
    return []

def _next_week_start_date_for_household(data: Dict[str, Any], household_id: Optional[int]) -> str:
    base = date(2025, 1, 6)
    if household_id is None:
        return base.isoformat()
    plans = [m for m in data.get("meal_plans", []) if m.get("household_id") == household_id]
    if not plans:
        return base.isoformat()
    latest = max(plans, key=lambda m: str(m.get("week_start_date", "2025-01-06")))
    y, m, d = [int(x) for x in str(latest.get("week_start_date")).split("-")]
    return (date(y, m, d) + timedelta(days=7)).isoformat()

def _sum_grocery_items(data: Dict[str, Any], recipe_ids: List[int]) -> List[Dict[str, Any]]:
    rows = _collect_recipe_ingredients(data, recipe_ids)
    agg: Dict[Tuple[int, str], float] = {}
    for r in rows:
        key = (int(r["ingredient_id"]), str(r["unit"]))
        agg[key] = agg.get(key, 0) + float(r["quantity"])
    out = []
    for (ingredient_id, unit), qty in agg.items():
        out.append({"ingredient_id": ingredient_id, "quantity": qty, "unit": unit})
    return out

def _max_id(records: List[Dict[str, Any]], key: str, default: int) -> int:
    if not records:
        return default
    return max(int(r.get(key, default)) for r in records)

def _latest_meal_plan_for_household(data: Dict[str, Any], household_id: Optional[int]) -> Optional[Dict[str, Any]]:
    if household_id is None:
        return None
    plans = [m for m in data.get("meal_plans", []) if m.get("household_id") == household_id]
    if not plans:
        return None
    return sorted(plans, key=lambda m: int(m.get("meal_plan_id", 0)), reverse=True)[0]

def _json_dump(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)

def _ingredient_by_id(data: Dict[str, Any], ingredient_id: int) -> Optional[Dict[str, Any]]:
    return next((i for i in data.get("ingredients", []) if i.get("ingredient_id") == ingredient_id), None)

def _first_user_id(data: Dict[str, Any]) -> Optional[int]:
    users = data.get("users", [])
    if not users:
        return None
    return int(sorted(users, key=lambda u: int(u.get("user_id", 10**9)))[0]["user_id"])

def _default_household_id(data: Dict[str, Any], user_id: Optional[int] = None) -> Optional[int]:
    hh = _household_for_user(data, user_id)
    return hh.get("household_id") if hh else None

class CreateMealPlan(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        created_by_user_id = kwargs.get("created_by_user_id")
        if created_by_user_id is None:
            created_by_user_id = _first_user_id(data)
        if household_id is None:
            household_id = _default_household_id(data, created_by_user_id)
        week_start_date = kwargs.get("week_start_date") or _next_week_start_date_for_household(data, household_id)
        if household_id is None or created_by_user_id is None:
            return _json_dump({"error": "unable to infer household or user"})
        meal_plans = data.get("meal_plans", [])
        next_id = _max_id(meal_plans, "meal_plan_id", 6000) + 1
        new_row = {
            "meal_plan_id": next_id,
            "household_id": int(household_id),
            "week_start_date": str(week_start_date),
            "created_by_user_id": int(created_by_user_id),
            "created_at": "2025-01-01T00:00:00Z"
        }
        meal_plans.append(new_row)
        return _json_dump({"meal_plan_id": next_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"create_meal_plan","description":"Insert a new meal_plan with defaults for household, creator, and week_start_date.","parameters":{"type":"object","properties":{"household_id":{"type":"integer"},"week_start_date":{"type":"string"},"created_by_user_id":{"type":"integer"}},"required":[]}}}

class BulkAddMealPlanEntries(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        meal_plan_id = kwargs.get("meal_plan_id")
        week_start_date = kwargs.get("week_start_date")
        recipe_ids_json = kwargs.get("selected_recipe_ids_json")
        if meal_plan_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
            created = json.loads(CreateMealPlan.invoke(data, household_id=household_id))
            meal_plan_id = int(created.get("meal_plan_id"))
        if not week_start_date:
            mp_row = next((m for m in data.get("meal_plans", []) if m.get("meal_plan_id") == meal_plan_id), None)
            week_start_date = mp_row.get("week_start_date") if mp_row else _next_week_start_date_for_household(data, _default_household_id(data, _first_user_id(data)))
        recipes = _parse_json_list_ids(recipe_ids_json)
        if not recipes:
            token = BuildRecipeFilters.invoke(data)
            candidates = json.loads(ListRecipesByFilters.invoke(data, filter_token=json.loads(token)["filter_token"]))["candidate_recipe_ids_json"]
            excluded = json.loads(ExcludeRecentRecipes.invoke(data, candidate_recipe_ids_json=candidates))["filtered_recipe_ids_json"]
            limited = json.loads(ApplyCuisineLimit.invoke(data, recipe_ids_json=excluded))["cuisine_limited_recipe_ids_json"]
            ranked = json.loads(RankRecipesForTargets.invoke(data, recipe_ids_json=limited, needed_count=7))["selected_recipe_ids_json"]
            recipes = _parse_json_list_ids(ranked)
        dates = _plan_week_dates(str(week_start_date))
        entries_tbl = data.get("meal_plan_entries", [])
        created_ids: List[int] = []
        next_id = _max_id(entries_tbl, "entry_id", 6100)
        for i, rid in enumerate(recipes[:7]):
            next_id += 1
            row = {
                "entry_id": next_id,
                "meal_plan_id": meal_plan_id,
                "plan_date": dates[i] if i < len(dates) else dates[-1],
                "meal_type": "Dinner",
                "recipe_id": rid,
                "servings_adult": 2,
                "servings_child": 1,
                "notes": ""
            }
            entries_tbl.append(row)
            created_ids.append(next_id)
        return _json_dump({"created_entry_ids": created_ids})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"bulk_add_meal_plan_entries","description":"Insert a week of Dinner entries; defaults to an auto-selected set of recipes.","parameters":{"type":"object","properties":{"meal_plan_id":{"type":"integer"},"week_start_date":{"type":"string"},"selected_recipe_ids_json":{"type":"string"}},"required":[]}}}

class CreateGroceryListFromMealPlan(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], created_by_user_id, household_id, meal_plan_id) -> str:
        if created_by_user_id is None:
            created_by_user_id = _first_user_id(data)
        if household_id is None:
            household_id = _default_household_id(data, created_by_user_id)
        if meal_plan_id is None:
            mp = _latest_meal_plan_for_household(data, household_id)
            if mp is None:
                mp_created = json.loads(CreateMealPlan.invoke(data, household_id=household_id, created_by_user_id=created_by_user_id))
                meal_plan_id = int(mp_created["meal_plan_id"])
                BulkAddMealPlanEntries.invoke(data, meal_plan_id=meal_plan_id)
            else:
                meal_plan_id = int(mp["meal_plan_id"])
        entries = [e for e in data.get("meal_plan_entries", []) if e.get("meal_plan_id") == meal_plan_id]
        recipe_ids = [int(e.get("recipe_id")) for e in entries]
        items = _sum_grocery_items(data, recipe_ids)
        gl_tbl = data.get("grocery_lists", [])
        next_list = _max_id(gl_tbl, "list_id", 8000) + 1
        new_gl = {
            "list_id": next_list,
            "household_id": household_id,
            "source_meal_plan_id": meal_plan_id,
            "created_by_user_id": created_by_user_id,
            "created_at": "2025-01-01T12:00:00Z",
            "status_enum": "initialized",
        }
        gl_tbl.append(new_gl)
        gli_tbl = data.get("grocery_list_items", [])
        next_item = _max_id(gli_tbl, "item_id", 8100)
        created_items = []
        for it in items:
            next_item += 1
            ingr = _ingredient_by_id(data, it["ingredient_id"])
            gli = {
                "item_id": next_item,
                "list_id": next_list,
                "ingredient_id": it["ingredient_id"],
                "quantity": it["quantity"],
                "unit": it["unit"],
                "grocery_section": (ingr or {}).get("grocery_section", "Misc"),
                "pantry_staple_flag": bool((ingr or {}).get("pantry_staple_flag", False)),
                "overlap_last_month_flag": False,
            }
            gli_tbl.append(gli)
            created_items.append(next_item)
        return _json_dump({"list_id": next_list, "created_item_ids": created_items})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"create_grocery_list_from_meal_plan","description":"Create and populate a grocery list; infers meal plan, household, and creator.","parameters":{"type":"object","properties":{"meal_plan_id":{"type":"integer"},"household_id":{"type":"integer"},"created_by_user_id":{"type":"integer"}},"required":[]}}}