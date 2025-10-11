# Sierra Copyright

import datetime
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

class AddItemToGroceryListTool(Tool):
    """
    A tool to add a single item to an existing grocery list.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "add_item_to_grocery_list",
                "description": (
                    "Adds a single ingredient to a grocery list. If the ingredient already "
                    "exists on the list, its quantity is updated. Otherwise, a new item is created."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "integer",
                            "description": "The unique ID for the grocery list to modify."
                        },
                        "ingredient_id": {
                            "type": "integer",
                            "description": "The unique ID of the ingredient to add."
                        },
                        "quantity": {
                            "type": "number",
                            "description": "The quantity of the ingredient to add."
                        },
                        "unit": {
                            "type": "string",
                            "description": "The unit of measurement for the quantity."
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user performing the action, for auditing."
                        }
                    },
                    "required": ["list_id", "ingredient_id", "quantity", "unit"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], ingredient_id, list_id, quantity, unit, user_id) -> Dict[str, Any]:
        """
        Executes the logic to add or update a grocery list item.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the final state of the grocery list item.
        """
        # 1. Verify Input Data
        param_definitions = {
            "list_id": {"type": int, "required": True},
            "ingredient_id": {"type": int, "required": True},
            "quantity": {"type": (int, float), "required": True},
            "unit": {"type": str, "required": True},
            "user_id": {"type": int, "required": False},
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(validation_error["error_code"], validation_error["details"])

        # 2. Validation of Preconditions
        if not any(g.get("list_id") == list_id for g in data.get("grocery_lists", [])):
            return _build_error_response("NOT_FOUND", {"entity": "GroceryList", "entity_id": list_id})
        ingredient_meta = next((i for i in list(data.get("ingredients", {}).values()) if i.get("ingredient_id") == ingredient_id), None)
        if not ingredient_meta:
            return _build_error_response("NOT_FOUND", {"entity": "Ingredient", "entity_id": ingredient_id})

        # 3. Logic: Locate current item or set up for creation
        gli_table = data.setdefault("grocery_list_items", [])
        existing_item = next(
            (item for item in gli_table if item.get("list_id") == list_id and item.get("ingredient_id") == ingredient_id),
            None
        )

        list_record = next(g for g in data.get("grocery_lists", []) if g.get("list_id") == list_id)
        household_id = list_record.get("household_id")

        if existing_item:
            # Modify current item
            action = "update"
            # To simplify, we assume compatible units and directly sum the quantities.
            # An enhanced normalizer could manage unit conversions.
            existing_item["quantity"] += quantity
            final_record = existing_item
            entity_id = existing_item["item_id"]
        else:
            # Generate a new item.
            action = "create"
            max_id = max((i.get("item_id", 0) for i in gli_table), default=DEFAULT_BUSINESS_RULES["INITIAL_ID_DEFAULTS"]["grocery_list_items"])
            new_item_id = max_id + 1

            new_record = {
                "item_id": new_item_id,
                "list_id": list_id,
                "ingredient_id": ingredient_id,
                "quantity": quantity,
                "unit": unit,
                "grocery_section": ingredient_meta.get("grocery_section", "Misc"),
                "pantry_staple_flag": ingredient_meta.get("pantry_staple_flag", False),
                "overlap_last_month_flag": False # Indeterminate at this point.
            }
            gli_table.append(new_record)
            final_record = new_record
            entity_id = new_item_id

        # 4. Review and verification
        _log_audit_event(
            data=data,
            household_id=household_id,
            user_id=user_id,
            entity_type="grocery_list_items",
            entity_id=entity_id,
            action_enum=action,
            payload_json={"ingredient_id": ingredient_id, "quantity_added": quantity, "unit": unit}
        )

        # 5. Reply
        return _build_success_response(final_record)