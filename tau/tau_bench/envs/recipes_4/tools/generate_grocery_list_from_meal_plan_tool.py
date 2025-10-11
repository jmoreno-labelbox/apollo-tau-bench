# Copyright Sierra

import datetime, collections
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

class GenerateGroceryListFromMealPlanTool(Tool):
    """
    A tool to create an optimized grocery list from a meal plan and inventory.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "generate_grocery_list_from_meal_plan",
                "description": (
                    "Creates a new grocery list by calculating ingredients needed for a meal plan, "
                    "subtracting items already in the household's inventory."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_plan_id": {
                            "type": "integer",
                            "description": "The unique ID for the meal plan."
                        },
                        "household_id": {
                            "type": "integer",
                            "description": "The unique ID for the household the plan belongs to."
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user creating the list, for auditing."
                        }
                    },
                    "required": ["meal_plan_id", "household_id", "user_id"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], household_id, meal_plan_id, user_id) -> Dict[str, Any]:
        """
        Executes the logic to generate an optimized grocery list.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the ID of the new list and its item IDs.
        """
        # 1. Confirm Input Validity
        param_definitions = {
            "meal_plan_id": {"type": int, "required": True},
            "household_id": {"type": int, "required": True},
            "user_id": {"type": int, "required": True},
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(validation_error["error_code"], validation_error["details"])

        # 2. Preconditions Verification
        meal_plan = next((p for p in data.get("meal_plans", []) if p.get("meal_plan_id") == meal_plan_id), None)
        if not meal_plan:
            return _build_error_response("NOT_FOUND", {"entity": "MealPlan", "entity_id": meal_plan_id})
        if meal_plan.get("household_id") != household_id:
            return _build_error_response("UNSUPPORTED_OPERATION", {"operation": "Generate List", "entity": "MealPlan does not belong to the specified household."})

        # 3. Main Functionality: Compute Net Requirements
        all_ingredients_meta = list(data.get("ingredients", {}).values())
        context = {"ingredients": all_ingredients_meta}

        # 3a. Compile all necessary ingredients for the plan, standardizing units.
        plan_entries = [e for e in data.get("meal_plan_entries", []) if e.get("meal_plan_id") == meal_plan_id]
        recipe_ids = {e["recipe_id"] for e in plan_entries}
        required_ingredients_list = [ri for ri in data.get("recipe_ingredients", []) if ri["recipe_id"] in recipe_ids]

        required_totals = collections.defaultdict(float)
        for req in required_ingredients_list:
            normalized_req = _normalize_domain_data("unit_measurement", req, context)
            required_totals[normalized_req["ingredient_id"]] += normalized_req["quantity"]

        # 3b. Retrieve available stock, standardizing units.
        inventory_items = [i for i in data.get("inventory_items", []) if i.get("household_id") == household_id]
        available_totals = collections.defaultdict(float)
        for item in inventory_items:
            normalized_item = _normalize_domain_data("unit_measurement", item, context)
            available_totals[normalized_item["ingredient_id"]] += normalized_item["quantity"]

        # 3c. Determine the items that need to be purchased.
        net_needed_items = []
        for ingredient_id, required_qty in required_totals.items():
            needed_qty = required_qty - available_totals.get(ingredient_id, 0)
            if needed_qty > 0:
                ingredient_meta = next((i for i in all_ingredients_meta if i["ingredient_id"] == ingredient_id), {})
                net_needed_items.append({
                    "ingredient_id": ingredient_id,
                    "quantity": round(needed_qty, 2),
                    "unit": ingredient_meta.get("default_unit", "units"),
                    "grocery_section": ingredient_meta.get("grocery_section", "Misc"),
                    "pantry_staple_flag": ingredient_meta.get("pantry_staple_flag", False)
                })

        # 4. Generate Grocery List and Items
        gl_table = data.setdefault("grocery_lists", [])
        max_list_id = max((g.get("list_id", 0) for g in gl_table), default=DEFAULT_BUSINESS_RULES["INITIAL_ID_DEFAULTS"]["grocery_lists"])
        new_list_id = max_list_id + 1

        timestamp = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
        new_list_record = {
            "list_id": new_list_id, "household_id": household_id, "source_meal_plan_id": meal_plan_id,
            "created_by_user_id": user_id, "created_at": timestamp, "status_enum": "initialized"
        }
        gl_table.append(new_list_record)

        gli_table = data.setdefault("grocery_list_items", [])
        max_item_id = max((i.get("item_id", 0) for i in gli_table), default=DEFAULT_BUSINESS_RULES["INITIAL_ID_DEFAULTS"]["grocery_list_items"])
        created_item_ids = []

        for item in net_needed_items:
            max_item_id += 1
            new_item_record = {
                "item_id": max_item_id, "list_id": new_list_id, "overlap_last_month_flag": False, **item
            }
            gli_table.append(new_item_record)
            created_item_ids.append(max_item_id)

        # 5. Review and verification
        _log_audit_event(
            data, household_id=household_id, user_id=user_id, entity_type="grocery_lists",
            entity_id=new_list_id, action_enum="create", payload_json={"source_meal_plan_id": meal_plan_id}
        )

        # 6. Reply
        return _build_success_response({
            "list_id": new_list_id,
            "items_added_count": len(created_item_ids),
            "created_item_ids": created_item_ids
        })