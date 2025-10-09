#tools.py
#Recipes & Shopping List — Tools Interface (structured similarly to the given example)
#
#Assumptions:
#- Data is a dictionary mapping table_name to a list of dictionaries.
#- IDs are integers. New IDs are calculated as (maximum existing id + 1) for each table.
#- Tools generate deterministic timestamps/URIs when necessary (static strings),
#unless a value is specifically provided by the task.

import json
from typing import Any

from tau_bench.envs.tool import Tool


def _ingredient_by_id(
    data: dict[str, Any], ingredient_id: int
) -> dict[str, Any] | None:
    pass
    return next(
        (
            i
            for i in data.get("ingredients", [])
            if int(i.get("ingredient_id")) == ingredient_id
        ),
        None,
    )


def _plan_week_dates(week_start_date: str) -> list[str]:
    pass
    #Deterministic: create 7 sequential ISO dates starting from a given date YYYY-MM-DD
    from datetime import date, timedelta

    y, m, d = (int(x) for x in str(week_start_date).split("-"))
    start = date(y, m, d)
    return [(start + timedelta(days=i)).isoformat() for i in range(7)]


def _store_products_for_ingredient(
    data: dict[str, Any], store_id: int, ingredient_id: int
) -> list[dict[str, Any]]:
    pass
    return [
        p
        for p in data.get("store_products", [])
        if int(p.get("store_id")) == store_id
        and int(p.get("ingredient_id")) == ingredient_id
    ]


def _index_by(records: list[dict[str, Any]], key: str) -> dict[Any, dict[str, Any]]:
    pass
    out: dict[Any, dict[str, Any]] = {}
    for r in records:
        if key in r:
            out[r[key]] = r
    return out

#-----------------------
#Helpers (deterministic)
#-----------------------


def _json_dump(obj: Any) -> str:
    pass
    payload = obj
    out = json.dumps(payload, indent=2, ensure_ascii=False)
    return out


def _require(
    data: dict[str, Any], table: str, key: str, value: Any
) -> dict[str, Any] | None:
    pass
    row = next((r for r in data.get(table, []) if r.get(key) == value), None)
    return row


def _collect_recipe_ingredients(
    data: dict[str, Any], recipe_ids: list[int]
) -> list[dict[str, Any]]:
    pass
    ri = data.get("recipe_ingredients", [])
    ridset = set(recipe_ids)
    return [row for row in ri if int(row.get("recipe_id")) in ridset]


