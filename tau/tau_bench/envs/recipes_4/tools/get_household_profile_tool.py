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

class GetHouseholdProfileTool(Tool):
    """
    A tool to retrieve a comprehensive profile of a household, including its members.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetHouseholdProfile",
                "description": (
                    "Retrieves a full household profile, including its list of members, "
                    "by its ID. If no ID is provided, it defaults to the primary "
                    "household of the first user in the dataset."
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
        Executes the tool's logic to fetch household and member data.

        This method validates inputs, finds the target household (either directly
        or via a default), retrieves the household's data, enriches it with
        member information, and returns a standardized response.

        Args:
            data: The main in-memory dictionary containing all datasets.
            household_id: An optional household ID to specify the target household.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the hydrated household profile. On failure,
            it contains a structured error object.
        """
        #1. Validate Inputs using our helper
        param_definitions = {"household_id": {"type": int, "required": False}}
        validation_error = _validate_inputs({"household_id": household_id}, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Business Logic: Determine target household if not provided
        if not household_id:
            first_user = data.get("users", {}).values()[0] if data.get("users") else None
            if not first_user:
                return _build_error_response("NO_DATA_FOUND", {"entity": "Users"})

            first_user_id = first_user.get("user_id")
            household = next(
                (
                    h
                    for h in data.get("households", {}).values()
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

        #3. Data Retrieval
        target_household = next(
            (
                h
                for h in data.get("households", {}).values()
                if h.get("household_id") == household_id
            ),
            None,
        )

        if not target_household:
            return _build_error_response(
                "NOT_FOUND", {"entity": "Household", "entity_id": household_id}
            )

        #4. Data Enrichment (Hydration): Fetch associated members
        household_members = [
            m for m in data.get("members", {}).values() if m.get("household_id") == household_id
        ]

        #5. Build the final profile object
        profile_data = {
            "household_info": target_household,
            "members": household_members,
        }

        #6. Return a standardized success response
        return _build_success_response(profile_data)
