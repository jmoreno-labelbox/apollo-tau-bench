# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RemoveRecipeFromMealPlanTool(Tool):
    """
    A tool to remove a single recipe entry from a meal plan.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "remove_recipe_from_meal_plan",
                "description": "Removes a single recipe entry from a meal plan using its unique entry ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "entry_id": {
                            "type": "integer",
                            "description": "The unique ID for the meal plan entry to remove."
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user performing the action, for auditing."
                        }
                    },
                    "required": ["entry_id"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> Dict[str, Any]:
        """
        Executes the logic to find and remove a meal plan entry.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool. Expects 'entry_id'.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains a confirmation of the deletion.
        """
        # 1. Verify Input Data
        param_definitions = {
            "entry_id": {"type": int, "required": True},
            "user_id": {"type": int, "required": False},
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(validation_error["error_code"], validation_error["details"])

        entry_id = kwargs["entry_id"]
        user_id = kwargs.get("user_id")

        entries_table = data.get("meal_plan_entries", [])

        # 2. Locate the item to delete
        entry_to_remove = next((e for e in entries_table if e.get("entry_id") == entry_id), None)

        if not entry_to_remove:
            return _build_error_response("NOT_FOUND", {"entity": "MealPlanEntry", "entity_id": entry_id})

        # 3. Audit (required prior to data deletion)
        meal_plan = next((p for p in data.get("meal_plans", []) if p.get("meal_plan_id") == entry_to_remove["meal_plan_id"]), None)
        household_id = meal_plan.get("household_id") if meal_plan else None

        _log_audit_event(
            data=data,
            household_id=household_id,
            user_id=user_id,
            entity_type="meal_plan_entries",
            entity_id=entry_id,
            action_enum="delete",
            payload_json=entry_to_remove # Record the deleted data.
        )

        # 4. Execute the deletion.
        data["meal_plan_entries"] = [e for e in entries_table if e.get("entry_id") != entry_id]

        # 5. Reply
        return _build_success_response({
            "status": "success",
            "deleted_entry": entry_to_remove
        })
