from tau_bench.envs.tool import Tool
import collections
import json
from datetime import date, datetime, timedelta, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateMealPlanEntryTool(Tool):
    """
    A tool to update a single entry within an existing meal plan.
    """

    #Defines which fields of a meal plan entry are safely updatable.
    UPDATABLE_FIELDS = {"recipe_id", "servings_adult", "servings_child", "notes"}

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "UpdateMealPlanEntry",
                "description": "Updates a single entry within a meal plan. Allows changing the recipe, serving sizes, or notes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "entry_id": {
                            "type": "integer",
                            "description": "The unique ID for the meal plan entry to update.",
                        },
                        "updates": {
                            "type": "object",
                            "description": "A dictionary of fields and their new values to apply.",
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user performing the action, for auditing.",
                        },
                    },
                    "required": ["entry_id", "updates"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], entry_id: int, updates: dict, user_id: int = None) -> dict[str, Any]:
        """
        Executes the logic to find and modify a meal plan entry.

        Args:
            data: The main in-memory dictionary containing all datasets.
            entry_id: The ID of the meal plan entry to update.
            updates: A dictionary containing the fields to update.
            user_id: The ID of the user making the update, if applicable.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the updated meal plan entry object.
        """
        #1. Validate Inputs
        param_definitions = {
            "entry_id": {"type": int, "required": True},
            "updates": {"type": dict, "required": True},
            "user_id": {"type": int, "required": False},
        }
        validation_error = _validate_inputs({"entry_id": entry_id, "updates": updates, "user_id": user_id}, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Pre-condition Check: If updating recipe_id, ensure it exists
        if "recipe_id" in updates:
            new_recipe_id = updates["recipe_id"]
            if not any(
                r.get("recipe_id") == new_recipe_id for r in data.get("recipes", {}).values()
            ):
                return _build_error_response(
                    "NOT_FOUND", {"entity": "Recipe", "entity_id": new_recipe_id}
                )

        #3. Find and Update the Record
        entry_record = next(
            (
                e
                for e in data.get("meal_plan_entries", {}).values()
                if e.get("entry_id") == entry_id
            ),
            None,
        )

        if not entry_record:
            return _build_error_response(
                "NOT_FOUND", {"entity": "MealPlanEntry", "entity_id": entry_id}
            )

        for key, value in updates.items():
            if key in UpdateMealPlanEntryTool.UPDATABLE_FIELDS:
                entry_record[key] = value

        #4. Auditing
        meal_plan = next(
            (
                p
                for p in data.get("meal_plans", {}).values()
                if p.get("meal_plan_id") == entry_record["meal_plan_id"]
            ),
            None,
        )
        household_id = meal_plan.get("household_id") if meal_plan else None

        _log_audit_event(
            data=data,
            household_id=household_id,
            user_id=user_id,
            entity_type="meal_plan_entries",
            entity_id=entry_id,
            action_enum="update",
            payload_json=updates,
        )

        #5. Response
        return _build_success_response(entry_record)
