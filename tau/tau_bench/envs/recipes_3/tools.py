import json
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db


def _error(msg: str) -> str:
    pass
    payload = {"error": msg}
    out = json.dumps(payload, indent=2)
    return out


def _get_table(data: dict[str, Any], name: str) -> list[dict[str, Any]]:
    pass
    table = data.setdefault(name, [])
    return _convert_db_to_list(table)


def _max_int(items: list[dict[str, Any]], key: str, default: int = 0) -> int:
    pass
    max_val = default
    for it in items:
        v = it.get(key)
        if isinstance(v, int) and v > max_val:
            max_val = v
    return max_val


#------------------------- READ / ACQUIRE TOOLS (15) -------------------------


class GetUserByEmail(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], email: str) -> str:
        users = _get_table(data, "users")
        user = next((u for u in users if u.get("email") == email), None)
        payload = {"user": user}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getUserByEmail",
                "description": "Returns the user row with the specified email.",
                "parameters": {
                    "type": "object",
                    "properties": {"email": {"type": "string"}},
                    "required": ["email"],
                },
            },
        }


class GetUserByFullName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], full_name: str) -> str:
        users = _get_table(data, "users")
        user = next((u for u in users if u.get("full_name") == full_name), None)
        payload = {"user": user}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserByFullName",
                "description": "Returns the user row with the specified full_name.",
                "parameters": {
                    "type": "object",
                    "properties": {"full_name": {"type": "string"}},
                    "required": ["full_name"],
                },
            },
        }


class GetHouseholdByPrimaryUser(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: int) -> str:
        households = _get_table(data, "households")
        hh = next((h for h in households if h.get("primary_user_id") == user_id), None)
        payload = {"household": hh}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetHouseholdByPrimaryUser",
                "description": "Returns the household where primary_user_id matches user_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "integer"}},
                    "required": ["user_id"],
                },
            },
        }


class ListHouseholdMembers(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], household_id: int) -> str:
        members = _get_table(data, "members")
        rows = [m for m in members.values() if m.get("household_id") == household_id]
        payload = {"members": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListHouseholdMembers",
                "description": "Lists all member rows for a household.",
                "parameters": {
                    "type": "object",
                    "properties": {"household_id": {"type": "integer"}},
                    "required": ["household_id"],
                },
            },
        }


class GetMemberTargets(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], member_id: int) -> str:
        members = _get_table(data, "members")
        m = next((x for x in members if x.get("member_id") == member_id), None)
        if not m:
            return _error("member not found")
        payload = {"calories": m.get("target_calories"), "protein": m.get("target_protein")}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getMemberTargets",
                "description": "Returns stored calorie and protein targets for a member.",
                "parameters": {
                    "type": "object",
                    "properties": {"member_id": {"type": "integer"}},
                    "required": ["member_id"],
                },
            },
        }


class ListRecipes(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        filters: dict[str, Any] = None
    ) -> str:
        if filters is None:
            filters = {}
        meal_type = filters.get("meal_type")
        cuisine = filters.get("cuisine")
        peanut_free = filters.get("peanut_free")
        min_protein_g = filters.get("min_protein_g")
        no_heat_required = filters.get("no_heat_required")
        minimal_prep = filters.get("minimal_prep")
        recipes = _get_table(data, "recipes")
        rows = recipes
        if meal_type:
            rows = [r for r in rows.values() if r.get("meal_type") == meal_type]
        if cuisine:
            rows = [r for r in rows.values() if r.get("cuisine") == cuisine]
        if peanut_free is True:
            rows = [r for r in rows.values() if r.get("is_peanut_free") is True]
        if isinstance(min_protein_g, (int, float)):
            rows = [
                r for r in rows if (r.get("protein_g_per_serving") or 0) >= min_protein_g
            ]
        if no_heat_required is True:
            rows = [r for r in rows.values() if (r.get("cook_minutes") or 0) == 0]
        if minimal_prep is True:
            rows = [r for r in rows.values() if (r.get("prep_minutes") or 999) <= 10]
        payload = {"recipes": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listRecipes",
                "description": "Lists recipes filtered by fields (meal_type, cuisine, peanut_free, min_protein_g, no_heat_required, minimal_prep).",
                "parameters": {
                    "type": "object",
                    "properties": {"filters": {"type": "object"}},
                    "required": ["filters"],
                },
            },
        }


class GetRecipeDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], recipe_id: int) -> str:
        recipes = _get_table(data, "recipes")
        row = next((r for r in recipes if r.get("recipe_id") == recipe_id), None)
        payload = {"recipe": row}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRecipeDetails",
                "description": "Returns the recipe row for recipe_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"recipe_id": {"type": "integer"}},
                    "required": ["recipe_id"],
                },
            },
        }


class ListRecipeIngredients(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], recipe_id: int) -> str:
        ri = _get_table(data, "recipe_ingredients")
        rows = [x for x in ri.values() if x.get("recipe_id") == recipe_id]
        payload = {"recipe_ingredients": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listRecipeIngredients",
                "description": "Returns recipe_ingredients rows for recipe_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"recipe_id": {"type": "integer"}},
                    "required": ["recipe_id"],
                },
            },
        }


class GetInventoryItems(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], household_id: int) -> str:
        inv = _get_table(data, "inventory_items")
        items = [x for x in inv.values() if x.get("household_id") == household_id]
        payload = {"inventory_items": items}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetInventoryItems",
                "description": "Returns inventory_items rows for a household.",
                "parameters": {
                    "type": "object",
                    "properties": {"household_id": {"type": "integer"}},
                    "required": ["household_id"],
                },
            },
        }


class GetMealHistoryRange(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], household_id: int, start_date: str, end_date: str
    ) -> str:
        mh = _get_table(data, "meal_history")
        rows = [
            h
            for h in mh
            if h.get("household_id") == household_id
            and start_date <= h.get("plan_date", "") <= end_date
        ]
        payload = {"meal_history": rows}
        out = json.dumps(payload, indent=2)
        return out
        pass
        mh = _get_table(data, "meal_history")
        rows = [
            h
            for h in mh
            if h.get("household_id") == household_id
            and start_date <= h.get("plan_date", "") <= end_date
        ]
        payload = {"meal_history": rows}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMealHistoryRange",
                "description": "Returns meal_history rows for a household in an inclusive date range (ISO yyyy-mm-dd).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"},
                    },
                    "required": ["household_id", "start_date", "end_date"],
                },
            },
        }


class ListStores(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], stores: list = None) -> str:
        stores = _get_table(data, "stores")
        payload = {"stores": stores}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listStores",
                "description": "Returns all stores.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }


