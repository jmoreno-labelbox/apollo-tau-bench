import json
from typing import Any, Dict, List, Optional, Tuple
from datetime import date, timedelta
from domains.dto import Tool

def _max_id(records: List[Dict[str, Any]], key: str, default: int) -> int:
    if not records:
        return default
    return max(int(r.get(key, default)) for r in records)

def _ensure_list_id(data: Dict[str, Any], list_id: int) -> Dict[str, Any]:
    for gl in data.get("grocery_lists", []):
        if gl.get("list_id") == list_id:
            return gl
    return {}

def _ingredient_by_id(data: Dict[str, Any], ingredient_id: int) -> Optional[Dict[str, Any]]:
    return next((i for i in data.get("ingredients", []) if i.get("ingredient_id") == ingredient_id), None)

def _recipe_by_id(data: Dict[str, Any], recipe_id: int) -> Optional[Dict[str, Any]]:
    return next((r for r in data.get("recipes", []) if r.get("recipe_id") == recipe_id), None)

def _store_products_for_ingredient(data: Dict[str, Any], store_id: int, ingredient_id: int) -> List[Dict[str, Any]]:
    return [
        p for p in data.get("store_products", [])
        if p.get("store_id") == store_id and p.get("ingredient_id") == ingredient_id
    ]

