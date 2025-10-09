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

class CreateMealPlanTool(Tool):
    """
    A tool to create a new, empty meal plan for a household for a specific week.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateMealPlan",
                "description": "Creates a new, empty meal plan for a household for a specific week, defined by its start date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {
                            "type": "integer",
                            "description": "The unique ID for the household.",
                        },
                        "week_start_date": {
                            "type": "string",
                            "description": "The start date of the meal plan week, in 'YYYY-MM-DD' format.",
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user creating the plan, for auditing.",
                        },
                    },
                    "required": ["household_id", "week_start_date", "user_id"],
                },
            },
        }

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        household_id: int, 
        week_start_date: str, 
        user_id: int
    ) -> dict[str, Any]:
        """
        Executes the logic to create a new meal plan record.

        Args:
            data: The main in-memory dictionary containing all datasets.
            household_id: The ID of the household for which the meal plan is created.
            week_start_date: The start date of the week for the meal plan.
            user_id: The ID of the user creating the meal plan.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the newly created meal plan object.
        """
        #1. Validate Inputs
        param_definitions = {
            "household_id": {"type": int, "required": True},
            "week_start_date": {"type": str, "required": True},
            "user_id": {"type": int, "required": True},
        }
        validation_error = _validate_inputs(
            {"household_id": household_id, "week_start_date": week_start_date, "user_id": user_id}, 
            param_definitions
        )
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Pre-condition Checks
        if not any(
            h.get("household_id") == household_id for h in data.get("households", {}).values()
        ):
            return _build_error_response(
                "NOT_FOUND", {"entity": "Household", "entity_id": household_id}
            )
        if not any(u.get("user_id") == user_id for u in data.get("users", {}).values():
            return _build_error_response(
                "NOT_FOUND", {"entity": "User", "entity_id": user_id}
            )

        #Business Rule: Prevent duplicate plans for the same week
        existing_plan = any(
            p
            for p in data.get("meal_plans", {}).values()
            if p.get("household_id") == household_id
            and p.get("week_start_date") == week_start_date
        )
        if existing_plan:
            return _build_error_response(
                "ALREADY_EXISTS",
                {
                    "entity": "MealPlan",
                    "entity_id": f"for household {household_id} on {week_start_date}",
                },
            )

        #3. Data Creation Logic
        meal_plans_table = data.setdefault("meal_plans", [])

        #Generate a new unique ID
        max_id = max(
            (p.get("meal_plan_id", 0) for p in meal_plans_table.values()),
            default=DEFAULT_BUSINESS_RULES["INITIAL_ID_DEFAULTS"]["meal_plans"],
        )
        new_plan_id = max_id + 1

        timestamp = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

        new_plan_record = {
            "meal_plan_id": new_plan_id,
            "household_id": household_id,
            "week_start_date": week_start_date,
            "created_by_user_id": user_id,
            "created_at": timestamp,
        }

        data["meal_plans"][new_plan_record["meal_plan_id"]] = new_plan_record

        #4. Auditing
        _log_audit_event(
            data=data,
            household_id=household_id,
            user_id=user_id,
            entity_type="meal_plans",
            entity_id=new_plan_id,
            action_enum="create",
            payload_json={"week_start_date": week_start_date},
        )

        #5. Response
        return _build_success_response(new_plan_record)