def _sum_grocery_items(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    pass
    #Aggregate quantities by (ingredient_id, unit)
    agg: dict[tuple[int, str], float] = {}
    for r in rows:
        iid = int(r["ingredient_id"])
        unit = str(r.get("unit"))
        qty = float(r.get("quantity", 0))
        agg[(iid, unit)] = agg.get((iid, unit), 0.0) + qty
    out = []
    for (iid, unit), qty in agg.items():
        out.append({"ingredient_id": iid, "quantity": qty, "unit": unit})
    return out


def _lowest_price_pref_stock(products: list[dict[str, Any]]) -> dict[str, Any] | None:
    pass
    #Sort by stock preference followed by price, in a deterministic manner
    rank = {"in_stock": 0, "low": 1, "out_of_stock": 2}

    def keyer(p: dict[str, Any]):
        pass
        return (
            rank.get(p.get("stock_status_enum"), 3),
            int(p.get("price_cents", 10**9)),
            int(p.get("product_id", 10**9)),
        )

    return sorted(products, key=keyer)[0] if products else None


def _max_id(records: list[dict[str, Any]], key: str, default: int) -> int:
    pass
    if not records:
        return default
    vals = []
    for r in records:
        try:
            vals.append(int(r.get(key)))
        except Exception:
            pass
    return max(vals) if vals else default


def _parse_json_list_ids(json_str: str) -> list[int]:
    pass
    try:
        arr = json.loads(json_str)
        if isinstance(arr, list):
            return [int(x) for x in arr]
    except Exception:
        pass
    return []


def _recipe_by_id(data: dict[str, Any], recipe_id: int) -> dict[str, Any] | None:
    pass
    return next(
        (r for r in data.get("recipes", []) if int(r.get("recipe_id")) == recipe_id),
        None,
    )


#-----------------------
#Read / Lookup
#-----------------------


class GetUserById(Tool):
    """Retrieve a user row using user_id."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        if user_id is None:
            return _json_dump({"error": "user_id is required"})
        row = _require(data, "users", "user_id", user_id)
        return _json_dump(row or {"error": f"user_id {user_id} not found"})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserById",
                "description": "Return user by user_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "integer"}},
                    "required": ["user_id"],
                },
            },
        }


class GetHouseholdById(Tool):
    """Retrieve household using household_id."""

    @staticmethod
    def invoke(data: dict[str, Any], household_id: str = None) -> str:
        if household_id is None:
            return _json_dump({"error": "household_id is required"})
        row = _require(data, "households", "household_id", household_id)
        return _json_dump(row or {"error": f"household_id {household_id} not found"})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetHouseholdById",
                "description": "Return a household row by household_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"household_id": {"type": "integer"}},
                    "required": ["household_id"],
                },
            },
        }


class ListHouseholdMembers(Tool):
    """Enumerate all members of a household."""

    @staticmethod
    def invoke(data: dict[str, Any], household_id: int = None) -> str:
        if household_id is None:
            return _json_dump({"error": "household_id is required"})
        rows = [
            m
            for m in data.get("members", [])
            if int(m.get("household_id")) == int(household_id)
        ]
        return _json_dump(rows)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListHouseholdMembers",
                "description": "List all members belonging to a household.",
                "parameters": {
                    "type": "object",
                    "properties": {"household_id": {"type": "integer"}},
                    "required": ["household_id"],
                },
            },
        }


class GetMemberTargets(Tool):
    """Retrieve target_calories/target_protein and flags for a member."""

    @staticmethod
    def invoke(data: dict[str, Any], member_id: str = None) -> str:
        if member_id is None:
            return _json_dump({"error": "member_id is required"})
        row = _require(data, "members", "member_id", member_id)
        if not row:
            return _json_dump({"error": f"member_id {member_id} not found"})
        out = {
            "member_id": member_id,
            "target_calories": row.get("target_calories"),
            "target_protein": row.get("target_protein"),
            "is_child": row.get("is_child"),
            "activity_level": row.get("activity_level"),
            "allergies_json": row.get("allergies_json"),
        }
        return _json_dump(out)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMemberTargets",
                "description": "Return member nutrition targets and key flags.",
                "parameters": {
                    "type": "object",
                    "properties": {"member_id": {"type": "integer"}},
                    "required": ["member_id"],
                },
            },
        }


class ListInventoryByHousehold(Tool):
    """Retrieve all inventory_items for a household (can be filtered by location if desired)."""

    @staticmethod
    def invoke(data: dict[str, Any], household_id: int = None, location_enum: str = None) -> str:
        if household_id is None:
            return _json_dump({"error": "household_id is required"})
        rows = [
            i
            for i in data.get("inventory_items", [])
            if int(i.get("household_id")) == int(household_id)
        ]
        if location_enum:
            rows = [
                r for r in rows if str(r.get("location_enum")) == str(location_enum)
            ]
        return _json_dump({"household_id": household_id, "inventory_items": rows})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListInventoryByHousehold",
                "description": "List inventory items for a household; optional location filter.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "location_enum": {"type": "string"},
                    },
                    "required": ["household_id"],
                },
            },
        }


class ListRecentMealHistory(Tool):
    """Retrieve recipe_ids from meal_history for a household over the last N days (anchor_date is optional)."""

    @staticmethod
    def invoke(data: dict[str, Any], household_id: int = None, days_back: int = None, anchor_date: str = None) -> str:
        if household_id is None or days_back is None:
            return _json_dump({"error": "household_id and days_back are required"})
        from datetime import date, timedelta

        if anchor_date:
            y, m, d = (int(x) for x in str(anchor_date).split("-"))
            end = date(y, m, d)
        else:
            hh = [
                h
                for h in data.get("meal_history", [])
                if int(h.get("household_id")) == int(household_id)
            ]
            if hh:
                md = max(str(h["plan_date"]) for h in hh)
                y, m, d = (int(x) for x in md.split("-"))
                end = date(y, m, d)
            else:
                end = date(2025, 1, 1)
        start = end - timedelta(days=int(days_back))
        out = [
            int(r.get("recipe_id"))
            for r in data.get("meal_history", [])
            if int(r.get("household_id")) == int(household_id)
            and str(r.get("plan_date")) >= start.isoformat()
        ]
        return _json_dump(
            {
                "household_id": household_id,
                "days_back": days_back,
                "recent_recipe_ids": out,
            }
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListRecentMealHistory",
                "description": "List recent recipe_ids from meal_history for a household.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "days_back": {"type": "integer"},
                        "anchor_date": {"type": "string"},
                    },
                    "required": ["household_id", "days_back"],
                },
            },
        }


class GetRecipeById(Tool):
    """Retrieve a recipe row using its id."""

    @staticmethod
    def invoke(data: dict[str, Any], recipe_id: str = None) -> str:
        if recipe_id is None:
            return _json_dump({"error": "recipe_id is required"})
        row = _recipe_by_id(data, int(recipe_id))
        return _json_dump(row or {"error": f"recipe_id {recipe_id} not found"})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRecipeById",
                "description": "Return a recipe by recipe_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"recipe_id": {"type": "integer"}},
                    "required": ["recipe_id"],
                },
            },
        }


class ListRecipeIngredients(Tool):
    """Retrieve combined recipe_ingredients for a recipe_id along with ingredient metadata."""

    @staticmethod
    def invoke(data: dict[str, Any], recipe_id: int = None) -> str:
        if recipe_id is None:
            return _json_dump({"error": "recipe_id is required"})
        rows = [
            r
            for r in data.get("recipe_ingredients", [])
            if int(r.get("recipe_id")) == int(recipe_id)
        ]
        ingr_ix = _index_by(data.get("ingredients", []), "ingredient_id")
        out = []
        for ri in rows:
            iid = int(ri["ingredient_id"])
            meta = ingr_ix.get(iid, {})
            out.append(
                {
                    **ri,
                    **{
                        "ingredient_name": meta.get("ingredient_name"),
                        "grocery_section": meta.get("grocery_section"),
                        "pantry_staple_flag": meta.get("pantry_staple_flag"),
                        "peanut_free_flag": meta.get("peanut_free_flag"),
                        "default_unit": meta.get("default_unit"),
                    },
                }
            )
        return _json_dump(out)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListRecipeIngredients",
                "description": "Join recipe_ingredients with ingredient metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {"recipe_id": {"type": "integer"}},
                    "required": ["recipe_id"],
                },
            },
        }


#-----------------------
#Filters / Selection
#-----------------------


class BuildRecipeFilters(Tool):
    """
    Construct a compact token that encodes filters:
      token = "F:<meal_type>:P<min_protein>:PF<0|1>:EX<csv_excluded_cuisines>"
    """

    @staticmethod
    def invoke(data: dict[str, Any], meal_type: str = "Dinner", min_protein_g: int = 0, peanut_free: bool = False, cuisines_exclude: list = None,
        no_heat: Any = None,
        max_prep_minutes: Any = None,
    ) -> str:
        if cuisines_exclude is None:
            cuisines_exclude = []
        if not isinstance(cuisines_exclude, list):
            cuisines_exclude = []
        ex = ",".join(sorted(str(c) for c in cuisines_exclude))
        token = f"F:{meal_type}:P{min_protein_g}:PF{1 if peanut_free else 0}:EX{ex}"
        return _json_dump({"filter_token": token})

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "BuildRecipeFilters",
                "description": "Construct a compact string token that encodes recipe filters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_type": {"type": "string"},
                        "min_protein_g": {"type": "integer"},
                        "peanut_free": {"type": "boolean"},
                        "cuisines_exclude": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["meal_type"],
                },
            },
        }


class ListRecipesByFilters(Tool):
    """Enumerate recipe_ids (in JSON string format) that correspond to a filter_token."""

    @staticmethod
    def invoke(data: dict[str, Any], filter_token: str = None, no_heat: Any = None) -> str:
        if not filter_token:
            return _json_dump({"error": "filter_token is required"})
        try:
            parts = filter_token.split(":")
            meal_type = parts[1]
            min_protein = int(parts[2][1:])
            pf = parts[3] == "PF1"
            ex = parts[4][2:] if len(parts) > 4 else ""
            excluded = {c for c in ex.split(",") if c} if ex else set()
        except Exception:
            return _json_dump({"error": "invalid filter_token"})
        out = []
        for r in data.get("recipes", []):
            if str(r.get("meal_type")) != meal_type:
                continue
            if int(r.get("protein_g_per_serving", 0)) < min_protein:
                continue
            if pf and not bool(r.get("is_peanut_free", False)):
                continue
            if excluded and str(r.get("cuisine")) in excluded:
                continue
            out.append(int(r.get("recipe_id")))
        return _json_dump({"candidate_recipe_ids_json": json.dumps(out)})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListRecipesByFilters",
                "description": "List recipe_ids (as JSON string) matching a filter token.",
                "parameters": {
                    "type": "object",
                    "properties": {"filter_token": {"type": "string"}},
                    "required": ["filter_token"],
                },
            },
        }


class ExcludeRecipeIds(Tool):
    """Eliminate any recipe_ids found in a given exclusion list."""

    @staticmethod
    def invoke(data: dict[str, Any], candidate_recipe_ids_json: str = "[]", ExcludeRecipeIds: list = None,
    exclude_recipe_ids: Any = None,
    ) -> str:
        candidates_json = candidate_recipe_ids_json
        exclude_ids = ExcludeRecipeIds or []
        cand = _parse_json_list_ids(candidates_json)
        exset = {int(x) for x in exclude_ids}
        out = [rid for rid in cand if rid not in exset]
        return _json_dump({"filtered_recipe_ids_json": json.dumps(out)})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ExcludeRecipeIds",
                "description": "Return candidates minus provided recipe_ids.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_recipe_ids_json": {"type": "string"},
                        "ExcludeRecipeIds": {
                            "type": "array",
                            "items": {"type": "integer"},
                        },
                    },
                    "required": ["candidate_recipe_ids_json", "ExcludeRecipeIds"],
                },
            },
        }


class ApplyCuisineCap(Tool):
    """Restrict a list of recipe_ids to a maximum of N for each cuisine."""

    @staticmethod
    def invoke(data: dict[str, Any], recipe_ids_json: str = "[]", max_per_cuisine: int = 2, exclude_recipe_ids: Any = None) -> str:
        ids = _parse_json_list_ids(recipe_ids_json)
        counts: dict[str, int] = {}
        selected: list[int] = []
        for rid in ids:
            r = _recipe_by_id(data, rid)
            if not r:
                continue
            cz = str(r.get("cuisine"))
            c = counts.get(cz, 0)
            if c < max_per_cuisine:
                selected.append(rid)
                counts[cz] = c + 1
        return _json_dump({"cuisine_limited_recipe_ids_json": json.dumps(selected)})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ApplyCuisineCap",
                "description": "Apply a per-cuisine maximum to a recipe set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_ids_json": {"type": "string"},
                        "max_per_cuisine": {"type": "integer"},
                    },
                    "required": ["recipe_ids_json", "max_per_cuisine"],
                },
            },
        }


class MinimizeNewIngredients(Tool):
    """Retain only recipes with a non-staple ingredient count ≤ cap."""
    @staticmethod
    def invoke(data: dict[str, Any], recipe_ids_json: str = "[]", max_new_ingredients_per_recipe: int = 3) -> str:
        ids = _parse_json_list_ids(recipe_ids_json)
        kept: list[int] = []
        for rid in ids:
            rows = [
                r
                for r in data.get("recipe_ingredients", [])
                if int(r.get("recipe_id")) == rid
            ]
            non_staples = 0
            for ri in rows:
                ing = _ingredient_by_id(data, int(ri["ingredient_id"]))
                if not ing or not bool(ing.get("pantry_staple_flag", False)):
                    non_staples += 1
            if non_staples <= max_new_ingredients_per_recipe:
                kept.append(rid)
        return _json_dump({"minimized_recipe_ids_json": json.dumps(kept)})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "MinimizeNewIngredients",
                "description": "Filter recipes by maximum non-staple ingredient count.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_ids_json": {"type": "string"},
                        "max_new_ingredients_per_recipe": {"type": "integer"},
                    },
                    "required": ["recipe_ids_json", "max_new_ingredients_per_recipe"],
                },
            },
        }


class RankRecipesForTargets(Tool):
    """Evaluate recipes based on proximity to (target_calories, target_protein); a lower score is preferable."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        recipe_ids_json: str = "[]",
        target_calories: int = 2000,
        target_protein: int = 100,
        needed_count: int = 7
    ) -> str:
        ids = _parse_json_list_ids(recipe_ids_json)
        scored: list[tuple[float, int, float]] = []
        for rid in ids:
            r = _recipe_by_id(data, rid)
            if not r:
                continue
            cal = int(r.get("calories_per_serving", 0))
            prot = int(r.get("protein_g_per_serving", 0))
            dev = abs(cal - target_calories) / max(1, target_calories) + 10.0 * abs(
                prot - target_protein
            ) / max(1, target_protein)
            scored.append((dev, rid, float(prot)))
        picked = [
            rid
            for _, rid, _ in sorted(scored, key=lambda x: (x[0], -x[2], x[1]))[
                :needed_count
            ]
        ]
        return _json_dump({"selected_recipe_ids_json": json.dumps(picked)})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RankRecipesForTargets",
                "description": "Select up to N recipes closest to nutrition targets.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_ids_json": {"type": "string"},
                        "needed_count": {"type": "integer"},
                        "target_calories": {"type": "integer"},
                        "target_protein": {"type": "integer"},
                    },
                    "required": [
                        "recipe_ids_json",
                        "needed_count",
                        "target_calories",
                        "target_protein",
                    ],
                },
            },
        }


