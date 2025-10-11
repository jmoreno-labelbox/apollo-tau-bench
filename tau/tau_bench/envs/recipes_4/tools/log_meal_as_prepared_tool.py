# Sierra Copyright

import datetime
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

def _log_audit_event(data: Dict[str, Any], household_id, user_id, entity_type, entity_id, action_enum = "custom_action", payload_json = {}) -> None:
    """
    Logs an action to the audit trail.

    This helper constructs and appends a new audit log entry to the in-memory
    'audit_logs' dataset. It automatically generates a new unique 'audit_id'
    and a UTC timestamp for the 'created_at' field. This function modifies
    the 'data' dictionary in place.

    Args:
        data: The main in-memory dictionary containing all datasets, which
              will be mutated by this function.
        **kwargs: Keyword arguments that map to the audit log schema. Expected
            keys include 'household_id', 'user_id', 'entity_type',
            'entity_id', 'action_enum', and 'payload_json'.
    """
    audit_logs_table = data.setdefault("audit_logs", [])

    # 1. Generate a new unique ID based on the last entry or the default start value
    base_id = DEFAULT_BUSINESS_RULES["INITIAL_ID_DEFAULTS"]["audit_logs"]
    max_id = base_id
    if audit_logs_table:
        max_id = max(int(log.get("audit_id", 0)) for log in audit_logs_table)
    next_id = max_id + 1

    # 2. Get the current timestamp in ISO 8601 format (UTC)
    timestamp = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')

    # 3. Construct the new log entry from kwargs
    new_log_entry = {
        "audit_id": next_id,
        "household_id": household_id,
        "user_id": user_id,
        "entity_type": entity_type,
        "entity_id": entity_id,
        "action_enum": action_enum,
        "payload_json": payload_json,
        "created_at": timestamp
    }

    # 4. Append the new entry to the table
    audit_logs_table.append(new_log_entry)

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

class LogMealAsPreparedTool(Tool):
    """
    A tool to log that a recipe was prepared, adding an entry to the meal history.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "log_meal_as_prepared",
                "description": "Logs that a recipe was prepared for a household on a specific date. Optionally includes a user rating.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {
                            "type": "integer",
                            "description": "The unique ID for the household."
                        },
                        "recipe_id": {
                            "type": "integer",
                            "description": "The unique ID of the recipe that was prepared."
                        },
                        "plan_date": {
                            "type": "string",
                            "description": "The date the meal was prepared, in 'YYYY-MM-DD' format."
                        },
                        "rating_int": {
                            "type": "integer",
                            "description": "An optional integer rating for the meal (e.g., 1-5)."
                        },
                        "was_prepared": {
                            "type": "boolean",
                            "description": "Indicates if the meal was actually prepared. Defaults to True."
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user performing the action, for auditing."
                        }
                    },
                    "required": ["household_id", "recipe_id", "plan_date"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], household_id, plan_date, rating_int, recipe_id, user_id, was_prepared = True) -> Dict[str, Any]:
        """
        Executes the logic to create a new meal history entry.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the newly created meal history object.
        """
        # 1. Verify Input Values
        param_definitions = {
            "household_id": {"type": int, "required": True},
            "recipe_id": {"type": int, "required": True},
            "plan_date": {"type": str, "required": True},
            "rating_int": {"type": int, "required": False},
            "was_prepared": {"type": bool, "required": False},
            "user_id": {"type": int, "required": False}
        }
        validation_error = _validate_inputs({"household_id": household_id, "plan_date": plan_date, "rating_int": rating_int, "recipe_id": recipe_id, "user_id": user_id, "was_prepared": was_prepared}, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"],
                validation_error["details"]
            )

        # 2. Validation Checks: Confirm the existence of associated entities
        if not any(h.get("household_id") == household_id for h in data.get("households", [])):
            return _build_error_response("NOT_FOUND", {"entity": "Household", "entity_id": household_id})
        if not any(r.get("recipe_id") == recipe_id for r in list(data.get("recipes", {}).values())):
            return _build_error_response("NOT_FOUND", {"entity": "Recipe", "entity_id": recipe_id})

        # 3. Logic for Data Generation
        history_table = data.setdefault("meal_history", [])

        # Create a new distinct identifier.
        max_id = max((h.get("history_id", 0) for h in history_table), default=6000)
        new_history_id = max_id + 1

        # Create the new entry.
        new_history_record = {
            "history_id": new_history_id,
            "household_id": household_id,
            "recipe_id": recipe_id,
            "plan_date": plan_date,
            "was_prepared": was_prepared,
            "rating_int": rating_int # If absent, defaults to None.
        }

        history_table.append(new_history_record)

        # 4. Review and verification
        _log_audit_event(
            data=data,
            household_id=household_id,
            user_id=user_id,
            entity_type="meal_history",
            entity_id=new_history_id,
            action_enum="create",
            payload_json={"recipe_id": recipe_id, "plan_date": plan_date}
        )

        # 5. Reply
        return _build_success_response(new_history_record)