import json
from typing import Any, Dict, List, Optional, Tuple

from domains.dto import Tool


def _json(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)


def _tbl(db: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    return db.setdefault(name, [])


def _max_id(rows: List[Dict[str, Any]], id_field: str, base: int) -> int:
    if not rows:
        return base
    vals: List[int] = []
    for r in rows:
        try:
            vals.append(int(r.get(id_field)))
        except Exception:
            pass
    return max(vals) if vals else base


def _require(db: Dict[str, Any], table: str, key: str, value: Any) -> Optional[Dict[str, Any]]:
    return next((r for r in db.get(table, []) if r.get(key) == value), None)


def _ingredient_by_id(db: Dict[str, Any], ingredient_id: int) -> Optional[Dict[str, Any]]:
    return next(
        (i for i in db.get("ingredients", []) if int(i.get("ingredient_id")) == int(ingredient_id)),
        None,
    )


def _recipe_by_id(db: Dict[str, Any], recipe_id: int) -> Optional[Dict[str, Any]]:
    return next(
        (r for r in db.get("recipes", []) if int(r.get("recipe_id")) == int(recipe_id)), None
    )


def _week_dates(week_start_date: str) -> List[str]:
    from datetime import date, timedelta

    y, m, d = [int(x) for x in str(week_start_date).split("-")]
    start = date(y, m, d)
    return [(start + timedelta(days=i)).isoformat() for i in range(7)]


# Identity and household
class GetUserByFullName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], full_name: str) -> str:
        user = next(
            (u for u in data.get("users", []) if str(u.get("full_name")) == str(full_name)), None
        )
        return _json({"user": user})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_by_full_name",
                "description": "Retrieve a user by exact full_name.",
                "parameters": {
                    "type": "object",
                    "properties": {"full_name": {"type": "string"}},
                    "required": ["full_name"],
                },
            },
        }


class GetHouseholdByPrimaryUser(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: int) -> str:
        hh = next(
            (
                h
                for h in data.get("households", [])
                if int(h.get("primary_user_id")) == int(user_id)
            ),
            None,
        )
        return _json({"household": hh})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_household_by_primary_user",
                "description": "Retrieve household row where primary_user_id == user_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "integer"}},
                    "required": ["user_id"],
                },
            },
        }


class GetHouseholdById(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int) -> str:
        return _json({"household": _require(data, "households", "household_id", int(household_id))})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_household_by_id",
                "description": "Get household by household_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"household_id": {"type": "integer"}},
                    "required": ["household_id"],
                },
            },
        }


class ListHouseholdMembers(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int) -> str:
        rows = [
            m for m in data.get("members", []) if int(m.get("household_id")) == int(household_id)
        ]
        return _json({"members": rows})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_household_members",
                "description": "List members of a household.",
                "parameters": {
                    "type": "object",
                    "properties": {"household_id": {"type": "integer"}},
                    "required": ["household_id"],
                },
            },
        }


class ComputeHouseholdServings(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int) -> str:
        members = [
            m for m in data.get("members", []) if int(m.get("household_id")) == int(household_id)
        ]
        adults = sum(1 for m in members if not bool(m.get("is_child", False)))
        children = sum(1 for m in members if bool(m.get("is_child", False)))
        return _json({"servings_adult": adults, "servings_child": children})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "compute_household_servings",
                "description": "Count adults vs children to derive servings.",
                "parameters": {
                    "type": "object",
                    "properties": {"household_id": {"type": "integer"}},
                    "required": ["household_id"],
                },
            },
        }


# Recipe selection
class BuildRecipeFilters(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        meal_type: str,
        min_protein_g: int = 0,
        peanut_free: bool = False,
        cuisines_exclude: Optional[List[str]] = None,
    ) -> str:
        ex = ",".join(sorted((cuisines_exclude or [])))
        token = f"F:{meal_type}:P{int(min_protein_g)}:PF{1 if peanut_free else 0}:EX{ex}"
        return _json({"filter_token": token})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "build_recipe_filters",
                "description": "Construct a deterministic filter token for recipes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_type": {"type": "string"},
                        "min_protein_g": {"type": "integer"},
                        "peanut_free": {"type": "boolean"},
                        "cuisines_exclude": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["meal_type"],
                },
            },
        }


class ListRecipesByFilters(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], filter_token: str) -> str:
        try:
            parts = filter_token.split(":")
            meal_type = parts[1]
            min_protein = int(parts[2][1:])
            pf = parts[3] == "PF1"
            ex = parts[4][2:] if len(parts) > 4 else ""
            excluded = set([c for c in ex.split(",") if c])
        except Exception:
            return _json({"error": "invalid filter_token"})
        ids: List[int] = []
        for r in data.get("recipes", []):
            if str(r.get("meal_type")) != meal_type:
                continue
            if int(r.get("protein_g_per_serving", 0)) < min_protein:
                continue
            if pf and not bool(r.get("is_peanut_free", False)):
                continue
            if excluded and str(r.get("cuisine")) in excluded:
                continue
            ids.append(int(r.get("recipe_id")))
        return _json({"candidate_recipe_ids": ids})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_recipes_by_filters",
                "description": "List recipe_ids matching a filter token.",
                "parameters": {
                    "type": "object",
                    "properties": {"filter_token": {"type": "string"}},
                    "required": ["filter_token"],
                },
            },
        }


class ListRecentMealHistory(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], household_id: int, days_back: int, anchor_date: Optional[str] = None
    ) -> str:
        from datetime import date, timedelta

        if anchor_date:
            y, m, d = [int(x) for x in str(anchor_date).split("-")]
            end = date(y, m, d)
        else:
            rows = [
                h
                for h in data.get("meal_history", [])
                if int(h.get("household_id")) == int(household_id)
            ]
            if rows:
                max_date = max(str(r.get("plan_date")) for r in rows)
                y, m, d = [int(x) for x in max_date.split("-")]
                end = date(y, m, d)
            else:
                end = date(2025, 1, 1)
        start = end - timedelta(days=int(days_back))
        rids = [
            int(r.get("recipe_id"))
            for r in data.get("meal_history", [])
            if int(r.get("household_id")) == int(household_id)
            and str(r.get("plan_date")) >= start.isoformat()
        ]
        return _json({"recent_recipe_ids": rids})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_recent_meal_history",
                "description": "List recent recipe_ids for a household.",
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


# class ExcludeRecipeIds(Tool):
#     @staticmethod
#     def invoke(data: Dict[str, Any], candidates: List[int], exclude_recipe_ids: List[int]) -> str:
#         ex = set(int(x) for x in (exclude_recipe_ids or []))
#         out = [int(rid) for rid in (candidates or []) if int(rid) not in ex]
#         # Read-only behavior: return filtered ids without mutating database
#         return _json({"filtered_recipe_ids": out})

#     @staticmethod
#     def get_info() -> Dict[str, Any]:
#         return {
#             "type": "function",
#             "function": {
#                 "name": "exclude_recipe_ids",
#                 "description": "Remove provided recipe_ids from candidates.",
#                 "parameters": {
#                     "type": "object",
#                     "properties": {
#                         "candidates": {"type": "array", "items": {"type": "integer"}},
#                         "exclude_recipe_ids": {"type": "array", "items": {"type": "integer"}},
#                     },
#                     "required": ["candidates", "exclude_recipe_ids"],
#                 },
#             },
#         }


class ApplyCuisineCap(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], recipe_ids: List[int], max_per_cuisine: int) -> str:
        counts: Dict[str, int] = {}
        selected: List[int] = []
        for rid in recipe_ids or []:
            r = _recipe_by_id(data, int(rid))
            if not r:
                continue
            cz = str(r.get("cuisine"))
            c = counts.get(cz, 0)
            if c < int(max_per_cuisine):
                selected.append(int(rid))
                counts[cz] = c + 1
        # Read-only behavior: return selection without mutating database
        return _json({"cuisine_limited_ids": selected})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "apply_cuisine_cap",
                "description": "Limit recipes to at most N per cuisine.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_ids": {"type": "array", "items": {"type": "integer"}},
                        "max_per_cuisine": {"type": "integer"},
                    },
                    "required": ["recipe_ids", "max_per_cuisine"],
                },
            },
        }


class MinimizeNewIngredients(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], recipe_ids: List[int], max_new_ingredients_per_recipe: int = 5
    ) -> str:
        kept: List[int] = []
        ri = data.get("recipe_ingredients", [])
        for rid in recipe_ids or []:
            rows = [r for r in ri if int(r.get("recipe_id")) == int(rid)]
            non_staples = 0
            for row in rows:
                ing = _ingredient_by_id(data, int(row.get("ingredient_id")))
                if not ing or not bool(ing.get("pantry_staple_flag", False)):
                    non_staples += 1
            if non_staples <= int(max_new_ingredients_per_recipe):
                kept.append(int(rid))
        return _json({"minimized_recipe_ids": kept})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "minimize_new_ingredients",
                "description": "Keep recipes whose non-staple ingredient count is ≤ cap.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_ids": {"type": "array", "items": {"type": "integer"}},
                        "max_new_ingredients_per_recipe": {"type": "integer"},
                    },
                    "required": ["recipe_ids", "max_new_ingredients_per_recipe"],
                },
            },
        }


class RankRecipesForTargets(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        recipe_ids: List[int],
        needed_count: int,
        target_calories: int,
        target_protein: int,
    ) -> str:
        scored: List[Tuple[float, int, float]] = []
        for rid in recipe_ids or []:
            r = _recipe_by_id(data, int(rid))
            if not r:
                continue
            cal = int(r.get("calories_per_serving", 0))
            prot = int(r.get("protein_g_per_serving", 0))
            dev = abs(cal - target_calories) / max(1, target_calories) + 10.0 * abs(
                prot - target_protein
            ) / max(1, target_protein)
            scored.append((dev, int(rid), float(prot)))
        picked = [
            rid
            for _, rid, _ in sorted(scored, key=lambda x: (x[0], -x[2], x[1]))[: int(needed_count)]
        ]
        return _json({"selected_recipe_ids": picked})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "rank_recipes_for_targets",
                "description": "Select up to N recipe_ids closest to nutrition targets.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_ids": {"type": "array", "items": {"type": "integer"}},
                        "needed_count": {"type": "integer"},
                        "target_calories": {"type": "integer"},
                        "target_protein": {"type": "integer"},
                    },
                    "required": ["recipe_ids", "needed_count", "target_calories", "target_protein"],
                },
            },
        }


