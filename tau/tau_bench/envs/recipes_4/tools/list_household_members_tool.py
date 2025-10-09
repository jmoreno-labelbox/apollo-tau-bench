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

class ListHouseholdMembersTool(Tool):
    """
    A tool to list all members belonging to a specific household.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListHouseholdMembers",
                "description": (
                    "Lists all members for a given household ID. If the ID is "
                    "omitted, it defaults to the primary household of the "
                    "first user in the dataset."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {
                            "type": "integer",
                            "description": "The unique identifier for the household.",
                        },
                    },
                    "required": [],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], household_id: int = None) -> dict[str, Any]:
        """
        Executes the tool's logic to fetch all members of a household.

        This method validates the input household_id, determines the target
        household if one is not provided, and then retrieves all member records
        associated with that household ID.

        Args:
            data: The main in-memory dictionary containing all datasets.
            household_id: An optional household ID to specify the target household.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains a list of member objects. On failure,
            it contains a structured error object.
        """
        pass
        #1. Validate Inputs
        param_definitions = {"household_id": {"type": int, "required": False}}
        validation_error = _validate_inputs({"household_id": household_id}, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Business Logic: Determine target household if not provided
        if not household_id:
            users = data.get("users", [])
            if not users:
                return _build_error_response("NO_DATA_FOUND", {"entity": "Users"})

            first_user = data.get("users", [])[0] if data.get("users") else None
            if not first_user:
                return _build_error_response("NO_DATA_FOUND", {"entity": "Users"})

            first_user_id = first_user.get("user_id")
            household = next(
                (
                    h
                    for h in data.get("households", [])
                    if h.get("primary_user_id") == first_user_id
                ),
                None,
            )
            if not household:
                return _build_error_response(
                    "NOT_FOUND",
                    {"entity": "Household", "entity_id": f"for user {first_user_id}"},
                )
            household_id = household.get("household_id")

        #3. Defensive Check: Ensure the target household exists
        target_household = next(
            (
                h
                for h in data.get("households", [])
                if h.get("household_id") == household_id
            ),
            None,
        )
        if not target_household:
            return _build_error_response(
                "NOT_FOUND", {"entity": "Household", "entity_id": household_id}
            )

        #4. Data Retrieval: Filter members by the determined household_id
        household_members = [
            m for m in data.get("members", []) if m.get("household_id") == household_id
        ]

        #5. Return a standardized success response
        return _build_success_response(household_members)