class GenerateChildModifications(Tool):
    """Provide notes for each recipe_id regarding child-friendly modifications (mild spice, bite-sized)."""

    @staticmethod
    def invoke(data: dict[str, Any], recipe_ids_json: str = "[]") -> str:
        ids = _parse_json_list_ids(recipe_ids_json)
        notes: dict[str, str] = {}
        for rid in ids:
            base = (_recipe_by_id(data, rid) or {}).get("notes") or ""
            add = " Child-friendly: mild seasoning; cut to bite-size; soft textures."
            notes[str(rid)] = (str(base) + add).strip()
        return _json_dump({"child_mod_notes": notes})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateChildModifications",
                "description": "Create deterministic child-friendly notes for recipes.",
                "parameters": {
                    "type": "object",
                    "properties": {"recipe_ids_json": {"type": "string"}},
                    "required": ["recipe_ids_json"],
                },
            },
        }


#-----------------------
#Create / Update (Plans & Lists)
#-----------------------


class CreateMealPlan(Tool):
    """Add a new meal_plan row and return the meal_plan_id."""

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        household_id: int = None, 
        week_start_date: str = None, 
        created_by_user_id: int = None
    ) -> str:
        if household_id is None or created_by_user_id is None or not week_start_date:
            return _json_dump(
                {
                    "error": "household_id, week_start_date, created_by_user_id are required"
                }
            )
        tbl = data.setdefault("meal_plans", [])
        next_id = _max_id(tbl, "meal_plan_id", 6000) + 1
        row = {
            "meal_plan_id": next_id,
            "household_id": int(household_id),
            "week_start_date": str(week_start_date),
            "created_by_user_id": int(created_by_user_id),
            "created_at": "2025-01-01T00:00:00Z",
        }
        tbl.append(row)
        return _json_dump({"meal_plan_id": next_id})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateMealPlan",
                "description": "Create a new meal plan (header).",
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