class ListStoreProductsByIngredientIds(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], store_id: int, ingredient_ids: list[int]) -> str:
        sp = _get_table(data, "store_products")
        rows = [
            p
            for p in sp
            if p.get("store_id") == store_id
            and p.get("ingredient_id") in (ingredient_ids or [])
        ]
        payload = {"products": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListStoreProductsByIngredientIds",
                "description": "Returns store_products for a store filtered by ingredient_ids.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {"type": "integer"},
                        "ingredient_ids": {
                            "type": "array",
                            "items": {"type": "integer"},
                        },
                    },
                    "required": ["store_id", "ingredient_ids"],
                },
            },
        }


class GetGroceryList(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], list_id: int) -> str:
        lists_ = _get_table(data, "grocery_lists")
        gli = _get_table(data, "grocery_list_items")
        lst = next((l for l in lists_ if l.get("list_id") == list_id), None)
        items = [i for i in gli.values() if i.get("list_id") == list_id]
        payload = {"grocery_list": lst, "items": items}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetGroceryList",
                "description": "Returns grocery_list row and its items.",
                "parameters": {
                    "type": "object",
                    "properties": {"list_id": {"type": "integer"}},
                    "required": ["list_id"],
                },
            },
        }


class GetOrdersForHousehold(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], household_id: int) -> str:
        orders = _get_table(data, "orders")
        rows = [o for o in orders.values() if o.get("household_id") == household_id]
        payload = {"orders": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOrdersForHousehold",
                "description": "Returns all orders for a household.",
                "parameters": {
                    "type": "object",
                    "properties": {"household_id": {"type": "integer"}},
                    "required": ["household_id"],
                },
            },
        }


class GetOrderDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: int) -> str:
        orders = _get_table(data, "orders")
        items = _get_table(data, "order_items")
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        rows = [it for it in items.values() if it.get("order_id") == order_id]
        payload = {"order": order, "items": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOrderDetails",
                "description": "Returns an order row and its items.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "integer"}},
                    "required": ["order_id"],
                },
            },
        }


#------------------------- CALCULATE / MODIFY TOOLS (12) -------------------------


class ComputeNutritionTargets(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], member_ids: list[int]) -> str:
        members = _get_table(data, "members")
        out = {}
        for mid in member_ids or []:
            m = next((x for x in members if x.get("member_id") == mid), None)
            if m:
                out[str(mid)] = {
                    "calories": m.get("target_calories"),
                    "protein": m.get("target_protein"),
                }
        payload = {"targets": out}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputeNutritionTargets",
                "description": "Collects stored targets for the provided member_ids.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "member_ids": {"type": "array", "items": {"type": "integer"}}
                    },
                    "required": ["member_ids"],
                },
            },
        }


class BuildRecipeFilters(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        meal_type: str,
        peanut_free: bool | None = None,
        min_protein_g: int | None = None,
        no_heat_required: bool | None = None,
        minimal_prep: bool | None = None,
        no_heat: Any = None,
        max_prep_minutes: Any = None
    ) -> str:
        filters = {
            "meal_type": meal_type,
            "peanut_free": peanut_free,
            "min_protein_g": min_protein_g,
            "no_heat_required": no_heat_required,
            "minimal_prep": minimal_prep,
        }
        # Eliminate Nones in a deterministic manner
        filters = {k: v for k, v in filters.items() if v is not None}
        payload = {"filters": filters}
        out = json.dumps(payload, indent=2)
        return out
        pass
        filters = {
            "meal_type": meal_type,
            "peanut_free": peanut_free,
            "min_protein_g": min_protein_g,
            "no_heat_required": no_heat_required,
            "minimal_prep": minimal_prep,
        }
        #Eliminate Nones in a deterministic manner
        filters = {k: v for k, v in filters.items() if v is not None}
        payload = {"filters": filters}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "buildRecipeFilters",
                "description": "Returns a normalized recipe filter object.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_type": {"type": "string"},
                        "peanut_free": {"type": "boolean"},
                        "min_protein_g": {"type": "integer"},
                        "no_heat_required": {"type": "boolean"},
                        "minimal_prep": {"type": "boolean"},
                    },
                    "required": ["meal_type"],
                },
            },
        }


class ScoreAndRankCandidates(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], recipe_ids: list[int], targets: dict[str, Any], no_heat: Any = None) -> str:
        pass
        # Deterministic ranking: prioritize higher protein, then lower calories, followed by ascending recipe_id
        recipes = _get_table(data, "recipes")
        subset = [r for r in recipes.values() if r.get("recipe_id") in (recipe_ids or [])]
        ranked = sorted(
            subset,
            key=lambda r: (
                -(r.get("protein_g_per_serving") or 0),
                (r.get("calories_per_serving") or 0),
                r.get("recipe_id"),
            ),
        )
        payload = {"ranked": [r.get("recipe_id") for r in ranked]}
        out = json.dumps(payload, indent=2)
        return out
        pass
        #Deterministic ranking: prioritize higher protein, then lower calories, followed by ascending recipe_id
        recipes = _get_table(data, "recipes")
        subset = [r for r in recipes.values() if r.get("recipe_id") in (recipe_ids or [])]
        ranked = sorted(
            subset,
            key=lambda r: (
                -(r.get("protein_g_per_serving") or 0),
                (r.get("calories_per_serving") or 0),
                r.get("recipe_id"),
            ),
        )
        payload = {"ranked": [r.get("recipe_id") for r in ranked]}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "scoreAndRankCandidates",
                "description": "Ranks candidate recipe_ids deterministically by protein desc, calories asc, id asc.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_ids": {"type": "array", "items": {"type": "integer"}},
                        "targets": {"type": "object"},
                    },
                    "required": ["recipe_ids", "targets"],
                },
            },
        }


class ExcludeRecentRecipes(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        recipe_ids: list[int],
        recent_history: list[dict[str, Any]]
,
    candidate_recipe_ids_json: Any = None,
    ) -> str:
        recent_set = {row.get("recipe_id") for row in (recent_history or [])}
        kept = [rid for rid in (recipe_ids or []) if rid not in recent_set]
        payload = {"filtered": kept}
        out = json.dumps(payload, indent=2)
        return out
        pass
        recent_set = {row.get("recipe_id") for row in (recent_history or [])}
        kept = [rid for rid in (recipe_ids or []) if rid not in recent_set]
        payload = {"filtered": kept}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "excludeRecentRecipes",
                "description": "Filters out recipe_ids that appear in recent meal_history rows.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_ids": {"type": "array", "items": {"type": "integer"}},
                        "recent_history": {"type": "array", "items": {"type": "object"}},
                    },
                    "required": ["recipe_ids", "recent_history"],
                },
            },
        }


