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

class UpdateMemberPreferencesTool(Tool):
    """
    A tool to update the preferences and data for a specific household member.
    """

    #Defines which fields are safely updatable by an agent.
    #Prevents modification of critical IDs or structural fields.
    UPDATABLE_FIELDS = {
        "full_name",
        "activity_level",
        "dietary_notes",
        "allergies_json",
        "target_calories",
        "target_protein",
    }

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "UpdateMemberPreferences",
                "description": (
                    "Updates profile data for a specific member. The 'updates' "
                    "parameter must be a dictionary containing the fields to change."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "member_id": {
                            "type": "integer",
                            "description": "The unique identifier for the member to update.",
                        },
                        "updates": {
                            "type": "object",
                            "description": "A dictionary of fields and their new values.",
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user performing the action, for auditing.",
                        },
                    },
                    "required": ["member_id", "updates"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], member_id: int, updates: dict, user_id: int = None) -> dict[str, Any]:
        """
        Executes the logic to find and modify a member's data.

        This method validates inputs, finds the target member, applies the
        changes for a whitelisted set of fields, logs the action to the audit
        trail, and returns the updated member profile.

        Args:
            data: The main in-memory dictionary containing all datasets.
            member_id: The ID of the member to update.
            updates: A dictionary of updates to apply to the member.
            user_id: An optional ID of the user performing the update, used for logging.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the full, updated member object.
        """
        #1. Validate Inputs
        param_definitions = {
            "member_id": {"type": int, "required": True},
            "updates": {"type": dict, "required": True},
            "user_id": {"type": int, "required": False},
        }
        validation_error = _validate_inputs({"member_id": member_id, "updates": updates, "user_id": user_id}, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Find the member record
        member_record = next(
            (m for m in data.get("members", []) if m.get("member_id") == member_id),
            None,
        )

        if not member_record:
            return _build_error_response(
                "NOT_FOUND", {"entity": "Member", "entity_id": member_id}
            )

        #3. Apply updates safely
        for key, value in updates.items():
            if key in UpdateMemberPreferencesTool.UPDATABLE_FIELDS:
                member_record[key] = value

        #4. Log the audit event for traceability
        _log_audit_event(
            data=data,
            household_id=member_record.get("household_id"),
            user_id=user_id,  #Can be None if not provided
            entity_type="members",
            entity_id=member_id,
            action_enum="update",
            payload_json=updates,
        )

        #5. Return the updated object to confirm the change
        return _build_success_response(member_record)
