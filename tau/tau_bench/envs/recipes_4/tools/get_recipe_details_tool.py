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
    def invoke(data: Dict[str, Any], recipe_id) -> Dict[str, Any]:
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
        validation_error = _validate_inputs({"recipe_id": recipe_id}, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"],
                validation_error["details"]
            )

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