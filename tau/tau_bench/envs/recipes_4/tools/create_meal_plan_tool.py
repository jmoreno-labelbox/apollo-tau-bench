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

def _log_audit_event(data: Dict[str, Any], **kwargs: Any) -> None:
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
        "household_id": kwargs.get("household_id"),
        "user_id": kwargs.get("user_id"),
        "entity_type": kwargs.get("entity_type"),
        "entity_id": kwargs.get("entity_id"),
        "action_enum": kwargs.get("action_enum", "custom_action"),
        "payload_json": kwargs.get("payload_json", {}),
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

class CreateMealPlanTool(Tool):
    """
    A tool to create a new, empty meal plan for a household for a specific week.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "create_meal_plan",
                "description": "Creates a new, empty meal plan for a household for a specific week, defined by its start date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {
                            "type": "integer",
                            "description": "The unique ID for the household."
                        },
                        "week_start_date": {
                            "type": "string",
                            "description": "The start date of the meal plan week, in 'YYYY-MM-DD' format."
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user creating the plan, for auditing."
                        }
                    },
                    "required": ["household_id", "week_start_date", "user_id"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], household_id, user_id, week_start_date) -> Dict[str, Any]:
        """
        Executes the logic to create a new meal plan record.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the newly created meal plan object.
        """
        # 1. Check Input Validity
        param_definitions = {
            "household_id": {"type": int, "required": True},
            "week_start_date": {"type": str, "required": True},
            "user_id": {"type": int, "required": True}
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"],
                validation_error["details"]
            )

        # 2. Validation of Preconditions
        if not any(h.get("household_id") == household_id for h in data.get("households", [])):
            return _build_error_response("NOT_FOUND", {"entity": "Household", "entity_id": household_id})
        if not any(u.get("user_id") == user_id for u in list(data.get("users", {}).values())):
            return _build_error_response("NOT_FOUND", {"entity": "User", "entity_id": user_id})

        # Business Rule: Disallow duplicate plans within the same week.
        existing_plan = any(
            p for p in data.get("meal_plans", [])
            if p.get("household_id") == household_id and p.get("week_start_date") == week_start_date
        )
        if existing_plan:
            return _build_error_response("ALREADY_EXISTS", {"entity": "MealPlan", "entity_id": f"for household {household_id} on {week_start_date}"})

        # 3. Logic for Data Generation
        meal_plans_table = data.setdefault("meal_plans", [])

        # Create a new distinct identifier.
        max_id = max((p.get("meal_plan_id", 0) for p in meal_plans_table), default=DEFAULT_BUSINESS_RULES["INITIAL_ID_DEFAULTS"]["meal_plans"])
        new_plan_id = max_id + 1

        timestamp = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')

        new_plan_record = {
            "meal_plan_id": new_plan_id,
            "household_id": household_id,
            "week_start_date": week_start_date,
            "created_by_user_id": user_id,
            "created_at": timestamp
        }

        meal_plans_table.append(new_plan_record)

        # 4. Review and verification
        _log_audit_event(
            data=data,
            household_id=household_id,
            user_id=user_id,
            entity_type="meal_plans",
            entity_id=new_plan_id,
            action_enum="create",
            payload_json={"week_start_date": week_start_date}
        )

        # 5. Reply
        return _build_success_response(new_plan_record)