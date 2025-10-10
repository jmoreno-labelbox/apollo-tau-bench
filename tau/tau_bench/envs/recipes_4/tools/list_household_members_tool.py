# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListHouseholdMembersTool(Tool):
    """
    A tool to list all members belonging to a specific household.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "list_household_members",
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
                            "description": "The unique identifier for the household."
                        },
                    },
                    "required": [],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> Dict[str, Any]:
        """
        Executes the tool's logic to fetch all members of a household.

        This method validates the input household_id, determines the target
        household if one is not provided, and then retrieves all member records
        associated with that household ID.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool. Expects an optional
                      'household_id'.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains a list of member objects. On failure,
            it contains a structured error object.
        """
        # 1. Verify Inputs
        param_definitions = {
            "household_id": {"type": int, "required": False}
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"],
                validation_error["details"]
            )

        household_id = kwargs.get("household_id")

        # 2. Business Logic: Identify target household if it hasn't been specified.
        if not household_id:
            users = list(data.get("users", {}).values())
            if not users:
                return _build_error_response("NO_DATA_FOUND", {"entity": "Users"})

            first_user = list(data.get("users", {}).values())[0] if data.get("users") else None
            if not first_user:
                return _build_error_response("NO_DATA_FOUND", {"entity": "Users"})

            first_user_id = first_user.get("user_id")
            household = next((h for h in data.get("households", []) if h.get("primary_user_id") == first_user_id), None)
            if not household:
                return _build_error_response("NOT_FOUND", {"entity": "Household", "entity_id": f"for user {first_user_id}"})
            household_id = household.get("household_id")

        # 3. Validation Step: Confirm the existence of the target household.
        target_household = next((h for h in data.get("households", []) if h.get("household_id") == household_id), None)
        if not target_household:
            return _build_error_response("NOT_FOUND", {"entity": "Household", "entity_id": household_id})

        # 4. Data Fetching: Select members based on the specified household_id.
        household_members = [
            m for m in data.get("members", []) if m.get("household_id") == household_id
        ]

        # 5. Provide a uniform success response.
        return _build_success_response(household_members)
