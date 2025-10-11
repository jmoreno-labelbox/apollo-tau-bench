# Copyright Sierra

from typing import Tuple
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump
from . import _first_user_id
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

def _parse_json_list_ids(json_str: str) -> List[int]:
    try:
        arr = json.loads(json_str)
        if isinstance(arr, list):
            return [int(x) for x in arr]
    except Exception:
        pass
    return []

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

def _household_for_user(data: Dict[str, Any], user_id: Optional[int]) -> Optional[Dict[str, Any]]:
    if user_id is not None:
        h = next((h for h in data.get("households", []) if h.get("primary_user_id") == user_id), None)
        if h:
            return h
    households = data.get("households", [])
    if not households:
        return None
    return sorted(households, key=lambda h: int(h.get("household_id", 10**9)))[0]

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

def _json_dump(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)

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

def _first_user_id(data: Dict[str, Any]) -> Optional[int]:
    users = data.get("users", [])
    if not users:
        return None
    return int(sorted(users, key=lambda u: int(u.get("user_id", 10**9)))[0]["user_id"])

def _default_household_id(data: Dict[str, Any], user_id: Optional[int] = None) -> Optional[int]:
    hh = _household_for_user(data, user_id)
    return hh.get("household_id") if hh else None

class ExcludeRecentRecipes(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], anchor_date, household_id, recent_recipe_ids, days_back = 14) -> str:
        if household_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
        cand = _ids_from_kwargs_or_defaults(data, kwargs)
        recent = recent_recipe_ids
        if recent is None:
            days_back = int(days_back)
            recent = _recent_recipe_ids(data, household_id, days_back, anchor_date)
        filtered = [rid for rid in cand if rid not in set(int(x) for x in recent)]
        return _json_dump({"filtered_recipe_ids_json": json.dumps(filtered)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"exclude_recent_recipes","description":"Remove recipes that appeared in recent history; defaults to last 14 days for default household.","parameters":{"type":"object","properties":{"candidate_recipe_ids_json":{"type":"string"},"filter_token":{"type":"string"},"meal_type":{"type":"string"},"min_protein_g":{"type":"integer"},"peanut_free":{"type":"boolean"},"recent_recipe_ids":{"type":"array","items":{"type":"integer"}},"household_id":{"type":"integer"},"days_back":{"type":"integer"},"anchor_date":{"type":"string"}},"required":[]}}}