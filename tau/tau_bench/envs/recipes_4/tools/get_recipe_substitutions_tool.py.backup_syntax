from tau_bench.envs.tool import Tool
import collections
import json
from datetime import date, datetime, timedelta, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetRecipeSubstitutionsTool(Tool):
    """
    A tool to suggest ingredient substitutions for a specific recipe.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetRecipeSubstitutions",
                "description": (
                    "Suggests ingredient substitutions for a given ingredient within "
                    "a specific recipe, based on a predefined knowledge base."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_id": {
                            "type": "integer",
                            "description": "The unique ID for the recipe requiring a substitution.",
                        },
                        "ingredient_id_to_replace": {
                            "type": "integer",
                            "description": "The unique ID of the ingredient that is missing.",
                        },
                    },
                    "required": ["recipe_id", "ingredient_id_to_replace"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], recipe_id: int, ingredient_id_to_replace: int) -> dict[str, Any]:
        """
        Executes the logic to find and suggest ingredient substitutions.

        This method validates the inputs, confirms the ingredient is part of the
        recipe, then consults a predefined knowledge base (SUBSTITUTION_RULES)
        for valid alternatives, enriching the response with ingredient names.

        Args:
            data: The main in-memory dictionary containing all datasets.
            recipe_id: The ID of the recipe.
            ingredient_id_to_replace: The ID of the ingredient to replace.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains a list of substitution suggestions.
        """
        pass
        #1. Validate Inputs
        param_definitions = {
            "recipe_id": {"type": int, "required": True},
            "ingredient_id_to_replace": {"type": int, "required": True},
        }
        validation_error = _validate_inputs({"recipe_id": recipe_id, "ingredient_id_to_replace": ingredient_id_to_replace}, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Pre-condition Checks
        if not any(r.get("recipe_id") == recipe_id for r in data.get("recipes", {}).values():
            return _build_error_response(
                "NOT_FOUND", {"entity": "Recipe", "entity_id": recipe_id}
            )

        if not any(
            i.get("ingredient_id") == ingredient_id_to_replace
            for i in data.get("ingredients", {}).values()
        ):
            return _build_error_response(
                "NOT_FOUND", {"entity": "Ingredient", "entity_id": ingredient_id_to_replace}
            )

        recipe_ingredients = {
            ri["ingredient_id"]
            for ri in data.get("recipe_ingredients", {}).values()
            if ri["recipe_id"] == recipe_id
        }
        if ingredient_id_to_replace not in recipe_ingredients:
            return _build_error_response(
                "UNSUPPORTED_OPERATION",
                {
                    "operation": "Substitution",
                    "entity": f"Ingredient {ingredient_id_to_replace} is not part of Recipe {recipe_id}",
                },
            )

        #3. Get suggestions from the knowledge base
        suggestions = SUBSTITUTION_RULES.get(ingredient_id_to_replace, [])

        #4. Enrich suggestions with ingredient names
        enriched_suggestions = []
        all_ingredients_meta = data.get("ingredients", {}).values()
        for suggestion in suggestions:
            sub_id = suggestion["substitute_ingredient_id"]
            sub_meta = next(
                (i for i in all_ingredients_meta.values() if i["ingredient_id"] == sub_id), None
            )

            if sub_meta:
                enriched_suggestion = suggestion.copy()
                enriched_suggestion["substitute_ingredient_name"] = sub_meta.get(
                    "ingredient_name"
                )
                enriched_suggestions.append(enriched_suggestion)

        #5. Return the standardized success response
        return _build_success_response(enriched_suggestions)