class BulkAddMealPlanEntries(Tool):
    """Generate Dinner entries for a week based on ordered recipe_ids_json; returns entry_ids."""

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        meal_plan_id: int = None, 
        week_start_date: str = None, 
        selected_recipe_ids_json: str = "[]",
        meal_type_enum: Any = None,
        entry_dates_json: Any = None,
        enforce_cuisine_diversity: Any = None,
        enforce_nutrition_window: Any = None
    ) -> str:
        if meal_plan_id is None or not week_start_date or not selected_recipe_ids_json:
            return _json_dump(
                {
                    "error": "meal_plan_id, week_start_date, selected_recipe_ids_json are required"
                }
            )
        recipes = _parse_json_list_ids(selected_recipe_ids_json)
        if not recipes:
            return _json_dump({"error": "no recipes provided"})
        dates = _plan_week_dates(str(week_start_date))
        tbl = data.setdefault("meal_plan_entries", [])
        next_id = _max_id(tbl, "entry_id", 6100)
        created: list[int] = []
        for i, rid in enumerate(recipes[:7]):
            next_id += 1
            row = {
                "entry_id": next_id,
                "meal_plan_id": int(meal_plan_id),
                "plan_date": dates[i] if i < len(dates) else dates[-1],
                "meal_type": "Dinner",
                "recipe_id": int(rid),
                "servings_adult": 2,
                "servings_child": 1,
                "notes": "",
            }
            tbl.append(row)
            created.append(next_id)
        return _json_dump({"created_entry_ids": created})
        
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "BulkAddMealPlanEntries",
                "description": "Insert a week of Dinner entries for a meal plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_plan_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                        "selected_recipe_ids_json": {"type": "string"},
                    },
                    "required": [
                        "meal_plan_id",
                        "week_start_date",
                        "selected_recipe_ids_json",
                    ],
                },
            },
        }


