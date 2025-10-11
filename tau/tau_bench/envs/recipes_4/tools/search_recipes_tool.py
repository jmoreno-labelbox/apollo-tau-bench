# Copyright Sierra

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
    def invoke(data: Dict[str, Any], cuisine, is_peanut_free, max_calories, meal_type, min_protein_g) -> Dict[str, Any]:
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
        validation_error = _validate_inputs({"cuisine": cuisine, "is_peanut_free": is_peanut_free, "max_calories": max_calories, "meal_type": meal_type, "min_protein_g": min_protein_g}, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"],
                validation_error["details"]
            )

        # Begin with the complete set of recipes.
        results = list(data.get("recipes", {}).values())

        # 3. Sequentially implement filters.
        if "cuisine" in kwargs:
            cuisine = cuisine.lower()
            results = [r for r in results if r.get("cuisine", "").lower() == cuisine]

        if "meal_type" in kwargs:
            meal_type = meal_type.lower()
            results = [r for r in results if r.get("meal_type", "").lower() == meal_type]


        if "max_calories" in kwargs:
            results = [r for r in results if (calories := r.get("calories_per_serving")) is not None and calories <= max_calories]

        if "min_protein_g" in kwargs:
            results = [r for r in results if (protein := r.get("protein_g_per_serving")) is not None and protein >= min_protein_g]

        if is_peanut_free is True:
            results = [r for r in results if r.get("is_peanut_free") is True]

        # 4. Provide the filtered list within a standard success response format.
        return _build_success_response(results)