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

class GetGroceryListDetailsTool(Tool):
    """
    A tool to retrieve the full details of a grocery list, including its items.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "get_grocery_list_details",
                "description": "Retrieves a grocery list and all its items, enriched with ingredient names, by its unique ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "integer",
                            "description": "The unique identifier for the grocery list to retrieve."
                        }
                    },
                    "required": ["list_id"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], list_id) -> Dict[str, Any]:
        """
        Executes the logic to fetch and enrich a full grocery list.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool. Expects 'list_id'.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the fully detailed grocery list object.
        """
        # 1. Verify Input Data
        param_definitions = {
            "list_id": {"type": int, "required": True}
        }
        validation_error = _validate_inputs({"list_id": list_id}, param_definitions)
        if validation_error:
            return _build_error_response(validation_error["error_code"], validation_error["details"])

        # 2. Data Acquisition: Locate the primary grocery list object.
        list_record = next(
            (g for g in data.get("grocery_lists", []) if g.get("list_id") == list_id),
            None
        )

        if not list_record:
            return _build_error_response("NOT_FOUND", {"entity": "GroceryList", "entity_id": list_id})

        # 3. Data Enrichment (Hydration): Retrieve and augment list elements.
        list_items = [
            item for item in data.get("grocery_list_items", []) if item.get("list_id") == list_id
        ]

        enriched_items = []
        all_ingredients_meta = list(data.get("ingredients", {}).values())
        for item in list_items:
            ingredient_meta = next(
                (i for i in all_ingredients_meta if i.get("ingredient_id") == item.get("ingredient_id")),
                None
            )
            enriched_item = item.copy()
            enriched_item["ingredient_name"] = ingredient_meta.get("ingredient_name") if ingredient_meta else "Unknown Ingredient"
            enriched_items.append(enriched_item)

        # Arrange items according to grocery categories for better organization.
        enriched_items.sort(key=lambda x: (x.get("grocery_section", ""), x.get("ingredient_name", "")))

        # 4. Construct the ultimate response object.
        detailed_list = list_record.copy()
        detailed_list["items"] = enriched_items

        # 5. Provide the standardized success reply
        return _build_success_response(detailed_list)