class UpdateMealPlanEntryNotes(Tool):
    """Assign entry notes using a mapping {recipe_id: note} for a specified meal_plan_id."""

    @staticmethod
    def invoke(data: dict[str, Any], meal_plan_id: int = None, notes_map: dict = None) -> str:
        if meal_plan_id is None or not isinstance(notes_map, dict):
            return _json_dump({"error": "meal_plan_id and notes_map are required"})
        updated = 0
        for e in data.get("meal_plan_entries", []):
            if int(e.get("meal_plan_id")) != int(meal_plan_id):
                continue
            rid = str(e.get("recipe_id"))
            if rid in notes_map:
                e["notes"] = notes_map[rid]
                updated += 1
        return _json_dump({"updated_entries": updated})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateMealPlanEntryNotes",
                "description": "Update notes for entries in a meal plan using a recipe_id->note map.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_plan_id": {"type": "integer"},
                        "notes_map": {"type": "object"},
                    },
                    "required": ["meal_plan_id", "notes_map"],
                },
            },
        }


class CreateEmptyGroceryList(Tool):
    """Generate an empty grocery_list header; returns list_id."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        household_id: int,
        created_by_user_id: int,
        source_meal_plan_id: int = None,
        status_enum: str = "initialized"
    ) -> str:
        if household_id is None or created_by_user_id is None:
            return _json_dump(
                {"error": "household_id and created_by_user_id are required"}
            )
        tbl = data.setdefault("grocery_lists", [])
        next_id = _max_id(tbl, "list_id", 8000) + 1
        row = {
            "list_id": next_id,
            "household_id": int(household_id),
            "source_meal_plan_id": (
                int(source_meal_plan_id) if source_meal_plan_id is not None else None
            ),
            "created_by_user_id": int(created_by_user_id),
            "created_at": "2025-01-01T12:00:00Z",
            "status_enum": str(status_enum),
        }
        tbl.append(row)
        return _json_dump({"list_id": next_id})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateEmptyGroceryList",
                "description": "Create an empty grocery_list header.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "source_meal_plan_id": {"type": "integer"},
                        "created_by_user_id": {"type": "integer"},
                        "status_enum": {"type": "string"},
                    },
                    "required": ["household_id", "created_by_user_id"],
                },
            },
        }


class UpsertGroceryListItemsFromRecipes(Tool):
    """Substitute all items for list_id with the combined ingredients from recipe_ids_json."""

    @staticmethod
    def invoke(data: dict[str, Any], list_id: int = None, recipe_ids_json: str = "[]") -> str:
        if list_id is None:
            return _json_dump({"error": "list_id is required"})
        recipe_ids = _parse_json_list_ids(recipe_ids_json)
        ri = _collect_recipe_ingredients(data, recipe_ids)
        items = _sum_grocery_items(ri)

        #delete old
        gli_tbl = data.setdefault("grocery_list_items", [])
        gli_tbl[:] = [r for r in gli_tbl if int(r.get("list_id")) != int(list_id)]

        #add new
        next_id = _max_id(gli_tbl, "item_id", 8100)
        created_ids: list[int] = []
        for it in items:
            next_id += 1
            ing = _ingredient_by_id(data, int(it["ingredient_id"]))
            row = {
                "item_id": next_id,
                "list_id": int(list_id),
                "ingredient_id": int(it["ingredient_id"]),
                "quantity": float(it["quantity"]),
                "unit": str(it["unit"]),
                "grocery_section": (ing or {}).get("grocery_section", "Misc"),
                "pantry_staple_flag": bool(
                    (ing or {}).get("pantry_staple_flag", False)
                ),
                "overlap_last_month_flag": False,
            }
            gli_tbl.append(row)
            created_ids.append(next_id)
        return _json_dump({"created_item_ids": created_ids})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpsertGroceryListItemsFromRecipes",
                "description": "Replace list items with aggregation from the provided recipe_ids.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {"type": "integer"},
                        "recipe_ids_json": {"type": "string"},
                    },
                    "required": ["list_id", "recipe_ids_json"],
                },
            },
        }


class CategorizeGroceryListSections(Tool):
    """Update grocery_section for all items in a list based on ingredient definitions."""

    @staticmethod
    def invoke(data: dict[str, Any], list_id: int = None) -> str:
        if list_id is None:
            return _json_dump({"error": "list_id is required"})
        updated = 0
        for item in data.get("grocery_list_items", []):
            if int(item.get("list_id")) != int(list_id):
                continue
            ing = _ingredient_by_id(data, int(item.get("ingredient_id")))
            item["grocery_section"] = (ing or {}).get("grocery_section", "Misc")
            updated += 1
        return _json_dump({"updated_items": updated})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CategorizeGroceryListSections",
                "description": "Set grocery_section on each item in a list from ingredients table.",
                "parameters": {
                    "type": "object",
                    "properties": {"list_id": {"type": "integer"}},
                    "required": ["list_id"],
                },
            },
        }


class FlagPantryStaplesOnList(Tool):
    """Assign pantry_staple_flag to list items according to the ingredients table."""

    @staticmethod
    def invoke(data: dict[str, Any], list_id: int = None) -> str:
        if list_id is None:
            return _json_dump({"error": "list_id is required"})
        updated = 0
        for item in data.get("grocery_list_items", []):
            if int(item.get("list_id")) != int(list_id):
                continue
            ing = _ingredient_by_id(data, int(item.get("ingredient_id")))
            item["pantry_staple_flag"] = bool(
                (ing or {}).get("pantry_staple_flag", False)
            )
            updated += 1
        return _json_dump({"updated_items": updated})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FlagPantryStaplesOnList",
                "description": "Fill pantry_staple_flag for items in a list.",
                "parameters": {
                    "type": "object",
                    "properties": {"list_id": {"type": "integer"}},
                    "required": ["list_id"],
                },
            },
        }


class FlagOverlapLastMonthOnList(Tool):
    """Set overlap_last_month_flag if the ingredient was used in recipes prepared in the last 30 days."""

    @staticmethod
    def invoke(data: dict[str, Any], list_id: int = None, household_id: int = None, anchor_date: str = None) -> str:
        if list_id is None or household_id is None:
            return _json_dump({"error": "list_id and household_id are required"})
        lr = json.loads(
            ListRecentMealHistory.invoke(
                data, household_id=household_id, days_back=30, anchor_date=anchor_date
            )
        )
        recent = [int(x) for x in lr.get("recent_recipe_ids", [])]
        ingr_recent = {
            int(r["ingredient_id"]) for r in _collect_recipe_ingredients(data, recent)
        }
        updated = 0
        for item in data.get("grocery_list_items", []):
            if int(item.get("list_id")) != int(list_id):
                continue
            item["overlap_last_month_flag"] = (
                int(item.get("ingredient_id")) in ingr_recent
            )
            updated += 1
        return _json_dump({"updated_items": updated})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FlagOverlapLastMonthOnList",
                "description": "Set overlap flag for list items based on last 30 days of meals.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {"type": "integer"},
                        "household_id": {"type": "integer"},
                        "anchor_date": {"type": "string"},
                    },
                    "required": ["list_id", "household_id"],
                },
            },
        }


class SetGroceryListStatus(Tool):
    """Modify grocery_lists.status_enum for the specified list_id."""

    @staticmethod
    def invoke(data: dict[str, Any], list_id: int = None, status_enum: str = None) -> str:
        if list_id is None or not status_enum:
            return _json_dump({"error": "list_id and status_enum are required"})
        row = _require(data, "grocery_lists", "list_id", int(list_id))
        if not row:
            return _json_dump({"error": f"list_id {list_id} not found"})
        row["status_enum"] = str(status_enum)
        return _json_dump(row)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetGroceryListStatus",
                "description": "Set the status of a grocery list.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {"type": "integer"},
                        "status_enum": {"type": "string"},
                    },
                    "required": ["list_id", "status_enum"],
                },
            },
        }


#-----------------------
#Store / Substitutions / Orders
#-----------------------


class CheckStoreInventoryForList(Tool):
    """Mark low/out_of_stock items for a list at a specific store; include the best in-store option if it exists."""

    @staticmethod
    def invoke(data: dict[str, Any], list_id: int = None, store_id: int = None) -> str:
        if list_id is None or store_id is None:
            return _json_dump({"error": "list_id and store_id are required"})
        gl_items = [
            i
            for i in data.get("grocery_list_items", [])
            if int(i.get("list_id")) == int(list_id)
        ]
        results = []
        for it in gl_items:
            iid = int(it["ingredient_id"])
            prods = _store_products_for_ingredient(data, int(store_id), iid)
            best = _lowest_price_pref_stock(prods)
            status = best.get("stock_status_enum") if best else "out_of_catalog"
            results.append(
                {
                    "item_id": int(it["item_id"]),
                    "ingredient_id": iid,
                    "matched_product_id": int(best["product_id"]) if best else None,
                    "stock_status_enum": status,
                    "price_cents": int(best.get("price_cents", 0)) if best else None,
                }
            )
        return _json_dump({"store_check": results})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckStoreInventoryForList",
                "description": "Check availability for each list item at a store and return best options.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {"type": "integer"},
                        "store_id": {"type": "integer"},
                    },
                    "required": ["list_id", "store_id"],
                },
            },
        }


class ProposeSubstituteProducts(Tool):
    """For marked items, suggest in-stock alternatives at the same store; respect peanut-free requirements if require_peanut_free is set."""

    @staticmethod
    def invoke(data: dict[str, Any], store_id: int = None, flagged_items: list = None, require_peanut_free: bool = False,
    list_id: Any = None,
    ) -> str:
        if flagged_items is None:
            flagged_items = []
        if store_id is None or not isinstance(flagged_items, list):
            return _json_dump({"error": "store_id and flagged_items are required"})
        suggestions = []
        for f in flagged_items:
            iid = int(f.get("ingredient_id"))
            # Primary: same ingredient with the best availability
            prods = _store_products_for_ingredient(data, int(store_id), iid)
            best = _lowest_price_pref_stock(
                [p for p in prods if p.get("stock_status_enum") in ("in_stock", "low")]
            )
            if best:
                suggestions.append(
                    {
                        "ingredient_id": iid,
                        "substitute_ingredient_id": iid,
                        "substitute_product_id": int(best["product_id"]),
                    }
                )
                continue
            # Fallback: any in-store item for the same ingredient category (skip if no dataset category)
            # Maintain deterministic behavior by providing no suggestions when none exist
            ing = _ingredient_by_id(data, iid)
            if (
                require_peanut_free
                and ing
                and not bool(ing.get("peanut_free_flag", True))
            ):
                # omit non-peanut-free bases if necessary
                continue
        return _json_dump({"substitutions": suggestions})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ProposeSubstituteProducts",
                "description": "Suggest in-store substitute products for flagged items.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {"type": "integer"},
                        "flagged_items": {"type": "array", "items": {"type": "object"}},
                        "require_peanut_free": {"type": "boolean"},
                    },
                    "required": ["store_id", "flagged_items"],
                },
            },
        }


class UpdateGroceryListWithSubstitutes(Tool):
    """Implement substitutions on grocery_list_items by modifying ingredient_id and updating grocery_section."""

    @staticmethod
    def invoke(data: dict[str, Any], list_id: int = None, substitutions: list = None) -> str:
        if list_id is None or not isinstance(substitutions, list):
            return _json_dump({"error": "list_id and substitutions are required"})
        mapping = {
            int(s["ingredient_id"]): int(s["substitute_ingredient_id"])
            for s in substitutions
            if "ingredient_id" in s and "substitute_ingredient_id" in s
        }
        updated = 0
        for it in data.get("grocery_list_items", []):
            if int(it.get("list_id")) != int(list_id):
                continue
            old = int(it.get("ingredient_id"))
            if old in mapping:
                new_iid = mapping[old]
                it["ingredient_id"] = new_iid
                ing = _ingredient_by_id(data, new_iid)
                it["grocery_section"] = (ing or {}).get("grocery_section", "Misc")
                updated += 1
        return _json_dump({"updated_items": updated})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateGroceryListWithSubstitutes",
                "description": "Replace ingredient_ids on list items using a substitution mapping.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {"type": "integer"},
                        "substitutions": {"type": "array", "items": {"type": "object"}},
                    },
                    "required": ["list_id", "substitutions"],
                },
            },
        }


class CreateOrderFromList(Tool):
    """Generate an order shell for a list and store with a scheduled slot; returns order_id."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        household_id: int = None,
        store_id: int = None,
        list_id: int = None,
        scheduled_slot_start_ts: str = None,
        scheduled_slot_end_ts: str = None,
    ) -> str:
        if (
            household_id is None
            or store_id is None
            or list_id is None
            or not scheduled_slot_start_ts
            or not scheduled_slot_end_ts
        ):
            return _json_dump(
                {
                    "error": "household_id, store_id, list_id, scheduled_slot_start_ts, scheduled_slot_end_ts are required"
                }
            )
        tbl = data.setdefault("orders", [])
        next_id = _max_id(tbl, "order_id", 10000) + 1
        row = {
            "order_id": next_id,
            "household_id": int(household_id),
            "store_id": int(store_id),
            "list_id": int(list_id),
            "status_enum": "initialized",
            "subtotal_cents": 0,
            "total_cents": 0,
            "placed_ts": "2025-01-02T10:00:00Z",
            "scheduled_slot_start_ts": str(scheduled_slot_start_ts),
            "scheduled_slot_end_ts": str(scheduled_slot_end_ts),
        }
        tbl.append(row)
        return _json_dump({"order_id": next_id})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateOrderFromList",
                "description": "Create a new order shell for a grocery list and store.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "store_id": {"type": "integer"},
                        "list_id": {"type": "integer"},
                        "scheduled_slot_start_ts": {"type": "string"},
                        "scheduled_slot_end_ts": {"type": "string"},
                    },
                    "required": [
                        "household_id",
                        "store_id",
                        "list_id",
                        "scheduled_slot_start_ts",
                        "scheduled_slot_end_ts",
                    ],
                },
            },
        }


