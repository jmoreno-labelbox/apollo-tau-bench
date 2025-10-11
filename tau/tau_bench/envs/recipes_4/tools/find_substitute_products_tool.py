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

class FindSubstituteProductsTool(Tool):
    """
    A tool to find available in-stock substitutes for out-of-stock items.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "find_substitute_products",
                "description": (
                    "For a given list of out-of-stock or low-stock ingredients at a specific store, "
                    "suggests available in-stock products as substitutes based on a predefined knowledge base."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {
                            "type": "integer",
                            "description": "The unique ID of the store where the check is being performed."
                        },
                        "problem_items": {
                            "type": "array",
                            "items": {"type": "object"},
                            "description": "The list of items with stock issues, from the 'check_product_availability_at_store' tool."
                        }
                    },
                    "required": ["store_id", "problem_items"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], problem_items, store_id) -> Dict[str, Any]:
        """
        Executes the logic to find viable, in-stock substitute products.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains a list of substitution suggestions.
        """
        # 1. Verify Input Data
        param_definitions = {
            "store_id": {"type": int, "required": True},
            "problem_items": {"type": list, "required": True},
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(validation_error["error_code"], validation_error["details"])

        # 2. Condition Verification Before Execution
        if not any(s.get("store_id") == store_id for s in data.get("stores", [])):
            return _build_error_response("NOT_FOUND", {"entity": "Store", "entity_id": store_id})

        # 3. Fundamental Logic
        suggestions = []
        all_store_products = data.get("store_products", [])

        for item in problem_items:
            original_ingredient_id = item.get("ingredient_id")

            # Determine replacement guidelines for the issue ingredient.
            substitute_options = INGREDIENT_SUBSTITUTE_MAP.get(original_ingredient_id, [])

            for sub_ingredient_id in substitute_options:
                # Locate all items for the alternative ingredient in the store.
                candidate_products = [
                    p for p in all_store_products
                    if p.get("store_id") == store_id and p.get("ingredient_id") == sub_ingredient_id
                ]

                # Identify the most affordable option that is currently in stock.
                in_stock_products = [p for p in candidate_products if p.get("stock_status_enum") in ("in_stock", "low")]

                if in_stock_products:
                    best_sub_product = min(in_stock_products, key=lambda p: p.get("price_cents", float('inf')))

                    suggestions.append({
                        "original_ingredient_id": original_ingredient_id,
                        "substitute_ingredient_id": sub_ingredient_id,
                        "substitute_product_id": best_sub_product["product_id"],
                        "substitute_product_name": best_sub_product.get("product_name"),
                        "price_cents": best_sub_product.get("price_cents")
                    })
                    # Identified an acceptable alternative, cease the search for this item.
                    break

        # 4. Reply
        return _build_success_response(suggestions)