# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetHouseholdProfileTool(Tool):
    """
    A tool to retrieve a comprehensive profile of a household, including its members.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "get_household_profile",
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
                            "description": "The unique identifier for the household."
                        },
                    },
                    "required": [],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], household_id) -> Dict[str, Any]:
        """
        Executes the tool's logic to fetch household and member data.

        This method validates inputs, finds the target household (either directly
        or via a default), retrieves the household's data, enriches it with
        member information, and returns a standardized response.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool. Expects an optional
                      'household_id'.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the hydrated household profile. On failure,
            it contains a structured error object.
        """
        # 1. Use our helper to verify inputs.
        param_definitions = {
            "household_id": {"type": int, "required": False}
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"],
                validation_error["details"]
            )

        # 2. Business Logic: Identify target household if it's not specified.
        if not household_id:
            first_user = list(data.get("users", {}).values())[0] if data.get("users") else None
            if not first_user:
                return _build_error_response("NO_DATA_FOUND", {"entity": "Users"})

            first_user_id = first_user.get("user_id")
            household = next((h for h in data.get("households", []) if h.get("primary_user_id") == first_user_id), None)
            if not household:
                return _build_error_response("NOT_FOUND", {"entity": "Household", "entity_id": f"for user {first_user_id}"})
            household_id = household.get("household_id")

        # 3. Data Extraction
        target_household = next((h for h in data.get("households", []) if h.get("household_id") == household_id), None)

        if not target_household:
            return _build_error_response("NOT_FOUND", {"entity": "Household", "entity_id": household_id})

        # 4. Data Enrichment (Hydration): Retrieve related members
        household_members = [
            m for m in data.get("members", []) if m.get("household_id") == household_id
        ]

        # 5. Construct the final profile object.
        profile_data = {
            "household_info": target_household,
            "members": household_members
        }

        # 6. Generate a uniform success reply.
        return _build_success_response(profile_data)
