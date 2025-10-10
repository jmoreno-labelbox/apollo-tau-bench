# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetRecipeDetailsTool(Tool):
    """
    A tool to retrieve the full, detailed profile of a single recipe.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "get_recipe_details",
                "description": (
                    "Retrieves the full profile for a single recipe by its unique ID, "
                    "including its hydrated list of ingredients and preparation instructions."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_id": {
                            "type": "integer",
                            "description": "The unique identifier for the recipe to retrieve."
                        },
                    },
                    "required": ["recipe_id"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> Dict[str, Any]:
        """
        Executes the logic to fetch and enrich a specific recipe's data.

        This method validates the required recipe_id, finds the corresponding
        recipe, and then enriches it by fetching all its ingredients and their
        full names, providing a complete data packet for the agent.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool. Expects a required
                      'recipe_id'.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the fully detailed and hydrated recipe object.
        """
        # 1. Verify Input Data
        param_definitions = {
            "recipe_id": {"type": int, "required": True}
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"],
                validation_error["details"]
            )

        recipe_id = kwargs["recipe_id"]

        # 2. Data Acquisition: Locate the primary recipe object.
        recipe_record = next(
            (r for r in list(data.get("recipes", {}).values()) if r.get("recipe_id") == recipe_id),
            None
        )

        if not recipe_record:
            return _build_error_response("NOT_FOUND", {"entity": "Recipe", "entity_id": recipe_id})

        # 3. Data Enrichment (Hydration): Retrieve and enhance ingredient details.
        recipe_ingredients_links = [
            ri for ri in data.get("recipe_ingredients", []) if ri.get("recipe_id") == recipe_id
        ]

        enriched_ingredients = []
        all_ingredients_meta = list(data.get("ingredients", {}).values())
        for link in recipe_ingredients_links:
            ingredient_meta = next(
                (i for i in all_ingredients_meta if i.get("ingredient_id") == link.get("ingredient_id")),
                None
            )
            enriched_ingredients.append({
                "ingredient_id": link.get("ingredient_id"),
                "ingredient_name": ingredient_meta.get("ingredient_name") if ingredient_meta else "Unknown",
                "quantity": link.get("quantity"),
                "unit": link.get("unit"),
            })

        # 4. Construct the ultimate response object.
        detailed_recipe = recipe_record.copy()
        detailed_recipe["ingredients"] = enriched_ingredients

        # 5. Provide the normalized success response.
        return _build_success_response(detailed_recipe)
