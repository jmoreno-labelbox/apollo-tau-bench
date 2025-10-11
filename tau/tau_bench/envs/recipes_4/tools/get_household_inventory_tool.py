# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool








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

class GetHouseholdInventoryTool(Tool):
    """
    A tool to retrieve all inventory items for a specific household.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "get_household_inventory",
                "description": "Retrieves a list of all inventory items for a given household, enriched with ingredient names.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {
                            "type": "integer",
                            "description": "The unique identifier for the household."
                        }
                    },
                    "required": ["household_id"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], household_id) -> Dict[str, Any]:
        """
        Executes the logic to find and return a household's inventory.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool. Expects 'household_id'.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains a list of enriched inventory items.
        """
        # 1. Verify Input Data
        param_definitions = {
            "household_id": {"type": int, "required": True}
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(validation_error["error_code"], validation_error["details"])

        # 2. Pre-condition Validation: Verify the existence of the household.
        if not any(h.get("household_id") == household_id for h in data.get("households", [])):
            return _build_error_response("NOT_FOUND", {"entity": "Household", "entity_id": household_id})

        # 3. Data Acquisition and Enhancement (Hydration)
        inventory_items = [i for i in data.get("inventory_items", []) if i.get("household_id") == household_id]

        enriched_items = []
        all_ingredients_meta = list(data.get("ingredients", {}).values())
        for item in inventory_items:
            ingredient_meta = next(
                (i for i in all_ingredients_meta if i.get("ingredient_id") == item.get("ingredient_id")),
                None
            )
            enriched_item = item.copy()
            enriched_item["ingredient_name"] = ingredient_meta.get("ingredient_name") if ingredient_meta else "Unknown Ingredient"
            enriched_items.append(enriched_item)

        # 4. Organize results in alphabetical order for uniformity.
        enriched_items.sort(key=lambda x: x.get("ingredient_name", ""))

        # 5. Provide the standardized success response.
        return _build_success_response(enriched_items)