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

class GetMemberDetailsTool(Tool):
    """
    A tool to retrieve the detailed profile of a single household member.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "get_member_details",
                "description": "Retrieves the full profile for a single member by their unique ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "member_id": {
                            "type": "integer",
                            "description": "The unique identifier for the member."
                        },
                    },
                    "required": ["member_id"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], member_id) -> Dict[str, Any]:
        """
        Executes the tool's logic to fetch a specific member's profile.

        This method validates that a member_id is provided and is of the correct
        type. It then searches the dataset for the corresponding member and
        returns their complete profile.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool. Expects a required
                      'member_id'.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the member object. On failure, it
            contains a structured error object.
        """
        # 1. Input Validation: The 'member_id' is required for this tool.
        param_definitions = {
            "member_id": {"type": int, "required": True}
        }
        validation_error = _validate_inputs({"member_id": member_id}, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"],
                validation_error["details"]
            )

        # 2. Data Acquisition: Locate the particular member within the dataset.
        member_profile = next(
            (m for m in data.get("members", []) if m.get("member_id") == member_id),
            None
        )

        # 3. Manage scenarios when the member cannot be located.
        if not member_profile:
            return _build_error_response(
                "NOT_FOUND",
                details={"entity": "Member", "entity_id": member_id}
            )

        # 4. Provide a uniform success response.
        return _build_success_response(member_profile)