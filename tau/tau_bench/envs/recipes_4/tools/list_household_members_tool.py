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

class ListHouseholdMembersTool(Tool):
    """
    A tool to list all members belonging to a specific household.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "list_household_members",
                "description": (
                    "Lists all members for a given household ID. If the ID is "
                    "omitted, it defaults to the primary household of the "
                    "first user in the dataset."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {
                            "type": "integer",
                            "description": "The unique identifier for the household."
                        },
                    },
                    "required": [],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], household_id) -> Dict[str, Any]:
        """
        Executes the tool's logic to fetch all members of a household.

        This method validates the input household_id, determines the target
        household if one is not provided, and then retrieves all member records
        associated with that household ID.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool. Expects an optional
                      'household_id'.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains a list of member objects. On failure,
            it contains a structured error object.
        """
        # 1. Verify Inputs
        param_definitions = {
            "household_id": {"type": int, "required": False}
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"],
                validation_error["details"]
            )

        # 2. Business Logic: Identify target household if it hasn't been specified.
        if not household_id:
            users = list(data.get("users", {}).values())
            if not users:
                return _build_error_response("NO_DATA_FOUND", {"entity": "Users"})

            first_user = list(data.get("users", {}).values())[0] if data.get("users") else None
            if not first_user:
                return _build_error_response("NO_DATA_FOUND", {"entity": "Users"})

            first_user_id = first_user.get("user_id")
            household = next((h for h in data.get("households", []) if h.get("primary_user_id") == first_user_id), None)
            if not household:
                return _build_error_response("NOT_FOUND", {"entity": "Household", "entity_id": f"for user {first_user_id}"})
            household_id = household.get("household_id")

        # 3. Validation Step: Confirm the existence of the target household.
        target_household = next((h for h in data.get("households", []) if h.get("household_id") == household_id), None)
        if not target_household:
            return _build_error_response("NOT_FOUND", {"entity": "Household", "entity_id": household_id})

        # 4. Data Fetching: Select members based on the specified household_id.
        household_members = [
            m for m in data.get("members", []) if m.get("household_id") == household_id
        ]

        # 5. Provide a uniform success response.
        return _build_success_response(household_members)