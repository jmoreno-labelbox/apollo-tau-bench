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

def _normalize_domain_data(
    entity: str,
    data: Any,
    context: Optional[Dict[str, Any]] = None
) -> Any:
    """
    Normalizes domain-specific data, such as units and ingredient names.

    This function acts as a centralized translator for various data formats
    encountered in the domain, converting them into a canonical format that
    the tools can reliably process.

    Args:
        entity: The type of data to normalize. Supported values are
                'ingredient_name' and 'unit_measurement'.
        data: The data to be normalized. The expected format depends on the
              'entity' type.
        context: An optional dictionary providing additional context, such as
                 the full ingredients dataset for lookups.

    Returns:
        The normalized data. The format of the returned data depends on the
        normalization performed.
    """
    if entity == "ingredient_name":
        # Input 'data' is a string like "Tomatoes" or "flour"
        # Output is the canonical ingredient_id (int)
        if not isinstance(data, str):
            return None

        processed_name = data.lower().strip()
        # Simple plural handling
        if processed_name.endswith('s'):
            processed_name = processed_name[:-1]

        return INGREDIENT_NAME_MAP.get(processed_name)

    if entity == "unit_measurement":
        # Input 'data' is a dict: {"ingredient_id": int, "quantity": float, "unit": str}
        # Output is a dict with quantity/unit normalized to g/ml
        if not isinstance(data, dict) or not all(k in data for k in ["ingredient_id", "quantity", "unit"]):
            return data # Return original data if format is incorrect

        # Find the ingredient's default unit (g or ml)
        # This requires access to the full ingredients dataset, passed in context
        all_ingredients = (context or {}).get("ingredients", [])
        ingredient_meta = next((i for i in all_ingredients if i["ingredient_id"] == data["ingredient_id"]), None)
        if not ingredient_meta:
            return data # Cannot normalize without metadata

        default_unit = ingredient_meta.get("default_unit")
        current_unit = data["unit"].lower()

        # No conversion needed
        if current_unit == default_unit:
            return data

        quantity = data["quantity"]
        new_quantity = quantity

        # Conversion logic
        if current_unit == "cup" and default_unit == "g":
            conversion_factor = UNIT_CONVERSION_RULES["cup_to_g"].get(data["ingredient_id"], UNIT_CONVERSION_RULES["cup_to_g"]["default"])
            new_quantity = quantity * conversion_factor
        elif current_unit == "tbsp" and default_unit == "ml":
            new_quantity = quantity * UNIT_CONVERSION_RULES["tbsp_to_ml"]
        elif current_unit == "tsp" and default_unit == "ml":
            new_quantity = quantity * UNIT_CONVERSION_RULES["tsp_to_ml"]
        elif current_unit == "cup" and default_unit == "ml":
            new_quantity = quantity * UNIT_CONVERSION_RULES["cup_to_ml"]
        else:
            # Return original data if no rule exists
            return data

        return {
            "ingredient_id": data["ingredient_id"],
            "quantity": round(new_quantity, 2),
            "unit": default_unit
        }

    # Return original data if entity type is not supported
    return data

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

class AddItemToInventoryTool(Tool):
    """
    A tool to add an item to a household's inventory or update its quantity.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "add_item_to_inventory",
                "description": (
                    "Adds an item to a household's inventory. If the ingredient already exists, "
                    "it updates the quantity. Otherwise, it creates a new inventory entry."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {
                            "type": "integer",
                            "description": "The unique ID for the household."
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
                    "required": ["household_id", "ingredient_id", "quantity", "unit"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], household_id, ingredient_id, quantity, unit, user_id) -> Dict[str, Any]:
        """
        Executes the logic to add or update an inventory item.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the final state of the inventory item.
        """
        # 1. Verify Input Data
        param_definitions = {
            "household_id": {"type": int, "required": True},
            "ingredient_id": {"type": int, "required": True},
            "quantity": {"type": (int, float), "required": True},
            "unit": {"type": str, "required": True},
            "user_id": {"type": int, "required": False},
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(validation_error["error_code"], validation_error["details"])

        # 2. Validation of Preconditions
        if not any(h.get("household_id") == household_id for h in data.get("households", [])):
            return _build_error_response("NOT_FOUND", {"entity": "Household", "entity_id": household_id})
        if not any(i.get("ingredient_id") == ingredient_id for i in list(data.get("ingredients", {}).values())):
            return _build_error_response("NOT_FOUND", {"entity": "Ingredient", "entity_id": ingredient_id})

        # 3. Logic: Locate existing item or set up for creation.
        inventory_table = data.setdefault("inventory_items", [])
        existing_item = next(
            (item for item in inventory_table if item.get("household_id") == household_id and item.get("ingredient_id") == ingredient_id),
            None
        )

        context = {"ingredients": list(data.get("ingredients", {}).values())}

        if existing_item:
            action = "update"
            normalized_addition = _normalize_domain_data(
                "unit_measurement",
                {"ingredient_id": ingredient_id, "quantity": quantity, "unit": unit},
                context
            )

            normalized_existing = _normalize_domain_data(
                "unit_measurement",
                existing_item,
                context
            )

            # Having converted both to the standard unit, we can now add them without concern.
            new_total_quantity = normalized_existing["quantity"] + normalized_addition["quantity"]

            existing_item["quantity"] = round(new_total_quantity, 2)
            existing_item["unit"] = normalized_existing["unit"] # Save in the default unit.

            final_record = existing_item
            entity_id = existing_item["inv_item_id"]
        else:
            # Generate a new item (standardize the input for uniformity)
            action = "create"
            normalized_input = _normalize_domain_data(
                "unit_measurement",
                {"ingredient_id": ingredient_id, "quantity": quantity, "unit": unit},
                context
            )

            max_id = max((i.get("inv_item_id", 0) for i in inventory_table), default=7000)
            new_item_id = max_id + 1

            new_record = {
                "inv_item_id": new_item_id,
                "household_id": household_id,
                "ingredient_id": ingredient_id,
                "quantity": normalized_input["quantity"],
                "unit": normalized_input["unit"],
                "location_enum": "pantry", # Standard location
                "best_by_date": None
            }
            inventory_table.append(new_record)
            final_record = new_record
            entity_id = new_item_id

        # 4. Review and verification
        _log_audit_event(
            data=data,
            household_id=household_id,
            user_id=user_id,
            entity_type="inventory_items",
            entity_id=entity_id,
            action_enum=action,
            payload_json={"ingredient_id": ingredient_id, "quantity_added": quantity, "unit": unit}
        )

        # 5. Reply
        return _build_success_response(final_record)