class EnforceCuisineAndOverlap(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        recipe_ids: list[int],
        max_per_cuisine: int,
        max_unique_ingredients: int, candidate_recipe_ids_json: Any = None) -> str:
        recipes = _get_table(data, "recipes")
        ri = _get_table(data, "recipe_ingredients")
        by_id = {r.get("recipe_id"): r for r in recipes}
        cuisine_count: dict[str, int] = {}
        selected: list[int] = []
        # Monitor distinct ingredients throughout the selection
        selected_ing: set = set()
        for rid in recipe_ids or []:
            rec = by_id.get(rid)
            if not rec:
                continue
            cz = rec.get("cuisine")
            cnt = cuisine_count.get(cz, 0)
            if cnt >= max_per_cuisine:
                continue
            # calculate ingredients for this recipe
            ings = {
                row.get("ingredient_id") for row in ri if row.get("recipe_id") == rid
            }
            new_ing = ings - selected_ing
            if len(new_ing) > max_unique_ingredients:
                continue
            selected.append(rid)
            cuisine_count[cz] = cnt + 1
            selected_ing |= ings
        payload = {"selected": selected}
        out = json.dumps(payload, indent=2)
        return out
        pass
        recipes = _get_table(data, "recipes")
        ri = _get_table(data, "recipe_ingredients")
        by_id = {r.get("recipe_id"): r for r in recipes}
        cuisine_count: dict[str, int] = {}
        selected: list[int] = []
        #Monitor distinct ingredients throughout the selection
        selected_ing: set = set()
        for rid in recipe_ids or []:
            rec = by_id.get(rid)
            if not rec:
                continue
            cz = rec.get("cuisine")
            cnt = cuisine_count.get(cz, 0)
            if cnt >= max_per_cuisine:
                continue
            #calculate ingredients for this recipe
            ings = {
                row.get("ingredient_id") for row in ri if row.get("recipe_id") == rid
            }
            new_ing = ings - selected_ing
            if len(new_ing) > max_unique_ingredients:
                continue
            selected.append(rid)
            cuisine_count[cz] = cnt + 1
            selected_ing |= ings
        payload = {"selected": selected}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "enforceCuisineAndOverlap",
                "description": "Enforces cuisine cap and unique ingredient overlap budget across ordered recipe_ids.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_ids": {"type": "array", "items": {"type": "integer"}},
                        "max_per_cuisine": {"type": "integer"},
                        "max_unique_ingredients": {"type": "integer"},
                    },
                    "required": [
                        "recipe_ids",
                        "max_per_cuisine",
                        "max_unique_ingredients",
                    ],
                },
            },
        }


class DeriveChildModifications(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], recipe_ids: list[int], ruleset: str) -> str:
        pass
        # Deterministic notes suitable for children
        recipes = _get_table(data, "recipes")
        by_id = {r.get("recipe_id"): r for r in recipes}
        notes = {}
        for rid in recipe_ids or []:
            r = by_id.get(rid)
            base = (r or {}).get("notes") or ""
            note = "Child: low spice, small pieces"
            if "kid" in (base or "").lower() or "child" in (base or "").lower():
                note = base
            notes[str(rid)] = note
        payload = {"child_notes": notes}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deriveChildModifications",
                "description": "Returns a map of recipe_id -> child-friendly note deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_ids": {"type": "array", "items": {"type": "integer"}},
                        "ruleset": {"type": "string"},
                    },
                    "required": ["recipe_ids", "ruleset"],
                },
            },
        }


class ConsolidateIngredients(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], recipe_ids: list[int]) -> str:
        ri = _get_table(data, "recipe_ingredients")
        agg: dict[tuple[int, str], float] = {}
        for rid in recipe_ids or []:
            for row in ri:
                if row["recipe_id"] != rid:
                    continue
                key = (row["ingredient_id"], row["unit"])
                qty = float(row["quantity"] or 0)
                agg[key] = agg.get(key, 0.0) + qty
        items = [
            {"ingredient_id": ing, "quantity": qty, "unit": unit}
            for (ing, unit), qty in agg.items()
        ]
        payload = {"items": items}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "consolidateIngredients",
                "description": "Aggregates recipe_ingredients for provided recipe_ids by ingredient_id and unit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_ids": {"type": "array", "items": {"type": "integer"}}
                    },
                    "required": ["recipe_ids"],
                },
            },
        }


class CategorizeAndFlag(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        items: list[dict[str, Any]],
        household_id: int,
        recent_30d: list[dict[str, Any]],
        ingredient_id: int = None,
        quantity: float = None,
        unit: str = None
    ) -> str:
        ingredients = _get_table(data, "ingredients")
        ing_map = {i.get("ingredient_id"): i for i in ingredients}
        recent_set = {h.get("recipe_id") for h in (recent_30d or [])}
        # To set the overlap flag, identify ingredients present in any recipe utilized in the past 30 days
        ri = _get_table(data, "recipe_ingredients")
        recent_ings = {
            x.get("ingredient_id") for x in ri if x.get("recipe_id") in recent_set
        }
        out_items = []
        for it in items or []:
            ing = ing_map.get(it.get("ingredient_id")) or {}
            out_items.append(
                {
                    "ingredient_id": it.get("ingredient_id"),
                    "quantity": it.get("quantity"),
                    "unit": it.get("unit"),
                    "grocery_section": ing.get("grocery_section"),
                    "pantry_staple_flag": bool(ing.get("pantry_staple_flag")),
                    "overlap_last_month_flag": it.get("ingredient_id") in recent_ings,
                }
            )
        payload = {"categorized_items": out_items}
        out = json.dumps(payload, indent=2)
        return out
        pass
        ingredients = _get_table(data, "ingredients")
        ing_map = {i.get("ingredient_id"): i for i in ingredients}
        recent_set = {h.get("recipe_id") for h in (recent_30d or [])}
        #To set the overlap flag, identify ingredients present in any recipe utilized in the past 30 days
        ri = _get_table(data, "recipe_ingredients")
        recent_ings = {
            x.get("ingredient_id") for x in ri if x.get("recipe_id") in recent_set
        }
        out_items = []
        for it in items or []:
            ing = ing_map.get(it.get("ingredient_id")) or {}
            out_items.append(
                {
                    "ingredient_id": it.get("ingredient_id"),
                    "quantity": it.get("quantity"),
                    "unit": it.get("unit"),
                    "grocery_section": ing.get("grocery_section"),
                    "pantry_staple_flag": bool(ing.get("pantry_staple_flag")),
                    "overlap_last_month_flag": it.get("ingredient_id") in recent_ings,
                }
            )
        payload = {"categorized_items": out_items}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "categorizeAndFlag",
                "description": "Adds grocery_section and flags to consolidated items using ingredients and recent history.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "items": {"type": "array", "items": {"type": "object"}},
                        "household_id": {"type": "integer"},
                        "recent_30d": {"type": "array", "items": {"type": "object"}},
                    },
                    "required": ["items", "household_id", "recent_30d"],
                },
            },
        }


