# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetMemberDetailsTool(Tool):
    """
    A tool to retrieve the detailed profile of a single household member.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "get_member_details",
                "description": "Retrieves the full profile for a single member by their unique ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "member_id": {
                            "type": "integer",
                            "description": "The unique identifier for the member."
                        },
                    },
                    "required": ["member_id"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], member_id) -> Dict[str, Any]:
        """
        Executes the tool's logic to fetch a specific member's profile.

        This method validates that a member_id is provided and is of the correct
        type. It then searches the dataset for the corresponding member and
        returns their complete profile.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool. Expects a required
                      'member_id'.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the member object. On failure, it
            contains a structured error object.
        """
        # 1. Input Validation: The 'member_id' is required for this tool.
        param_definitions = {
            "member_id": {"type": int, "required": True}
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"],
                validation_error["details"]
            )

        # 2. Data Acquisition: Locate the particular member within the dataset.
        member_profile = next(
            (m for m in data.get("members", []) if m.get("member_id") == member_id),
            None
        )

        # 3. Manage scenarios when the member cannot be located.
        if not member_profile:
            return _build_error_response(
                "NOT_FOUND",
                details={"entity": "Member", "entity_id": member_id}
            )

        # 4. Provide a uniform success response.
        return _build_success_response(member_profile)
