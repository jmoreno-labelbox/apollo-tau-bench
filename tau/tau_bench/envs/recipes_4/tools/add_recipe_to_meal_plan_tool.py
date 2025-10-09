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

class AddRecipeToMealPlanTool(Tool):
    """
    A tool to add a single recipe entry to an existing meal plan.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "AddRecipeToMealPlan",
                "description": "Adds a single recipe to an existing meal plan for a specific date and meal type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_plan_id": {
                            "type": "integer",
                            "description": "The unique ID for the meal plan to be modified.",
                        },
                        "recipe_id": {
                            "type": "integer",
                            "description": "The unique ID of the recipe to add.",
                        },
                        "plan_date": {
                            "type": "string",
                            "description": "The date for the meal entry, in 'YYYY-MM-DD' format.",
                        },
                        "meal_type": {
                            "type": "string",
                            "description": "The type of meal (e.g., 'Breakfast', 'Lunch', 'Dinner'). Defaults to 'Dinner'.",
                        },
                        "servings_adult": {
                            "type": "integer",
                            "description": "Number of adult servings. Defaults to 2.",
                        },
                        "servings_child": {
                            "type": "integer",
                            "description": "Number of child servings. Defaults to 0.",
                        },
                        "notes": {
                            "type": "string",
                            "description": "Optional notes for the meal entry.",
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user performing the action, for auditing.",
                        },
                    },
                    "required": ["meal_plan_id", "recipe_id", "plan_date"],
                },
            },
        }

    @staticmethod
    def invoke(
        data: dict[str, Any],
        meal_plan_id: int,
        recipe_id: int,
        plan_date: str,
        meal_type: str = "Dinner",
        servings_adult: int = 2,
        servings_child: int = 0,
        notes: str = "",
        user_id: int = None
    ) -> dict[str, Any]:
        """
        Executes the logic to create a new meal plan entry.

        Args:
            data: The main in-memory dictionary containing all datasets.
            meal_plan_id: The ID of the meal plan.
            recipe_id: The ID of the recipe.
            plan_date: The date for the meal plan entry.
            meal_type: The type of meal (e.g., Breakfast, Lunch, Dinner).
            servings_adult: Number of adult servings.
            servings_child: Number of child servings.
            notes: Additional notes for the meal plan entry.
            user_id: The ID of the user.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the newly created meal plan entry object.
        """
        #1. Validate Inputs
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
        validation_error = _validate_inputs(locals(), param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Pre-condition Checks
        meal_plan_record = next(
            (
                p
                for p in data.get("meal_plans", {}).values()
                if p.get("meal_plan_id") == meal_plan_id
            ),
            None,
        )
        if not meal_plan_record:
            return _build_error_response(
                "NOT_FOUND", {"entity": "MealPlan", "entity_id": meal_plan_id}
            )
        if not any(r.get("recipe_id") == recipe_id for r in data.get("recipes", {}).values()):
            return _build_error_response(
                "NOT_FOUND", {"entity": "Recipe", "entity_id": recipe_id}
            )

        #Business Rule: Ensure date is within the plan's week
        try:
            plan_start_date = date.fromisoformat(meal_plan_record["week_start_date"])
            entry_date = date.fromisoformat(plan_date)
        except ValueError:
            return _build_error_response(
                "INVALID_PARAMETER_TYPE",
                {"param": "plan_date", "expected_type": "string in YYYY-MM-DD format"},
            )

        plan_end_date = plan_start_date + timedelta(days=6)
        if not (plan_start_date <= entry_date <= plan_end_date):
            return _build_error_response(
                "UNSUPPORTED_OPERATION",
                {
                    "operation": "Add Entry",
                    "entity": f"Date {plan_date} is outside the week of MealPlan {meal_plan_id}",
                },
            )

        #Business Rule: Prevent duplicate entries
        if any(
            e
            for e in data.get("meal_plan_entries", {}).values()
            if e.get("meal_plan_id") == meal_plan_id
            and e.get("plan_date") == plan_date
            and e.get("meal_type") == meal_type
        ):
            return _build_error_response(
                "ALREADY_EXISTS",
                {
                    "entity": "MealPlanEntry",
                    "entity_id": f"for {plan_date} {meal_type}",
                },
            )

        #3. Data Creation
        entries_table = data.setdefault("meal_plan_entries", [])
        max_id = max(
            (e.get("entry_id", 0) for e in entries_table.values()),
            default=DEFAULT_BUSINESS_RULES["INITIAL_ID_DEFAULTS"]["meal_plan_entries"],
        )
        new_entry_id = max_id + 1

        new_entry_record = {
            "entry_id": new_entry_id,
            "meal_plan_id": meal_plan_id,
            "plan_date": plan_date,
            "meal_type": meal_type,
            "recipe_id": recipe_id,
            "servings_adult": servings_adult,
            "servings_child": servings_child,
            "notes": notes,
        }
        entries_table.append(new_entry_record)

        #4. Auditing
        _log_audit_event(
            data=data,
            household_id=meal_plan_record.get("household_id"),
            user_id=user_id,
            entity_type="meal_plan_entries",
            entity_id=new_entry_id,
            action_enum="create",
            payload_json={"recipe_id": recipe_id, "plan_date": plan_date},
        )

        #5. Response
        return _build_success_response(new_entry_record)
