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

class GetMemberDetailsTool(Tool):
    """
    A tool to retrieve the detailed profile of a single household member.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetMemberDetails",
                "description": "Retrieves the full profile for a single member by their unique ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "member_id": {
                            "type": "integer",
                            "description": "The unique identifier for the member.",
                        },
                    },
                    "required": ["member_id"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], member_id: int) -> dict[str, Any]:
        """
        Executes the tool's logic to fetch a specific member's profile.

        This method validates that a member_id is provided and is of the correct
        type. It then searches the dataset for the corresponding member and
        returns their complete profile.

        Args:
            data: The main in-memory dictionary containing all datasets.
            member_id: The ID of the member to fetch.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the member object. On failure, it
            contains a structured error object.
        """
        pass
        #1. Validate Inputs: 'member_id' is mandatory for this tool.
        param_definitions = {"member_id": {"type": int, "required": True}}
        validation_error = _validate_inputs({"member_id": member_id}, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Data Retrieval: Find the specific member in the dataset.
        member_profile = next(
            (m for m in data.get("members", {}).values() if m.get("member_id") == member_id),
            None,
        )

        #3. Handle cases where the member is not found
        if not member_profile:
            return _build_error_response(
                "NOT_FOUND", details={"entity": "Member", "entity_id": member_id}
            )

        #4. Return a standardized success response
        return _build_success_response(member_profile)
