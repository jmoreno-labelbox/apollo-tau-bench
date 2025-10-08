from tau_bench.envs.tool import Tool
import json
from typing import Any

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
        recipe_rows = [x for x in ri if x.get("recipe_id") == recipe_id]
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
        recipe_rows = [x for x in ri if x.get("recipe_id") == recipe_id]
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
