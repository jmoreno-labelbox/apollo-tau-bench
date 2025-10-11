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

class GetRecipeSubstitutionsTool(Tool):
    """
    A tool to suggest ingredient substitutions for a specific recipe.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "get_recipe_substitutions",
                "description": (
                    "Suggests ingredient substitutions for a given ingredient within "
                    "a specific recipe, based on a predefined knowledge base."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_id": {
                            "type": "integer",
                            "description": "The unique ID for the recipe requiring a substitution."
                        },
                        "ingredient_id_to_replace": {
                            "type": "integer",
                            "description": "The unique ID of the ingredient that is missing."
                        }
                    },
                    "required": ["recipe_id", "ingredient_id_to_replace"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], ingredient_id_to_replace, recipe_id) -> Dict[str, Any]:
        """
        Executes the logic to find and suggest ingredient substitutions.

        This method validates the inputs, confirms the ingredient is part of the
        recipe, then consults a predefined knowledge base (SUBSTITUTION_RULES)
        for valid alternatives, enriching the response with ingredient names.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool. Expects 'recipe_id'
                      and 'ingredient_id_to_replace'.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains a list of substitution suggestions.
        """
        # 1. Verify Input Data
        param_definitions = {
            "recipe_id": {"type": int, "required": True},
            "ingredient_id_to_replace": {"type": int, "required": True}
        }
        validation_error = _validate_inputs({"ingredient_id_to_replace": ingredient_id_to_replace, "recipe_id": recipe_id}, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"],
                validation_error["details"]
            )
        ing_id_to_replace = ingredient_id_to_replace

        # 2. Preconditions Validation
        if not any(r.get("recipe_id") == recipe_id for r in list(data.get("recipes", {}).values())):
            return _build_error_response("NOT_FOUND", {"entity": "Recipe", "entity_id": recipe_id})

        if not any(i.get("ingredient_id") == ing_id_to_replace for i in list(data.get("ingredients", {}).values())):
            return _build_error_response("NOT_FOUND", {"entity": "Ingredient", "entity_id": ing_id_to_replace})

        recipe_ingredients = {ri["ingredient_id"] for ri in data.get("recipe_ingredients", []) if ri["recipe_id"] == recipe_id}
        if ing_id_to_replace not in recipe_ingredients:
            return _build_error_response("UNSUPPORTED_OPERATION", {
                "operation": "Substitution",
                "entity": f"Ingredient {ing_id_to_replace} is not part of Recipe {recipe_id}"
            })

        # 3. Retrieve recommendations from the knowledge base.
        suggestions = SUBSTITUTION_RULES.get(ing_id_to_replace, [])

        # 4. Enhance recommendations by including ingredient names.
        enriched_suggestions = []
        all_ingredients_meta = list(data.get("ingredients", {}).values())
        for suggestion in suggestions:
            sub_id = suggestion["substitute_ingredient_id"]
            sub_meta = next((i for i in all_ingredients_meta if i["ingredient_id"] == sub_id), None)

            if sub_meta:
                enriched_suggestion = suggestion.copy()
                enriched_suggestion["substitute_ingredient_name"] = sub_meta.get("ingredient_name")
                enriched_suggestions.append(enriched_suggestion)

        # 5. Provide the uniform success response.
        return _build_success_response(enriched_suggestions)