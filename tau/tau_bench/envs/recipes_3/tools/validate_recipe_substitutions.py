from tau_bench.envs.tool import Tool
import json
from typing import Any

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
                        "substitutions": {"type": "array"},
                        "require_peanut_free": {"type": "boolean"},
                        "preserve_section": {"type": "boolean"},
                    },
                    "required": ["recipe_id", "household_id", "substitutions"],
                },
            },
        }