class ComputePlateBalance(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], recipe_id: int) -> str:
        pass
        # Deterministic macro categorization using ingredient grocery_section as a reference
        ri = _get_table(data, "recipe_ingredients")
        ingredients = _get_table(data, "ingredients")
        section_map = {
            i["ingredient_id"]: i["grocery_section"] for i in ingredients
        }
        rows = [r for r in ri.values() if r["recipe_id"] == recipe_id]
        counts = {"veggies": 0, "protein": 0, "carb": 0, "fats": 0}
        for r in rows:
            sec = section_map.get(r["ingredient_id"]) or ""
            if sec in ("Produce", "Cereal & Breakfast"):
                counts["veggies"] += 1
            elif sec in ("Meat", "Seafood", "Refrigerated", "Deli"):
                counts["protein"] += 1
            elif sec in ("Pasta & Grains", "Bakery", "Canned Goods"):
                counts["carb"] += 1
            elif sec in ("Oils & Vinegars", "Spreads", "Health Foods"):
                counts["fats"] += 1
        payload = {"plate": counts}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "computePlateBalance",
                "description": "Returns a coarse macro balance proxy for a recipe.",
                "parameters": {
                    "type": "object",
                    "properties": {"recipe_id": {"type": "integer"}},
                    "required": ["recipe_id"],
                },
            },
        }


#------------------------- INVENTORY FILTER (EXPLICIT) -------------------------


class FilterRecipesByInventory(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        household_id: int,
        recipe_ids: list[int],
        allow_pantry_staples: bool = True,
        max_missing_ingredients: int = 1,
        recent_history: list[dict[str, Any]] | None = None
    ) -> str:
        ingredients = _get_table(data, "ingredients")
        inv = _get_table(data, "inventory_items")
        ri = _get_table(data, "recipe_ingredients")
        ing_map = {i.get("ingredient_id"): i for i in ingredients}
        # Create available set: quantity greater than 0 in inventory along with pantry staples (if permitted)
        inv_ids = {
            row.get("ingredient_id")
            for row in inv
            if row.get("household_id") == household_id
            and float(row.get("quantity") or 0) > 0
        }
        if allow_pantry_staples:
            for ing in ingredients:
                if bool(ing.get("pantry_staple_flag")):
                    inv_ids.add(ing.get("ingredient_id"))
        # Recent removal
        recent_set = {row.get("recipe_id") for row in (recent_history or [])}
        eligible: list[int] = []
        missing_counts: dict[str, int] = {}
        for rid in recipe_ids or []:
            if rid in recent_set:
                continue
            rows = [x for x in ri.values() if x.get("recipe_id") == rid]
            missing = 0
            for x in rows:
                ing_id = x.get("ingredient_id")
                if ing_id in inv_ids:
                    continue
                missing += 1
                if missing > int(max_missing_ingredients or 0):
                    break
            if missing <= int(max_missing_ingredients or 0):
                eligible.append(rid)
                missing_counts[str(rid)] = missing
        payload = {"eligible_recipe_ids": eligible, "missing_counts": missing_counts}
        out = json.dumps(
            payload, indent=2,
        )
        return out
        pass
        ingredients = _get_table(data, "ingredients")
        inv = _get_table(data, "inventory_items")
        ri = _get_table(data, "recipe_ingredients")
        ing_map = {i.get("ingredient_id"): i for i in ingredients}
        #Create available set: quantity greater than 0 in inventory along with pantry staples (if permitted)
        inv_ids = {
            row.get("ingredient_id")
            for row in inv
            if row.get("household_id") == household_id
            and float(row.get("quantity") or 0) > 0
        }
        if allow_pantry_staples:
            for ing in ingredients:
                if bool(ing.get("pantry_staple_flag")):
                    inv_ids.add(ing.get("ingredient_id"))
        #Recent removal
        recent_set = {row.get("recipe_id") for row in (recent_history or [])}
        eligible: list[int] = []
        missing_counts: dict[str, int] = {}
        for rid in recipe_ids or []:
            if rid in recent_set:
                continue
            rows = [x for x in ri.values() if x.get("recipe_id") == rid]
            missing = 0
            for x in rows:
                ing_id = x.get("ingredient_id")
                if ing_id in inv_ids:
                    continue
                missing += 1
                if missing > int(max_missing_ingredients or 0):
                    break
            if missing <= int(max_missing_ingredients or 0):
                eligible.append(rid)
                missing_counts[str(rid)] = missing
        payload = {"eligible_recipe_ids": eligible, "missing_counts": missing_counts}
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "filterRecipesByInventory",
                "description": "Filters recipe_ids by household inventory with optional pantry staples and missing-ingredient budget; excludes recent_history.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "recipe_ids": {"type": "array", "items": {"type": "integer"}},
                        "allow_pantry_staples": {"type": "boolean"},
                        "max_missing_ingredients": {"type": "integer"},
                        "recent_history": {"type": "array", "items": {"type": "object"}},
                    },
                    "required": ["household_id", "recipe_ids"],
                },
            },
        }


