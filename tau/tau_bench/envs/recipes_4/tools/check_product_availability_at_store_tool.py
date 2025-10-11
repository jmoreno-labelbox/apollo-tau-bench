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

class CheckProductAvailabilityAtStoreTool(Tool):
    """
    A tool to check product availability for a grocery list at a specific store.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "check_product_availability_at_store",
                "description": (
                    "Checks the stock status for each item on a grocery list at a specific store. "
                    "Returns a list of items that are low in stock or out of stock."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "integer",
                            "description": "The unique ID for the grocery list to check."
                        },
                        "store_id": {
                            "type": "integer",
                            "description": "The unique ID of the store to check against."
                        }
                    },
                    "required": ["list_id", "store_id"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], list_id, store_id) -> Dict[str, Any]:
        """
        Executes the logic to check store inventory against a grocery list.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool. Expects 'list_id' and 'store_id'.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains a list of items with potential stock issues.
        """
        # 1. Verify Input Data
        param_definitions = {
            "list_id": {"type": int, "required": True},
            "store_id": {"type": int, "required": True},
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(validation_error["error_code"], validation_error["details"])

        # 2. Preconditions Verification
        if not any(g.get("list_id") == list_id for g in data.get("grocery_lists", [])):
            return _build_error_response("NOT_FOUND", {"entity": "GroceryList", "entity_id": list_id})
        if not any(s.get("store_id") == store_id for s in data.get("stores", [])):
            return _build_error_response("NOT_FOUND", {"entity": "Store", "entity_id": store_id})

        # 3. Fundamental Logic
        list_items = [item for item in data.get("grocery_list_items", []) if item.get("list_id") == list_id]
        all_store_products = data.get("store_products", [])
        all_ingredients_meta = list(data.get("ingredients", {}).values())

        problem_items = []
        for item in list_items:
            ingredient_id = item["ingredient_id"]

            # Retrieve all items in the store containing this ingredient.
            candidate_products = [
                p for p in all_store_products
                if p.get("store_id") == store_id and p.get("ingredient_id") == ingredient_id
            ]

            # Identify the optimal product that is either in stock or has low availability and is the least expensive.
            in_stock_products = [p for p in candidate_products if p.get("stock_status_enum") in ("in_stock", "low")]

            best_product = None
            if in_stock_products:
                best_product = min(in_stock_products, key=lambda p: p.get("price_cents", float('inf')))

            status = ""
            if not best_product:
                status = "out_of_stock"
            elif best_product.get("stock_status_enum") == "low":
                status = "low_stock"

            if status:
                ingredient_meta = next((i for i in all_ingredients_meta if i["ingredient_id"] == ingredient_id), {})
                problem_items.append({
                    "ingredient_id": ingredient_id,
                    "ingredient_name": ingredient_meta.get("ingredient_name", "Unknown"),
                    "status": status
                })

        # 4. Reply
        return _build_success_response(problem_items)