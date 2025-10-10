# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateMealPlanTool(Tool):
    """
    A tool to create a new, empty meal plan for a household for a specific week.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "create_meal_plan",
                "description": "Creates a new, empty meal plan for a household for a specific week, defined by its start date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {
                            "type": "integer",
                            "description": "The unique ID for the household."
                        },
                        "week_start_date": {
                            "type": "string",
                            "description": "The start date of the meal plan week, in 'YYYY-MM-DD' format."
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user creating the plan, for auditing."
                        }
                    },
                    "required": ["household_id", "week_start_date", "user_id"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> Dict[str, Any]:
        """
        Executes the logic to create a new meal plan record.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the newly created meal plan object.
        """
        # 1. Check Input Validity
        param_definitions = {
            "household_id": {"type": int, "required": True},
            "week_start_date": {"type": str, "required": True},
            "user_id": {"type": int, "required": True}
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"],
                validation_error["details"]
            )

        household_id = kwargs["household_id"]
        week_start_date = kwargs["week_start_date"]
        user_id = kwargs["user_id"]

        # 2. Validation of Preconditions
        if not any(h.get("household_id") == household_id for h in data.get("households", [])):
            return _build_error_response("NOT_FOUND", {"entity": "Household", "entity_id": household_id})
        if not any(u.get("user_id") == user_id for u in list(data.get("users", {}).values())):
            return _build_error_response("NOT_FOUND", {"entity": "User", "entity_id": user_id})

        # Business Rule: Disallow duplicate plans within the same week.
        existing_plan = any(
            p for p in data.get("meal_plans", [])
            if p.get("household_id") == household_id and p.get("week_start_date") == week_start_date
        )
        if existing_plan:
            return _build_error_response("ALREADY_EXISTS", {"entity": "MealPlan", "entity_id": f"for household {household_id} on {week_start_date}"})

        # 3. Logic for Data Generation
        meal_plans_table = data.setdefault("meal_plans", [])

        # Create a new distinct identifier.
        max_id = max((p.get("meal_plan_id", 0) for p in meal_plans_table), default=DEFAULT_BUSINESS_RULES["INITIAL_ID_DEFAULTS"]["meal_plans"])
        new_plan_id = max_id + 1

        timestamp = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')

        new_plan_record = {
            "meal_plan_id": new_plan_id,
            "household_id": household_id,
            "week_start_date": week_start_date,
            "created_by_user_id": user_id,
            "created_at": timestamp
        }

        meal_plans_table.append(new_plan_record)

        # 4. Review and verification
        _log_audit_event(
            data=data,
            household_id=household_id,
            user_id=user_id,
            entity_type="meal_plans",
            entity_id=new_plan_id,
            action_enum="create",
            payload_json={"week_start_date": week_start_date}
        )

        # 5. Reply
        return _build_success_response(new_plan_record)