class ProposeSubstitutionsForRecipe(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        recipe_id: int,
        household_id: int,
        preserve_section: bool = True,
        require_peanut_free: bool = True,
        prefer_pantry_staples: bool = True
    ) -> str:
        ingredients = _get_table(data, "ingredients")
        ri = _get_table(data, "recipe_ingredients")
        inv = _get_table(data, "inventory_items")
        ing_map = {i.get("ingredient_id"): i for i in ingredients}
        inv_ids = {
            row.get("ingredient_id")
            for row in inv
            if row.get("household_id") == household_id
            and float(row.get("quantity") or 0) > 0
        }
        recipe_rows = [x for x in ri.values() if x.get("recipe_id") == recipe_id]
        substitutions: list[dict[str, int]] = []
        # Identify absent non-staple ingredients
        missing_ids: list[int] = []
        for r in recipe_rows:
            ing_id = r.get("ingredient_id")
            ing = ing_map.get(ing_id) or {}
            if ing_id in inv_ids:
                continue
            # pantry staples are deemed available; bypass substitution
            if bool(ing.get("pantry_staple_flag")):
                continue
            missing_ids.append(ing_id)

        # Pool of candidates adhering to constraints
        def candidate_pool(for_ing: dict[str, Any]) -> list[dict[str, Any]]:
            pool = []
            for cand in ingredients:
                if require_peanut_free and cand.get("peanut_free_flag") is False:
                    continue
                if preserve_section and cand.get("grocery_section") != for_ing.get(
                    "grocery_section"
                ):
                    continue
                if prefer_pantry_staples and not bool(cand.get("pantry_staple_flag")):
                    continue
                pool.append(cand)
            # if no pantry-staple candidate is available and the preference flag is activated, allow same-section regardless of staple
            if not pool:
                for cand in ingredients:
                    if require_peanut_free and cand.get("peanut_free_flag") is False:
                        continue
                    if preserve_section and cand.get("grocery_section") != for_ing.get(
                        "grocery_section"
                    ):
                        continue
                    pool.append(cand)
            # deterministic arrangement by ingredient_id in ascending order
            pool = sorted(pool, key=lambda c: c.get("ingredient_id"))
            return pool

        for mid in missing_ids:
            base = ing_map.get(mid) or {}
            pool = candidate_pool(base)
            if not pool:
                continue
            sub = pool[0]
            substitutions.append(
                {
                    "ingredient_id": mid,
                    "substitute_ingredient_id": sub.get("ingredient_id"),
                }
            )
        payload = {"substitutions": substitutions}
        out = json.dumps(payload, indent=2)
        return out
        pass
        ingredients = _get_table(data, "ingredients")
        ri = _get_table(data, "recipe_ingredients")
        inv = _get_table(data, "inventory_items")
        ing_map = {i.get("ingredient_id"): i for i in ingredients}
        inv_ids = {
            row.get("ingredient_id")
            for row in inv
            if row.get("household_id") == household_id
            and float(row.get("quantity") or 0) > 0
        }
        recipe_rows = [x for x in ri.values() if x.get("recipe_id") == recipe_id]
        substitutions: list[dict[str, int]] = []
        #Identify absent non-staple ingredients
        missing_ids: list[int] = []
        for r in recipe_rows:
            ing_id = r.get("ingredient_id")
            ing = ing_map.get(ing_id) or {}
            if ing_id in inv_ids:
                continue
            #pantry staples are deemed available; bypass substitution
            if bool(ing.get("pantry_staple_flag")):
                continue
            missing_ids.append(ing_id)

        #Pool of candidates adhering to constraints
        def candidate_pool(for_ing: dict[str, Any]) -> list[dict[str, Any]]:
            pass
            pool = []
            for cand in ingredients:
                if require_peanut_free and cand.get("peanut_free_flag") is False:
                    continue
                if preserve_section and cand.get("grocery_section") != for_ing.get(
                    "grocery_section"
                ):
                    continue
                if prefer_pantry_staples and not bool(cand.get("pantry_staple_flag")):
                    continue
                pool.append(cand)
            #if no pantry-staple candidate is available and the preference flag is activated, allow same-section regardless of staple
            if not pool:
                for cand in ingredients:
                    if require_peanut_free and cand.get("peanut_free_flag") is False:
                        continue
                    if preserve_section and cand.get("grocery_section") != for_ing.get(
                        "grocery_section"
                    ):
                        continue
                    pool.append(cand)
            #deterministic arrangement by ingredient_id in ascending order
            pool = sorted(pool, key=lambda c: c.get("ingredient_id"))
            return pool

        for mid in missing_ids:
            base = ing_map.get(mid) or {}
            pool = candidate_pool(base)
            if not pool:
                continue
            sub = pool[0]
            substitutions.append(
                {
                    "ingredient_id": mid,
                    "substitute_ingredient_id": sub.get("ingredient_id"),
                }
            )
        payload = {"substitutions": substitutions}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "proposeSubstitutionsForRecipe",
                "description": "Proposes deterministic substitutions for a recipe's missing non-staple ingredients based on inventory and ingredient constraints.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_id": {"type": "integer"},
                        "household_id": {"type": "integer"},
                        "preserve_section": {"type": "boolean"},
                        "require_peanut_free": {"type": "boolean"},
                        "prefer_pantry_staples": {"type": "boolean"},
                    },
                    "required": ["recipe_id", "household_id"],
                },
            },
        }


class ValidateRecipeSubstitutions(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        recipe_id: int,
        household_id: int,
        substitutions: list[dict[str, int]],
        require_peanut_free: bool = True,
        preserve_section: bool = True
    ) -> str:
        ingredients = _get_table(data, "ingredients")
        ri = _get_table(data, "recipe_ingredients")
        inv = _get_table(data, "inventory_items")
        ing_map = {i.get("ingredient_id"): i for i in ingredients}
        recipe_rows = [x for x in ri.values() if x.get("recipe_id") == recipe_id]
        inv_ids = {
            row.get("ingredient_id")
            for row in inv
            if row.get("household_id") == household_id
            and float(row.get("quantity") or 0) > 0
        }
        # Create a set of absent non-staples in relation to inventory
        missing_nonstaples = {
            x.get("ingredient_id")
            for x in recipe_rows
            if (x.get("ingredient_id") not in inv_ids)
            and not bool(
                (ing_map.get(x.get("ingredient_id")) or {}).get("pantry_staple_flag")
            )
        }
        covered = set()
        valid_pairs: list[dict[str, int]] = []
        for pair in substitutions or []:
            src = pair.get("ingredient_id")
            dst = pair.get("substitute_ingredient_id")
            src_ing = ing_map.get(src) or {}
            dst_ing = ing_map.get(dst) or {}
            if src not in missing_nonstaples:
                continue
            if require_peanut_free and dst_ing.get("peanut_free_flag") is False:
                continue
            if preserve_section and dst_ing.get("grocery_section") != src_ing.get(
                "grocery_section"
            ):
                continue
            valid_pairs.append({"ingredient_id": src, "substitute_ingredient_id": dst})
            covered.add(src)
        feasible = covered == missing_nonstaples
        payload = {"valid": feasible, "validated_substitutions": valid_pairs}
        out = json.dumps(
            payload, indent=2
        )
        return out
        pass
        ingredients = _get_table(data, "ingredients")
        ri = _get_table(data, "recipe_ingredients")
        inv = _get_table(data, "inventory_items")
        ing_map = {i.get("ingredient_id"): i for i in ingredients}
        recipe_rows = [x for x in ri.values() if x.get("recipe_id") == recipe_id]
        inv_ids = {
            row.get("ingredient_id")
            for row in inv
            if row.get("household_id") == household_id
            and float(row.get("quantity") or 0) > 0
        }
        #Create a set of absent non-staples in relation to inventory
        missing_nonstaples = {
            x.get("ingredient_id")
            for x in recipe_rows
            if (x.get("ingredient_id") not in inv_ids)
            and not bool(
                (ing_map.get(x.get("ingredient_id")) or {}).get("pantry_staple_flag")
            )
        }
        covered = set()
        valid_pairs: list[dict[str, int]] = []
        for pair in substitutions or []:
            src = pair.get("ingredient_id")
            dst = pair.get("substitute_ingredient_id")
            src_ing = ing_map.get(src) or {}
            dst_ing = ing_map.get(dst) or {}
            if src not in missing_nonstaples:
                continue
            if require_peanut_free and dst_ing.get("peanut_free_flag") is False:
                continue
            if preserve_section and dst_ing.get("grocery_section") != src_ing.get(
                "grocery_section"
            ):
                continue
            valid_pairs.append({"ingredient_id": src, "substitute_ingredient_id": dst})
            covered.add(src)
        feasible = covered == missing_nonstaples
        payload = {"valid": feasible, "validated_substitutions": valid_pairs}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "validateRecipeSubstitutions",
                "description": "Validates substitutions against household inventory; preserves peanut-free and grocery_section; returns feasibility and normalized pairs.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_id": {"type": "integer"},
                        "household_id": {"type": "integer"},
                        "substitutions": {"type": "array", "items": {"type": "object"}},
                        "require_peanut_free": {"type": "boolean"},
                        "preserve_section": {"type": "boolean"},
                    },
                    "required": ["recipe_id", "household_id", "substitutions"],
                },
            },
        }