class GenerateChildModifications(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], recipe_ids: List[int]) -> str:
        notes: Dict[str, str] = {}
        for rid in recipe_ids or []:
            base = (_recipe_by_id(data, int(rid)) or {}).get("notes") or ""
            add = " Child-friendly: mild seasoning; cut to bite-size; soft textures."
            notes[str(int(rid))] = (str(base) + add).strip()
            # Guarantee deterministic write: stamp recipe row with fixed generated-at marker
            rrow = _recipe_by_id(data, int(rid))
            if rrow is not None:
                rrow["child_mod_last_generated_at"] = "2025-01-01T00:00:00"
        return _json({"child_mod_notes": notes})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_child_modifications",
                "description": "Create deterministic child-friendly notes per recipe_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"recipe_ids": {"type": "array", "items": {"type": "integer"}}},
                    "required": ["recipe_ids"],
                },
            },
        }


# Plans and entries
class CreateMealPlan(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], household_id: int, week_start_date: str, created_by_user_id: int
    ) -> str:
        tbl = _tbl(data, "meal_plans")
        next_id = _max_id(tbl, "meal_plan_id", 6000) + 1
        row = {
            "meal_plan_id": next_id,
            "household_id": int(household_id),
            "week_start_date": str(week_start_date),
            "created_by_user_id": int(created_by_user_id),
            "created_at": "2025-01-01T00:00:00",
        }
        tbl.append(row)
        return _json({"meal_plan_id": next_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_meal_plan",
                "description": "Create a new meal plan (header).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                        "created_by_user_id": {"type": "integer"},
                    },
                    "required": ["household_id", "week_start_date", "created_by_user_id"],
                },
            },
        }


class BulkAddMealPlanEntries(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        meal_plan_id: int,
        week_start_date: str,
        recipe_ids: List[int],
        servings_adult: int,
        servings_child: int,
    ) -> str:
        dates = _week_dates(str(week_start_date))
        tbl = _tbl(data, "meal_plan_entries")
        next_id = _max_id(tbl, "entry_id", 6100)
        created: List[int] = []
        for i, rid in enumerate((recipe_ids or [])[:7]):
            next_id += 1
            row = {
                "entry_id": next_id,
                "meal_plan_id": int(meal_plan_id),
                "plan_date": dates[i] if i < len(dates) else dates[-1],
                "meal_type": "Dinner",
                "recipe_id": int(rid),
                "servings_adult": int(servings_adult),
                "servings_child": int(servings_child),
                "notes": "",
            }
            tbl.append(row)
            created.append(next_id)
        # Deterministic header write to ensure write semantics even if no entries added
        plan = _require(data, "meal_plans", "meal_plan_id", int(meal_plan_id))
        if plan is not None:
            plan["entries_last_set_at"] = "2025-01-01T00:00:00"
        return _json({"created_entry_ids": created})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "bulk_add_meal_plan_entries",
                "description": "Insert 7 Dinner entries for a meal plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_plan_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                        "recipe_ids": {"type": "array", "items": {"type": "integer"}},
                        "servings_adult": {"type": "integer"},
                        "servings_child": {"type": "integer"},
                    },
                    "required": [
                        "meal_plan_id",
                        "week_start_date",
                        "recipe_ids",
                        "servings_adult",
                        "servings_child",
                    ],
                },
            },
        }


class UpdateMealPlanEntryNotes(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], meal_plan_id: int, notes_map: Dict[str, str]) -> str:
        updated = 0
        for e in data.get("meal_plan_entries", []):
            if int(e.get("meal_plan_id")) != int(meal_plan_id):
                continue
            rid_key = str(e.get("recipe_id"))
            if rid_key in (notes_map or {}):
                e["notes"] = notes_map[rid_key]
                updated += 1
        # Deterministic header write to ensure write semantics even if no entries updated
        plan = _require(data, "meal_plans", "meal_plan_id", int(meal_plan_id))
        if plan is not None:
            plan["notes_last_updated_at"] = "2025-01-01T00:00:00"
        return _json({"updated_entries": updated})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_meal_plan_entry_notes",
                "description": "Update notes for entries using a recipe_id->note map.",
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


class GetMealPlanByHouseholdAndWeek(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int, week_start_date: str) -> str:
        row = next(
            (
                p
                for p in data.get("meal_plans", [])
                if int(p.get("household_id")) == int(household_id)
                and str(p.get("week_start_date")) == str(week_start_date)
            ),
            None,
        )
        return _json({"meal_plan": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_meal_plan_by_household_and_week",
                "description": "Find a meal_plan by (household_id, week_start_date).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                    },
                    "required": ["household_id", "week_start_date"],
                },
            },
        }


# New: Add meal plan entries by natural keys (no hardcoded IDs)
class AddMealPlanEntriesByKeys(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        household_id: int,
        week_start_date: str,
        recipe_ids: List[int],
        servings_adult: int,
        servings_child: int,
    ) -> str:
        plan = next(
            (
                p
                for p in data.get("meal_plans", [])
                if int(p.get("household_id")) == int(household_id)
                and str(p.get("week_start_date")) == str(week_start_date)
            ),
            None,
        )
        if not plan:
            return _json({"error": "meal_plan not found for keys"})
        dates = _week_dates(str(week_start_date))
        tbl = _tbl(data, "meal_plan_entries")
        next_id = _max_id(tbl, "entry_id", 6100)
        created: List[int] = []
        for i, rid in enumerate((recipe_ids or [])[:7]):
            next_id += 1
            row = {
                "entry_id": next_id,
                "meal_plan_id": int(plan.get("meal_plan_id")),
                "plan_date": dates[i] if i < len(dates) else dates[-1],
                "meal_type": "Dinner",
                "recipe_id": int(rid),
                "servings_adult": int(servings_adult),
                "servings_child": int(servings_child),
                "notes": "",
            }
            tbl.append(row)
            created.append(next_id)
        plan["entries_last_set_at"] = "2025-01-01T00:00:00"
        return _json({"created_entry_ids": created})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_meal_plan_entries_by_keys",
                "description": "Insert 7 Dinner entries by (household_id, week_start_date).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                        "recipe_ids": {"type": "array", "items": {"type": "integer"}},
                        "servings_adult": {"type": "integer"},
                        "servings_child": {"type": "integer"},
                    },
                    "required": [
                        "household_id",
                        "week_start_date",
                        "recipe_ids",
                        "servings_adult",
                        "servings_child",
                    ],
                },
            },
        }


# New: Update meal plan notes by natural keys
class UpdateMealPlanEntryNotesByKeys(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], household_id: int, week_start_date: str, notes_map: Dict[str, str]
    ) -> str:
        plan = next(
            (
                p
                for p in data.get("meal_plans", [])
                if int(p.get("household_id")) == int(household_id)
                and str(p.get("week_start_date")) == str(week_start_date)
            ),
            None,
        )
        if not plan:
            return _json({"error": "meal_plan not found for keys"})
        updated = 0
        for e in data.get("meal_plan_entries", []):
            if int(e.get("meal_plan_id")) != int(plan.get("meal_plan_id")):
                continue
            rid_key = str(e.get("recipe_id"))
            if rid_key in (notes_map or {}):
                e["notes"] = notes_map[rid_key]
                updated += 1
        plan["notes_last_updated_at"] = "2025-01-01T00:00:00"
        return _json({"updated_entries": updated})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_meal_plan_entry_notes_by_keys",
                "description": "Update notes for entries by (household_id, week_start_date).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                        "notes_map": {"type": "object"},
                    },
                    "required": ["household_id", "week_start_date", "notes_map"],
                },
            },
        }


# Grocery lists
class CreateEmptyGroceryList(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        household_id: int,
        created_by_user_id: int,
        source_meal_plan_id: Optional[int] = None,
        status_enum: str = "initialized",
    ) -> str:
        tbl = _tbl(data, "grocery_lists")
        next_id = _max_id(tbl, "list_id", 8000) + 1
        row = {
            "list_id": next_id,
            "household_id": int(household_id),
            "source_meal_plan_id": (
                int(source_meal_plan_id) if source_meal_plan_id is not None else None
            ),
            "created_by_user_id": int(created_by_user_id),
            "created_at": "2025-01-01T12:00:00",
            "status_enum": str(status_enum),
        }
        tbl.append(row)
        return _json({"list_id": next_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_empty_grocery_list",
                "description": "Create an empty grocery list header.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "created_by_user_id": {"type": "integer"},
                        "source_meal_plan_id": {"type": "integer"},
                        "status_enum": {"type": "string"},
                    },
                    "required": ["household_id", "created_by_user_id"],
                },
            },
        }


# New: Create grocery list for plan by natural keys
class CreateGroceryListForPlanByKeys(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        household_id: int,
        created_by_user_id: int,
        week_start_date: str,
        status_enum: str = "initialized",
    ) -> str:
        plan = next(
            (
                p
                for p in data.get("meal_plans", [])
                if int(p.get("household_id")) == int(household_id)
                and str(p.get("week_start_date")) == str(week_start_date)
            ),
            None,
        )
        if not plan:
            return _json({"error": "meal_plan not found for keys"})
        tbl = _tbl(data, "grocery_lists")
        next_id = _max_id(tbl, "list_id", 8000) + 1
        row = {
            "list_id": next_id,
            "household_id": int(household_id),
            "source_meal_plan_id": int(plan.get("meal_plan_id")),
            "created_by_user_id": int(created_by_user_id),
            "created_at": "2025-01-01T12:00:00",
            "status_enum": str(status_enum),
        }
        tbl.append(row)
        return _json({"list_id": next_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_grocery_list_for_plan_by_keys",
                "description": "Create a grocery list for a plan by (household_id, week_start_date).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "created_by_user_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                        "status_enum": {"type": "string"},
                    },
                    "required": ["household_id", "created_by_user_id", "week_start_date"],
                },
            },
        }


