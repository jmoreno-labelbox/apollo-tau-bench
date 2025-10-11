# Copyright Sierra

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

class AddNewRecipeTool(Tool):
    """
    A tool to add a new recipe to the dataset.
    """

    # Specifies the required fields for the primary recipe data.
    EXPECTED_RECIPE_FIELDS = {
        "recipe_title", "meal_type", "cuisine", "servings_default",
        "prep_minutes", "cook_minutes", "is_peanut_free",
        "calories_per_serving", "protein_g_per_serving", "instructions_json",
        "notes"
    }

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "add_new_recipe",
                "description": (
                    "Adds a new recipe to the dataset. Requires recipe metadata and a "
                    "list of its ingredients with quantities and units."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_data": {
                            "type": "object",
                            "description": "A dictionary with the new recipe's main data."
                        },
                        "ingredients_list": {
                            "type": "array",
                            "items": {"type": "object"},
                            "description": "A list of ingredient objects, each with ingredient_id, quantity, and unit."
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user performing the action, for auditing."
                        }
                    },
                    "required": ["recipe_data", "ingredients_list", "user_id"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], ingredients_list, recipe_data, user_id) -> Dict[str, Any]:
        """
        Executes the logic to create a new recipe and its ingredient links.

        This method performs deep validation on the provided recipe data and
        ingredient list, creates records in both the 'recipes' and
        'recipe_ingredients' tables, logs the event, and returns the new recipe.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool. Expects 'recipe_data',
                      'ingredients_list', and 'user_id'.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the newly created recipe object.
        """
        # 1. Basic Validation
        param_definitions = {
            "recipe_data": {"type": dict, "required": True},
            "ingredients_list": {"type": list, "required": True},
            "user_id": {"type": int, "required": True}
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"],
                validation_error["details"]
            )

        # 2. Comprehensive Validation
        if not AddNewRecipeTool.EXPECTED_RECIPE_FIELDS.issubset(recipe_data.keys()):
            return _build_error_response("INVALID_PARAMETER_TYPE", {"param": "recipe_data", "expected_type": "object with all required recipe fields"})
        if not ingredients_list:
             return _build_error_response("INVALID_PARAMETER_TYPE", {"param": "ingredients_list", "expected_type": "non-empty list"})

        all_ingredient_ids = {i["ingredient_id"] for i in list(data.get("ingredients", {}).values())}
        for item in ingredients_list:
            if not isinstance(item, dict) or not all(k in item for k in ["ingredient_id", "quantity", "unit"]):
                return _build_error_response("INVALID_PARAMETER_TYPE", {"param": "ingredients_list", "expected_type": "list of valid ingredient objects"})
            if item["ingredient_id"] not in all_ingredient_ids:
                return _build_error_response("NOT_FOUND", {"entity": "Ingredient", "entity_id": item["ingredient_id"]})

        # 3. Generate Recipe Entry
        recipes_table = data.setdefault("recipes", [])
        max_recipe_id = max((r.get("recipe_id", 0) for r in recipes_table), default=400)
        new_recipe_id = max_recipe_id + 1

        new_recipe_record = {"recipe_id": new_recipe_id}
        new_recipe_record.update({key: recipe_data.get(key) for key in AddNewRecipeTool.EXPECTED_RECIPE_FIELDS})
        recipes_table.append(new_recipe_record)

        # 4. Establish Links Between Recipes and Ingredients
        ri_table = data.setdefault("recipe_ingredients", [])
        max_ri_id = max((ri.get("ri_id", 0) for ri in ri_table), default=5000)

        for ingredient in ingredients_list:
            max_ri_id += 1
            new_ri_record = {
                "ri_id": max_ri_id,
                "recipe_id": new_recipe_id,
                "ingredient_id": ingredient["ingredient_id"],
                "quantity": ingredient["quantity"],
                "unit": ingredient["unit"]
            }
            ri_table.append(new_ri_record)

        # 5. Review and verification
        user_household = next((h for h in data.get("households", []) if h.get("primary_user_id") == user_id), None)
        household_id = user_household.get("household_id") if user_household else None

        _log_audit_event(
            data=data,
            household_id=household_id,
            user_id=user_id,
            entity_type="recipes",
            entity_id=new_recipe_id,
            action_enum="create",
            payload_json={"recipe_data": recipe_data, "ingredients_list": ingredients_list}
        )

        # 6. Reply
        return _build_success_response(new_recipe_record)