class ProposeAndValidateSubstitutions(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        recipe_id: int,
        household_id: int,
        preserve_section: bool = True,
        require_peanut_free: bool = True,
        prefer_pantry_staples: bool = True
    ) -> str:
        # Initially, suggest deterministic substitutions
        proposed = json.loads(
            ProposeSubstitutionsForRecipe.invoke(
                data,
                recipe_id=recipe_id,
                household_id=household_id,
                preserve_section=preserve_section,
                require_peanut_free=require_peanut_free,
                prefer_pantry_staples=prefer_pantry_staples,
            )
        ).get("substitutions", [])
        # Subsequently, verify those substitutions based on integrity rules
        validated = json.loads(
            ValidateRecipeSubstitutions.invoke(
                data,
                recipe_id=recipe_id,
                household_id=household_id,
                substitutions=proposed,
                require_peanut_free=require_peanut_free,
                preserve_section=preserve_section,
            )
        )
        payload = {
            "valid": bool(validated.get("valid")),
            "validated_substitutions": validated.get("validated_substitutions", []),
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        pass
        #Initially, suggest deterministic substitutions
        proposed = json.loads(
            ProposeSubstitutionsForRecipe.invoke(
                data,
                recipe_id=recipe_id,
                household_id=household_id,
                preserve_section=preserve_section,
                require_peanut_free=require_peanut_free,
                prefer_pantry_staples=prefer_pantry_staples,
            )
        ).get("substitutions", [])
        #Subsequently, verify those substitutions based on integrity rules
        validated = json.loads(
            ValidateRecipeSubstitutions.invoke(
                data,
                recipe_id=recipe_id,
                household_id=household_id,
                substitutions=proposed,
                require_peanut_free=require_peanut_free,
                preserve_section=preserve_section,
            )
        )
        payload = {
                "valid": bool(validated.get("valid")),
                "validated_substitutions": validated.get("validated_substitutions", []),
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
                "name": "ProposeAndValidateSubstitutions",
                "description": "Proposes substitutions for a recipe and validates them in one deterministic step.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_id": {"type": "integer"},
                        "household_id": {"type": "integer"},
                        "preserve_section": {"type": "boolean"},
                        "require_peanut_free": {"type": "boolean"},
                        "prefer_pantry_staples": {"type": "boolean"},
                    },
                    "required": ["recipe_id", "household_id"],
                },
            },
        }


#------------------------- WRITE / PROTOCOL TOOLS (12) -------------------------


class CreateMealPlan(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        household_id: int,
        week_start_date: str,
        created_by_user_id: int
    ) -> str:
        table = _get_table(data, "meal_plans")
        existing = next(
            (
                m
                for m in table
                if m.get("household_id") == household_id
                and m.get("week_start_date") == week_start_date
                and m.get("created_by_user_id") == created_by_user_id
            ),
            None,
        )
        if existing:
            payload = {"meal_plan_id": existing.get("meal_plan_id"), "deduplicated": True}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        next_id = _max_int(table, "meal_plan_id", 0) + 1
        rec = {
            "meal_plan_id": next_id,
            "household_id": household_id,
            "week_start_date": week_start_date,
            "created_by_user_id": created_by_user_id,
            "created_at": "FIXED",
        }
        table.append(rec)
        payload = {"meal_plan_id": next_id, "deduplicated": False}
        out = json.dumps(payload, indent=2)
        return out
        pass
        table = _get_table(data, "meal_plans")
        existing = next(
            (
                m
                for m in table
                if m.get("household_id") == household_id
                and m.get("week_start_date") == week_start_date
                and m.get("created_by_user_id") == created_by_user_id
            ),
            None,
        )
        if existing:
            payload = {"meal_plan_id": existing.get("meal_plan_id"), "deduplicated": True}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        next_id = _max_int(table, "meal_plan_id", 0) + 1
        rec = {
            "meal_plan_id": next_id,
            "household_id": household_id,
            "week_start_date": week_start_date,
            "created_by_user_id": created_by_user_id,
            "created_at": "FIXED",
        }
        table.append(rec)
        payload = {"meal_plan_id": next_id, "deduplicated": False}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createMealPlan",
                "description": "Creates or returns an existing meal_plan deterministically.",
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


class CreateGroceryList(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        household_id: int,
        source_meal_plan_id: int,
        created_by_user_id: int,
        status_enum: str = "initialized"
    ) -> str:
        table = _get_table(data, "grocery_lists")
        existing = next(
            (
                g
                for g in table
                if g.get("household_id") == household_id
                and g.get("source_meal_plan_id") == source_meal_plan_id
            ),
            None,
        )
        if existing:
            payload = {"list_id": existing.get("list_id"), "deduplicated": True}
            out = json.dumps(
                payload, indent=2
            )
            return out
        next_id = _max_int(table, "list_id", 0) + 1
        rec = {
            "list_id": next_id,
            "household_id": household_id,
            "source_meal_plan_id": source_meal_plan_id,
            "created_by_user_id": created_by_user_id,
            "created_at": "FIXED",
            "status_enum": status_enum,
        }
        table.append(rec)
        payload = {"list_id": next_id, "deduplicated": False}
        out = json.dumps(payload, indent=2)
        return out
        pass
        table = _get_table(data, "grocery_lists")
        existing = next(
            (
                g
                for g in table
                if g.get("household_id") == household_id
                and g.get("source_meal_plan_id") == source_meal_plan_id
            ),
            None,
        )
        if existing:
            payload = {"list_id": existing.get("list_id"), "deduplicated": True}
            out = json.dumps(
                payload, indent=2
            )
            return out
        next_id = _max_int(table, "list_id", 0) + 1
        rec = {
            "list_id": next_id,
            "household_id": household_id,
            "source_meal_plan_id": source_meal_plan_id,
            "created_by_user_id": created_by_user_id,
            "created_at": "FIXED",
            "status_enum": status_enum,
        }
        table.append(rec)
        payload = {"list_id": next_id, "deduplicated": False}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createGroceryList",
                "description": "Creates or returns an existing grocery_list deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "source_meal_plan_id": {"type": "integer"},
                        "created_by_user_id": {"type": "integer"},
                        "status_enum": {"type": "string"},
                    },
                    "required": [
                        "household_id",
                        "source_meal_plan_id",
                        "created_by_user_id",
                    ],
                },
            },
        }


