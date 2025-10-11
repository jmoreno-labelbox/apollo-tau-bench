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

class GetMealPlanForWeekTool(Tool):
    """
    A tool to retrieve the full details of a meal plan, including all its entries.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "get_meal_plan_for_week",
                "description": (
                    "Retrieves a full meal plan and its daily entries by its unique ID. "
                    "The entries are enriched with recipe titles for clarity."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_plan_id": {
                            "type": "integer",
                            "description": "The unique identifier for the meal plan to retrieve."
                        }
                    },
                    "required": ["meal_plan_id"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], meal_plan_id) -> Dict[str, Any]:
        """
        Executes the logic to fetch and enrich a full meal plan.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool. Expects 'meal_plan_id'.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the fully detailed and hydrated meal plan object.
        """
        # 1. Verify Input Values
        param_definitions = {
            "meal_plan_id": {"type": int, "required": True}
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(validation_error["error_code"], validation_error["details"])

        # 2. Data Acquisition: Locate the primary meal plan object
        meal_plan_record = next(
            (p for p in data.get("meal_plans", []) if p.get("meal_plan_id") == meal_plan_id),
            None
        )

        if not meal_plan_record:
            return _build_error_response("NOT_FOUND", {"entity": "MealPlan", "entity_id": meal_plan_id})

        # 3. Data Enrichment (Hydration): Retrieve and enhance plan records.
        plan_entries = [
            e for e in data.get("meal_plan_entries", []) if e.get("meal_plan_id") == meal_plan_id
        ]

        enriched_entries = []
        all_recipes = list(data.get("recipes", {}).values())
        for entry in plan_entries:
            recipe_info = next(
                (r for r in all_recipes if r.get("recipe_id") == entry.get("recipe_id")),
                None
            )
            enriched_entry = entry.copy()
            enriched_entry["recipe_title"] = recipe_info.get("recipe_title") if recipe_info else "Unknown Recipe"
            enriched_entries.append(enriched_entry)

        # Organize entries chronologically for better clarity.
        enriched_entries.sort(key=lambda x: x.get("plan_date", ""))

        # 4. Construct the final response object.
        detailed_plan = meal_plan_record.copy()
        detailed_plan["entries"] = enriched_entries

        # 5. Provide the uniform success response.
        return _build_success_response(detailed_plan)