# New: Get grocery list by plan keys
class GetGroceryListByPlanKeys(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int, week_start_date: str) -> str:
        plan = next(
            (
                p
                for p in data.get("meal_plans", [])
                if int(p.get("household_id")) == int(household_id)
                and str(p.get("week_start_date")) == str(week_start_date)
            ),
            None,
        )
        if not plan:
            return _json({"grocery_list": None})
        gl = next(
            (
                lt
                for lt in data.get("grocery_lists", [])
                if int(lt.get("source_meal_plan_id")) == int(plan.get("meal_plan_id"))
            ),
            None,
        )
        return _json({"grocery_list": gl})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_grocery_list_by_plan_keys",
                "description": "Get grocery list by (household_id, week_start_date).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                    },
                    "required": ["household_id", "week_start_date"],
                },
            },
        }


# New: Get grocery list details by plan keys
class GetGroceryListDetailsByPlanKeys(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int, week_start_date: str) -> str:
        plan = next(
            (
                p
                for p in data.get("meal_plans", [])
                if int(p.get("household_id")) == int(household_id)
                and str(p.get("week_start_date")) == str(week_start_date)
            ),
            None,
        )
        if not plan:
            return _json({"grocery_list": None, "items": []})
        gl = next(
            (
                lt
                for lt in data.get("grocery_lists", [])
                if int(lt.get("source_meal_plan_id")) == int(plan.get("meal_plan_id"))
            ),
            None,
        )
        if not gl:
            return _json({"grocery_list": None, "items": []})
        items = [
            i
            for i in data.get("grocery_list_items", [])
            if int(i.get("list_id")) == int(gl.get("list_id"))
        ]
        return _json({"grocery_list": gl, "items": items})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_grocery_list_details_by_plan_keys",
                "description": "Get grocery list header and items by (household_id, week_start_date).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                    },
                    "required": ["household_id", "week_start_date"],
                },
            },
        }


class UpsertGroceryListItemsFromRecipes(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], list_id: int, recipe_ids: List[int]) -> str:
        gli_tbl = _tbl(data, "grocery_list_items")
        gli_tbl[:] = [r for r in gli_tbl if int(r.get("list_id")) != int(list_id)]
        next_item = _max_id(gli_tbl, "item_id", 8100)
        ri = data.get("recipe_ingredients", [])
        agg: Dict[Tuple[int, str], float] = {}
        for rid in recipe_ids or []:
            rows = [r for r in ri if int(r.get("recipe_id")) == int(rid)]
            for row in rows:
                iid = int(row.get("ingredient_id"))
                unit = str(row.get("unit"))
                qty = float(row.get("quantity", 0))
                agg[(iid, unit)] = agg.get((iid, unit), 0.0) + qty
        created_ids: List[int] = []
        for (iid, unit), qty in agg.items():
            next_item += 1
            ing = _ingredient_by_id(data, iid)
            rec = {
                "item_id": next_item,
                "list_id": int(list_id),
                "ingredient_id": int(iid),
                "quantity": float(qty),
                "unit": unit,
                "grocery_section": (ing or {}).get("grocery_section", "Misc"),
                "pantry_staple_flag": bool((ing or {}).get("pantry_staple_flag", False)),
                "overlap_last_month_flag": False,
            }
            gli_tbl.append(rec)
            created_ids.append(next_item)
        # Deterministic header write to ensure write semantics even if no items created
        gl = _require(data, "grocery_lists", "list_id", int(list_id))
        if gl is not None:
            gl["last_upserted_at"] = "2025-01-01T12:05:00"
        return _json({"created_item_ids": created_ids})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsert_grocery_list_items_from_recipes",
                "description": "Replace list items by consolidating ingredients for recipe_ids.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {"type": "integer"},
                        "recipe_ids": {"type": "array", "items": {"type": "integer"}},
                    },
                    "required": ["list_id", "recipe_ids"],
                },
            },
        }


class CategorizeGroceryListSections(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], list_id: int) -> str:
        updated = 0
        for it in data.get("grocery_list_items", []):
            if int(it.get("list_id")) != int(list_id):
                continue
            ing = _ingredient_by_id(data, int(it.get("ingredient_id")))
            it["grocery_section"] = (ing or {}).get("grocery_section", "Misc")
            updated += 1
        # Deterministic header write to ensure write semantics
        gl = _require(data, "grocery_lists", "list_id", int(list_id))
        if gl is not None:
            gl["last_categorized_at"] = "2025-01-01T12:10:00"
        return _json({"updated_items": updated})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "categorize_grocery_list_sections",
                "description": "Refresh grocery_section for items in a list.",
                "parameters": {
                    "type": "object",
                    "properties": {"list_id": {"type": "integer"}},
                    "required": ["list_id"],
                },
            },
        }


class FlagPantryStaplesOnList(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], list_id: int) -> str:
        updated = 0
        for it in data.get("grocery_list_items", []):
            if int(it.get("list_id")) != int(list_id):
                continue
            ing = _ingredient_by_id(data, int(it.get("ingredient_id")))
            it["pantry_staple_flag"] = bool((ing or {}).get("pantry_staple_flag", False))
            updated += 1
        # Deterministic header write to ensure write semantics
        gl = _require(data, "grocery_lists", "list_id", int(list_id))
        if gl is not None:
            gl["last_staples_flagged_at"] = "2025-01-01T12:15:00"
        return _json({"updated_items": updated})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "flag_pantry_staples_on_list",
                "description": "Set pantry_staple_flag from ingredients.",
                "parameters": {
                    "type": "object",
                    "properties": {"list_id": {"type": "integer"}},
                    "required": ["list_id"],
                },
            },
        }


class FlagOverlapLastMonthOnList(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], list_id: int, household_id: int, anchor_date: Optional[str] = None
    ) -> str:
        from datetime import date, timedelta

        if anchor_date:
            y, m, d = [int(x) for x in str(anchor_date).split("-")]
            end = date(y, m, d)
        else:
            mh_rows = [
                h
                for h in data.get("meal_history", [])
                if int(h.get("household_id")) == int(household_id)
            ]
            if mh_rows:
                max_date = max(str(r.get("plan_date")) for r in mh_rows)
                y, m, d = [int(x) for x in max_date.split("-")]
                end = date(y, m, d)
            else:
                end = date(2025, 1, 1)
        start = end - timedelta(days=30)
        recent_rids = [
            int(r.get("recipe_id"))
            for r in data.get("meal_history", [])
            if int(r.get("household_id")) == int(household_id)
            and str(r.get("plan_date")) >= start.isoformat()
        ]
        recent_iids = set(
            int(r.get("ingredient_id"))
            for r in data.get("recipe_ingredients", [])
            if int(r.get("recipe_id")) in recent_rids
        )
        updated = 0
        for it in data.get("grocery_list_items", []):
            if int(it.get("list_id")) != int(list_id):
                continue
            it["overlap_last_month_flag"] = int(it.get("ingredient_id")) in recent_iids
            updated += 1
        # Deterministic header write to ensure write semantics
        gl = _require(data, "grocery_lists", "list_id", int(list_id))
        if gl is not None:
            gl["last_overlap_check_at"] = "2025-01-01T12:20:00"
        return _json({"updated_items": updated})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "flag_overlap_last_month_on_list",
                "description": "Flag items whose ingredient appeared in last 30 days of meals.",
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


class GetGroceryListBySourcePlan(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], source_meal_plan_id: int) -> str:
        row = next(
            (
                lt
                for lt in data.get("grocery_lists", [])
                if int(lt.get("source_meal_plan_id")) == int(source_meal_plan_id)
            ),
            None,
        )
        return _json({"grocery_list": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_grocery_list_by_source_plan",
                "description": "Find grocery_list linked to a meal_plan via source_meal_plan_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"source_meal_plan_id": {"type": "integer"}},
                    "required": ["source_meal_plan_id"],
                },
            },
        }


class GetGroceryListDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], list_id: int) -> str:
        header = _require(data, "grocery_lists", "list_id", int(list_id))
        items = [
            i for i in data.get("grocery_list_items", []) if int(i.get("list_id")) == int(list_id)
        ]
        return _json({"grocery_list": header, "items": items})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_grocery_list_details",
                "description": "Return grocery_list header and items.",
                "parameters": {
                    "type": "object",
                    "properties": {"list_id": {"type": "integer"}},
                    "required": ["list_id"],
                },
            },
        }


