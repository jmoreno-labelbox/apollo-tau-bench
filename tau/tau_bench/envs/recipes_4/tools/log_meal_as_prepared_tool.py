from tau_bench.envs.tool import Tool
import collections
import json
from datetime import date, datetime, timedelta, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class LogMealAsPreparedTool(Tool):
    """
    A tool to log that a recipe was prepared, adding an entry to the meal history.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "LogMealAsPrepared",
                "description": "Logs that a recipe was prepared for a household on a specific date. Optionally includes a user rating.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {
                            "type": "integer",
                            "description": "The unique ID for the household.",
                        },
                        "recipe_id": {
                            "type": "integer",
                            "description": "The unique ID of the recipe that was prepared.",
                        },
                        "plan_date": {
                            "type": "string",
                            "description": "The date the meal was prepared, in 'YYYY-MM-DD' format.",
                        },
                        "rating_int": {
                            "type": "integer",
                            "description": "An optional integer rating for the meal (e.g., 1-5).",
                        },
                        "was_prepared": {
                            "type": "boolean",
                            "description": "Indicates if the meal was actually prepared. Defaults to True.",
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user performing the action, for auditing.",
                        },
                    },
                    "required": ["household_id", "recipe_id", "plan_date"],
                },
            },
        }

    @staticmethod
    def invoke(
        data: dict[str, Any],
        household_id: int,
        recipe_id: int,
        plan_date: str,
        rating_int: int = None,
        was_prepared: bool = True,
        user_id: int = None, notes: Any = None) -> dict[str, Any]:
        """
        Executes the logic to create a new meal history entry.

        Args:
            data: The main in-memory dictionary containing all datasets.
            household_id: The ID of the household.
            recipe_id: The ID of the recipe.
            plan_date: The date the meal is planned.
            rating_int: The rating of the meal.
            was_prepared: Whether the meal was prepared.
            user_id: The ID of the user.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the newly created meal history object.
        """
        #1. Validate Inputs
        param_definitions = {
            "household_id": {"type": int, "required": True},
            "recipe_id": {"type": int, "required": True},
            "plan_date": {"type": str, "required": True},
            "rating_int": {"type": int, "required": False},
            "was_prepared": {"type": bool, "required": False},
            "user_id": {"type": int, "required": False},
        }
        validation_error = _validate_inputs(locals(), param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Pre-condition Checks: Ensure related entities exist
        if not any(
            h.get("household_id") == household_id for h in data.get("households", [])
        ):
            return _build_error_response(
                "NOT_FOUND", {"entity": "Household", "entity_id": household_id}
            )
        if not any(r.get("recipe_id") == recipe_id for r in data.get("recipes", [])):
            return _build_error_response(
                "NOT_FOUND", {"entity": "Recipe", "entity_id": recipe_id}
            )

        #3. Data Creation Logic
        history_table = data.setdefault("meal_history", [])

        #Generate a new unique ID
        max_id = max((h.get("history_id", 0) for h in history_table), default=6000)
        new_history_id = max_id + 1

        #Build the new record
        new_history_record = {
            "history_id": new_history_id,
            "household_id": household_id,
            "recipe_id": recipe_id,
            "plan_date": plan_date,
            "was_prepared": was_prepared,
            "rating_int": rating_int,  #Defaults to None if not present
        }

        history_table.append(new_history_record)

        #4. Auditing
        _log_audit_event(
            data=data,
            household_id=household_id,
            user_id=user_id,
            entity_type="meal_history",
            entity_id=new_history_id,
            action_enum="create",
            payload_json={"recipe_id": recipe_id, "plan_date": plan_date},
        )

        #5. Response
        return _build_success_response(new_history_record)
