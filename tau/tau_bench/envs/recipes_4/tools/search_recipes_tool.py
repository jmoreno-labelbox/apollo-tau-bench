# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchRecipesTool(Tool):
    """
    A tool to search for recipes based on a combination of filters.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "search_recipes",
                "description": (
                    "Searches for recipes using various optional filters. "
                    "Multiple filters can be combined to narrow down the results."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cuisine": {
                            "type": "string",
                            "description": "The cuisine type to filter by (e.g., 'Italian', 'Mexican')."
                        },
                        "meal_type": {
                            "type": "string",
                            "description": "The meal type to filter by (e.g., 'Dinner', 'Lunch')."
                        },
                        "max_calories": {
                            "type": "integer",
                            "description": "The maximum calories per serving."
                        },
                        "min_protein_g": {
                            "type": "integer",
                            "description": "The minimum grams of protein per serving."
                        },
                        "is_peanut_free": {
                            "type": "boolean",
                            "description": "Filter for recipes that are marked as peanut-free."
                        }
                    },
                    "required": [],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> Dict[str, Any]:
        """
        Executes the search logic by applying a series of filters.

        This method validates all provided filters and applies them sequentially
        to the main list of recipes. An empty list is a valid successful
        result if no recipes match the criteria.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments for filtering. Can include 'cuisine',
                      'meal_type', 'max_calories', 'min_protein_g', and
                      'is_peanut_free'.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains a list of matching recipe objects.
        """
        # 1. Verify all submitted inputs
        param_definitions = {
            "cuisine": {"type": str, "required": False},
            "meal_type": {"type": str, "required": False},
            "max_calories": {"type": int, "required": False},
            "min_protein_g": {"type": int, "required": False},
            "is_peanut_free": {"type": bool, "required": False},
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"],
                validation_error["details"]
            )

        # Begin with the complete set of recipes.
        results = list(data.get("recipes", {}).values())

        # 3. Sequentially implement filters.
        if "cuisine" in kwargs:
            cuisine = kwargs["cuisine"].lower()
            results = [r for r in results if r.get("cuisine", "").lower() == cuisine]

        if "meal_type" in kwargs:
            meal_type = kwargs["meal_type"].lower()
            results = [r for r in results if r.get("meal_type", "").lower() == meal_type]


        if "max_calories" in kwargs:
            max_calories = kwargs["max_calories"]
            results = [r for r in results if (calories := r.get("calories_per_serving")) is not None and calories <= max_calories]

        if "min_protein_g" in kwargs:
            min_protein_g = kwargs["min_protein_g"]
            results = [r for r in results if (protein := r.get("protein_g_per_serving")) is not None and protein >= min_protein_g]

        if kwargs.get("is_peanut_free") is True:
            results = [r for r in results if r.get("is_peanut_free") is True]

        # 4. Provide the filtered list within a standard success response format.
        return _build_success_response(results)