def _lowest_price_in_stock(products: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    in_stock = [p for p in products if p.get("stock_status_enum") in ("in_stock", "low")]
    if not in_stock:
        return None
    return sorted(in_stock, key=lambda x: int(x.get("price_cents", 10**9)))[0]

def _json_dump(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)

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

def _plan_week_dates(week_start_date: str) -> List[str]:
    y, m, d = [int(x) for x in week_start_date.split("-")]
    start = date(y, m, d)
    return [(start + timedelta(days=i)).isoformat() for i in range(7)]

def _collect_recipe_ingredients(data: Dict[str, Any], recipe_ids: List[int]) -> List[Dict[str, Any]]:
    ri = data.get("recipe_ingredients", [])
    return [row for row in ri if row.get("recipe_id") in recipe_ids]

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

def _first_user_id(data: Dict[str, Any]) -> Optional[int]:
    users = data.get("users", [])
    if not users:
        return None
    return int(sorted(users, key=lambda u: int(u.get("user_id", 10**9)))[0]["user_id"])

def _household_for_user(data: Dict[str, Any], user_id: Optional[int]) -> Optional[Dict[str, Any]]:
    if user_id is not None:
        h = next((h for h in data.get("households", []) if h.get("primary_user_id") == user_id), None)
        if h:
            return h
    households = data.get("households", [])
    if not households:
        return None
    return sorted(households, key=lambda h: int(h.get("household_id", 10**9)))[0]

def _default_household_id(data: Dict[str, Any], user_id: Optional[int] = None) -> Optional[int]:
    hh = _household_for_user(data, user_id)
    return hh.get("household_id") if hh else None

def _default_store_id(data: Dict[str, Any]) -> Optional[int]:
    stores = data.get("stores", [])
    if not stores:
        return None
    return int(sorted(stores, key=lambda s: int(s.get("store_id", 10**9)))[0]["store_id"])

def _latest_meal_plan_for_household(data: Dict[str, Any], household_id: Optional[int]) -> Optional[Dict[str, Any]]:
    if household_id is None:
        return None
    plans = [m for m in data.get("meal_plans", []) if m.get("household_id") == household_id]
    if not plans:
        return None
    return sorted(plans, key=lambda m: int(m.get("meal_plan_id", 0)), reverse=True)[0]

def _latest_list_for_household(data: Dict[str, Any], household_id: Optional[int]) -> Optional[Dict[str, Any]]:
    if household_id is None:
        return None
    lists_ = [l for l in data.get("grocery_lists", []) if l.get("household_id") == household_id]
    if not lists_:
        return None
    return sorted(lists_, key=lambda l: int(l.get("list_id", 0)), reverse=True)[0]

def _latest_order_for_household(data: Dict[str, Any], household_id: Optional[int]) -> Optional[Dict[str, Any]]:
    if household_id is None:
        return None
    orders = [o for o in data.get("orders", []) if o.get("household_id") == household_id]
    if not orders:
        return None
    return sorted(orders, key=lambda o: int(o.get("order_id", 0)), reverse=True)[0]

def _decode_filter_token(token: Optional[str]) -> Tuple[str, int, bool]:
    if not token:
        return ("Dinner", 0, False)
    try:
        _, meal_type, ppart, pfpart = token.split(":")
        min_protein = int(ppart[1:])
        pf = True if pfpart == "PF1" else False
        return (meal_type, min_protein, pf)
    except Exception:
        return ("Dinner", 0, False)

def _all_recipe_ids_filtered(data: Dict[str, Any], meal_type: str = "Dinner", min_protein_g: int = 0, peanut_free: bool = False) -> List[int]:
    out = []
    for r in data.get("recipes", []):
        if r.get("meal_type") != meal_type:
            continue
        if int(r.get("protein_g_per_serving", 0)) < int(min_protein_g):
            continue
        if peanut_free and not r.get("is_peanut_free", False):
            continue
        out.append(int(r.get("recipe_id")))
    return out

def _recent_recipe_ids(data: Dict[str, Any], household_id: Optional[int], days_back: int = 14, anchor_date: Optional[str] = None) -> List[int]:
    if household_id is None:
        return []
    if anchor_date:
        y, m, d = [int(x) for x in str(anchor_date).split("-")]
        end = date(y, m, d)
    else:
        hh_rows = [h for h in data.get("meal_history", []) if h.get("household_id") == household_id]
        if hh_rows:
            md = max([h["plan_date"] for h in hh_rows])
            y, m, d = [int(x) for x in md.split("-")]
            end = date(y, m, d)
        else:
            end = date(2025, 1, 1)
    start = end - timedelta(days=int(days_back))
    return [
        int(r.get("recipe_id"))
        for r in data.get("meal_history", [])
        if r.get("household_id") == household_id and str(r.get("plan_date")) >= start.isoformat()
    ]

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

def _pick_target_from_member(data: Dict[str, Any], member_id: Optional[int]) -> Tuple[int, int]:
    if member_id is not None:
        m = next((x for x in data.get("members", []) if x.get("member_id") == member_id), None)
        if m:
            cal = int(m.get("target_calories") or 0)
            pro = int(m.get("target_protein") or 0)
            if cal and pro:
                return cal, pro
    members = data.get("members", [])
    adults = [m for m in members if not m.get("is_child")]
    m = adults[0] if adults else (members[0] if members else None)
    if m:
        cal = int(m.get("target_calories") or 2200)
        pro = int(m.get("target_protein") or 110)
        return cal or 2200, pro or 110
    return 2200, 110

def _latest_meal_plan_id(data: Dict[str, Any], household_id: Optional[int]) -> Optional[int]:
    mp = _latest_meal_plan_for_household(data, household_id)
    return int(mp["meal_plan_id"]) if mp else None

def _latest_list_id(data: Dict[str, Any], household_id: Optional[int]) -> Optional[int]:
    gl = _latest_list_for_household(data, household_id)
    return int(gl["list_id"]) if gl else None

def _latest_order_id(data: Dict[str, Any], household_id: Optional[int]) -> Optional[int]:
    o = _latest_order_for_household(data, household_id)
    return int(o["order_id"]) if o else None

def _ids_from_kwargs_or_defaults(data: Dict[str, Any], kwargs: Dict[str, Any]) -> List[int]:
    ids = _parse_json_list_ids(kwargs.get("recipe_ids_json") or kwargs.get("candidate_recipe_ids_json"))
    if ids:
        return ids
    ft = kwargs.get("filter_token")
    if ft:
        meal, mp, pf = _decode_filter_token(ft)
        return _all_recipe_ids_filtered(data, meal, mp, pf)
    meal = kwargs.get("meal_type", "Dinner")
    mp = int(kwargs.get("min_protein_g", 0))
    pf = bool(kwargs.get("peanut_free", False))
    return _all_recipe_ids_filtered(data, meal, mp, pf)

class GetUserByEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        email = kwargs.get("email")
        user_id = kwargs.get("user_id")
        user = None
        if email:
            user = next((u for u in data.get("users", []) if u.get("email") == email), None)
        if user is None and user_id is not None:
            user = next((u for u in data.get("users", []) if u.get("user_id") == user_id), None)
        if user is None:
            fid = _first_user_id(data)
            user = next((u for u in data.get("users", []) if u.get("user_id") == fid), None)
        if not user:
            return _json_dump({"error": "no users available"})
        return _json_dump(user)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function":{"name":"get_user_by_email","description":"Retrieve a user by email or user_id; defaults to the first user.","parameters":{"type":"object","properties":{"email":{"type":"string"},"user_id":{"type":"integer"}},"required":[]}}}

class GetHouseholdByUserId(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        if user_id is None:
            user_id = _first_user_id(data)
        hh = _household_for_user(data, user_id)
        if not hh:
            return _json_dump({"error": "no households available"})
        return _json_dump(hh)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"get_household_by_user_id","description":"Get household for user_id; defaults to the first household if unspecified.","parameters":{"type":"object","properties":{"user_id":{"type":"integer"}},"required":[]}}}

