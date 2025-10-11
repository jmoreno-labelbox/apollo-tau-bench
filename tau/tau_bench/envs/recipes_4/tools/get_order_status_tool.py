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

class GetOrderStatusTool(Tool):
    """
    A tool to retrieve the status and details of a grocery order.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "get_order_status",
                "description": "Retrieves the full details of a grocery order, including its status and all line items enriched with product names.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "integer",
                            "description": "The unique identifier for the order to retrieve."
                        }
                    },
                    "required": ["order_id"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], order_id) -> Dict[str, Any]:
        """
        Executes the logic to find and return the details of an order.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool. Expects 'order_id'.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the fully detailed and hydrated order object.
        """
        # 1. Verify Input Data
        param_definitions = {
            "order_id": {"type": int, "required": True}
        }
        validation_error = _validate_inputs({"order_id": order_id}, param_definitions)
        if validation_error:
            return _build_error_response(validation_error["error_code"], validation_error["details"])

        # 2. Data Extraction
        order_record = next((o for o in list(data.get("orders", {}).values()) if o.get("order_id") == order_id), None)

        if not order_record:
            return _build_error_response("NOT_FOUND", {"entity": "Order", "entity_id": order_id})

        # 3. Data Enhancement (Hydration)
        order_items = [item for item in data.get("order_items", []) if item.get("order_id") == order_id]
        all_products = data.get("store_products", [])

        enriched_items = []
        for item in order_items:
            enriched_item = item.copy()

            # Augment with the primary product name.
            product_info = next((p for p in all_products if p.get("product_id") == item.get("product_id")), None)
            enriched_item["product_name"] = product_info.get("product_name") if product_info else "Unknown Product"

            # Add the alternative product name if relevant.
            sub_id = item.get("substitute_product_id")
            if sub_id:
                sub_info = next((p for p in all_products if p.get("product_id") == sub_id), None)
                enriched_item["substitute_product_name"] = sub_info.get("product_name") if sub_info else "Unknown Substitute"

            enriched_items.append(enriched_item)

        # 4. Construct the completed response object.
        detailed_order = order_record.copy()
        detailed_order["items"] = enriched_items

        # 5. Return the uniform success response.
        return _build_success_response(detailed_order)