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

class GetMealHistoryTool(Tool):
    """
    A tool to retrieve the meal history for a household.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "get_meal_history",
                "description": "Retrieves the meal history for a household, optionally filtered by the number of days back.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {
                            "type": "integer",
                            "description": "The unique identifier for the household."
                        },
                        "days_back": {
                            "type": "integer",
                            "description": "Optional. The number of days of history to retrieve from today."
                        }
                    },
                    "required": ["household_id"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], days_back, household_id) -> Dict[str, Any]:
        """
        Executes the logic to find and return a household's meal history.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool. Expects 'household_id'
                      and an optional 'days_back'.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains a list of meal history objects, sorted
            by date descending.
        """
        # 1. Verify Input Data
        param_definitions = {
            "household_id": {"type": int, "required": True},
            "days_back": {"type": int, "required": False}
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"],
                validation_error["details"]
            )

        # 2. Preconditions Validation: Verify the existence of the household.
        if not any(h for h in data.get("households", []) if h.get("household_id") == household_id):
            return _build_error_response("NOT_FOUND", {"entity": "Household", "entity_id": household_id})

        # 3. Data Acquisition & Selection
        all_history = data.get("meal_history", [])
        household_history = [h for h in all_history if h.get("household_id") == household_id]

        if days_back is not None:
            # The current date is supplied in the context to ensure consistency.
            today = date(2025, 9, 1)
            start_date = today - timedelta(days=days_back)

            # Restrict by date interval
            household_history = [
                h for h in household_history
                if date.fromisoformat(h.get("plan_date", "1900-01-01")) >= start_date
            ]

        # 4. Arrange results from newest to oldest.
        household_history.sort(key=lambda x: x.get("plan_date", ""), reverse=True)

        # 5. Provide a consistent success response.
        return _build_success_response(household_history)