class ListHouseholdMembers(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        if household_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
        rows = [m for m in data.get("members", []) if m.get("household_id") == household_id]
        return _json_dump(rows)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"list_household_members","description":"List members for a household; household defaults if omitted.","parameters":{"type":"object","properties":{"household_id":{"type":"integer"}},"required":[]}}}

class GetMemberByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        full_name = kwargs.get("full_name")
        if household_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
        members = [m for m in data.get("members", []) if m.get("household_id") == household_id]
        m = None
        if full_name:
            m = next((x for x in members if x.get("full_name") == full_name), None)
        if m is None and members:
            adults = [x for x in members if not x.get("is_child")]
            m = adults[0] if adults else members[0]
        if not m:
            return _json_dump({"error": "no member found"})
        return _json_dump(m)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"get_member_by_name","description":"Find a member by name; defaults to the first adult in the default household.","parameters":{"type":"object","properties":{"household_id":{"type":"integer"},"full_name":{"type":"string"}},"required":[]}}}

class ComputeAndSetMemberTargets(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        member_id = kwargs.get("member_id")
        if member_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
            members = [m for m in data.get("members", []) if m.get("household_id") == household_id]
            if not members:
                return _json_dump({"error": "no members available"})
            adults = [m for m in members if not m.get("is_child")]
            member_id = adults[0]["member_id"] if adults else members[0]["member_id"]
        m = next((x for x in data.get("members", []) if x.get("member_id") == member_id), None)
        if not m:
            return _json_dump({"error": f"member_id {member_id} not found"})
        if m.get("is_child"):
            calories, protein = 1200, 30
        else:
            calories, protein = 2200, 110
        level = (m.get("activity_level") or "medium").lower()
        bump = {"low": 0.0, "medium": 0.05, "high": 0.10}.get(level, 0.05)
        protein = int(round(protein * (1.0 + bump), 0))
        m["target_calories"] = calories
        m["target_protein"] = protein
        return _json_dump(m)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"compute_and_set_member_targets","description":"Compute and set targets for a member; defaults to first adult member.","parameters":{"type":"object","properties":{"member_id":{"type":"integer"}},"required":[]}}}

class ListRecentMealHistory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        days_back = int(kwargs.get("days_back", 14))
        anchor_date = kwargs.get("anchor_date")
        if household_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
        out = _recent_recipe_ids(data, household_id, days_back, anchor_date)
        return _json_dump({"household_id": household_id, "days_back": days_back, "recent_recipe_ids": out})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"list_recent_meal_history","description":"Return recent recipe_ids; defaults to last 14 days for default household.","parameters":{"type":"object","properties":{"household_id":{"type":"integer"},"days_back":{"type":"integer"},"anchor_date":{"type":"string"}},"required":[]}}}

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

class GenerateChildModifications(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ids = _parse_json_list_ids(kwargs.get("recipe_ids_json"))
        if not ids:
            household_id = _default_household_id(data, _first_user_id(data))
            mp = _latest_meal_plan_for_household(data, household_id)
            if mp:
                ids = [int(e.get("recipe_id")) for e in data.get("meal_plan_entries", []) if e.get("meal_plan_id") == mp.get("meal_plan_id")]
        notes = {}
        for rid in ids:
            r = _recipe_by_id(data, rid)
            if not r:
                continue
            base = r.get("notes") or ""
            add = " Child-friendly: mild seasoning; cut into bite-sized pieces."
            notes[str(rid)] = (base + add).strip()
        return _json_dump({"child_mod_notes": notes})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"generate_child_modifications","description":"Return a note per recipe_id; defaults to latest meal plan entries.","parameters":{"type":"object","properties":{"recipe_ids_json":{"type":"string"}},"required":[]}}}

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

