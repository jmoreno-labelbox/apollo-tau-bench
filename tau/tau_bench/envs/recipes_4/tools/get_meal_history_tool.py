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

class GetMealHistoryTool(Tool):
    """
    A tool to retrieve the meal history for a household.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetMealHistory",
                "description": "Retrieves the meal history for a household, optionally filtered by the number of days back.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {
                            "type": "integer",
                            "description": "The unique identifier for the household.",
                        },
                        "days_back": {
                            "type": "integer",
                            "description": "Optional. The number of days of history to retrieve from today.",
                        },
                    },
                    "required": ["household_id"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], household_id: int, days_back: int = None) -> dict[str, Any]:
        """
        Executes the logic to find and return a household's meal history.

        Args:
            data: The main in-memory dictionary containing all datasets.
            household_id: The ID of the household to retrieve meal history for.
            days_back: Optional number of days back to filter the meal history.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains a list of meal history objects, sorted
            by date descending.
        """
        #1. Validate Inputs
        param_definitions = {
            "household_id": {"type": int, "required": True},
            "days_back": {"type": int, "required": False},
        }
        validation_error = _validate_inputs({"household_id": household_id, "days_back": days_back}, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Pre-condition Check: Ensure the household exists
        if not any(
            h
            for h in data.get("households", [])
            if h.get("household_id") == household_id
        ):
            return _build_error_response(
                "NOT_FOUND", {"entity": "Household", "entity_id": household_id}
            )

        #3. Data Retrieval & Filtering
        all_history = data.get("meal_history", [])
        household_history = [
            h for h in all_history if h.get("household_id") == household_id
        ]

        if days_back is not None:
            #Current date is provided in context for determinism
            today = date(2025, 9, 1)
            start_date = today - timedelta(days=days_back)

            #Filter by date range
            household_history = [
                h
                for h in household_history
                if date.fromisoformat(h.get("plan_date", "1900-01-01")) >= start_date
            ]

        #4. Sort results from most recent to oldest
        household_history.sort(key=lambda x: x.get("plan_date", ""), reverse=True)

        #5. Return a standardized success response
        return _build_success_response(household_history)