class AddOrderItemsFromList(Tool):
    """Fill order_items from a list by selecting the lowest-priced in-stock product for each ingredient."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: int = None, store_id: int = None, product_overrides: dict = None,
    allowed_stock_statuses_json: Any = None,
    only_in_stock: Any = None,
    allow_instore_substitutions: Any = None,
    price_strategy: Any = None
    ) -> str:
        if product_overrides is None:
            product_overrides = {}
        if order_id is None or store_id is None:
            return _json_dump({"error": "order_id and store_id are required"})
        order = _require(data, "orders", "order_id", int(order_id))
        if not order:
            return _json_dump({"error": f"order_id {order_id} not found"})
        list_id = int(order["list_id"])
        items = [
            i
            for i in data.get("grocery_list_items", [])
            if int(i.get("list_id")) == list_id
        ]
        oi_tbl = data.setdefault("order_items", [])
        next_oi = _max_id(oi_tbl, "order_item_id", 10100)
        subtotal = 0
        created_ids: list[int] = []
        for it in items:
            ingr_id = int(it["ingredient_id"])
            override_pid = product_overrides.get(str(ingr_id)) or product_overrides.get(
                ingr_id
            )
            product = None
            if override_pid is not None:
                product = next(
                    (
                        p
                        for p in data.get("store_products", [])
                        if int(p.get("product_id")) == int(override_pid)
                    ),
                    None,
                )
            if product is None:
                prods = _store_products_for_ingredient(data, int(store_id), ingr_id)
                prods = [
                    p
                    for p in prods
                    if p.get("stock_status_enum") in ("in_stock", "low")
                ]
                product = _lowest_price_pref_stock(prods)
            if product is None:
                continue
            next_oi += 1
            row = {
                "order_item_id": next_oi,
                "order_id": int(order_id),
                "product_id": int(product.get("product_id")),
                "requested_qty": 1,
                "fulfilled_qty": 1,
                "substitute_product_id": None,
            }
            oi_tbl.append(row)
            created_ids.append(next_oi)
            subtotal += int(product.get("price_cents", 0))
        order["subtotal_cents"] = subtotal
        order["total_cents"] = subtotal  #deterministic (no hidden fees)
        return _json_dump(
            {
                "created_order_item_ids": created_ids,
                "subtotal_cents": order["subtotal_cents"],
                "total_cents": order["total_cents"],
            }
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddOrderItemsFromList",
                "description": "Populate order_items by selecting lowest-price in-stock products for each ingredient.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "integer"},
                        "store_id": {"type": "integer"},
                        "product_overrides": {"type": "object"},
                    },
                    "required": ["order_id", "store_id"],
                },
            },
        }


class UpdateOrderStatus(Tool):
    """Update orders.status_enum to a new state (e.g., 'placed', 'delivered')."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: int = None, new_status: str = None) -> str:
        if order_id is None or not new_status:
            return _json_dump({"error": "order_id and new_status are required"})
        row = _require(data, "orders", "order_id", int(order_id))
        if not row:
            return _json_dump({"error": f"order_id {order_id} not found"})
        row["status_enum"] = str(new_status)
        return _json_dump(row)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateOrderStatus",
                "description": "Update the status of an order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "integer"},
                        "new_status": {"type": "string"},
                    },
                    "required": ["order_id", "new_status"],
                },
            },
        }