class UpdateMealPlanEntryNotes(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        meal_plan_id = kwargs.get("meal_plan_id")
        notes_map = kwargs.get("notes_map")
        if meal_plan_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
            meal_plan_id = _latest_meal_plan_id(data, household_id)
        if notes_map is None:
            rec_ids = [int(e.get("recipe_id")) for e in data.get("meal_plan_entries", []) if e.get("meal_plan_id") == meal_plan_id]
            gen = json.loads(GenerateChildModifications.invoke(data, recipe_ids_json=json.dumps(rec_ids)))["child_mod_notes"]
            notes_map = gen
        updated = 0
        for e in data.get("meal_plan_entries", []):
            if e.get("meal_plan_id") != meal_plan_id:
                continue
            rid = str(e.get("recipe_id"))
            if rid in notes_map:
                e["notes"] = notes_map[rid]
                updated += 1
        return _json_dump({"updated_entries": updated})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"update_meal_plan_entry_notes","description":"Set notes for entries; defaults to child-friendly notes for latest plan.","parameters":{"type":"object","properties":{"meal_plan_id":{"type":"integer"},"notes_map":{"type":"object"}},"required":[]}}}

class CreateGroceryListFromMealPlan(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        meal_plan_id = kwargs.get("meal_plan_id")
        household_id = kwargs.get("household_id")
        created_by_user_id = kwargs.get("created_by_user_id")
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

class CategorizeGroceryListSections(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        list_id = kwargs.get("list_id")
        if list_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
            list_id = _latest_list_id(data, household_id)
        if list_id is None:
            return _json_dump({"updated_items": 0})
        cnt = 0
        for item in data.get("grocery_list_items", []):
            if item.get("list_id") != list_id:
                continue
            ingr = _ingredient_by_id(data, int(item.get("ingredient_id")))
            item["grocery_section"] = (ingr or {}).get("grocery_section", "Misc")
            cnt += 1
        return _json_dump({"updated_items": cnt})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"categorize_grocery_list_sections","description":"Refresh grocery_section on all items; defaults to latest list.","parameters":{"type":"object","properties":{"list_id":{"type":"integer"}},"required":[]}}}

class FlagPantryStaplesOnList(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        list_id = kwargs.get("list_id")
        if list_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
            list_id = _latest_list_id(data, household_id)
        if list_id is None:
            return _json_dump({"updated_items": 0})
        cnt = 0
        for item in data.get("grocery_list_items", []):
            if item.get("list_id") != list_id:
                continue
            ingr = _ingredient_by_id(data, int(item.get("ingredient_id")))
            item["pantry_staple_flag"] = bool((ingr or {}).get("pantry_staple_flag", False))
            cnt += 1
        return _json_dump({"updated_items": cnt})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"flag_pantry_staples_on_list","description":"Set pantry_staple_flag on list items; defaults to latest list.","parameters":{"type":"object","properties":{"list_id":{"type":"integer"}},"required":[]}}}

class FlagOverlapLastMonthOnList(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        list_id = kwargs.get("list_id")
        household_id = kwargs.get("household_id")
        anchor_date = kwargs.get("anchor_date")
        if household_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
        if list_id is None:
            list_id = _latest_list_id(data, household_id)
        if list_id is None or household_id is None:
            return _json_dump({"updated_items": 0})
        recent_ingrs = set([row["ingredient_id"] for row in _collect_recipe_ingredients(data, _recent_recipe_ids(data, household_id, 30, anchor_date))])
        cnt = 0
        for item in data.get("grocery_list_items", []):
            if item.get("list_id") != list_id:
                continue
            item["overlap_last_month_flag"] = int(item.get("ingredient_id")) in recent_ingrs
            cnt += 1
        return _json_dump({"updated_items": cnt})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"flag_overlap_last_month_on_list","description":"Mark grocery items that overlap with last 30 days; defaults to latest list and household.","parameters":{"type":"object","properties":{"list_id":{"type":"integer"},"household_id":{"type":"integer"},"anchor_date":{"type":"string"}},"required":[]}}}

class ListInventoryByHousehold(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        if household_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
        rows = [i for i in data.get("inventory_items", []) if i.get("household_id") == household_id]
        return _json_dump({"household_id": household_id, "inventory_items": rows})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"list_inventory_by_household","description":"Get inventory items for a household; defaults to primary household.","parameters":{"type":"object","properties":{"household_id":{"type":"integer"}},"required":[]}}}

