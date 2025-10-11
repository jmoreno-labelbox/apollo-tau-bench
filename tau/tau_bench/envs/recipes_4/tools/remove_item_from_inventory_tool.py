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

class RemoveItemFromInventoryTool(Tool):
    """
    A tool to explicitly remove an item from a household's inventory.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "remove_item_from_inventory",
                "description": (
                    "Explicitly removes an entire item from inventory. Useful for scenarios "
                    "like discarding expired food. Identify the item either by its unique 'inv_item_id' "
                    "or by the combination of 'household_id' and 'ingredient_id'."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inv_item_id": {
                            "type": "integer",
                            "description": "The unique ID of the inventory item to remove."
                        },
                        "household_id": {
                            "type": "integer",
                            "description": "The household ID, used with ingredient_id if inv_item_id is absent."
                        },
                        "ingredient_id": {
                            "type": "integer",
                            "description": "The ingredient ID, used with household_id if inv_item_id is absent."
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user performing the action, for auditing."
                        }
                    },
                    "required": [],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], household_id, ingredient_id, inv_item_id, user_id) -> Dict[str, Any]:
        """
        Executes the logic to find and explicitly remove an inventory item.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the item that was removed.
        """
        # 1. Check Input Data Types
        param_definitions = {
            "inv_item_id": {"type": int, "required": False},
            "household_id": {"type": int, "required": False},
            "ingredient_id": {"type": int, "required": False},
            "user_id": {"type": int, "required": False},
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(validation_error["error_code"], validation_error["details"])

        # 2. Specific Validation: Confirm that at least one form of identification is supplied.
        if not inv_item_id and not (household_id and ingredient_id):
            return _build_error_response("REQUIRED_PARAMETER", {"param": "'inv_item_id' or both 'household_id' and 'ingredient_id'"})

        # 3. Locate the item for deletion
        inventory_table = data.get("inventory_items", [])
        item_to_remove = None
        if inv_item_id:
            item_to_remove = next((item for item in inventory_table if item.get("inv_item_id") == inv_item_id), None)
        else:
            item_to_remove = next((item for item in inventory_table if item.get("household_id") == household_id and item.get("ingredient_id") == ingredient_id), None)

        if not item_to_remove:
            return _build_error_response("NOT_FOUND", {"entity": "Inventory Item", "entity_id": inv_item_id or f"for ingredient {ingredient_id}"})

        # 4. Data verification (prior to deletion)
        item_id_to_remove = item_to_remove["inv_item_id"]
        _log_audit_event(
            data=data,
            household_id=item_to_remove.get("household_id"),
            user_id=user_id,
            entity_type="inventory_items",
            entity_id=item_id_to_remove,
            action_enum="delete",
            payload_json=item_to_remove # Record the complete entry that is being removed.
        )

        # 5. Execute the deletion.
        data["inventory_items"] = [item for item in inventory_table if item.get("inv_item_id") != item_id_to_remove]

        # 6. Reply
        return _build_success_response({
            "status": "success",
            "removed_item": item_to_remove
        })