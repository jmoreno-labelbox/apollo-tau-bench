# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddHouseholdMemberTool(Tool):
    """
    A tool to add a new member to a specified household.
    """

    # Defines the set of expected and allowed fields for a new member.
    EXPECTED_FIELDS = {
        "full_name",
        "birthdate",
        "is_child",
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
                "name": "add_household_member",
                "description": (
                    "Adds a new member to a specified household. The 'new_member_data' "
                    "parameter must be a dictionary with the new member's details."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {
                            "type": "integer",
                            "description": "The ID of the household to add the member to."
                        },
                        "new_member_data": {
                            "type": "object",
                            "description": "A dictionary with the new member's profile data."
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user performing the action, for auditing."
                        }
                    },
                    "required": ["household_id", "new_member_data"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> Dict[str, Any]:
        """
        Executes the logic to create and add a new member to the dataset.

        This method validates all required inputs, ensures the target household
        exists, generates a new unique member_id, constructs the new member
        record, appends it to the dataset, and logs the creation event.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool. Expects 'household_id'
                      and 'new_member_data'. An optional 'user_id' is for logging.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the newly created member object.
        """
        # 1. Validate Inputs
        param_definitions = {
            "household_id": {"type": int, "required": True},
            "new_member_data": {"type": dict, "required": True},
            "user_id": {"type": int, "required": False}
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"],
                validation_error["details"]
            )

        household_id = kwargs["household_id"]
        new_member_data = kwargs["new_member_data"]
        user_id = kwargs.get("user_id")

        # 2. Pre-condition Check: Ensure the household exists before adding to it.
        if not any(h for h in data.get("households", []) if h.get("household_id") == household_id):
            return _build_error_response("NOT_FOUND", {"entity": "Household", "entity_id": household_id})

        # 3. Data Creation Logic
        members_table = data.setdefault("members", [])

        # Generate a new unique ID
        max_id = max((m.get("member_id", 0) for m in members_table), default=300)
        new_member_id = max_id + 1

        # Construct the new member record safely
        new_member_record = {
            "member_id": new_member_id,
            "household_id": household_id,
        }
        for field in AddHouseholdMemberTool.EXPECTED_FIELDS:
            new_member_record[field] = new_member_data.get(field)

        members_table.append(new_member_record)

        # 4. Log the audit event for traceability
        _log_audit_event(
            data=data,
            household_id=household_id,
            user_id=user_id,
            entity_type="members",
            entity_id=new_member_id,
            action_enum="create",
            payload_json=new_member_data
        )

        # 5. Return the newly created object
        return _build_success_response(new_member_record)