class CheckStoreInventoryForList(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        list_id = kwargs.get("list_id")
        store_id = kwargs.get("store_id")
        if store_id is None:
            store_id = _default_store_id(data)
        if list_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
            list_id = _latest_list_id(data, household_id)
        if list_id is None or store_id is None:
            return _json_dump({"flagged_items": []})
        flagged = []
        for item in data.get("grocery_list_items", []):
            if item.get("list_id") != list_id:
                continue
            products = _store_products_for_ingredient(data, store_id, int(item["ingredient_id"]))
            best = _lowest_price_in_stock(products)
            if not best:
                flagged.append({"ingredient_id": int(item["ingredient_id"]), "status": "out_of_stock"})
            else:
                if best.get("stock_status_enum") == "low":
                    flagged.append({"ingredient_id": int(item["ingredient_id"]), "status": "low"})
        return _json_dump({"flagged_items": flagged})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"check_store_inventory_for_list","description":"Flag low/out-of-stock items for a list and store; defaults to latest list and first store.","parameters":{"type":"object","properties":{"list_id":{"type":"integer"},"store_id":{"type":"integer"}},"required":[]}}}

class FindSubstituteProducts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        store_id = kwargs.get("store_id")
        flagged_items = kwargs.get("flagged_items")
        list_id = kwargs.get("list_id")
        if store_id is None:
            store_id = _default_store_id(data)
        if flagged_items is None:
            if list_id is None:
                household_id = _default_household_id(data, _first_user_id(data))
                list_id = _latest_list_id(data, household_id)
            flagged_items = json.loads(CheckStoreInventoryForList.invoke(data, list_id=list_id, store_id=store_id)).get("flagged_items", [])
        suggestions = []
        for f in flagged_items:
            iid = int(f.get("ingredient_id"))
            if iid == 1002:
                products = _store_products_for_ingredient(data, store_id, 1001)
                best = _lowest_price_in_stock(products)
                if best:
                    suggestions.append({"ingredient_id": 1002, "substitute_ingredient_id": 1001, "substitute_product_id": int(best["product_id"])})
                    continue
            for cand in (1003, 1001):
                products = _store_products_for_ingredient(data, store_id, cand)
                best = _lowest_price_in_stock(products)
                if best:
                    suggestions.append({"ingredient_id": iid, "substitute_ingredient_id": cand, "substitute_product_id": int(best["product_id"])})
                    break
        return _json_dump({"substitutions": suggestions})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"find_substitute_products","description":"Propose deterministic substitutes; defaults to computing flagged items for latest list.","parameters":{"type":"object","properties":{"store_id":{"type":"integer"},"flagged_items":{"type":"array","items":{"type":"object"}},"list_id":{"type":"integer"}},"required":[]}}}

class UpdateGroceryListWithSubstitutes(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        list_id = kwargs.get("list_id")
        substitutions = kwargs.get("substitutions", [])
        if list_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
            list_id = _latest_list_id(data, household_id)
        if list_id is None:
            return _json_dump({"updated_items": 0})
        replaced = 0
        mapping = {int(s["ingredient_id"]): int(s["substitute_ingredient_id"]) for s in substitutions if "ingredient_id" in s and "substitute_ingredient_id" in s}
        for item in data.get("grocery_list_items", []):
            if item.get("list_id") != list_id:
                continue
            old = int(item.get("ingredient_id"))
            if old in mapping:
                new_ing_id = mapping[old]
                item["ingredient_id"] = new_ing_id
                ing = _ingredient_by_id(data, new_ing_id)
                item["grocery_section"] = (ing or {}).get("grocery_section", "Misc")
                replaced += 1
        return _json_dump({"updated_items": replaced})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"update_grocery_list_with_substitutes","description":"Replace ingredient_id for grocery items; defaults to latest list.","parameters":{"type":"object","properties":{"list_id":{"type":"integer"},"substitutions":{"type":"array","items":{"type":"object"}}},"required":[]}}}