class LogAuditEvent(Tool):
    """Add a row to audit_logs with a deterministic timestamp; returns audit_id."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        household_id: int = None,
        user_id: int = None,
        entity_type: str = None,
        entity_id: int = None,
        action_enum: str = None,
        payload_json: dict = {}
,
    created_at: Any = None,
    ) -> str:
        if (
            household_id is None
            or user_id is None
            or not entity_type
            or entity_id is None
            or not action_enum
        ):
            return _json_dump(
                {
                    "error": "household_id, user_id, entity_type, entity_id, action_enum are required"
                }
            )
        tbl = data.setdefault("audit_logs", [])
        next_id = _max_id(tbl, "audit_id", 12000) + 1
        row = {
            "audit_id": next_id,
            "household_id": int(household_id),
            "user_id": int(user_id),
            "entity_type": str(entity_type),
            "entity_id": int(entity_id),
            "action_enum": str(action_enum),
            "payload_json": payload_json,
            "created_at": "2025-01-03T10:00:00Z",
        }
        tbl.append(row)
        return _json_dump({"audit_id": next_id})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogAuditEvent",
                "description": "Append an audit log entry with a deterministic timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "user_id": {"type": "integer"},
                        "entity_type": {"type": "string"},
                        "entity_id": {"type": "integer"},
                        "action_enum": {"type": "string"},
                        "payload_json": {"type": "object"},
                    },
                    "required": [
                        "household_id",
                        "user_id",
                        "entity_type",
                        "entity_id",
                        "action_enum",
                    ],
                },
            },
        }


#-----------------------
#Retrieval / Utilities
#-----------------------


class GetMealPlanDetails(Tool):
    """Retrieve a meal_plan row using its id."""

    @staticmethod
    def invoke(data: dict[str, Any], meal_plan_id: int = None) -> str:
        if meal_plan_id is None:
            return _json_dump({"error": "meal_plan_id is required"})
        row = _require(data, "meal_plans", "meal_plan_id", int(meal_plan_id))
        return _json_dump(row or {"error": f"meal_plan_id {meal_plan_id} not found"})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMealPlanDetails",
                "description": "Get a meal_plan header by id.",
                "parameters": {
                    "type": "object",
                    "properties": {"meal_plan_id": {"type": "integer"}},
                    "required": ["meal_plan_id"],
                },
            },
        }


class GetGroceryListDetails(Tool):
    """Retrieve the grocery_list header and all items associated with list_id."""

    @staticmethod
    def invoke(data: dict[str, Any], list_id: int = None) -> str:
        if list_id is None:
            return _json_dump({"error": "list_id is required"})
        header = _require(data, "grocery_lists", "list_id", int(list_id))
        if not header:
            return _json_dump({"error": f"list_id {list_id} not found"})
        items = [
            i
            for i in data.get("grocery_list_items", [])
            if int(i.get("list_id")) == int(list_id)
        ]
        return _json_dump({"grocery_list": header, "items": items})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetGroceryListDetails",
                "description": "Get a grocery_list header plus items.",
                "parameters": {
                    "type": "object",
                    "properties": {"list_id": {"type": "integer"}},
                    "required": ["list_id"],
                },
            },
        }


class ListStores(Tool):
    """Retrieve all stores."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        return _json_dump(data.get("stores", []))
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listStores",
                "description": "List available stores.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class ListStoreProducts(Tool):
    """Enumerate store_products for a store (can be filtered by ingredient_id if desired)."""

    @staticmethod
    def invoke(data: dict[str, Any], store_id: int = None, ingredient_id: int = None) -> str:
        if store_id is None:
            return _json_dump({"error": "store_id is required"})
        rows = [
            p
            for p in data.get("store_products", [])
            if int(p.get("store_id")) == int(store_id)
        ]
        if ingredient_id is not None:
            rows = [
                p for p in rows if int(p.get("ingredient_id")) == int(ingredient_id)
            ]
        return _json_dump(rows)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listStoreProducts",
                "description": "List products for a store, optionally for an ingredient.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {"type": "integer"},
                        "ingredient_id": {"type": "integer"},
                    },
                    "required": ["store_id"],
                },
            },
        }