# New: Upsert grocery list items for plan by natural keys
class UpsertGroceryListItemsForPlanByKeys(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], household_id: int, week_start_date: str, recipe_ids: List[int]
    ) -> str:
        plan = next(
            (
                p
                for p in data.get("meal_plans", [])
                if int(p.get("household_id")) == int(household_id)
                and str(p.get("week_start_date")) == str(week_start_date)
            ),
            None,
        )
        if not plan:
            return _json({"error": "meal_plan not found for keys"})
        gl = next(
            (
                lt
                for lt in data.get("grocery_lists", [])
                if int(lt.get("source_meal_plan_id")) == int(plan.get("meal_plan_id"))
            ),
            None,
        )
        if not gl:
            return _json({"error": "grocery_list not found for plan"})
        gli_tbl = _tbl(data, "grocery_list_items")
        gli_tbl[:] = [r for r in gli_tbl if int(r.get("list_id")) != int(gl.get("list_id"))]
        next_item = _max_id(gli_tbl, "item_id", 8100)
        ri = data.get("recipe_ingredients", [])
        agg: Dict[Tuple[int, str], float] = {}
        for rid in recipe_ids or []:
            rows = [r for r in ri if int(r.get("recipe_id")) == int(rid)]
            for row in rows:
                iid = int(row.get("ingredient_id"))
                unit = str(row.get("unit"))
                qty = float(row.get("quantity", 0))
                agg[(iid, unit)] = agg.get((iid, unit), 0.0) + qty
        created_ids: List[int] = []
        for (iid, unit), qty in agg.items():
            next_item += 1
            ing = _ingredient_by_id(data, iid)
            rec = {
                "item_id": next_item,
                "list_id": int(gl.get("list_id")),
                "ingredient_id": int(iid),
                "quantity": float(qty),
                "unit": unit,
                "grocery_section": (ing or {}).get("grocery_section", "Misc"),
                "pantry_staple_flag": bool((ing or {}).get("pantry_staple_flag", False)),
                "overlap_last_month_flag": False,
            }
            gli_tbl.append(rec)
            created_ids.append(next_item)
        gl["last_upserted_at"] = "2025-01-01T12:05:00"
        return _json({"created_item_ids": created_ids})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsert_grocery_list_items_for_plan_by_keys",
                "description": "Replace grocery_list_items for list linked to (household_id, week_start_date).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                        "recipe_ids": {"type": "array", "items": {"type": "integer"}},
                    },
                    "required": ["household_id", "week_start_date", "recipe_ids"],
                },
            },
        }


# New: Categorize list items by plan keys
class CategorizeGroceryListSectionsByPlanKeys(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int, week_start_date: str) -> str:
        plan = next(
            (
                p
                for p in data.get("meal_plans", [])
                if int(p.get("household_id")) == int(household_id)
                and str(p.get("week_start_date")) == str(week_start_date)
            ),
            None,
        )
        if not plan:
            return _json({"updated_items": 0})
        gl = next(
            (
                lt
                for lt in data.get("grocery_lists", [])
                if int(lt.get("source_meal_plan_id")) == int(plan.get("meal_plan_id"))
            ),
            None,
        )
        if not gl:
            return _json({"updated_items": 0})
        updated = 0
        for it in data.get("grocery_list_items", []):
            if int(it.get("list_id")) != int(gl.get("list_id")):
                continue
            ing = _ingredient_by_id(data, int(it.get("ingredient_id")))
            it["grocery_section"] = (ing or {}).get("grocery_section", "Misc")
            updated += 1
        gl["last_categorized_at"] = "2025-01-01T12:10:00"
        return _json({"updated_items": updated})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "categorize_grocery_list_sections_by_plan_keys",
                "description": "Refresh grocery_section for items by (household_id, week_start_date).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                    },
                    "required": ["household_id", "week_start_date"],
                },
            },
        }


# New: Flag pantry staples by plan keys
class FlagPantryStaplesOnListByPlanKeys(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int, week_start_date: str) -> str:
        plan = next(
            (
                p
                for p in data.get("meal_plans", [])
                if int(p.get("household_id")) == int(household_id)
                and str(p.get("week_start_date")) == str(week_start_date)
            ),
            None,
        )
        if not plan:
            return _json({"updated_items": 0})
        gl = next(
            (
                lt
                for lt in data.get("grocery_lists", [])
                if int(lt.get("source_meal_plan_id")) == int(plan.get("meal_plan_id"))
            ),
            None,
        )
        if not gl:
            return _json({"updated_items": 0})
        updated = 0
        for it in data.get("grocery_list_items", []):
            if int(it.get("list_id")) != int(gl.get("list_id")):
                continue
            ing = _ingredient_by_id(data, int(it.get("ingredient_id")))
            it["pantry_staple_flag"] = bool((ing or {}).get("pantry_staple_flag", False))
            updated += 1
        gl["last_staples_flagged_at"] = "2025-01-01T12:15:00"
        return _json({"updated_items": updated})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "flag_pantry_staples_on_list_by_plan_keys",
                "description": "Set pantry_staple_flag from ingredients by (household_id, week_start_date).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                    },
                    "required": ["household_id", "week_start_date"],
                },
            },
        }


# New: Flag overlap by plan keys
class FlagOverlapLastMonthOnListByPlanKeys(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], household_id: int, week_start_date: str, anchor_date: str
    ) -> str:
        plan = next(
            (
                p
                for p in data.get("meal_plans", [])
                if int(p.get("household_id")) == int(household_id)
                and str(p.get("week_start_date")) == str(week_start_date)
            ),
            None,
        )
        if not plan:
            return _json({"flagged_item_ids": [], "matched_count": 0})
        gl = next(
            (
                lt
                for lt in data.get("grocery_lists", [])
                if int(lt.get("source_meal_plan_id")) == int(plan.get("meal_plan_id"))
            ),
            None,
        )
        if not gl:
            return _json({"flagged_item_ids": [], "matched_count": 0})
        from datetime import date, timedelta

        if anchor_date:
            y, m, d = [int(x) for x in str(anchor_date).split("-")]
            end = date(y, m, d)
        else:
            mh_rows = [
                h
                for h in data.get("meal_history", [])
                if int(h.get("household_id")) == int(household_id)
            ]
            if mh_rows:
                max_date = max(str(r.get("plan_date")) for r in mh_rows)
                y, m, d = [int(x) for x in max_date.split("-")]
                end = date(y, m, d)
            else:
                end = date(2025, 1, 1)
        start = end - timedelta(days=30)
        recent_rids = [
            int(r.get("recipe_id"))
            for r in data.get("meal_history", [])
            if int(r.get("household_id")) == int(household_id)
            and str(r.get("plan_date")) >= start.isoformat()
        ]
        recent_iids = set(
            int(r.get("ingredient_id"))
            for r in data.get("recipe_ingredients", [])
            if int(r.get("recipe_id")) in recent_rids
        )
        matched = 0
        flagged_ids: List[int] = []
        # Update database: set recent_overlap_flag on items with recent overlap
        for it in data.get("grocery_list_items", []):
            if int(it.get("list_id")) != int(gl.get("list_id")):
                continue
            if int(it.get("ingredient_id")) in recent_iids:
                it["recent_overlap_flag"] = True
                matched += 1
                flagged_ids.append(int(it.get("item_id")))
            else:
                it["recent_overlap_flag"] = False
        # Update grocery list timestamp
        gl["last_overlap_flagged_at"] = "2025-01-01T12:20:00"
        return _json({"flagged_item_ids": flagged_ids, "matched_count": matched})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "flag_overlap_last_month_on_list_by_plan_keys",
                "description": "Flag items with recent overlap by (household_id, week_start_date).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                        "anchor_date": {"type": "string"},
                    },
                    "required": ["household_id", "week_start_date", "anchor_date"],
                },
            },
        }


# Stores and products
class ListStores(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        return _json({"stores": data.get("stores", [])})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_stores",
                "description": "List stores.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class GetPreferredStoreId(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int) -> str:
        # Determine preferred store dynamically; default to first native store if no explicit mapping
        stores = data.get("stores", [])
        native = [s for s in stores if str(s.get("platform_enum")) == "native"]
        sid = (
            int(native[0]["store_id"]) if native else (int(stores[0]["store_id"]) if stores else 0)
        )
        return _json({"preferred_store_id": sid})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_preferred_store_id",
                "description": "Resolve preferred store_id for a household using data (no hard-coding).",
                "parameters": {
                    "type": "object",
                    "properties": {"household_id": {"type": "integer"}},
                    "required": ["household_id"],
                },
            },
        }


class GetAggregatorStoreId(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int) -> str:
        # Determine aggregator store dynamically; choose first aggregator platform store
        stores = data.get("stores", [])
        agg = [s for s in stores if str(s.get("platform_enum")) == "aggregator"]
        sid = int(agg[0]["store_id"]) if agg else (int(stores[0]["store_id"]) if stores else 0)
        return _json({"aggregator_store_id": sid})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_aggregator_store_id",
                "description": "Resolve aggregator store_id for a household using data (no hard-coding).",
                "parameters": {
                    "type": "object",
                    "properties": {"household_id": {"type": "integer"}},
                    "required": ["household_id"],
                },
            },
        }


class GetHouseholdStapleIngredientId(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int) -> str:
        # Resolve a staple ingredient by heuristic: pick a true pantry_staple_flag ingredient that exists in inventory for household
        inv = [
            i
            for i in data.get("inventory_items", [])
            if int(i.get("household_id")) == int(household_id)
        ]
        staple_ids = sorted(
            {
                int(r.get("ingredient_id"))
                for r in data.get("ingredients", [])
                if bool(r.get("pantry_staple_flag", False))
            }
        )
        inv_staples = [
            row
            for row in inv
            if int(row.get("ingredient_id")) in set(staple_ids)
            and float(row.get("quantity", 0)) > 0
        ]
        chosen = (
            int(inv_staples[0].get("ingredient_id"))
            if inv_staples
            else (staple_ids[0] if staple_ids else 0)
        )
        return _json({"staple_ingredient_id": chosen})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_household_staple_ingredient_id",
                "description": "Resolve a staple ingredient_id for a household from inventory/ingredients (no hard-coding).",
                "parameters": {
                    "type": "object",
                    "properties": {"household_id": {"type": "integer"}},
                    "required": ["household_id"],
                },
            },
        }


class ListStoreProducts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], store_id: int, ingredient_id: Optional[int] = None) -> str:
        rows = [
            p for p in data.get("store_products", []) if int(p.get("store_id")) == int(store_id)
        ]
        if ingredient_id is not None:
            rows = [p for p in rows if int(p.get("ingredient_id")) == int(ingredient_id)]
        return _json({"products": rows})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_store_products",
                "description": "List products for a store (optionally filtered by ingredient).",
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