class CreateOrderFromList(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        store_id = kwargs.get("store_id")
        list_id = kwargs.get("list_id")
        slot_start = kwargs.get("scheduled_slot_start_ts")
        slot_end = kwargs.get("scheduled_slot_end_ts")
        if store_id is None:
            store_id = _default_store_id(data)
        if household_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
        if list_id is None:
            list_id = _latest_list_id(data, household_id)
        if not slot_start:
            slot_start = "2025-01-02T18:00:00Z"
        if not slot_end:
            slot_end = "2025-01-02T20:00:00Z"
        if household_id is None or store_id is None or list_id is None:
            return _json_dump({"error": "unable to infer household, store, or list"})
        orders = data.get("orders", [])
        next_id = _max_id(orders, "order_id", 10000) + 1
        row = {
            "order_id": next_id,
            "household_id": int(household_id),
            "store_id": int(store_id),
            "list_id": int(list_id),
            "status_enum": "initialized",
            "subtotal_cents": 0,
            "total_cents": 0,
            "placed_ts": "2025-01-02T10:00:00Z",
            "scheduled_slot_start_ts": str(slot_start),
            "scheduled_slot_end_ts": str(slot_end),
        }
        orders.append(row)
        return _json_dump({"order_id": next_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"create_order_from_list","description":"Create a new order shell; infers household, store, list, and slot if omitted.","parameters":{"type":"object","properties":{"household_id":{"type":"integer"},"store_id":{"type":"integer"},"list_id":{"type":"integer"},"scheduled_slot_start_ts":{"type":"string"},"scheduled_slot_end_ts":{"type":"string"}},"required":[]}}}

class AddOrderItemsFromList(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get("order_id")
        store_id = kwargs.get("store_id")
        product_overrides = kwargs.get("product_overrides", {})
        if order_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
            order_id = _latest_order_id(data, household_id)
        order = next((o for o in data.get("orders", []) if o.get("order_id") == order_id), None)
        if not order:
            return _json_dump({"error": "no order available"})
        if store_id is None:
            store_id = int(order.get("store_id"))
        list_id = order.get("list_id")
        items = [i for i in data.get("grocery_list_items", []) if i.get("list_id") == list_id]
        oi_tbl = data.get("order_items", [])
        next_oi = _max_id(oi_tbl, "order_item_id", 10100)
        created_ids = []
        subtotal = 0
        for item in items:
            ingr_id = int(item.get("ingredient_id"))
            override_pid = product_overrides.get(str(ingr_id)) or product_overrides.get(ingr_id)
            product = None
            if override_pid is not None:
                product = next((p for p in data.get("store_products", []) if p.get("product_id") == int(override_pid)), None)
            if product is None:
                products = _store_products_for_ingredient(data, store_id, ingr_id)
                product = _lowest_price_in_stock(products)
            if product is None:
                continue
            next_oi += 1
            oi = {"order_item_id": next_oi,"order_id": order_id,"product_id": int(product.get("product_id")),"requested_qty": 1,"fulfilled_qty": 1,"substitute_product_id": None}
            oi_tbl.append(oi)
            created_ids.append(next_oi)
            subtotal += int(product.get("price_cents", 0))
        order["subtotal_cents"] = subtotal
        order["total_cents"] = subtotal + 200
        return _json_dump({"created_order_item_ids": created_ids, "subtotal_cents": order["subtotal_cents"], "total_cents": order["total_cents"]})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"add_order_items_from_list","description":"Populate order_items using lowest-price in-stock products; infers order and store.","parameters":{"type":"object","properties":{"order_id":{"type":"integer"},"store_id":{"type":"integer"},"product_overrides":{"type":"object"}},"required":[]}}}

class UpdateOrderStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get("order_id")
        new_status = kwargs.get("new_status", "placed")
        if order_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
            order_id = _latest_order_id(data, household_id)
        order = next((o for o in data.get("orders", []) if o.get("order_id") == order_id), None)
        if not order:
            return _json_dump({"error": "no order available"})
        order["status_enum"] = str(new_status)
        return _json_dump(order)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"update_order_status","description":"Update order status; defaults to latest order and status 'placed'.","parameters":{"type":"object","properties":{"order_id":{"type":"integer"},"new_status":{"type":"string"}},"required":[]}}}

