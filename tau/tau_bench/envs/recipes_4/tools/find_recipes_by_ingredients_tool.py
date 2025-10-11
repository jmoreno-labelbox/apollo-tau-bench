# Owned by Sierra.

import collections
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


ERROR_MESSAGES = {
    "REQUIRED_PARAMETER": "Required parameter '{param}' is missing.",
    "INVALID_PARAMETER_TYPE": "Parameter '{param}' must be of type {expected_type}.",
    "NOT_FOUND": "{entity} with ID {entity_id} not found.",
    "OPERATION_FAILED": "Operation failed: {reason}",
}








def _validate_inputs(
    args: Dict[str, Any],
    param_definitions: Dict[str, Dict[str, Any]]
) -> Optional[Dict[str, Any]]:
    """
    Validates tool arguments against a set of definitions.

    This helper checks for the presence of required parameters and validates the
    data type for all provided parameters against the definitions. It's designed
    to be the first call within any tool's `invoke` method to act as a
    protective guard clause.

    Args:
        args: The dictionary of arguments passed to the tool (e.g., kwargs).
        param_definitions: A dictionary where each key is a parameter name and
            the value is another dictionary defining its rules, such as
            'type' (e.g., int, str) and 'required' (bool).

    Returns:
        None if all validations pass.
        A dictionary containing the 'error_code' and 'details' for the
        first validation failure, ready to be passed to _build_error_response().
    """
    for param, definition in param_definitions.items():
        is_required = definition.get("required", False)
        expected_type = definition.get("type")

        if is_required and param not in args:
            return {
                "error_code": "REQUIRED_PARAMETER",
                "details": {"param": param}
            }

        if param in args and expected_type is not None:
            value = args[param]
            if not isinstance(value, expected_type):
                return {
                    "error_code": "INVALID_PARAMETER_TYPE",
                    "details": {
                        "param": param,
                        "expected_type": expected_type.__name__
                    }
                }

    return None

def _build_success_response(data: Any) -> str:
    """
    Builds a standardized success response envelope as a JSON string.

    Args:
        data: The payload to be included in the response.

    Returns:
        A JSON string representing the successful response.
    """
    response_dict = {
        "success": True,
        "data": data
    }
    return json.dumps(response_dict, indent=2)

def _build_error_response(error_code: str, details: Optional[Dict[str, Any]] = None) -> str:
    """
    Builds a standardized error response envelope as a JSON string.

    Args:
        error_code: The error code, corresponding to a key in ERROR_MESSAGES.
        details: A dictionary with specific details to format the error message.

    Returns:
        A JSON string representing the failed response.
    """
    details = details or {}
    message_template = ERROR_MESSAGES.get(error_code, "An unknown error occurred.")

    try:
        message = message_template.format(**details)
    except KeyError:
        message = message_template

    response_dict = {
        "success": False,
        "error": {
            "code": error_code,
            "message": message,
            "details": details
        }
    }
    return json.dumps(response_dict, indent=2)

class FindRecipesByIngredientsTool(Tool):
    """
    A tool to find recipes based on a list of available ingredients.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "find_recipes_by_ingredients",
                "description": (
                    "Finds recipes that can be made with a list of available ingredient IDs. "
                    "Results are sorted by how closely they match the available ingredients."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "available_ingredient_ids": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "A list of ingredient IDs that are available."
                        },
                        "max_missing_ingredients": {
                            "type": "integer",
                            "description": "The maximum number of ingredients a recipe can be missing. Defaults to 1."
                        }
                    },
                    "required": ["available_ingredient_ids"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], available_ingredient_ids, max_missing_ingredients = 1) -> Dict[str, Any]:
        """
        Executes the logic to match available ingredients against recipe requirements.

        This method builds a map of ingredients required for each recipe, then
        compares this against the user's available ingredients to find matches.
        Results are enriched with information about missing ingredients and sorted
        by the number of missing ingredients.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool. Expects
                      'available_ingredient_ids' and optional
                      'max_missing_ingredients'.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains a list of matching recipes, sorted by
            the number of missing ingredients.
        """
        # 1. Verify Input Data
        param_definitions = {
            "available_ingredient_ids": {"type": list, "required": True},
            "max_missing_ingredients": {"type": int, "required": False}
        }
        validation_error = _validate_inputs({"available_ingredient_ids": available_ingredient_ids, "max_missing_ingredients": max_missing_ingredients}, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"],
                validation_error["details"]
            )

        available_ids = set(available_ingredient_ids)
        max_missing = max_missing_ingredients

        # 2. Prepare recipe specifications for optimized retrieval.
        recipe_requirements = collections.defaultdict(set)
        for ri in data.get("recipe_ingredients", []):
            recipe_requirements[ri["recipe_id"]].add(ri["ingredient_id"])

        # 3. Locate corresponding recipes
        matching_recipes = []
        for recipe in list(data.get("recipes", {}).values()):
            recipe_id = recipe["recipe_id"]
            required_ids = recipe_requirements[recipe_id]

            missing_ids = required_ids - available_ids

            if len(missing_ids) <= max_missing:
                match_details = {
                    "recipe_info": recipe,
                    "missing_ingredient_count": len(missing_ids),
                    "missing_ingredient_ids": sorted(list(missing_ids))
                }
                matching_recipes.append(match_details)

        # 4. Order results to display the top matches at the beginning.
        matching_recipes.sort(key=lambda x: x["missing_ingredient_count"])

        # 5. Provide the uniform success response.
        return _build_success_response(matching_recipes)