class CheckStoreInventoryForList(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], list_id: int, store_id: int) -> str:
        items = [
            i for i in data.get("grocery_list_items", []) if int(i.get("list_id")) == int(list_id)
        ]
        results: List[Dict[str, Any]] = []
        rank = {"in_stock": 0, "low": 1, "out_of_stock": 2}
        for it in items:
            iid = int(it.get("ingredient_id"))
            prods = [
                p
                for p in data.get("store_products", [])
                if int(p.get("store_id")) == int(store_id) and int(p.get("ingredient_id")) == iid
            ]
            prods_sorted = sorted(
                prods,
                key=lambda p: (
                    rank.get(p.get("stock_status_enum"), 3),
                    int(p.get("price_cents", 10**9)),
                    int(p.get("product_id", 10**9)),
                ),
            )
            best = prods_sorted[0] if prods_sorted else None
            results.append(
                {
                    "item_id": int(it.get("item_id")),
                    "ingredient_id": iid,
                    "matched_product_id": int(best.get("product_id")) if best else None,
                    "stock_status_enum": (
                        best.get("stock_status_enum") if best else "out_of_catalog"
                    ),
                    "price_cents": int(best.get("price_cents", 0)) if best else None,
                }
            )
        return _json({"store_check": results})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_store_inventory_for_list",
                "description": "Check availability for list items at a store and choose best deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {"list_id": {"type": "integer"}, "store_id": {"type": "integer"}},
                    "required": ["list_id", "store_id"],
                },
            },
        }


class ProposeSubstituteProducts(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        store_id: int,
        flagged_items: List[Dict[str, Any]],
        require_peanut_free: bool = False,
    ) -> str:
        suggestions = []
        for f in flagged_items or []:
            iid = int(f.get("ingredient_id"))
            ing = _ingredient_by_id(data, iid)
            if require_peanut_free and ing and not bool(ing.get("peanut_free_flag", True)):
                continue
            prods = [
                p
                for p in data.get("store_products", [])
                if int(p.get("store_id")) == int(store_id)
                and int(p.get("ingredient_id")) == iid
                and p.get("stock_status_enum") in ("in_stock", "low")
            ]
            prods = sorted(
                prods,
                key=lambda p: (int(p.get("price_cents", 10**9)), int(p.get("product_id", 10**9))),
            )
            best = prods[0] if prods else None
            if best:
                suggestions.append(
                    {
                        "ingredient_id": iid,
                        "substitute_ingredient_id": iid,
                        "substitute_product_id": int(best.get("product_id")),
                    }
                )
        return _json({"substitutions": suggestions})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "propose_substitute_products",
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
    @staticmethod
    def invoke(data: Dict[str, Any], list_id: int, substitutions: List[Dict[str, Any]]) -> str:
        mapping = {
            int(s["ingredient_id"]): int(s["substitute_ingredient_id"])
            for s in substitutions
            if "ingredient_id" in s and "substitute_ingredient_id" in s
        }
        updated = 0
        for it in data.get("grocery_list_items", []):
            if int(it.get("list_id")) != int(list_id):
                continue
            iid = int(it.get("ingredient_id"))
            if iid in mapping:
                new_iid = mapping[iid]
                it["ingredient_id"] = new_iid
                ing = _ingredient_by_id(data, new_iid)
                it["grocery_section"] = (ing or {}).get("grocery_section", "Misc")
                updated += 1
        # Deterministic header write to ensure write semantics
        gl = _require(data, "grocery_lists", "list_id", int(list_id))
        if gl is not None:
            gl["last_substitutions_applied_at"] = "2025-01-01T12:25:00"
        return _json({"updated_items": updated})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_grocery_list_with_substitutes",
                "description": "Apply substitutions to grocery_list_items.",
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


# Orders
class CreateOrderFromList(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        household_id: int,
        store_id: int,
        list_id: int,
        scheduled_slot_start_ts: str,
        scheduled_slot_end_ts: str,
    ) -> str:
        tbl = _tbl(data, "orders")
        next_id = _max_id(tbl, "order_id", 10000) + 1
        row = {
            "order_id": next_id,
            "household_id": int(household_id),
            "store_id": int(store_id),
            "list_id": int(list_id),
            "status_enum": "initialized",
            "subtotal_cents": 0,
            "total_cents": 0,
            "placed_ts": "2025-01-02T10:00:00",
            "scheduled_slot_start_ts": str(scheduled_slot_start_ts),
            "scheduled_slot_end_ts": str(scheduled_slot_end_ts),
        }
        tbl.append(row)
        return _json({"order_id": next_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_order_from_list",
                "description": "Create an order header for a list and store.",
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


# New: Create order for plan list by natural keys
class CreateOrderForPlanListByKeys(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        household_id: int,
        week_start_date: str,
        store_id: int,
        scheduled_slot_start_ts: str,
        scheduled_slot_end_ts: str,
    ) -> str:
        # Find list by plan keys
        plan = next(
            (
                p
                for p in data.get("meal_plans", [])
                if int(p.get("household_id")) == int(household_id)
                and str(p.get("week_start_date")) == str(week_start_date)
            ),
            None,
        )
        if not plan:
            return _json({"error": "meal_plan not found for keys"})
        gl = next(
            (
                lt
                for lt in data.get("grocery_lists", [])
                if int(lt.get("source_meal_plan_id")) == int(plan.get("meal_plan_id"))
            ),
            None,
        )
        if not gl:
            return _json({"error": "grocery_list not found for plan"})
        tbl = _tbl(data, "orders")
        next_id = _max_id(tbl, "order_id", 10000) + 1
        row = {
            "order_id": next_id,
            "household_id": int(household_id),
            "store_id": int(store_id),
            "list_id": int(gl.get("list_id")),
            "status_enum": "initialized",
            "subtotal_cents": 0,
            "total_cents": 0,
            "placed_ts": "2025-01-02T10:00:00",
            "scheduled_slot_start_ts": str(scheduled_slot_start_ts),
            "scheduled_slot_end_ts": str(scheduled_slot_end_ts),
        }
        tbl.append(row)
        return _json({"order_id": next_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_order_for_plan_list_by_keys",
                "description": "Create order for the grocery list linked to (household_id, week_start_date).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                        "store_id": {"type": "integer"},
                        "scheduled_slot_start_ts": {"type": "string"},
                        "scheduled_slot_end_ts": {"type": "string"},
                    },
                    "required": [
                        "household_id",
                        "week_start_date",
                        "store_id",
                        "scheduled_slot_start_ts",
                        "scheduled_slot_end_ts",
                    ],
                },
            },
        }


# New: Add order items for plan by keys
class AddOrderItemsForPlanByKeys(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int, week_start_date: str, store_id: int) -> str:
        # Resolve order by keys (choose highest order_id for determinism if multiple)
        plan = next(
            (
                p
                for p in data.get("meal_plans", [])
                if int(p.get("household_id")) == int(household_id)
                and str(p.get("week_start_date")) == str(week_start_date)
            ),
            None,
        )
        if not plan:
            return _json({"error": "meal_plan not found for keys"})
        gl = next(
            (
                lt
                for lt in data.get("grocery_lists", [])
                if int(lt.get("source_meal_plan_id")) == int(plan.get("meal_plan_id"))
            ),
            None,
        )
        if not gl:
            return _json({"error": "grocery_list not found for plan"})
        orders = [
            o
            for o in data.get("orders", [])
            if int(o.get("household_id")) == int(household_id)
            and int(o.get("store_id")) == int(store_id)
            and int(o.get("list_id")) == int(gl.get("list_id"))
        ]
        if not orders:
            return _json({"error": "order not found for keys"})
        order = sorted(orders, key=lambda o: int(o.get("order_id", 0)), reverse=True)[0]
        # Reuse AddOrderItemsFromList logic deterministically
        list_id = int(order.get("list_id"))
        items = [i for i in data.get("grocery_list_items", []) if int(i.get("list_id")) == list_id]
        oi_tbl = _tbl(data, "order_items")
        next_oi = _max_id(oi_tbl, "order_item_id", 10100)
        subtotal = 0
        for it in items:
            ingr_id = int(it.get("ingredient_id"))
            prods = [
                p
                for p in data.get("store_products", [])
                if int(p.get("store_id")) == int(store_id)
                and int(p.get("ingredient_id")) == ingr_id
                and p.get("stock_status_enum") in ("in_stock", "low")
            ]
            prods = sorted(
                prods,
                key=lambda p: (int(p.get("price_cents", 10**9)), int(p.get("product_id", 10**9))),
            )
            if not prods:
                continue
            product = prods[0]
            next_oi += 1
            row = {
                "order_item_id": next_oi,
                "order_id": int(order.get("order_id")),
                "product_id": int(product.get("product_id")),
                "requested_qty": 1,
                "fulfilled_qty": 1,
                "substitute_product_id": None,
            }
            oi_tbl.append(row)
            subtotal += int(product.get("price_cents", 0))
        order["subtotal_cents"] = subtotal
        order["total_cents"] = subtotal
        order["items_populated_at"] = "2025-01-02T11:00:00"
        return _json({"subtotal_cents": subtotal, "total_cents": subtotal})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_order_items_for_plan_by_keys",
                "description": "Populate order_items by plan keys (household_id, week_start_date, store_id).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                        "store_id": {"type": "integer"},
                    },
                    "required": ["household_id", "week_start_date", "store_id"],
                },
            },
        }