class LogAuditEvent(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        user_id = kwargs.get("user_id")
        entity_type = kwargs.get("entity_type")
        entity_id = kwargs.get("entity_id")
        action_enum = kwargs.get("action_enum", "create")
        payload_json = kwargs.get("payload_json", {})
        if user_id is None:
            user_id = _first_user_id(data)
        if household_id is None:
            household_id = _default_household_id(data, user_id)
        if not entity_type or entity_id is None:
            mp = _latest_meal_plan_for_household(data, household_id)
            gl = _latest_list_for_household(data, household_id)
            od = _latest_order_for_household(data, household_id)
            candidates = []
            if mp: candidates.append(("meal_plans", int(mp["meal_plan_id"])))
            if gl: candidates.append(("grocery_lists", int(gl["list_id"])))
            if od: candidates.append(("orders", int(od["order_id"])))
            if candidates:
                entity_type, entity_id = sorted(candidates, key=lambda x: x[1], reverse=True)[0]
            else:
                entity_type, entity_id = "system", 0
        al = data.get("audit_logs", [])
        next_a = _max_id(al, "audit_id", 12000) + 1
        row = {
            "audit_id": next_a,
            "household_id": household_id,
            "user_id": user_id,
            "entity_type": str(entity_type),
            "entity_id": entity_id,
            "action_enum": str(action_enum),
            "payload_json": payload_json,
            "created_at": "2025-01-03T10:00:00Z"
        }
        al.append(row)
        return _json_dump({"audit_id": next_a})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"log_audit_event","description":"Insert an audit row; infers household, user, entity_type/id, and defaults action to 'create'.","parameters":{"type":"object","properties":{"household_id":{"type":"integer"},"user_id":{"type":"integer"},"entity_type":{"type":"string"},"entity_id":{"type":"integer"},"action_enum":{"type":"string"},"payload_json":{"type":"object"}},"required":[]}}}

class GenerateRecipePacket(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        meal_plan_id = kwargs.get("meal_plan_id")
        if meal_plan_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
            meal_plan_id = _latest_meal_plan_id(data, household_id)
        if meal_plan_id is None:
            return _json_dump({"error": "no meal_plan available"})
        uri = f"packet://meal_plan/{int(meal_plan_id)}"
        return _json_dump({"packet_uri": uri})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"generate_recipe_packet","description":"Produce a deterministic packet URI; defaults to latest meal plan.","parameters":{"type":"object","properties":{"meal_plan_id":{"type":"integer"}},"required":[]}}}

class GetMealPlanDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        meal_plan_id = kwargs.get("meal_plan_id")
        if meal_plan_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
            meal_plan_id = _latest_meal_plan_id(data, household_id)
        if meal_plan_id is None:
            return _json_dump({"error": "no meal_plan available"})
        row = next((m for m in data.get("meal_plans", []) if m.get("meal_plan_id") == meal_plan_id), None)
        if not row:
            return _json_dump({"error": f"meal_plan_id {meal_plan_id} not found"})
        return _json_dump(row)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"get_meal_plan_details","description":"Get a meal_plan row; defaults to latest.","parameters":{"type":"object","properties":{"meal_plan_id":{"type":"integer"}},"required":[]}}}

class GetGroceryListDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        list_id = kwargs.get("list_id")
        if list_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
            list_id = _latest_list_id(data, household_id)
        if list_id is None:
            return _json_dump({"error": "no grocery_list available"})
        header = _ensure_list_id(data, list_id)
        if not header:
            return _json_dump({"error": f"list_id {list_id} not found"})
        items = [i for i in data.get("grocery_list_items", []) if i.get("list_id") == list_id]
        return _json_dump({"grocery_list": header, "items": items})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"get_grocery_list_details","description":"Get a grocery_list header and items; defaults to latest list.","parameters":{"type":"object","properties":{"list_id":{"type":"integer"}},"required":[]}}}

TOOLS = [
    GetUserByEmail(),
    GetHouseholdByUserId(),
    ListHouseholdMembers(),
    GetMemberByName(),
    ComputeAndSetMemberTargets(),
    ListRecentMealHistory(),
    BuildRecipeFilters(),
    ListRecipesByFilters(),
    ExcludeRecentRecipes(),
    ApplyCuisineLimit(),
    RankRecipesForTargets(),
    GenerateChildModifications(),
    CreateMealPlan(),
    BulkAddMealPlanEntries(),
    UpdateMealPlanEntryNotes(),
    CreateGroceryListFromMealPlan(),
    CategorizeGroceryListSections(),
    FlagPantryStaplesOnList(),
    FlagOverlapLastMonthOnList(),
    ListInventoryByHousehold(),
    CheckStoreInventoryForList(),
    FindSubstituteProducts(),
    UpdateGroceryListWithSubstitutes(),
    CreateOrderFromList(),
    AddOrderItemsFromList(),
    UpdateOrderStatus(),
    LogAuditEvent(),
    GenerateRecipePacket(),
    GetMealPlanDetails(),
    GetGroceryListDetails(),
]