class AddGroceryListItems(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], list_id: int, items: list[dict[str, Any]]) -> str:
        table = _get_table(data, "grocery_list_items")
        next_id = _max_int(table, "item_id", 0)
        inserted = []
        for it in items or []:
            next_id += 1
            rec = {
                "item_id": next_id,
                "list_id": list_id,
                "ingredient_id": it["ingredient_id"],
                "quantity": it["quantity"],
                "unit": it["unit"],
                "grocery_section": it["grocery_section"],
                "pantry_staple_flag": bool(it["pantry_staple_flag"]),
                "overlap_last_month_flag": bool(it["overlap_last_month_flag"]),
            }
            table.append(rec)
            inserted.append(rec)
        payload = {"count": len(inserted)}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addGroceryListItems",
                "description": "Appends categorized items to a grocery list with deterministic item_ids.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {"type": "integer"},
                        "items": {"type": "array", "items": {"type": "object"}},
                    },
                    "required": ["list_id", "items"],
                },
            },
        }


class SetGroceryListStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], list_id: int, status_enum: str) -> str:
        lists_ = _get_table(data, "grocery_lists")
        lst = next((l for l in lists_ if l.get("list_id") == list_id), None)
        if not lst:
            return _error("list not found")
        lst["status_enum"] = status_enum
        payload = {"list_id": list_id, "status_enum": status_enum}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setGroceryListStatus",
                "description": "Sets status_enum for a grocery list.",
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


class CreateGroceryListFromPlan(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], meal_plan_id: int, created_by_user_id: int) -> str:
        plans = _get_table(data, "meal_plans")
        mp = next((p for p in plans if p.get("meal_plan_id") == meal_plan_id), None)
        if not mp:
            return _error("meal_plan not found")
        return CreateGroceryList.invoke(
            data,
            household_id=mp.get("household_id"),
            source_meal_plan_id=meal_plan_id,
            created_by_user_id=created_by_user_id,
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateGroceryListFromPlan",
                "description": "Creates a grocery list from a meal_plan_id (derives household).",
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
        if any(i.get("list_id") == list_id for i in gli.values()):
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


class ApplyChildNotesForPlan(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        meal_plan_id: int,
        note: str = "Child: low spice, small pieces"
    ) -> str:
        entries = _get_table(data, "meal_plan_entries")
        updated_ids: list[int] = []
        for e in entries:
            if e.get("meal_plan_id") == meal_plan_id and e.get("meal_type") == "Dinner":
                prev = e.get("notes")
                if prev != note:
                    e["notes"] = note
                    updated_ids.append(e.get("entry_id"))
        payload = {"updated_entry_ids": updated_ids, "note": note}
        out = json.dumps(payload, indent=2)
        return out
        pass
        entries = _get_table(data, "meal_plan_entries")
        updated_ids: list[int] = []
        for e in entries:
            if e.get("meal_plan_id") == meal_plan_id and e.get("meal_type") == "Dinner":
                prev = e.get("notes")
                if prev != note:
                    e["notes"] = note
                    updated_ids.append(e.get("entry_id"))
        payload = {"updated_entry_ids": updated_ids, "note": note}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "applyChildNotesForPlan",
                "description": "Idempotently sets a child-friendly note on all Dinner entries of a meal plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_plan_id": {"type": "integer"},
                        "note": {"type": "string"},
                    },
                    "required": ["meal_plan_id"],
                },
            },
        }


#(Eliminated duplicate SelectInventoryDinnerAndLog; a single definition is present below under SELECTION HELPERS)


class RecordAuditLog(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        household_id: int,
        user_id: int,
        entity_type: str,
        entity_id: int,
        action_enum: str,
        payload_json: dict[str, Any]
    ) -> str:
        table = _get_table(data, "audit_logs")
        next_id = _max_int(table, "audit_id", 0) + 1
        rec = {
            "audit_id": next_id,
            "household_id": household_id,
            "user_id": user_id,
            "entity_type": entity_type,
            "entity_id": entity_id,
            "action_enum": action_enum,
            "payload_json": payload_json,
            "created_at": "FIXED",
        }
        table.append(rec)
        payload = {"audit_id": next_id}
        out = json.dumps(payload, indent=2)
        return out
        pass
        table = _get_table(data, "audit_logs")
        next_id = _max_int(table, "audit_id", 0) + 1
        rec = {
            "audit_id": next_id,
            "household_id": household_id,
            "user_id": user_id,
            "entity_type": entity_type,
            "entity_id": entity_id,
            "action_enum": action_enum,
            "payload_json": payload_json,
            "created_at": "FIXED",
        }
        table.append(rec)
        payload = {"audit_id": next_id}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordAuditLog",
                "description": "Appends an audit log entry with next audit_id.",
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
                        "payload_json",
                    ],
                },
            },
        }


class UpdateInventoryQuantity(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], household_id: int, ingredient_id: int, delta: float
    ) -> str:
        inv = _get_table(data, "inventory_items")
        row = next(
            (
                x
                for x in inv
                if x.get("household_id") == household_id
                and x.get("ingredient_id") == ingredient_id
            ),
            None,
        )
        if not row:
            row = {
                "inv_item_id": _max_int(inv, "inv_item_id", 0) + 1,
                "household_id": household_id,
                "ingredient_id": ingredient_id,
                "quantity": 0,
                "unit": None,
                "location_enum": None,
                "best_by_date": None,
            }
            inv.append(row)
        q = float(row.get("quantity") or 0)
        q = max(0.0, q + float(delta))
        row["quantity"] = q
        payload = {"ingredient_id": ingredient_id, "quantity": q}
        out = json.dumps(payload, indent=2)
        return out
        pass
        inv = _get_table(data, "inventory_items")
        row = next(
            (
                x
                for x in inv
                if x.get("household_id") == household_id
                and x.get("ingredient_id") == ingredient_id
            ),
            None,
        )
        if not row:
            row = {
                "inv_item_id": _max_int(inv, "inv_item_id", 0) + 1,
                "household_id": household_id,
                "ingredient_id": ingredient_id,
                "quantity": 0,
                "unit": None,
                "location_enum": None,
                "best_by_date": None,
            }
            inv.append(row)
        q = float(row.get("quantity") or 0)
        q = max(0.0, q + float(delta))
        row["quantity"] = q
        payload = {"ingredient_id": ingredient_id, "quantity": q}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateInventoryQuantity",
                "description": "Adjusts inventory quantity by delta with floor at zero.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "ingredient_id": {"type": "integer"},
                        "delta": {"type": "number"},
                    },
                    "required": ["household_id", "ingredient_id", "delta"],
                },
            },
        }