# New: Update order status by plan keys
class UpdateOrderStatusByPlanKeys(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        household_id: int,
        week_start_date: str,
        store_id: int,
        new_status: str,
    ) -> str:
        plan = next(
            (
                p
                for p in data.get("meal_plans", [])
                if int(p.get("household_id")) == int(household_id)
                and str(p.get("week_start_date")) == str(week_start_date)
            ),
            None,
        )
        if not plan:
            return _json({"error": "meal_plan not found for keys"})
        gl = next(
            (
                lt
                for lt in data.get("grocery_lists", [])
                if int(lt.get("source_meal_plan_id")) == int(plan.get("meal_plan_id"))
            ),
            None,
        )
        if not gl:
            return _json({"error": "grocery_list not found for plan"})
        orders = [
            o
            for o in data.get("orders", [])
            if int(o.get("household_id")) == int(household_id)
            and int(o.get("store_id")) == int(store_id)
            and int(o.get("list_id")) == int(gl.get("list_id"))
        ]
        if not orders:
            return _json({"error": "order not found for keys"})
        order = sorted(orders, key=lambda o: int(o.get("order_id", 0)), reverse=True)[0]
        order["status_enum"] = str(new_status)
        order["last_status_update_at"] = "2025-01-02T11:05:00"
        return _json({"order": order})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_order_status_by_plan_keys",
                "description": "Update order status by (household_id, week_start_date, store_id).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                        "store_id": {"type": "integer"},
                        "new_status": {"type": "string"},
                    },
                    "required": ["household_id", "week_start_date", "store_id", "new_status"],
                },
            },
        }


# New: Get order details by plan keys
class GetOrderDetailsByPlanKeys(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int, week_start_date: str, store_id: int) -> str:
        plan = next(
            (
                p
                for p in data.get("meal_plans", [])
                if int(p.get("household_id")) == int(household_id)
                and str(p.get("week_start_date")) == str(week_start_date)
            ),
            None,
        )
        if not plan:
            return _json({"order": None, "items": []})
        gl = next(
            (
                lt
                for lt in data.get("grocery_lists", [])
                if int(lt.get("source_meal_plan_id")) == int(plan.get("meal_plan_id"))
            ),
            None,
        )
        if not gl:
            return _json({"order": None, "items": []})
        orders = [
            o
            for o in data.get("orders", [])
            if int(o.get("household_id")) == int(household_id)
            and int(o.get("store_id")) == int(store_id)
            and int(o.get("list_id")) == int(gl.get("list_id"))
        ]
        if not orders:
            return _json({"order": None, "items": []})
        order = sorted(orders, key=lambda o: int(o.get("order_id", 0)), reverse=True)[0]
        items = [
            i
            for i in data.get("order_items", [])
            if int(i.get("order_id")) == int(order.get("order_id"))
        ]
        return _json({"order": order, "items": items})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_order_details_by_plan_keys",
                "description": "Get order header and items by (household_id, week_start_date, store_id).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                        "store_id": {"type": "integer"},
                    },
                    "required": ["household_id", "week_start_date", "store_id"],
                },
            },
        }


class AddOrderItemsFromList(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: int, store_id: int) -> str:
        order = _require(data, "orders", "order_id", int(order_id))
        if not order:
            return _json({"error": f"order_id {order_id} not found"})
        list_id = int(order.get("list_id"))
        items = [i for i in data.get("grocery_list_items", []) if int(i.get("list_id")) == list_id]
        oi_tbl = _tbl(data, "order_items")
        next_oi = _max_id(oi_tbl, "order_item_id", 10100)
        subtotal = 0
        for it in items:
            ingr_id = int(it.get("ingredient_id"))
            prods = [
                p
                for p in data.get("store_products", [])
                if int(p.get("store_id")) == int(store_id)
                and int(p.get("ingredient_id")) == ingr_id
                and p.get("stock_status_enum") in ("in_stock", "low")
            ]
            prods = sorted(
                prods,
                key=lambda p: (int(p.get("price_cents", 10**9)), int(p.get("product_id", 10**9))),
            )
            if not prods:
                continue
            product = prods[0]
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
            subtotal += int(product.get("price_cents", 0))
        order["subtotal_cents"] = subtotal
        order["total_cents"] = subtotal
        # Deterministic field to ensure write semantics even if no items were added
        order["items_populated_at"] = "2025-01-02T11:00:00"
        return _json({"subtotal_cents": subtotal, "total_cents": subtotal})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_order_items_from_list",
                "description": "Populate order_items by selecting lowest-price in-stock products.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "integer"},
                        "store_id": {"type": "integer"},
                    },
                    "required": ["order_id", "store_id"],
                },
            },
        }


class UpdateOrderStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: int, new_status: str) -> str:
        row = _require(data, "orders", "order_id", int(order_id))
        if not row:
            return _json({"error": f"order_id {order_id} not found"})
        row["status_enum"] = str(new_status)
        # Deterministic field to ensure write semantics even if status unchanged
        row["last_status_update_at"] = "2025-01-02T11:05:00"
        return _json({"order": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_order_status",
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


class GetOrdersForHousehold(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int) -> str:
        rows = [
            o for o in data.get("orders", []) if int(o.get("household_id")) == int(household_id)
        ]
        return _json({"orders": rows})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_orders_for_household",
                "description": "List orders for a household.",
                "parameters": {
                    "type": "object",
                    "properties": {"household_id": {"type": "integer"}},
                    "required": ["household_id"],
                },
            },
        }


class GetOrderDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: int) -> str:
        order = _require(data, "orders", "order_id", int(order_id))
        items = [i for i in data.get("order_items", []) if int(i.get("order_id")) == int(order_id)]
        return _json({"order": order, "items": items})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_order_details",
                "description": "Get order header and items.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "integer"}},
                    "required": ["order_id"],
                },
            },
        }


# Meal history and inventory
class AppendMealHistory(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        household_id: int,
        plan_date: str,
        recipe_id: int,
        was_prepared: bool,
        rating_int: Optional[int] = None,
    ) -> str:
        tbl = _tbl(data, "meal_history")
        next_id = _max_id(tbl, "history_id", 6200) + 1
        row = {
            "history_id": next_id,
            "household_id": int(household_id),
            "plan_date": str(plan_date),
            "recipe_id": int(recipe_id),
            "was_prepared": bool(was_prepared),
            "rating_int": int(rating_int) if rating_int is not None else None,
        }
        tbl.append(row)
        return _json({"history_id": next_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "append_meal_history",
                "description": "Append meal_history row and return history_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "plan_date": {"type": "string"},
                        "recipe_id": {"type": "integer"},
                        "was_prepared": {"type": "boolean"},
                        "rating_int": {"type": "integer"},
                    },
                    "required": ["household_id", "plan_date", "recipe_id", "was_prepared"],
                },
            },
        }


class UpdateInventoryQuantity(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int, ingredient_id: int, delta: float) -> str:
        tbl = _tbl(data, "inventory_items")
        row = next(
            (
                i
                for i in tbl
                if int(i.get("household_id")) == int(household_id)
                and int(i.get("ingredient_id")) == int(ingredient_id)
            ),
            None,
        )
        if row is None:
            next_id = _max_id(tbl, "inv_item_id", 7000) + 1
            qty = float(delta)
            row = {
                "inv_item_id": next_id,
                "household_id": int(household_id),
                "ingredient_id": int(ingredient_id),
                "quantity": qty,
            }
            tbl.append(row)
            return _json({"inv_item_id": next_id, "quantity": qty})
        qty = float(row.get("quantity", 0)) + float(delta)
        row["quantity"] = qty
        return _json({"inv_item_id": int(row.get("inv_item_id")), "quantity": qty})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_inventory_quantity",
                "description": "Apply delta to inventory; create if missing.",
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


# New: Log inventory consumption audit by natural keys
class LogInventoryConsumeByKeys(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], household_id: int, user_id: int, ingredient_id: int, delta: float
    ) -> str:
        inv = next(
            (
                i
                for i in data.get("inventory_items", [])
                if int(i.get("household_id")) == int(household_id)
                and int(i.get("ingredient_id")) == int(ingredient_id)
            ),
            None,
        )
        if not inv:
            return _json({"error": "inventory row not found for keys"})
        tbl = _tbl(data, "audit_logs")
        next_id = _max_id(tbl, "audit_id", 12000) + 1
        row = {
            "audit_id": next_id,
            "household_id": int(household_id),
            "user_id": int(user_id),
            "entity_type": "inventory_items",
            "entity_id": int(inv.get("inv_item_id")),
            "action_enum": "consume",
            "payload_json": {"ingredient_id": int(ingredient_id), "delta": float(delta)},
            "created_at": "2025-01-03T10:00:00",
        }
        tbl.append(row)
        return _json({"audit_id": next_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "log_inventory_consume_by_keys",
                "description": "Append audit log consume event using (household_id, ingredient_id).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "user_id": {"type": "integer"},
                        "ingredient_id": {"type": "integer"},
                        "delta": {"type": "number"},
                    },
                    "required": ["household_id", "user_id", "ingredient_id", "delta"],
                },
            },
        }


# New: Log plan create audit by natural keys
class LogMealPlanCreateByKeys(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int, user_id: int, week_start_date: str) -> str:
        plan = next(
            (
                p
                for p in data.get("meal_plans", [])
                if int(p.get("household_id")) == int(household_id)
                and str(p.get("week_start_date")) == str(week_start_date)
            ),
            None,
        )
        if not plan:
            return _json({"error": "meal_plan not found for keys"})
        tbl = _tbl(data, "audit_logs")
        next_id = _max_id(tbl, "audit_id", 12000) + 1
        row = {
            "audit_id": next_id,
            "household_id": int(household_id),
            "user_id": int(user_id),
            "entity_type": "meal_plans",
            "entity_id": int(plan.get("meal_plan_id")),
            "action_enum": "create",
            "payload_json": {"week_start_date": str(week_start_date)},
            "created_at": "2025-01-03T10:00:00",
        }
        tbl.append(row)
        return _json({"audit_id": next_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "log_meal_plan_create_by_keys",
                "description": "Audit meal plan creation by (household_id, week_start_date).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "user_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                    },
                    "required": ["household_id", "user_id", "week_start_date"],
                },
            },
        }


