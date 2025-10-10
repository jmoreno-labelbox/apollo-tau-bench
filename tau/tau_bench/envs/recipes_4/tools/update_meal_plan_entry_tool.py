# Copyright belongs to Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateMealPlanEntryTool(Tool):
    """
    A tool to update a single entry within an existing meal plan.
    """

    # Specifies the fields in a meal plan entry that can be updated without issues.
    UPDATABLE_FIELDS = {
        "recipe_id",
        "servings_adult",
        "servings_child",
        "notes"
    }

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "update_meal_plan_entry",
                "description": "Updates a single entry within a meal plan. Allows changing the recipe, serving sizes, or notes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "entry_id": {
                            "type": "integer",
                            "description": "The unique ID for the meal plan entry to update."
                        },
                        "updates": {
                            "type": "object",
                            "description": "A dictionary of fields and their new values to apply."
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user performing the action, for auditing."
                        }
                    },
                    "required": ["entry_id", "updates"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], entry_id, updates, user_id) -> Dict[str, Any]:
        """
        Executes the logic to find and modify a meal plan entry.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the updated meal plan entry object.
        """
        # 1. Verify Input Values
        param_definitions = {
            "entry_id": {"type": int, "required": True},
            "updates": {"type": dict, "required": True},
            "user_id": {"type": int, "required": False},
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(validation_error["error_code"], validation_error["details"])

        # 2. Pre-condition Verification: Confirm the existence of recipe_id before updating.
        if "recipe_id" in updates:
            new_recipe_id = updates["recipe_id"]
            if not any(r.get("recipe_id") == new_recipe_id for r in list(data.get("recipes", {}).values())):
                return _build_error_response("NOT_FOUND", {"entity": "Recipe", "entity_id": new_recipe_id})

        # 3. Locate and Modify the Entry
        entry_record = next((e for e in data.get("meal_plan_entries", []) if e.get("entry_id") == entry_id), None)

        if not entry_record:
            return _build_error_response("NOT_FOUND", {"entity": "MealPlanEntry", "entity_id": entry_id})

        for key, value in updates.items():
            if key in UpdateMealPlanEntryTool.UPDATABLE_FIELDS:
                entry_record[key] = value

        # 4. Review and verification
        meal_plan = next((p for p in data.get("meal_plans", []) if p.get("meal_plan_id") == entry_record["meal_plan_id"]), None)
        household_id = meal_plan.get("household_id") if meal_plan else None

        _log_audit_event(
            data=data,
            household_id=household_id,
            user_id=user_id,
            entity_type="meal_plan_entries",
            entity_id=entry_id,
            action_enum="update",
            payload_json=updates
        )

        # 5. Reply
        return _build_success_response(entry_record)
