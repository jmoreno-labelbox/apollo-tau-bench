# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetMealHistoryTool(Tool):
    """
    A tool to retrieve the meal history for a household.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "get_meal_history",
                "description": "Retrieves the meal history for a household, optionally filtered by the number of days back.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {
                            "type": "integer",
                            "description": "The unique identifier for the household."
                        },
                        "days_back": {
                            "type": "integer",
                            "description": "Optional. The number of days of history to retrieve from today."
                        }
                    },
                    "required": ["household_id"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], days_back, household_id) -> Dict[str, Any]:
        """
        Executes the logic to find and return a household's meal history.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool. Expects 'household_id'
                      and an optional 'days_back'.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains a list of meal history objects, sorted
            by date descending.
        """
        # 1. Verify Input Data
        param_definitions = {
            "household_id": {"type": int, "required": True},
            "days_back": {"type": int, "required": False}
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"],
                validation_error["details"]
            )

        # 2. Preconditions Validation: Verify the existence of the household.
        if not any(h for h in data.get("households", []) if h.get("household_id") == household_id):
            return _build_error_response("NOT_FOUND", {"entity": "Household", "entity_id": household_id})

        # 3. Data Acquisition & Selection
        all_history = data.get("meal_history", [])
        household_history = [h for h in all_history if h.get("household_id") == household_id]

        if days_back is not None:
            # The current date is supplied in the context to ensure consistency.
            today = date(2025, 9, 1)
            start_date = today - timedelta(days=days_back)

            # Restrict by date interval
            household_history = [
                h for h in household_history
                if date.fromisoformat(h.get("plan_date", "1900-01-01")) >= start_date
            ]

        # 4. Arrange results from newest to oldest.
        household_history.sort(key=lambda x: x.get("plan_date", ""), reverse=True)

        # 5. Provide a consistent success response.
        return _build_success_response(household_history)
