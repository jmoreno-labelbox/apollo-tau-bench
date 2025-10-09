from tau_bench.envs.tool import Tool
import collections
import json
from datetime import date, datetime, timedelta, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SearchRecipesTool(Tool):
    """
    A tool to search for recipes based on a combination of filters.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "searchRecipes",
                "description": (
                    "Searches for recipes using various optional filters. "
                    "Multiple filters can be combined to narrow down the results."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cuisine": {
                            "type": "string",
                            "description": "The cuisine type to filter by (e.g., 'Italian', 'Mexican').",
                        },
                        "meal_type": {
                            "type": "string",
                            "description": "The meal type to filter by (e.g., 'Dinner', 'Lunch').",
                        },
                        "max_calories": {
                            "type": "integer",
                            "description": "The maximum calories per serving.",
                        },
                        "min_protein_g": {
                            "type": "integer",
                            "description": "The minimum grams of protein per serving.",
                        },
                        "is_peanut_free": {
                            "type": "boolean",
                            "description": "Filter for recipes that are marked as peanut-free.",
                        },
                    },
                    "required": [],
                },
            },
        }

    @staticmethod
    def invoke(
        data: dict[str, Any],
        cuisine: str = None,
        meal_type: str = None,
        max_calories: int = None,
        min_protein_g: int = None,
        is_peanut_free: bool = None
    ) -> dict[str, Any]:
        """
        Executes the search logic by applying a series of filters.

        This method validates all provided filters and applies them sequentially
        to the main list of recipes. An empty list is a valid successful
        result if no recipes match the criteria.

        Args:
            data: The main in-memory dictionary containing all datasets.
            cuisine: Filter by cuisine type.
            meal_type: Filter by meal type.
            max_calories: Filter by maximum calories.
            min_protein_g: Filter by minimum protein in grams.
            is_peanut_free: Filter by peanut-free recipes.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains a list of matching recipe objects.
        """
        pass
        #1. Validate all provided inputs
        param_definitions = {
            "cuisine": {"type": str, "required": False},
            "meal_type": {"type": str, "required": False},
            "max_calories": {"type": int, "required": False},
            "min_protein_g": {"type": int, "required": False},
            "is_peanut_free": {"type": bool, "required": False},
        }
        validation_error = _validate_inputs(
            {
                "cuisine": cuisine,
                "meal_type": meal_type,
                "max_calories": max_calories,
                "min_protein_g": min_protein_g,
                "is_peanut_free": is_peanut_free
            },
            param_definitions
        )
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Start with the full list of recipes
        results = data.get("recipes", [])

        #3. Apply filters sequentially
        if cuisine is not None:
            cuisine = cuisine.lower()
            results = [r for r in results if r.get("cuisine", "").lower() == cuisine]

        if meal_type is not None:
            meal_type = meal_type.lower()
            results = [
                r for r in results if r.get("meal_type", "").lower() == meal_type
            ]

        if max_calories is not None:
            results = [
                r
                for r in results
                if (calories := r.get("calories_per_serving")) is not None
                and calories <= max_calories
            ]

        if min_protein_g is not None:
            results = [
                r
                for r in results
                if (protein := r.get("protein_g_per_serving")) is not None
                and protein >= min_protein_g
            ]

        if is_peanut_free is True:
            results = [r for r in results if r.get("is_peanut_free") is True]

        #4. Return the filtered list in a standard success response
        return _build_success_response(results)