class AppendMealHistory(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        household_id: int,
        plan_date: str,
        recipe_id: int,
        was_prepared: bool,
        rating_int: int | None = None
    ) -> str:
        table = _get_table(data, "meal_history")
        next_id = _max_int(table, "history_id", 0) + 1
        rec = {
            "history_id": next_id,
            "household_id": household_id,
            "plan_date": plan_date,
            "recipe_id": recipe_id,
            "was_prepared": was_prepared,
            "rating_int": rating_int,
        }
        table.append(rec)
        payload = {"history_id": next_id}
        out = json.dumps(payload, indent=2)
        return out
        pass
        table = _get_table(data, "meal_history")
        next_id = _max_int(table, "history_id", 0) + 1
        rec = {
            "history_id": next_id,
            "household_id": household_id,
            "plan_date": plan_date,
            "recipe_id": recipe_id,
            "was_prepared": was_prepared,
            "rating_int": rating_int,
        }
        table.append(rec)
        payload = {"history_id": next_id}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AppendMealHistory",
                "description": "Appends a meal_history record with next history_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "plan_date": {"type": "string"},
                        "recipe_id": {"type": "integer"},
                        "was_prepared": {"type": "boolean"},
                        "rating_int": {"type": "integer"},
                    },
                    "required": [
                        "household_id",
                        "plan_date",
                        "recipe_id",
                        "was_prepared",
                    ],
                },
            },
        }


class CreateOrder(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        store_id: int,
        household_id: int,
        list_id: int,
        status_enum: str,
        subtotal_cents: int,
        total_cents: int,
        slot_start_ts: str,
        slot_end_ts: str
    ) -> str:
        orders = _get_table(data, "orders")
        next_id = _max_int(orders, "order_id", 0) + 1
        rec = {
            "order_id": next_id,
            "household_id": household_id,
            "store_id": store_id,
            "list_id": list_id,
            "status_enum": status_enum,
            "subtotal_cents": subtotal_cents,
            "total_cents": total_cents,
            "placed_ts": slot_start_ts,
            "scheduled_slot_start_ts": slot_start_ts,
            "scheduled_slot_end_ts": slot_end_ts,
        }
        data["orders"][order_id] = rec
        payload = {"order_id": next_id}
        out = json.dumps(payload, indent=2)
        return out
        pass
        orders = _get_table(data, "orders")
        next_id = _max_int(orders, "order_id", 0) + 1
        rec = {
            "order_id": next_id,
            "household_id": household_id,
            "store_id": store_id,
            "list_id": list_id,
            "status_enum": status_enum,
            "subtotal_cents": subtotal_cents,
            "total_cents": total_cents,
            "placed_ts": slot_start_ts,
            "scheduled_slot_start_ts": slot_start_ts,
            "scheduled_slot_end_ts": slot_end_ts,
        }
        data["orders"][order_id] = rec
        payload = {"order_id": next_id}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateOrder",
                "description": "Creates an order deterministically with next order_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {"type": "integer"},
                        "household_id": {"type": "integer"},
                        "list_id": {"type": "integer"},
                        "status_enum": {"type": "string"},
                        "subtotal_cents": {"type": "integer"},
                        "total_cents": {"type": "integer"},
                        "slot_start_ts": {"type": "string"},
                        "slot_end_ts": {"type": "string"},
                    },
                    "required": [
                        "store_id",
                        "household_id",
                        "list_id",
                        "status_enum",
                        "subtotal_cents",
                        "total_cents",
                        "slot_start_ts",
                        "slot_end_ts",
                    ],
                },
            },
        }


class AddOrderItems(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: int, items: list[dict[str, Any]]) -> str:
        table = _get_table(data, "order_items")
        next_id = _max_int(table, "order_item_id", 0)
        count = 0
        for it in items or []:
            next_id += 1
            rec = {
                "order_item_id": next_id,
                "order_id": order_id,
                "product_id": it.get("product_id"),
                "requested_qty": it.get("requested_qty"),
                "fulfilled_qty": it.get("fulfilled_qty"),
                "substitute_product_id": it.get("substitute_product_id"),
            }
            table.append(rec)
            count += 1
        payload = {"count": count}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddOrderItems",
                "description": "Appends order_items for an order with deterministic order_item_ids.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "integer"},
                        "items": {"type": "array", "items": {"type": "object"}},
                    },
                    "required": ["order_id", "items"],
                },
            },
        }


class SetOrderStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: int, status_enum: str) -> str:
        orders = _get_table(data, "orders")
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            return _error("order not found")
        # basic valid transitions: placed -> delivered permitted, delivered unchangeable
        if order.get("status_enum") == "delivered" and status_enum != "delivered":
            return _error("illegal status transition")
        order["status_enum"] = status_enum
        payload = {"order_id": order_id, "status_enum": status_enum}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetOrderStatus",
                "description": "Sets the status_enum of an order with basic legal transition checks.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "integer"},
                        "status_enum": {"type": "string"},
                    },
                    "required": ["order_id", "status_enum"],
                },
            },
        }


#------------------------- SELECTION HELPERS (INVENTORY DINNER) -------------------------


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
            rows = [x for x in ri.values() if x.get("recipe_id") == rid]
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
                rows_local = [x for x in ri.values() if x.get("recipe_id") == rid]
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
            rows = [x for x in ri.values() if x.get("recipe_id") == rid]
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
                rows_local = [x for x in ri.values() if x.get("recipe_id") == rid]
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


#------------------------- UTILITY (1) -------------------------


class ReturnScalar(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], value: str) -> str:
        return str(value)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "returnScalar",
                "description": "Returns the provided scalar value as-is.",
                "parameters": {
                    "type": "object",
                    "properties": {"value": {"type": "string"}},
                    "required": ["value"],
                },
            },
        }


TOOLS = [
    #Inputs
    GetUserByEmail(),
    GetUserByFullName(),
    GetHouseholdByPrimaryUser(),
    ListHouseholdMembers(),
    GetMemberTargets(),
    ListRecipes(),
    GetRecipeDetails(),
    ListRecipeIngredients(),
    GetInventoryItems(),
    GetMealHistoryRange(),
    ListStores(),
    ListStoreProductsByIngredientIds(),
    GetGroceryList(),
    GetOrdersForHousehold(),
    GetOrderDetails(),
    #Calculate/Modify
    ComputeNutritionTargets(),
    BuildRecipeFilters(),
    ScoreAndRankCandidates(),
    ExcludeRecentRecipes(),
    EnforceCuisineAndOverlap(),
    DeriveChildModifications(),
    ConsolidateIngredients(),
    CategorizeAndFlag(),
    ComputePlateBalance(),
    FilterRecipesByInventory(),
    ProposeSubstitutionsForRecipe(),
    ValidateRecipeSubstitutions(),
    ProposeAndValidateSubstitutions(),
    #Outputs/Protocols
    CreateMealPlan(),
    AddMealPlanEntry(),
    AddMealPlanEntriesBulk(),
    CreateGroceryList(),
    AddGroceryListItems(),
    SetGroceryListStatus(),
    CreateMealPlanWithAutoEntries(),
    CreateGroceryListFromPlan(),
    CreateAndPopulateGroceryListFromPlan(),
    ApplyChildNotesForPlan(),
    SelectInventoryDinnerAndLog(),
    RecordAuditLog(),
    UpdateInventoryQuantity(),
    AppendMealHistory(),
    CreateOrder(),
    AddOrderItems(),
    SetOrderStatus(),
    #Utility
    ReturnScalar(),
]
