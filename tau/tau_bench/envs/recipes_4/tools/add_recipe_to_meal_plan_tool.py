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

class AddRecipeToMealPlanTool(Tool):
    """
    A tool to add a single recipe entry to an existing meal plan.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "add_recipe_to_meal_plan",
                "description": "Adds a single recipe to an existing meal plan for a specific date and meal type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_plan_id": {
                            "type": "integer",
                            "description": "The unique ID for the meal plan to be modified."
                        },
                        "recipe_id": {
                            "type": "integer",
                            "description": "The unique ID of the recipe to add."
                        },
                        "plan_date": {
                            "type": "string",
                            "description": "The date for the meal entry, in 'YYYY-MM-DD' format."
                        },
                        "meal_type": {
                            "type": "string",
                            "description": "The type of meal (e.g., 'Breakfast', 'Lunch', 'Dinner'). Defaults to 'Dinner'."
                        },
                        "servings_adult": { "type": "integer", "description": "Number of adult servings. Defaults to 2."},
                        "servings_child": { "type": "integer", "description": "Number of child servings. Defaults to 0."},
                        "notes": { "type": "string", "description": "Optional notes for the meal entry."},
                        "user_id": { "type": "integer", "description": "The ID of the user performing the action, for auditing."}
                    },
                    "required": ["meal_plan_id", "recipe_id", "plan_date"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], meal_plan_id, plan_date, recipe_id, user_id, meal_type = "Dinner", notes = "", servings_adult = 2, servings_child = 0) -> Dict[str, Any]:
        """
        Executes the logic to create a new meal plan entry.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the newly created meal plan entry object.
        """
        # 1. Verify Input Data
        param_definitions = {
            "meal_plan_id": {"type": int, "required": True},
            "recipe_id": {"type": int, "required": True},
            "plan_date": {"type": str, "required": True},
            "meal_type": {"type": str, "required": False},
            "servings_adult": {"type": int, "required": False},
            "servings_child": {"type": int, "required": False},
            "notes": {"type": str, "required": False},
            "user_id": {"type": int, "required": False},
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(validation_error["error_code"], validation_error["details"])

        # 2. Preconditions Verification
        meal_plan_record = next((p for p in data.get("meal_plans", []) if p.get("meal_plan_id") == meal_plan_id), None)
        if not meal_plan_record:
            return _build_error_response("NOT_FOUND", {"entity": "MealPlan", "entity_id": meal_plan_id})
        if not any(r.get("recipe_id") == recipe_id for r in list(data.get("recipes", {}).values())):
            return _build_error_response("NOT_FOUND", {"entity": "Recipe", "entity_id": recipe_id})

        # Business Rule: Confirm the date falls within the designated week of the plan.
        try:
            plan_start_date = date.fromisoformat(meal_plan_record["week_start_date"])
            entry_date = date.fromisoformat(plan_date)
        except ValueError:
            return _build_error_response("INVALID_PARAMETER_TYPE", {"param": "plan_date", "expected_type": "string in YYYY-MM-DD format"})

        plan_end_date = plan_start_date + timedelta(days=6)
        if not (plan_start_date <= entry_date <= plan_end_date):
            return _build_error_response("UNSUPPORTED_OPERATION", {"operation": "Add Entry", "entity": f"Date {plan_date} is outside the week of MealPlan {meal_plan_id}"})

        # Business Rule: Disallow repeating entries
        if any(e for e in data.get("meal_plan_entries", []) if e.get("meal_plan_id") == meal_plan_id and e.get("plan_date") == plan_date and e.get("meal_type") == meal_type):
            return _build_error_response("ALREADY_EXISTS", {"entity": "MealPlanEntry", "entity_id": f"for {plan_date} {meal_type}"})

        # 3. Data Generation
        entries_table = data.setdefault("meal_plan_entries", [])
        max_id = max((e.get("entry_id", 0) for e in entries_table), default=DEFAULT_BUSINESS_RULES["INITIAL_ID_DEFAULTS"]["meal_plan_entries"])
        new_entry_id = max_id + 1

        new_entry_record = {
            "entry_id": new_entry_id,
            "meal_plan_id": meal_plan_id,
            "plan_date": plan_date,
            "meal_type": meal_type,
            "recipe_id": recipe_id,
            "servings_adult": servings_adult,
            "servings_child": servings_child,
            "notes": notes
        }
        entries_table.append(new_entry_record)

        # 4. Review and verification
        _log_audit_event(
            data=data,
            household_id=meal_plan_record.get("household_id"),
            user_id=user_id,
            entity_type="meal_plan_entries",
            entity_id=new_entry_id,
            action_enum="create",
            payload_json={"recipe_id": recipe_id, "plan_date": plan_date}
        )

        # 5. Reply
        return _build_success_response(new_entry_record)