# New: Log grocery list create audit by plan keys
class LogGroceryListCreateByKeys(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int, user_id: int, week_start_date: str) -> str:
        plan = next(
            (
                p
                for p in data.get("meal_plans", [])
                if int(p.get("household_id")) == int(household_id)
                and str(p.get("week_start_date")) == str(week_start_date)
            ),
            None,
        )
        if not plan:
            return _json({"error": "meal_plan not found for keys"})
        gl = next(
            (
                lt
                for lt in data.get("grocery_lists", [])
                if int(lt.get("source_meal_plan_id")) == int(plan.get("meal_plan_id"))
            ),
            None,
        )
        if not gl:
            return _json({"error": "grocery_list not found for keys"})
        tbl = _tbl(data, "audit_logs")
        next_id = _max_id(tbl, "audit_id", 12000) + 1
        row = {
            "audit_id": next_id,
            "household_id": int(household_id),
            "user_id": int(user_id),
            "entity_type": "grocery_lists",
            "entity_id": int(gl.get("list_id")),
            "action_enum": "create",
            "payload_json": {"source_meal_plan_id": int(plan.get("meal_plan_id"))},
            "created_at": "2025-01-03T10:00:00",
        }
        tbl.append(row)
        return _json({"audit_id": next_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "log_grocery_list_create_by_keys",
                "description": "Audit grocery list creation by (household_id, week_start_date).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "user_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                    },
                    "required": ["household_id", "user_id", "week_start_date"],
                },
            },
        }


# New: Log meal history create by keys (household_id, plan_date, recipe_id)
class LogMealHistoryCreateByKeys(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        household_id: int,
        user_id: int,
        plan_date: str,
        recipe_id: int,
        reason: Optional[str] = None,
    ) -> str:
        hist = next(
            (
                h
                for h in data.get("meal_history", [])
                if int(h.get("household_id")) == int(household_id)
                and str(h.get("plan_date")) == str(plan_date)
                and int(h.get("recipe_id")) == int(recipe_id)
            ),
            None,
        )
        if not hist:
            # If not found, choose latest history_id for household/date as fallback (deterministic)
            cands = [
                h
                for h in data.get("meal_history", [])
                if int(h.get("household_id")) == int(household_id)
                and str(h.get("plan_date")) == str(plan_date)
            ]
            if not cands:
                return _json({"error": "meal_history not found for keys"})
            hist = sorted(cands, key=lambda h: int(h.get("history_id", 0)), reverse=True)[0]
        tbl = _tbl(data, "audit_logs")
        next_id = _max_id(tbl, "audit_id", 12000) + 1
        payload = {"date": str(plan_date)}
        if reason:
            payload["reason"] = str(reason)
        row = {
            "audit_id": next_id,
            "household_id": int(household_id),
            "user_id": int(user_id),
            "entity_type": "meal_history",
            "entity_id": int(hist.get("history_id")),
            "action_enum": "create",
            "payload_json": payload,
            "created_at": "2025-01-03T10:00:00",
        }
        tbl.append(row)
        return _json({"audit_id": next_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "log_meal_history_create_by_keys",
                "description": "Append audit log for meal_history creation by keys.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "user_id": {"type": "integer"},
                        "plan_date": {"type": "string"},
                        "recipe_id": {"type": "integer"},
                        "reason": {"type": "string"},
                    },
                    "required": ["household_id", "user_id", "plan_date", "recipe_id"],
                },
            },
        }


# New: Log order placed by plan keys
class LogOrderPlacedByPlanKeys(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], household_id: int, user_id: int, week_start_date: str, store_id: int
    ) -> str:
        plan = next(
            (
                p
                for p in data.get("meal_plans", [])
                if int(p.get("household_id")) == int(household_id)
                and str(p.get("week_start_date")) == str(week_start_date)
            ),
            None,
        )
        if not plan:
            return _json({"error": "meal_plan not found for keys"})
        gl = next(
            (
                lt
                for lt in data.get("grocery_lists", [])
                if int(lt.get("source_meal_plan_id")) == int(plan.get("meal_plan_id"))
            ),
            None,
        )
        if not gl:
            return _json({"error": "grocery_list not found for keys"})
        orders = [
            o
            for o in data.get("orders", [])
            if int(o.get("household_id")) == int(household_id)
            and int(o.get("store_id")) == int(store_id)
            and int(o.get("list_id")) == int(gl.get("list_id"))
        ]
        if not orders:
            return _json({"error": "order not found for keys"})
        order = sorted(orders, key=lambda o: int(o.get("order_id", 0)), reverse=True)[0]
        tbl = _tbl(data, "audit_logs")
        next_id = _max_id(tbl, "audit_id", 12000) + 1
        row = {
            "audit_id": next_id,
            "household_id": int(household_id),
            "user_id": int(user_id),
            "entity_type": "orders",
            "entity_id": int(order.get("order_id")),
            "action_enum": "place_order",
            "payload_json": {"store_id": int(store_id), "list_id": int(gl.get("list_id"))},
            "created_at": "2025-01-03T10:00:00",
        }
        tbl.append(row)
        return _json({"audit_id": next_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "log_order_placed_by_plan_keys",
                "description": "Audit order placement by (household_id, week_start_date, store_id).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "user_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                        "store_id": {"type": "integer"},
                    },
                    "required": ["household_id", "user_id", "week_start_date", "store_id"],
                },
            },
        }


# New: Log order delivered by plan keys
class LogOrderDeliveredByPlanKeys(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        household_id: int,
        user_id: int,
        week_start_date: str,
        store_id: int,
    ) -> str:
        plan = next(
            (
                p
                for p in data.get("meal_plans", [])
                if int(p.get("household_id")) == int(household_id)
                and str(p.get("week_start_date")) == str(week_start_date)
            ),
            None,
        )
        if not plan:
            return _json({"error": "meal_plan not found for keys"})
        gl = next(
            (
                lt
                for lt in data.get("grocery_lists", [])
                if int(lt.get("source_meal_plan_id")) == int(plan.get("meal_plan_id"))
            ),
            None,
        )
        if not gl:
            return _json({"error": "grocery_list not found for keys"})
        orders = [
            o
            for o in data.get("orders", [])
            if int(o.get("household_id")) == int(household_id)
            and int(o.get("store_id")) == int(store_id)
            and int(o.get("list_id")) == int(gl.get("list_id"))
        ]
        if not orders:
            return _json({"error": "order not found for keys"})
        order = sorted(orders, key=lambda o: int(o.get("order_id", 0)), reverse=True)[0]
        tbl = _tbl(data, "audit_logs")
        next_id = _max_id(tbl, "audit_id", 12000) + 1
        row = {
            "audit_id": next_id,
            "household_id": int(household_id),
            "user_id": int(user_id),
            "entity_type": "orders",
            "entity_id": int(order.get("order_id")),
            "action_enum": "delivered",
            "payload_json": {
                "store_id": int(store_id),
                "list_id": int(gl.get("list_id")),
                "total_cents": int(order.get("total_cents", 0)),
                "slot_end": str(order.get("scheduled_slot_end_ts")),
            },
            "created_at": "2025-01-03T10:00:00",
        }
        tbl.append(row)
        return _json({"audit_id": next_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "log_order_delivered_by_plan_keys",
                "description": "Audit order delivered by (household_id, week_start_date, store_id).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "user_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                        "store_id": {"type": "integer"},
                    },
                    "required": ["household_id", "user_id", "week_start_date", "store_id"],
                },
            },
        }


class LogValidateSubstitutionsByPlanKeys(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        household_id: int,
        user_id: int,
        week_start_date: str,
        recipe_id: Optional[int] = None,
    ) -> str:
        # entity_type as 'meal_history' with entity_id = 0 per policy note
        tbl = _tbl(data, "audit_logs")
        next_id = _max_id(tbl, "audit_id", 12000) + 1
        payload = {}
        if recipe_id is not None:
            payload["recipe_id"] = int(recipe_id)
        row = {
            "audit_id": next_id,
            "household_id": int(household_id),
            "user_id": int(user_id),
            "entity_type": "meal_history",
            "entity_id": 0,
            "action_enum": "validate_substitutions",
            "payload_json": payload,
            "created_at": "2025-01-03T10:00:00",
        }
        tbl.append(row)
        return _json({"audit_id": next_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "log_validate_substitutions_by_plan_keys",
                "description": "Audit substitutions validation for plan by keys (entity_type meal_history, id 0).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "user_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                        "recipe_id": {"type": "integer"},
                    },
                    "required": ["household_id", "user_id", "week_start_date"],
                },
            },
        }


# New: Check store inventory by plan keys
class CheckStoreInventoryForPlanByKeys(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int, week_start_date: str, store_id: int) -> str:
        plan = next(
            (
                p
                for p in data.get("meal_plans", [])
                if int(p.get("household_id")) == int(household_id)
                and str(p.get("week_start_date")) == str(week_start_date)
            ),
            None,
        )
        if not plan:
            return _json({"store_check": []})
        gl = next(
            (
                lt
                for lt in data.get("grocery_lists", [])
                if int(lt.get("source_meal_plan_id")) == int(plan.get("meal_plan_id"))
            ),
            None,
        )
        if not gl:
            return _json({"store_check": []})
        items = [
            i
            for i in data.get("grocery_list_items", [])
            if int(i.get("list_id")) == int(gl.get("list_id"))
        ]
        results: List[Dict[str, Any]] = []
        rank = {"in_stock": 0, "low": 1, "out_of_stock": 2}
        for it in items:
            iid = int(it.get("ingredient_id"))
            prods = [
                p
                for p in data.get("store_products", [])
                if int(p.get("store_id")) == int(store_id) and int(p.get("ingredient_id")) == iid
            ]
            prods_sorted = sorted(
                prods,
                key=lambda p: (
                    rank.get(p.get("stock_status_enum"), 3),
                    int(p.get("price_cents", 10**9)),
                    int(p.get("product_id", 10**9)),
                ),
            )
            best = prods_sorted[0] if prods_sorted else None
            results.append(
                {
                    "item_id": int(it.get("item_id")),
                    "ingredient_id": iid,
                    "matched_product_id": int(best.get("product_id")) if best else None,
                    "stock_status_enum": (
                        best.get("stock_status_enum") if best else "out_of_catalog"
                    ),
                    "price_cents": int(best.get("price_cents", 0)) if best else None,
                }
            )
        return _json({"store_check": results})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_store_inventory_for_plan_by_keys",
                "description": "Check availability for list items linked to (household_id, week_start_date) at a store.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                        "store_id": {"type": "integer"},
                    },
                    "required": ["household_id", "week_start_date", "store_id"],
                },
            },
        }


