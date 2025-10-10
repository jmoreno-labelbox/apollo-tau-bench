# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateMemberPreferencesTool(Tool):
    """
    A tool to update the preferences and data for a specific household member.
    """

    # Defines which fields are safely updatable by an agent.
    # Prevents modification of critical IDs or structural fields.
    UPDATABLE_FIELDS = {
        "full_name",
        "activity_level",
        "dietary_notes",
        "allergies_json",
        "target_calories",
        "target_protein",
    }

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "update_member_preferences",
                "description": (
                    "Updates profile data for a specific member. The 'updates' "
                    "parameter must be a dictionary containing the fields to change."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "member_id": {
                            "type": "integer",
                            "description": "The unique identifier for the member to update."
                        },
                        "updates": {
                            "type": "object",
                            "description": "A dictionary of fields and their new values."
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user performing the action, for auditing."
                        }
                    },
                    "required": ["member_id", "updates"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> Dict[str, Any]:
        """
        Executes the logic to find and modify a member's data.

        This method validates inputs, finds the target member, applies the
        changes for a whitelisted set of fields, logs the action to the audit
        trail, and returns the updated member profile.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool. Expects 'member_id'
                      and 'updates'. An optional 'user_id' is used for logging.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the full, updated member object.
        """
        # 1. Validate Inputs
        param_definitions = {
            "member_id": {"type": int, "required": True},
            "updates": {"type": dict, "required": True},
            "user_id": {"type": int, "required": False}
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"],
                validation_error["details"]
            )

        member_id = kwargs["member_id"]
        updates = kwargs["updates"]
        user_id = kwargs.get("user_id") # For logging

        # 2. Find the member record
        member_record = next(
            (m for m in data.get("members", []) if m.get("member_id") == member_id),
            None
        )

        if not member_record:
            return _build_error_response("NOT_FOUND", {"entity": "Member", "entity_id": member_id})

        # 3. Apply updates safely
        for key, value in updates.items():
            if key in UpdateMemberPreferencesTool.UPDATABLE_FIELDS:
                member_record[key] = value

        # 4. Log the audit event for traceability
        _log_audit_event(
            data=data,
            household_id=member_record.get("household_id"),
            user_id=user_id, # Can be None if not provided
            entity_type="members",
            entity_id=member_id,
            action_enum="update",
            payload_json=updates
        )

        # 5. Return the updated object to confirm the change
        return _build_success_response(member_record)