#-----------------------
#Tool registry
#-----------------------

TOOLS = [
    GetUserById(),
    GetHouseholdById(),
    ListHouseholdMembers(),
    GetMemberTargets(),
    ListInventoryByHousehold(),
    ListRecentMealHistory(),
    GetRecipeById(),
    ListRecipeIngredients(),
    BuildRecipeFilters(),
    ListRecipesByFilters(),
    ExcludeRecipeIds(),
    ApplyCuisineCap(),
    MinimizeNewIngredients(),
    RankRecipesForTargets(),
    GenerateChildModifications(),
    CreateMealPlan(),
    BulkAddMealPlanEntries(),
    UpdateMealPlanEntryNotes(),
    CreateEmptyGroceryList(),
    UpsertGroceryListItemsFromRecipes(),
    CategorizeGroceryListSections(),
    FlagPantryStaplesOnList(),
    FlagOverlapLastMonthOnList(),
    SetGroceryListStatus(),
    CheckStoreInventoryForList(),
    ProposeSubstituteProducts(),
    UpdateGroceryListWithSubstitutes(),
    CreateOrderFromList(),
    AddOrderItemsFromList(),
    UpdateOrderStatus(),
    LogAuditEvent(),
    GetMealPlanDetails(),
    GetGroceryListDetails(),
    ListStores(),
    ListStoreProducts(),
]