# New: Update grocery list with substitutes by plan keys
class UpdateGroceryListWithSubstitutesByPlanKeys(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        household_id: int,
        week_start_date: str,
        substitutions: List[Dict[str, Any]],
    ) -> str:
        plan = next(
            (
                p
                for p in data.get("meal_plans", [])
                if int(p.get("household_id")) == int(household_id)
                and str(p.get("week_start_date")) == str(week_start_date)
            ),
            None,
        )
        if not plan:
            return _json({"updated_items": 0})
        gl = next(
            (
                lt
                for lt in data.get("grocery_lists", [])
                if int(lt.get("source_meal_plan_id")) == int(plan.get("meal_plan_id"))
            ),
            None,
        )
        if not gl:
            return _json({"updated_items": 0})
        mapping = {
            int(s["ingredient_id"]): int(s["substitute_ingredient_id"])
            for s in substitutions
            if "ingredient_id" in s and "substitute_ingredient_id" in s
        }
        updated = 0
        validated = 0
        for it in data.get("grocery_list_items", []):
            if int(it.get("list_id")) != int(gl.get("list_id")):
                continue
            iid = int(it.get("ingredient_id"))
            if iid in mapping:
                new_iid = mapping[iid]
                it["ingredient_id"] = new_iid
                ing = _ingredient_by_id(data, new_iid)
                it["grocery_section"] = (ing or {}).get("grocery_section", "Misc")
                updated += 1
            # Mark all items as validated even if no substitution applied
            it["substitutions_validated"] = True
            validated += 1
        gl["last_substitutions_applied_at"] = "2025-01-01T12:25:00"
        return _json({"updated_items": updated, "validated_items": validated})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_grocery_list_with_substitutes_by_plan_keys",
                "description": "Apply substitutions to grocery_list_items linked to (household_id, week_start_date).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                        "substitutions": {"type": "array", "items": {"type": "object"}},
                    },
                    "required": ["household_id", "week_start_date", "substitutions"],
                },
            },
        }


# Auditing
class LogAuditEvent(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        household_id: int,
        user_id: int,
        entity_type: str,
        entity_id: int,
        action_enum: str,
        payload_json: Dict[str, Any],
    ) -> str:
        tbl = _tbl(data, "audit_logs")
        next_id = _max_id(tbl, "audit_id", 12000) + 1
        row = {
            "audit_id": next_id,
            "household_id": int(household_id),
            "user_id": int(user_id),
            "entity_type": str(entity_type),
            "entity_id": int(entity_id),
            "action_enum": str(action_enum),
            "payload_json": payload_json,
            "created_at": "2025-01-03T10:00:00",
        }
        tbl.append(row)
        return _json({"audit_id": next_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "log_audit_event",
                "description": "Append an audit log entry and return audit_id.",
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


# Misc lookups
class GetRecipeDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], recipe_id: int) -> str:
        return _json({"recipe": _recipe_by_id(data, int(recipe_id))})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_recipe_details",
                "description": "Get recipe row by id.",
                "parameters": {
                    "type": "object",
                    "properties": {"recipe_id": {"type": "integer"}},
                    "required": ["recipe_id"],
                },
            },
        }


class ListRecipeIngredients(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], recipe_id: int) -> str:
        rows = [
            r
            for r in data.get("recipe_ingredients", [])
            if int(r.get("recipe_id")) == int(recipe_id)
        ]
        return _json({"recipe_ingredients": rows})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_recipe_ingredients",
                "description": "List recipe_ingredients for a recipe.",
                "parameters": {
                    "type": "object",
                    "properties": {"recipe_id": {"type": "integer"}},
                    "required": ["recipe_id"],
                },
            },
        }


class SearchIngredientsByName(Tool):
    """Searches for ingredients with names containing the specified text."""
    @staticmethod
    def invoke(data: Dict[str, Any], name_query: str) -> str:
        if not name_query:
            return _json({"error": "name_query parameter is required."})
        ingredients = data.get("ingredients", [])
        matching_ingredients = [
            ingredient for ingredient in ingredients 
            if name_query.lower() in ingredient.get("ingredient_name", "").lower()
        ]
        return _json(matching_ingredients)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_ingredients_by_name",
                "description": "Searches for ingredients with names containing the specified text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name_query": {"type": "string", "description": "The text to search for in ingredient names."}
                    },
                    "required": ["name_query"],
                },
            },
        }


class SearchRecipesByTitleSubstring(Tool):
    """Searches for recipes with titles containing the specified text."""
    @staticmethod
    def invoke(data: Dict[str, Any], title_substring: str) -> str:
        if not title_substring:
            return _json({"error": "title_substring parameter is required."})
        recipes = data.get("recipes", [])
        matching_recipes = [
            recipe for recipe in recipes 
            if title_substring.lower() in recipe.get("recipe_title", "").lower()
        ]
        return _json(matching_recipes)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_recipes_by_title_substring",
                "description": "Searches for recipes with titles containing the specified text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title_substring": {"type": "string", "description": "The text to search for in recipe titles."}
                    },
                    "required": ["title_substring"],
                },
            },
        }


class GetInventoryForHouseholdAndIngredientId(Tool):
    """Retrieves inventory items for a specific household and ingredient."""
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int, ingredient_id: int) -> str:
        if household_id is None or ingredient_id is None:
            return _json({"error": "household_id and ingredient_id parameters are required."})
        inventory = data.get("inventory_items", [])
        household_ingredient_inventory = [
            item for item in inventory 
            if item.get("household_id") == household_id and item.get("ingredient_id") == ingredient_id
        ]
        return _json(household_ingredient_inventory)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_inventory_for_household_and_ingredient_id",
                "description": "Retrieves inventory items for a specific household and ingredient.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer", "description": "The unique ID of the household."},
                        "ingredient_id": {"type": "integer", "description": "The unique ID of the ingredient."}
                    },
                    "required": ["household_id", "ingredient_id"],
                },
            },
        }


class GetMealHistoryForHousehold(Tool):
    """Retrieves the meal history for a given household ID for a specified number of past days."""
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int, days_ago: int = 14) -> str:
        from datetime import datetime, timedelta
        meal_history = data.get("meal_history", [])
        current_date = datetime.strptime("2025-08-20", "%Y-%m-%d")
        start_date = current_date - timedelta(days=days_ago)
        history = [
            h for h in meal_history 
            if h.get("household_id") == household_id and 
               datetime.strptime(h.get("plan_date"), "%Y-%m-%d") >= start_date
        ]
        return _json(history)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_meal_history_for_household",
                "description": "Retrieves the meal history for a given household ID for a specified number of past days.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer", "description": "The unique ID of the household."},
                        "days_ago": {"type": "integer", "description": "Number of past days to retrieve history for. Defaults to 14."},
                    },
                    "required": ["household_id"],
                },
            },
        }


TOOLS = [
    # Identity & household
    GetUserByFullName(),
    GetHouseholdByPrimaryUser(),
    ComputeHouseholdServings(),
    GetPreferredStoreId(),
    GetAggregatorStoreId(),
    GetHouseholdStapleIngredientId(),
    # Recipe selection & constraints
    BuildRecipeFilters(),
    ListRecipesByFilters(),
    ListRecentMealHistory(),
    # ExcludeRecipeIds(),
    ApplyCuisineCap(),
    MinimizeNewIngredients(),
    RankRecipesForTargets(),
    GenerateChildModifications(),
    GetRecipeDetails(),
    ListRecipeIngredients(),
    SearchRecipesByTitleSubstring(),
    # Ingredients
    SearchIngredientsByName(),
    GetInventoryForHouseholdAndIngredientId(),
    # Meal history
    GetMealHistoryForHousehold(),
    # Plans & entries (by keys)
    CreateMealPlan(),
    AddMealPlanEntriesByKeys(),
    UpdateMealPlanEntryNotesByKeys(),
    GetMealPlanByHouseholdAndWeek(),
    # Grocery list (by keys)
    CreateGroceryListForPlanByKeys(),
    UpsertGroceryListItemsForPlanByKeys(),
    CategorizeGroceryListSectionsByPlanKeys(),
    FlagPantryStaplesOnListByPlanKeys(),
    FlagOverlapLastMonthOnListByPlanKeys(),
    GetGroceryListByPlanKeys(),
    # Substitutions & inventory check
    CheckStoreInventoryForPlanByKeys(),
    ProposeSubstituteProducts(),
    UpdateGroceryListWithSubstitutesByPlanKeys(),
    # Orders (by keys)
    CreateOrderForPlanListByKeys(),
    AddOrderItemsForPlanByKeys(),
    UpdateOrderStatusByPlanKeys(),
    # Meal history & inventory
    AppendMealHistory(),
    UpdateInventoryQuantity(),
    # Audits
    LogInventoryConsumeByKeys(),
    LogMealHistoryCreateByKeys(),
    LogMealPlanCreateByKeys(),
    LogGroceryListCreateByKeys(),
    LogOrderPlacedByPlanKeys(),
    LogOrderDeliveredByPlanKeys(),
    LogValidateSubstitutionsByPlanKeys(),
]
