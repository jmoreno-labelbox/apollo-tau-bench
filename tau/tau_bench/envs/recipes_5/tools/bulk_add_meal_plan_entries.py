# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump
from . import _first_user_id




























def _plan_week_dates(week_start_date: str) -> List[str]:
    y, m, d = [int(x) for x in week_start_date.split("-")]
    start = date(y, m, d)
    return [(start + timedelta(days=i)).isoformat() for i in range(7)]

def _parse_json_list_ids(json_str: Optional[str]) -> List[int]:
    try:
        if not json_str:
            return []
        val = json.loads(json_str)
        if isinstance(val, list) and all(isinstance(x, int) for x in val):
            return val
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

def _max_id(records: List[Dict[str, Any]], key: str, default: int) -> int:
    if not records:
        return default
    return max(int(r.get(key, default)) for r in records)

def _json_dump(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)

def _first_user_id(data: Dict[str, Any]) -> Optional[int]:
    users = data.get("users", [])
    if not users:
        return None
    return int(sorted(users, key=lambda u: int(u.get("user_id", 10**9)))[0]["user_id"])

def _default_household_id(data: Dict[str, Any], user_id: Optional[int] = None) -> Optional[int]:
    hh = _household_for_user(data, user_id)
    return hh.get("household_id") if hh else None

class RankRecipesForTargets(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ids = _ids_from_kwargs_or_defaults(data, kwargs)
        needed_count = int(kwargs.get("needed_count", 7))
        member_id = kwargs.get("member_id")
        tc = kwargs.get("target_calories")
        tp = kwargs.get("target_protein")
        if tc is None or tp is None:
            tc2, tp2 = _pick_target_from_member(data, member_id)
            target_calories = int(tc if tc is not None else tc2)
            target_protein = int(tp if tp is not None else tp2)
        else:
            target_calories = int(tc)
            target_protein = int(tp)
        scored: List[Tuple[float, int]] = []
        for rid in ids:
            r = _recipe_by_id(data, rid)
            if not r:
                continue
            dc = abs(int(r.get("calories_per_serving", 0)) - target_calories)
            dp = abs(int(r.get("protein_g_per_serving", 0)) - target_protein)
            score = float(dc) + float(dp) * 10.0
            scored.append((score, rid))
        picked = [rid for _, rid in sorted(scored, key=lambda x: (x[0], x[1]))[:needed_count]]
        return _json_dump({"selected_recipe_ids_json": json.dumps(picked)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"rank_recipes_for_targets","description":"Select up to N recipes closest to nutrition targets; targets default from a household member.","parameters":{"type":"object","properties":{"recipe_ids_json":{"type":"string"},"filter_token":{"type":"string"},"meal_type":{"type":"string"},"min_protein_g":{"type":"integer"},"peanut_free":{"type":"boolean"},"needed_count":{"type":"integer"},"target_calories":{"type":"integer"},"target_protein":{"type":"integer"},"member_id":{"type":"integer"}},"required":[]}}}

class ListRecipesByFilters(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        token = kwargs.get("filter_token")
        if token:
            meal_type, min_protein, pf = _decode_filter_token(token)
        else:
            meal_type = kwargs.get("meal_type", "Dinner")
            min_protein = int(kwargs.get("min_protein_g", 0))
            pf = bool(kwargs.get("peanut_free", False))
        out = _all_recipe_ids_filtered(data, meal_type, min_protein, pf)
        return _json_dump({"candidate_recipe_ids_json": json.dumps(out)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"list_recipes_by_filters","description":"List recipe_ids as JSON from a token or direct parameters.","parameters":{"type":"object","properties":{"filter_token":{"type":"string"},"meal_type":{"type":"string"},"min_protein_g":{"type":"integer"},"peanut_free":{"type":"boolean"}},"required":[]}}}

class ExcludeRecentRecipes(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        if household_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
        cand = _ids_from_kwargs_or_defaults(data, kwargs)
        recent = kwargs.get("recent_recipe_ids")
        if recent is None:
            days_back = int(kwargs.get("days_back", 14))
            anchor_date = kwargs.get("anchor_date")
            recent = _recent_recipe_ids(data, household_id, days_back, anchor_date)
        filtered = [rid for rid in cand if rid not in set(int(x) for x in recent)]
        return _json_dump({"filtered_recipe_ids_json": json.dumps(filtered)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"exclude_recent_recipes","description":"Remove recipes that appeared in recent history; defaults to last 14 days for default household.","parameters":{"type":"object","properties":{"candidate_recipe_ids_json":{"type":"string"},"filter_token":{"type":"string"},"meal_type":{"type":"string"},"min_protein_g":{"type":"integer"},"peanut_free":{"type":"boolean"},"recent_recipe_ids":{"type":"array","items":{"type":"integer"}},"household_id":{"type":"integer"},"days_back":{"type":"integer"},"anchor_date":{"type":"string"}},"required":[]}}}

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

class BuildRecipeFilters(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        meal_type = kwargs.get("meal_type", "Dinner")
        min_protein_g = int(kwargs.get("min_protein_g", 0))
        peanut_free = bool(kwargs.get("peanut_free", False))
        token = f"F:{meal_type}:P{min_protein_g}:PF{1 if peanut_free else 0}"
        return _json_dump({"filter_token": token})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"build_recipe_filters","description":"Construct a filter token; defaults to Dinner with no protein minimum.","parameters":{"type":"object","properties":{"meal_type":{"type":"string"},"min_protein_g":{"type":"integer"},"peanut_free":{"type":"boolean"}},"required":[]}}}

class ApplyCuisineLimit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ids = _ids_from_kwargs_or_defaults(data, kwargs)
        max_per_cuisine = int(kwargs.get("max_per_cuisine", 2))
        cuisine_counts: Dict[str, int] = {}
        selected: List[int] = []
        for rid in ids:
            r = _recipe_by_id(data, rid)
            if not r:
                continue
            cz = r.get("cuisine", "Unknown")
            cnt = cuisine_counts.get(cz, 0)
            if cnt < max_per_cuisine:
                selected.append(rid)
                cuisine_counts[cz] = cnt + 1
        return _json_dump({"cuisine_limited_recipe_ids_json": json.dumps(selected)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"apply_cuisine_limit","description":"Limit a list of recipes to at most N per cuisine; defaults to 2 and Dinner pool if none provided.","parameters":{"type":"object","properties":{"recipe_ids_json":{"type":"string"},"filter_token":{"type":"string"},"meal_type":{"type":"string"},"min_protein_g":{"type":"integer"},"peanut_free":{"type":"boolean"},"max_per_cuisine":{"type":"integer"}},"required":[]}}}

class BulkAddMealPlanEntries(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], meal_plan_id, selected_recipe_ids_json, week_start_date) -> str:
        recipe_ids_json = selected_recipe_ids_json
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