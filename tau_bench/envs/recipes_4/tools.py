"""
Recipe and Shopping List Agent Tools.

This module provides a comprehensive set of tools for an AI agent to manage
meal planning, grocery lists, inventory, and ordering within a simulated
household environment. The tools are designed to be deterministic, robust,
and adhere to a standardized response format to facilitate LLM training.

The file is structured as follows:
1.  Configuration: Centralized dictionaries for business rules and error messages.
2.  Core Helpers: Helper classes and functions for building responses, validation,
    normalization, and auditing.
3.  API Tool Classes: The implementation of the 28 tools available to the agent.
4.  Tool Manifest: A final list aggregating all tool instances for the framework.
"""

import collections
import json
from datetime import date, datetime, timedelta, timezone
from typing import Any

from tau_bench.envs.tool import Tool

#==============================================================================
#1. Configuration (Business Rules & Error Messages)
#==============================================================================

DEFAULT_BUSINESS_RULES = {
    #Meal Planning
    "MEAL_HISTORY_REPEAT_WINDOW_DAYS": 14,
    "RECENT_MEAL_EXCLUSION_WINDOW_DAYS": 7,
    "DEFAULT_WEEKLY_PLAN_DAYS": 7,
    "DEFAULT_MAX_RECIPES_PER_CUISINE": 2,
    "MAX_UNIQUE_INGREDIENT_OVERLAP": 3,
    #Recipe Filtering
    "MINIMUM_PROTEIN_THRESHOLD_G": 10,
    "PROTEIN_SCORING_WEIGHT_FACTOR": 10.0,
    #Nutrition & Members
    "DEFAULT_ADULT_CALORIES": 2200,
    "DEFAULT_ADULT_PROTEIN": 110,
    "DEFAULT_CHILD_CALORIES": 1200,
    "DEFAULT_CHILD_PROTEIN": 30,
    "ACTIVITY_LEVEL_MULTIPLIERS": {
        "low": 1.0,
        "medium": 1.05,
        "high": 1.10,
    },
    #Ordering & Groceries
    "DEFAULT_ORDER_FEE_CENTS": 200,
    #System Defaults
    "INITIAL_ID_DEFAULTS": {
        "meal_plans": 6000,
        "meal_plan_entries": 6100,
        "grocery_lists": 8000,
        "grocery_list_items": 8100,
        "orders": 10000,
        "order_items": 10100,
        "audit_logs": 12000,
    },
}

ERROR_MESSAGES = {
    #Validation Errors
    "INVALID_PARAMETER_TYPE": "Parameter '{param}' must be of type {expected_type}.",
    "REQUIRED_PARAMETER": "Required parameter '{param}' is missing.",
    "INVALID_ID_FORMAT": "ID '{entity_id}' for entity '{entity}' is invalid.",
    #Data Access Errors
    "NOT_FOUND": "{entity} with id '{entity_id}' not found.",
    "NO_DATA_FOUND": "No data found for {entity}.",
    "ALREADY_EXISTS": "{entity} with id '{entity_id}' already exists.",
    #Domain Logic Errors
    "OUT_OF_STOCK": "Ingredient '{ingredient_id}' is out of stock.",
    "ORDER_CONFLICT": "Order '{order_id}' has a conflict: {details}.",
    "UNSUPPORTED_OPERATION": "Operation '{operation}' is not supported for {entity}.",
    #Generic Errors
    "UNEXPECTED_ERROR": "An unexpected error occurred: {exception_details}",
}


INGREDIENT_NAME_MAP = {
    "chicken breast": 1001,
    "chicken breasts": 1001,
    "egg": 1030,
    "eggs": 1030,
    "yellow onion": 1010,
    "onions": 1010,
    "bell pepper": 1009,
    "bell peppers": 1009,
    "flour": 1027,
    "all-purpose flour": 1027,
}


UNIT_CONVERSION_RULES = {
    "cup_to_g": {
        "default": 180,  #Average for many dry goods
        1027: 125,  #Flour (All-Purpose)
        1028: 200,  #Granulated Sugar
        1118: 220,  #Brown Sugar
        1035: 90,  #Rolled Oats
    },
    "tbsp_to_ml": 15.0,
    "tsp_to_ml": 5.0,
    "cup_to_ml": 240.0,
}


SUBSTITUTION_RULES = {
    #Key: ingredient_id to be replaced
    #Value: List of possible substitutes
    1030: [
        #Eggs
        {
            "substitute_ingredient_id": 1034,  #Bananas
            "note": "Use 1/2 of a medium mashed banana per egg. Best for dense, moist baked goods.",
        },
        {
            "substitute_ingredient_id": 1081,  #Apples (assumes applesauce)
            "note": "Use 1/4 cup (approx. 60g) of unsweetened applesauce per egg. Adds moisture.",
        },
        {
            "substitute_ingredient_id": 1128,  #Chia Seeds
            "note": "Mix 1 tbsp of chia seeds with 3 tbsp of water and let it sit for 5 minutes to form a gel. Use per egg.",
        },
    ],
    1029: [
        #Unsalted Butter
        {
            "substitute_ingredient_id": 1110,  #Coconut Oil
            "note": "Use a 1:1 ratio of solid coconut oil for solid butter. May impart a slight coconut flavor.",
        },
        {
            "substitute_ingredient_id": 1023,  #Plain Greek Yogurt
            "note": "Use half the amount of Greek yogurt. E.g., for 1 cup of butter, use 1/2 cup of yogurt. Reduces fat content.",
        },
    ],
}


INGREDIENT_SUBSTITUTE_MAP = {
    1002: [1049, 1001],  #Salmon -> [Cod Fillet, Chicken Breast]
    1041: [1131, 1132],  #Peanut Butter -> [Almond Butter, Sunflower Seed Butter]
    1013: [1070, 1071],  #Romaine Lettuce -> [Spinach, Kale]
    1006: [1056, 1058, 1007],  #White Rice -> [Brown Rice, Basmati Rice, Quinoa]
}


def _log_audit_event(data: dict[str, Any], **kwargs: Any) -> None:
    """
    Logs an action to the audit trail.

    This helper constructs and appends a new audit log entry to the in-memory
    'audit_logs' dataset. It automatically generates a new unique 'audit_id'
    and a UTC timestamp for the 'created_at' field. This function modifies
    the 'data' dictionary in place.

    Args:
        data: The main in-memory dictionary containing all datasets, which
              will be mutated by this function.
        **kwargs: Keyword arguments that map to the audit log schema. Expected
            keys include 'household_id', 'user_id', 'entity_type',
            'entity_id', 'action_enum', and 'payload_json'.
    """
    pass
    audit_logs_table = data.setdefault("audit_logs", [])

    #1. Generate a new unique ID based on the last entry or the default start value
    base_id = DEFAULT_BUSINESS_RULES["INITIAL_ID_DEFAULTS"]["audit_logs"]
    max_id = base_id
    if audit_logs_table:
        max_id = max(int(log.get("audit_id", 0)) for log in audit_logs_table)
    next_id = max_id + 1

    #2. Get the current timestamp in ISO 8601 format (UTC)
    timestamp = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    #3. Construct the new log entry from kwargs
    new_log_entry = {
        "audit_id": next_id,
        "household_id": kwargs.get("household_id"),
        "user_id": kwargs.get("user_id"),
        "entity_type": kwargs.get("entity_type"),
        "entity_id": kwargs.get("entity_id"),
        "action_enum": kwargs.get("action_enum", "custom_action"),
        "payload_json": kwargs.get("payload_json", {}),
        "created_at": timestamp,
    }

    #4. Append the new entry to the table
    audit_logs_table.append(new_log_entry)


def _normalize_domain_data(
    entity: str, data: Any, context: dict[str, Any] | None = None
) -> Any:
    """
    Normalizes domain-specific data, such as units and ingredient names.

    This function acts as a centralized translator for various data formats
    encountered in the domain, converting them into a canonical format that
    the tools can reliably process.

    Args:
        entity: The type of data to normalize. Supported values are
                'ingredient_name' and 'unit_measurement'.
        data: The data to be normalized. The expected format depends on the
              'entity' type.
        context: An optional dictionary providing additional context, such as
                 the full ingredients dataset for lookups.

    Returns:
        The normalized data. The format of the returned data depends on the
        normalization performed.
    """
    _dataL = data or ''.lower()
    pass
    if entity == "ingredient_name":
        #Input 'data' is a string like "Tomatoes" or "flour"
        #Output is the canonical ingredient_id (int)
        if not isinstance(data, str):
            return None

        processed_name = data.lower().strip()
        #Simple plural handling
        if processed_name.endswith("s"):
            processed_name = processed_name[:-1]

        return INGREDIENT_NAME_MAP.get(processed_name)

    if entity == "unit_measurement":
        #Input 'data' is a dict: {"ingredient_id": int, "quantity": float, "unit": str}
        #Output is a dict with quantity/unit normalized to g/ml
        if not isinstance(data, dict) or not all(
            k in data for k in ["ingredient_id", "quantity", "unit"]
        ):
            return data  #Return original data if format is incorrect

        #Find the ingredient's default unit (g or ml)
        #This requires access to the full ingredients dataset, passed in context
        all_ingredients = (context or {}).get("ingredients", [])
        ingredient_meta = next(
            (i for i in all_ingredients if i["ingredient_id"] == data["ingredient_id"]),
            None,
        )
        if not ingredient_meta:
            return data  #Cannot normalize without metadata

        default_unit = ingredient_meta.get("default_unit")
        current_unit = data["unit"].lower()

        #No conversion needed
        if current_unit == default_unit:
            return data

        quantity = data["quantity"]
        new_quantity = quantity

        #Conversion logic
        if current_unit == "cup" and default_unit == "g":
            conversion_factor = UNIT_CONVERSION_RULES["cup_to_g"].get(
                data["ingredient_id"], UNIT_CONVERSION_RULES["cup_to_g"]["default"]
            )
            new_quantity = quantity * conversion_factor
        elif current_unit == "tbsp" and default_unit == "ml":
            new_quantity = quantity * UNIT_CONVERSION_RULES["tbsp_to_ml"]
        elif current_unit == "tsp" and default_unit == "ml":
            new_quantity = quantity * UNIT_CONVERSION_RULES["tsp_to_ml"]
        elif current_unit == "cup" and default_unit == "ml":
            new_quantity = quantity * UNIT_CONVERSION_RULES["cup_to_ml"]
        else:
            #Return original data if no rule exists
            return data

        return {
            "ingredient_id": data["ingredient_id"],
            "quantity": round(new_quantity, 2),
            "unit": default_unit,
        }

    #Return original data if entity type is not supported
    return data


def _validate_inputs(
    args: dict[str, Any], param_definitions: dict[str, dict[str, Any]]
) -> dict[str, Any] | None:
    """
    Validates tool arguments against a set of definitions.

    This helper checks for the presence of required parameters and validates the
    data type for all provided parameters against the definitions. It's designed
    to be the first call within any tool's `invoke` method to act as a
    protective guard clause.

    Args:
        args: The dictionary of arguments passed to the tool (e.g., kwargs).
        param_definitions: A dictionary where each key is a parameter name and
            the value is another dictionary defining its rules, such as
            'type' (e.g., int, str) and 'required' (bool).

    Returns:
        None if all validations pass.
        A dictionary containing the 'error_code' and 'details' for the
        first validation failure, ready to be passed to _build_error_response().
    """
    pass
    for param, definition in param_definitions.items():
        is_required = definition.get("required", False)
        expected_type = definition.get("type")

        if is_required and param not in args:
            return {"error_code": "REQUIRED_PARAMETER", "details": {"param": param}}

        if param in args and expected_type is not None:
            value = args[param]
            if not isinstance(value, expected_type):
                return {
                    "error_code": "INVALID_PARAMETER_TYPE",
                    "details": {
                        "param": param,
                        "expected_type": expected_type.__name__,
                    },
                }

    return None


def _build_error_response(
    error_code: str, details: dict[str, Any] | None = None
) -> str:
    """
    Builds a standardized error response envelope as a JSON string.

    Args:
        error_code: The error code, corresponding to a key in ERROR_MESSAGES.
        details: A dictionary with specific details to format the error message.

    Returns:
        A JSON string representing the failed response.
    """
    pass
    details = details or {}
    message_template = ERROR_MESSAGES.get(error_code, "An unknown error occurred.")

    try:
        message = message_template.format(**details)
    except KeyError:
        message = message_template

    response_dict = {
        "success": False,
        "error": {"code": error_code, "message": message, "details": details},
    }
    payload = response_dict
    out = json.dumps(payload, indent=2)
    return out

#==============================================================================
#2. Core Helpers
#==============================================================================


def _build_success_response(data: Any) -> str:
    """
    Builds a standardized success response envelope as a JSON string.

    Args:
        data: The payload to be included in the response.

    Returns:
        A JSON string representing the successful response.
    """
    pass
    response_dict = {"success": True, "data": data}
    payload = response_dict
    out = json.dumps(payload, indent=2)
    return out


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

        #3. Data Retrieval
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

        #4. Data Enrichment (Hydration): Fetch associated members
        household_members = [
            m for m in data.get("members", []) if m.get("household_id") == household_id
        ]

        #5. Build the final profile object
        profile_data = {
            "household_info": target_household,
            "members": household_members,
        }

        #6. Return a standardized success response
        return _build_success_response(profile_data)
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
            (m for m in data.get("members", []) if m.get("member_id") == member_id),
            None,
        )

        #3. Handle cases where the member is not found
        if not member_profile:
            return _build_error_response(
                "NOT_FOUND", details={"entity": "Member", "entity_id": member_id}
            )

        #4. Return a standardized success response
        return _build_success_response(member_profile)
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
class AddHouseholdMemberTool(Tool):
    """
    A tool to add a new member to a specified household.
    """

    #Defines the set of expected and allowed fields for a new member.
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
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "AddHouseholdMember",
                "description": (
                    "Adds a new member to a specified household. The 'new_member_data' "
                    "parameter must be a dictionary with the new member's details."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {
                            "type": "integer",
                            "description": "The ID of the household to add the member to.",
                        },
                        "new_member_data": {
                            "type": "object",
                            "description": "A dictionary with the new member's profile data.",
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user performing the action, for auditing.",
                        },
                    },
                    "required": ["household_id", "new_member_data"],
                },
            },
        }

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        household_id: int, 
        new_member_data: dict, 
        user_id: int = None
    ) -> dict[str, Any]:
        """
        Executes the logic to create and add a new member to the dataset.

        This method validates all required inputs, ensures the target household
        exists, generates a new unique member_id, constructs the new member
        record, appends it to the dataset, and logs the creation event.

        Args:
            data: The main in-memory dictionary containing all datasets.
            household_id: The ID of the household to which the new member will be added.
            new_member_data: A dictionary containing the new member's data.
            user_id: An optional ID for logging purposes.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the newly created member object.
        """
        #1. Validate Inputs
        param_definitions = {
            "household_id": {"type": int, "required": True},
            "new_member_data": {"type": dict, "required": True},
            "user_id": {"type": int, "required": False},
        }
        validation_error = _validate_inputs(
            {"household_id": household_id, "new_member_data": new_member_data, "user_id": user_id}, 
            param_definitions
        )
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Pre-condition Check: Ensure the household exists before adding to it.
        if not any(
            h
            for h in data.get("households", [])
            if h.get("household_id") == household_id
        ):
            return _build_error_response(
                "NOT_FOUND", {"entity": "Household", "entity_id": household_id}
            )

        #3. Data Creation Logic
        members_table = data.setdefault("members", [])

        #Generate a new unique ID
        max_id = max((m.get("member_id", 0) for m in members_table), default=300)
        new_member_id = max_id + 1

        #Construct the new member record safely
        new_member_record = {
            "member_id": new_member_id,
            "household_id": household_id,
        }
        for field in AddHouseholdMemberTool.EXPECTED_FIELDS:
            new_member_record[field] = new_member_data.get(field)

        members_table.append(new_member_record)

        #4. Log the audit event for traceability
        _log_audit_event(
            data=data,
            household_id=household_id,
            user_id=user_id,
            entity_type="members",
            entity_id=new_member_id,
            action_enum="create",
            payload_json=new_member_data,
        )

        #5. Return the newly created object
        return _build_success_response(new_member_record)
class SearchRecipesTool(Tool):
    """
    A tool to search for recipes based on a combination of filters.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "searchRecipes",
                "description": (
                    "Searches for recipes using various optional filters. "
                    "Multiple filters can be combined to narrow down the results."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cuisine": {
                            "type": "string",
                            "description": "The cuisine type to filter by (e.g., 'Italian', 'Mexican').",
                        },
                        "meal_type": {
                            "type": "string",
                            "description": "The meal type to filter by (e.g., 'Dinner', 'Lunch').",
                        },
                        "max_calories": {
                            "type": "integer",
                            "description": "The maximum calories per serving.",
                        },
                        "min_protein_g": {
                            "type": "integer",
                            "description": "The minimum grams of protein per serving.",
                        },
                        "is_peanut_free": {
                            "type": "boolean",
                            "description": "Filter for recipes that are marked as peanut-free.",
                        },
                    },
                    "required": [],
                },
            },
        }

    @staticmethod
    def invoke(
        data: dict[str, Any],
        cuisine: str = None,
        meal_type: str = None,
        max_calories: int = None,
        min_protein_g: int = None,
        is_peanut_free: bool = None
    ) -> dict[str, Any]:
        """
        Executes the search logic by applying a series of filters.

        This method validates all provided filters and applies them sequentially
        to the main list of recipes. An empty list is a valid successful
        result if no recipes match the criteria.

        Args:
            data: The main in-memory dictionary containing all datasets.
            cuisine: Filter by cuisine type.
            meal_type: Filter by meal type.
            max_calories: Filter by maximum calories.
            min_protein_g: Filter by minimum protein in grams.
            is_peanut_free: Filter by peanut-free recipes.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains a list of matching recipe objects.
        """
        pass
        #1. Validate all provided inputs
        param_definitions = {
            "cuisine": {"type": str, "required": False},
            "meal_type": {"type": str, "required": False},
            "max_calories": {"type": int, "required": False},
            "min_protein_g": {"type": int, "required": False},
            "is_peanut_free": {"type": bool, "required": False},
        }
        validation_error = _validate_inputs(
            {
                "cuisine": cuisine,
                "meal_type": meal_type,
                "max_calories": max_calories,
                "min_protein_g": min_protein_g,
                "is_peanut_free": is_peanut_free
            },
            param_definitions
        )
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Start with the full list of recipes
        results = data.get("recipes", [])

        #3. Apply filters sequentially
        if cuisine is not None:
            cuisine = cuisine.lower()
            results = [r for r in results if r.get("cuisine", "").lower() == cuisine]

        if meal_type is not None:
            meal_type = meal_type.lower()
            results = [
                r for r in results if r.get("meal_type", "").lower() == meal_type
            ]

        if max_calories is not None:
            results = [
                r
                for r in results
                if (calories := r.get("calories_per_serving")) is not None
                and calories <= max_calories
            ]

        if min_protein_g is not None:
            results = [
                r
                for r in results
                if (protein := r.get("protein_g_per_serving")) is not None
                and protein >= min_protein_g
            ]

        if is_peanut_free is True:
            results = [r for r in results if r.get("is_peanut_free") is True]

        #4. Return the filtered list in a standard success response
        return _build_success_response(results)
class GetRecipeDetailsTool(Tool):
    """
    A tool to retrieve the full, detailed profile of a single recipe.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetRecipeDetails",
                "description": (
                    "Retrieves the full profile for a single recipe by its unique ID, "
                    "including its hydrated list of ingredients and preparation instructions."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_id": {
                            "type": "integer",
                            "description": "The unique identifier for the recipe to retrieve.",
                        },
                    },
                    "required": ["recipe_id"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], recipe_id: int) -> dict[str, Any]:
        """
        Executes the logic to fetch and enrich a specific recipe's data.

        This method validates the required recipe_id, finds the corresponding
        recipe, and then enriches it by fetching all its ingredients and their
        full names, providing a complete data packet for the agent.

        Args:
            data: The main in-memory dictionary containing all datasets.
            recipe_id: The ID of the recipe to fetch and enrich.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the fully detailed and hydrated recipe object.
        """
        pass
        #1. Validate Inputs
        param_definitions = {"recipe_id": {"type": int, "required": True}}
        validation_error = _validate_inputs({"recipe_id": recipe_id}, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Data Retrieval: Find the base recipe object
        recipe_record = next(
            (r for r in data.get("recipes", []) if r.get("recipe_id") == recipe_id),
            None,
        )

        if not recipe_record:
            return _build_error_response(
                "NOT_FOUND", {"entity": "Recipe", "entity_id": recipe_id}
            )

        #3. Data Enrichment (Hydration): Fetch and enrich ingredients
        recipe_ingredients_links = [
            ri
            for ri in data.get("recipe_ingredients", [])
            if ri.get("recipe_id") == recipe_id
        ]

        enriched_ingredients = []
        all_ingredients_meta = data.get("ingredients", [])
        for link in recipe_ingredients_links:
            ingredient_meta = next(
                (
                    i
                    for i in all_ingredients_meta
                    if i.get("ingredient_id") == link.get("ingredient_id")
                ),
                None,
            )
            enriched_ingredients.append(
                {
                    "ingredient_id": link.get("ingredient_id"),
                    "ingredient_name": (
                        ingredient_meta.get("ingredient_name")
                        if ingredient_meta
                        else "Unknown"
                    ),
                    "quantity": link.get("quantity"),
                    "unit": link.get("unit"),
                }
            )

        #4. Build the final response object
        detailed_recipe = recipe_record.copy()
        detailed_recipe["ingredients"] = enriched_ingredients

        #5. Return the standardized success response
        return _build_success_response(detailed_recipe)
class FindRecipesByIngredientsTool(Tool):
    """
    A tool to find recipes based on a list of available ingredients.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "FindRecipesByIngredients",
                "description": (
                    "Finds recipes that can be made with a list of available ingredient IDs. "
                    "Results are sorted by how closely they match the available ingredients."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "available_ingredient_ids": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "A list of ingredient IDs that are available.",
                        },
                        "max_missing_ingredients": {
                            "type": "integer",
                            "description": "The maximum number of ingredients a recipe can be missing. Defaults to 1.",
                        },
                    },
                    "required": ["available_ingredient_ids"],
                },
            },
        }

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        available_ingredient_ids: list, 
        max_missing_ingredients: int = 1
    ) -> dict[str, Any]:
        """
        Executes the logic to match available ingredients against recipe requirements.

        This method builds a map of ingredients required for each recipe, then
        compares this against the user's available ingredients to find matches.
        Results are enriched with information about missing ingredients and sorted
        by the number of missing ingredients.

        Args:
            data: The main in-memory dictionary containing all datasets.
            available_ingredient_ids: List of IDs of available ingredients.
            max_missing_ingredients: Maximum number of missing ingredients allowed.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains a list of matching recipes, sorted by
            the number of missing ingredients.
        """
        #1. Validate Inputs
        param_definitions = {
            "available_ingredient_ids": {"type": list, "required": True},
            "max_missing_ingredients": {"type": int, "required": False},
        }
        validation_error = _validate_inputs(
            {"available_ingredient_ids": available_ingredient_ids, 
             "max_missing_ingredients": max_missing_ingredients}, 
            param_definitions
        )
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        available_ids = set(available_ingredient_ids)
        max_missing = max_missing_ingredients

        #2. Pre-process recipe requirements for efficient lookup
        recipe_requirements = collections.defaultdict(set)
        for ri in data.get("recipe_ingredients", []):
            recipe_requirements[ri["recipe_id"]].add(ri["ingredient_id"])

        #3. Find matching recipes
        matching_recipes = []
        for recipe in data.get("recipes", []):
            recipe_id = recipe["recipe_id"]
            required_ids = recipe_requirements[recipe_id]

            missing_ids = required_ids - available_ids

            if len(missing_ids) <= max_missing:
                match_details = {
                    "recipe_info": recipe,
                    "missing_ingredient_count": len(missing_ids),
                    "missing_ingredient_ids": sorted(list(missing_ids)),
                }
                matching_recipes.append(match_details)

        #4. Sort results to show the best matches first
        matching_recipes.sort(key=lambda x: x["missing_ingredient_count"])

        #5. Return the standardized success response
        return _build_success_response(matching_recipes)
class GetIngredientInfoTool(Tool):
    """
    A tool to retrieve the full data record for a single ingredient.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetIngredientInfo",
                "description": "Retrieves the full data record for a single ingredient by its unique ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ingredient_id": {
                            "type": "integer",
                            "description": "The unique identifier for the ingredient to retrieve.",
                        },
                    },
                    "required": ["ingredient_id"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], ingredient_id: int) -> dict[str, Any]:
        """
        Executes the logic to find and return a specific ingredient's data.

        Args:
            data: The main in-memory dictionary containing all datasets.
            ingredient_id: The ID of the ingredient to retrieve.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the ingredient object. On failure,
            it contains a structured error object.
        """
        #1. Validate Inputs
        param_definitions = {"ingredient_id": {"type": int, "required": True}}
        validation_error = _validate_inputs({"ingredient_id": ingredient_id}, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Data Retrieval
        ingredient_record = next(
            (
                i
                for i in data.get("ingredients", [])
                if i.get("ingredient_id") == ingredient_id
            ),
            None,
        )

        #3. Handle not found cases
        if not ingredient_record:
            return _build_error_response(
                "NOT_FOUND", {"entity": "Ingredient", "entity_id": ingredient_id}
            )

        #4. Return a standardized success response
        return _build_success_response(ingredient_record)
class GetRecipeSubstitutionsTool(Tool):
    """
    A tool to suggest ingredient substitutions for a specific recipe.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetRecipeSubstitutions",
                "description": (
                    "Suggests ingredient substitutions for a given ingredient within "
                    "a specific recipe, based on a predefined knowledge base."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_id": {
                            "type": "integer",
                            "description": "The unique ID for the recipe requiring a substitution.",
                        },
                        "ingredient_id_to_replace": {
                            "type": "integer",
                            "description": "The unique ID of the ingredient that is missing.",
                        },
                    },
                    "required": ["recipe_id", "ingredient_id_to_replace"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], recipe_id: int, ingredient_id_to_replace: int) -> dict[str, Any]:
        """
        Executes the logic to find and suggest ingredient substitutions.

        This method validates the inputs, confirms the ingredient is part of the
        recipe, then consults a predefined knowledge base (SUBSTITUTION_RULES)
        for valid alternatives, enriching the response with ingredient names.

        Args:
            data: The main in-memory dictionary containing all datasets.
            recipe_id: The ID of the recipe.
            ingredient_id_to_replace: The ID of the ingredient to replace.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains a list of substitution suggestions.
        """
        pass
        #1. Validate Inputs
        param_definitions = {
            "recipe_id": {"type": int, "required": True},
            "ingredient_id_to_replace": {"type": int, "required": True},
        }
        validation_error = _validate_inputs({"recipe_id": recipe_id, "ingredient_id_to_replace": ingredient_id_to_replace}, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Pre-condition Checks
        if not any(r.get("recipe_id") == recipe_id for r in data.get("recipes", [])):
            return _build_error_response(
                "NOT_FOUND", {"entity": "Recipe", "entity_id": recipe_id}
            )

        if not any(
            i.get("ingredient_id") == ingredient_id_to_replace
            for i in data.get("ingredients", [])
        ):
            return _build_error_response(
                "NOT_FOUND", {"entity": "Ingredient", "entity_id": ingredient_id_to_replace}
            )

        recipe_ingredients = {
            ri["ingredient_id"]
            for ri in data.get("recipe_ingredients", [])
            if ri["recipe_id"] == recipe_id
        }
        if ingredient_id_to_replace not in recipe_ingredients:
            return _build_error_response(
                "UNSUPPORTED_OPERATION",
                {
                    "operation": "Substitution",
                    "entity": f"Ingredient {ingredient_id_to_replace} is not part of Recipe {recipe_id}",
                },
            )

        #3. Get suggestions from the knowledge base
        suggestions = SUBSTITUTION_RULES.get(ingredient_id_to_replace, [])

        #4. Enrich suggestions with ingredient names
        enriched_suggestions = []
        all_ingredients_meta = data.get("ingredients", [])
        for suggestion in suggestions:
            sub_id = suggestion["substitute_ingredient_id"]
            sub_meta = next(
                (i for i in all_ingredients_meta if i["ingredient_id"] == sub_id), None
            )

            if sub_meta:
                enriched_suggestion = suggestion.copy()
                enriched_suggestion["substitute_ingredient_name"] = sub_meta.get(
                    "ingredient_name"
                )
                enriched_suggestions.append(enriched_suggestion)

        #5. Return the standardized success response
        return _build_success_response(enriched_suggestions)
class AddNewRecipeTool(Tool):
    """
    A tool to add a new recipe to the dataset.
    """

    #Defines the set of expected fields for the main recipe data.
    EXPECTED_RECIPE_FIELDS = {
        "recipe_title",
        "meal_type",
        "cuisine",
        "servings_default",
        "prep_minutes",
        "cook_minutes",
        "is_peanut_free",
        "calories_per_serving",
        "protein_g_per_serving",
        "instructions_json",
        "notes",
    }

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "AddNewRecipe",
                "description": (
                    "Adds a new recipe to the dataset. Requires recipe metadata and a "
                    "list of its ingredients with quantities and units."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_data": {
                            "type": "object",
                            "description": "A dictionary with the new recipe's main data.",
                        },
                        "ingredients_list": {
                            "type": "array",
                            "description": "A list of ingredient objects, each with ingredient_id, quantity, and unit.",
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user performing the action, for auditing.",
                        },
                    },
                    "required": ["recipe_data", "ingredients_list", "user_id"],
                },
            },
        }

    @staticmethod
    def invoke(
        data: dict[str, Any],
        recipe_data: dict,
        ingredients_list: list,
        user_id: int
    ) -> dict[str, Any]:
        """
        Executes the logic to create a new recipe and its ingredient links.

        This method performs deep validation on the provided recipe data and
        ingredient list, creates records in both the 'recipes' and
        'recipe_ingredients' tables, logs the event, and returns the new recipe.

        Args:
            data: The main in-memory dictionary containing all datasets.
            recipe_data: The data for the recipe to be created.
            ingredients_list: The list of ingredients for the recipe.
            user_id: The ID of the user creating the recipe.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the newly created recipe object.
        """
        #1. Standard Validation
        param_definitions = {
            "recipe_data": {"type": dict, "required": True},
            "ingredients_list": {"type": list, "required": True},
            "user_id": {"type": int, "required": True},
        }
        validation_error = _validate_inputs(
            {"recipe_data": recipe_data, "ingredients_list": ingredients_list, "user_id": user_id},
            param_definitions
        )
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Deep Validation
        if not AddNewRecipeTool.EXPECTED_RECIPE_FIELDS.issubset(recipe_data.keys()):
            return _build_error_response(
                "INVALID_PARAMETER_TYPE",
                {
                    "param": "recipe_data",
                    "expected_type": "object with all required recipe fields",
                },
            )
        if not ingredients_list:
            return _build_error_response(
                "INVALID_PARAMETER_TYPE",
                {"param": "ingredients_list", "expected_type": "non-empty list"},
            )

        all_ingredient_ids = {i["ingredient_id"] for i in data.get("ingredients", [])}
        for item in ingredients_list:
            if not isinstance(item, dict) or not all(
                k in item for k in ["ingredient_id", "quantity", "unit"]
            ):
                return _build_error_response(
                    "INVALID_PARAMETER_TYPE",
                    {
                        "param": "ingredients_list",
                        "expected_type": "list of valid ingredient objects",
                    },
                )
            if item["ingredient_id"] not in all_ingredient_ids:
                return _build_error_response(
                    "NOT_FOUND",
                    {"entity": "Ingredient", "entity_id": item["ingredient_id"]},
                )

        #3. Create Recipe Record
        recipes_table = data.setdefault("recipes", [])
        max_recipe_id = max((r.get("recipe_id", 0) for r in recipes_table), default=400)
        new_recipe_id = max_recipe_id + 1

        new_recipe_record = {"recipe_id": new_recipe_id}
        new_recipe_record.update(
            {
                key: recipe_data.get(key)
                for key in AddNewRecipeTool.EXPECTED_RECIPE_FIELDS
            }
        )
        recipes_table.append(new_recipe_record)

        #4. Create Recipe-Ingredient Links
        ri_table = data.setdefault("recipe_ingredients", [])
        max_ri_id = max((ri.get("ri_id", 0) for ri in ri_table), default=5000)

        for ingredient in ingredients_list:
            max_ri_id += 1
            new_ri_record = {
                "ri_id": max_ri_id,
                "recipe_id": new_recipe_id,
                "ingredient_id": ingredient["ingredient_id"],
                "quantity": ingredient["quantity"],
                "unit": ingredient["unit"],
            }
            ri_table.append(new_ri_record)

        #5. Auditing
        user_household = next(
            (
                h
                for h in data.get("households", [])
                if h.get("primary_user_id") == user_id
            ),
            None,
        )
        household_id = user_household.get("household_id") if user_household else None

        _log_audit_event(
            data=data,
            household_id=household_id,
            user_id=user_id,
            entity_type="recipes",
            entity_id=new_recipe_id,
            action_enum="create",
            payload_json={
                "recipe_data": recipe_data,
                "ingredients_list": ingredients_list,
            },
        )

        #6. Response
        return _build_success_response(new_recipe_record)
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
class LogMealAsPreparedTool(Tool):
    """
    A tool to log that a recipe was prepared, adding an entry to the meal history.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "LogMealAsPrepared",
                "description": "Logs that a recipe was prepared for a household on a specific date. Optionally includes a user rating.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {
                            "type": "integer",
                            "description": "The unique ID for the household.",
                        },
                        "recipe_id": {
                            "type": "integer",
                            "description": "The unique ID of the recipe that was prepared.",
                        },
                        "plan_date": {
                            "type": "string",
                            "description": "The date the meal was prepared, in 'YYYY-MM-DD' format.",
                        },
                        "rating_int": {
                            "type": "integer",
                            "description": "An optional integer rating for the meal (e.g., 1-5).",
                        },
                        "was_prepared": {
                            "type": "boolean",
                            "description": "Indicates if the meal was actually prepared. Defaults to True.",
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user performing the action, for auditing.",
                        },
                    },
                    "required": ["household_id", "recipe_id", "plan_date"],
                },
            },
        }

    @staticmethod
    def invoke(
        data: dict[str, Any],
        household_id: int,
        recipe_id: int,
        plan_date: str,
        rating_int: int = None,
        was_prepared: bool = True,
        user_id: int = None, notes: Any = None) -> dict[str, Any]:
        """
        Executes the logic to create a new meal history entry.

        Args:
            data: The main in-memory dictionary containing all datasets.
            household_id: The ID of the household.
            recipe_id: The ID of the recipe.
            plan_date: The date the meal is planned.
            rating_int: The rating of the meal.
            was_prepared: Whether the meal was prepared.
            user_id: The ID of the user.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the newly created meal history object.
        """
        #1. Validate Inputs
        param_definitions = {
            "household_id": {"type": int, "required": True},
            "recipe_id": {"type": int, "required": True},
            "plan_date": {"type": str, "required": True},
            "rating_int": {"type": int, "required": False},
            "was_prepared": {"type": bool, "required": False},
            "user_id": {"type": int, "required": False},
        }
        validation_error = _validate_inputs(locals(), param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Pre-condition Checks: Ensure related entities exist
        if not any(
            h.get("household_id") == household_id for h in data.get("households", [])
        ):
            return _build_error_response(
                "NOT_FOUND", {"entity": "Household", "entity_id": household_id}
            )
        if not any(r.get("recipe_id") == recipe_id for r in data.get("recipes", [])):
            return _build_error_response(
                "NOT_FOUND", {"entity": "Recipe", "entity_id": recipe_id}
            )

        #3. Data Creation Logic
        history_table = data.setdefault("meal_history", [])

        #Generate a new unique ID
        max_id = max((h.get("history_id", 0) for h in history_table), default=6000)
        new_history_id = max_id + 1

        #Build the new record
        new_history_record = {
            "history_id": new_history_id,
            "household_id": household_id,
            "recipe_id": recipe_id,
            "plan_date": plan_date,
            "was_prepared": was_prepared,
            "rating_int": rating_int,  #Defaults to None if not present
        }

        history_table.append(new_history_record)

        #4. Auditing
        _log_audit_event(
            data=data,
            household_id=household_id,
            user_id=user_id,
            entity_type="meal_history",
            entity_id=new_history_id,
            action_enum="create",
            payload_json={"recipe_id": recipe_id, "plan_date": plan_date},
        )

        #5. Response
        return _build_success_response(new_history_record)
#To be added to the "API Tool Classes" section of tools.py


class CreateMealPlanTool(Tool):
    """
    A tool to create a new, empty meal plan for a household for a specific week.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateMealPlan",
                "description": "Creates a new, empty meal plan for a household for a specific week, defined by its start date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {
                            "type": "integer",
                            "description": "The unique ID for the household.",
                        },
                        "week_start_date": {
                            "type": "string",
                            "description": "The start date of the meal plan week, in 'YYYY-MM-DD' format.",
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user creating the plan, for auditing.",
                        },
                    },
                    "required": ["household_id", "week_start_date", "user_id"],
                },
            },
        }

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        household_id: int, 
        week_start_date: str, 
        user_id: int
    ) -> dict[str, Any]:
        """
        Executes the logic to create a new meal plan record.

        Args:
            data: The main in-memory dictionary containing all datasets.
            household_id: The ID of the household for which the meal plan is created.
            week_start_date: The start date of the week for the meal plan.
            user_id: The ID of the user creating the meal plan.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the newly created meal plan object.
        """
        #1. Validate Inputs
        param_definitions = {
            "household_id": {"type": int, "required": True},
            "week_start_date": {"type": str, "required": True},
            "user_id": {"type": int, "required": True},
        }
        validation_error = _validate_inputs(
            {"household_id": household_id, "week_start_date": week_start_date, "user_id": user_id}, 
            param_definitions
        )
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Pre-condition Checks
        if not any(
            h.get("household_id") == household_id for h in data.get("households", [])
        ):
            return _build_error_response(
                "NOT_FOUND", {"entity": "Household", "entity_id": household_id}
            )
        if not any(u.get("user_id") == user_id for u in data.get("users", [])):
            return _build_error_response(
                "NOT_FOUND", {"entity": "User", "entity_id": user_id}
            )

        #Business Rule: Prevent duplicate plans for the same week
        existing_plan = any(
            p
            for p in data.get("meal_plans", [])
            if p.get("household_id") == household_id
            and p.get("week_start_date") == week_start_date
        )
        if existing_plan:
            return _build_error_response(
                "ALREADY_EXISTS",
                {
                    "entity": "MealPlan",
                    "entity_id": f"for household {household_id} on {week_start_date}",
                },
            )

        #3. Data Creation Logic
        meal_plans_table = data.setdefault("meal_plans", [])

        #Generate a new unique ID
        max_id = max(
            (p.get("meal_plan_id", 0) for p in meal_plans_table),
            default=DEFAULT_BUSINESS_RULES["INITIAL_ID_DEFAULTS"]["meal_plans"],
        )
        new_plan_id = max_id + 1

        timestamp = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

        new_plan_record = {
            "meal_plan_id": new_plan_id,
            "household_id": household_id,
            "week_start_date": week_start_date,
            "created_by_user_id": user_id,
            "created_at": timestamp,
        }

        meal_plans_table.append(new_plan_record)

        #4. Auditing
        _log_audit_event(
            data=data,
            household_id=household_id,
            user_id=user_id,
            entity_type="meal_plans",
            entity_id=new_plan_id,
            action_enum="create",
            payload_json={"week_start_date": week_start_date},
        )

        #5. Response
        return _build_success_response(new_plan_record)
class AddRecipeToMealPlanTool(Tool):
    """
    A tool to add a single recipe entry to an existing meal plan.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "AddRecipeToMealPlan",
                "description": "Adds a single recipe to an existing meal plan for a specific date and meal type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_plan_id": {
                            "type": "integer",
                            "description": "The unique ID for the meal plan to be modified.",
                        },
                        "recipe_id": {
                            "type": "integer",
                            "description": "The unique ID of the recipe to add.",
                        },
                        "plan_date": {
                            "type": "string",
                            "description": "The date for the meal entry, in 'YYYY-MM-DD' format.",
                        },
                        "meal_type": {
                            "type": "string",
                            "description": "The type of meal (e.g., 'Breakfast', 'Lunch', 'Dinner'). Defaults to 'Dinner'.",
                        },
                        "servings_adult": {
                            "type": "integer",
                            "description": "Number of adult servings. Defaults to 2.",
                        },
                        "servings_child": {
                            "type": "integer",
                            "description": "Number of child servings. Defaults to 0.",
                        },
                        "notes": {
                            "type": "string",
                            "description": "Optional notes for the meal entry.",
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user performing the action, for auditing.",
                        },
                    },
                    "required": ["meal_plan_id", "recipe_id", "plan_date"],
                },
            },
        }

    @staticmethod
    def invoke(
        data: dict[str, Any],
        meal_plan_id: int,
        recipe_id: int,
        plan_date: str,
        meal_type: str = "Dinner",
        servings_adult: int = 2,
        servings_child: int = 0,
        notes: str = "",
        user_id: int = None
    ) -> dict[str, Any]:
        """
        Executes the logic to create a new meal plan entry.

        Args:
            data: The main in-memory dictionary containing all datasets.
            meal_plan_id: The ID of the meal plan.
            recipe_id: The ID of the recipe.
            plan_date: The date for the meal plan entry.
            meal_type: The type of meal (e.g., Breakfast, Lunch, Dinner).
            servings_adult: Number of adult servings.
            servings_child: Number of child servings.
            notes: Additional notes for the meal plan entry.
            user_id: The ID of the user.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the newly created meal plan entry object.
        """
        #1. Validate Inputs
        param_definitions = {
            "meal_plan_id": {"type": int, "required": True},
            "recipe_id": {"type": int, "required": True},
            "plan_date": {"type": str, "required": True},
            "meal_type": {"type": str, "required": False},
            "servings_adult": {"type": int, "required": False},
            "servings_child": {"type": int, "required": False},
            "notes": {"type": str, "required": False},
            "user_id": {"type": int, "required": False},
        }
        validation_error = _validate_inputs(locals(), param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Pre-condition Checks
        meal_plan_record = next(
            (
                p
                for p in data.get("meal_plans", [])
                if p.get("meal_plan_id") == meal_plan_id
            ),
            None,
        )
        if not meal_plan_record:
            return _build_error_response(
                "NOT_FOUND", {"entity": "MealPlan", "entity_id": meal_plan_id}
            )
        if not any(r.get("recipe_id") == recipe_id for r in data.get("recipes", [])):
            return _build_error_response(
                "NOT_FOUND", {"entity": "Recipe", "entity_id": recipe_id}
            )

        #Business Rule: Ensure date is within the plan's week
        try:
            plan_start_date = date.fromisoformat(meal_plan_record["week_start_date"])
            entry_date = date.fromisoformat(plan_date)
        except ValueError:
            return _build_error_response(
                "INVALID_PARAMETER_TYPE",
                {"param": "plan_date", "expected_type": "string in YYYY-MM-DD format"},
            )

        plan_end_date = plan_start_date + timedelta(days=6)
        if not (plan_start_date <= entry_date <= plan_end_date):
            return _build_error_response(
                "UNSUPPORTED_OPERATION",
                {
                    "operation": "Add Entry",
                    "entity": f"Date {plan_date} is outside the week of MealPlan {meal_plan_id}",
                },
            )

        #Business Rule: Prevent duplicate entries
        if any(
            e
            for e in data.get("meal_plan_entries", [])
            if e.get("meal_plan_id") == meal_plan_id
            and e.get("plan_date") == plan_date
            and e.get("meal_type") == meal_type
        ):
            return _build_error_response(
                "ALREADY_EXISTS",
                {
                    "entity": "MealPlanEntry",
                    "entity_id": f"for {plan_date} {meal_type}",
                },
            )

        #3. Data Creation
        entries_table = data.setdefault("meal_plan_entries", [])
        max_id = max(
            (e.get("entry_id", 0) for e in entries_table),
            default=DEFAULT_BUSINESS_RULES["INITIAL_ID_DEFAULTS"]["meal_plan_entries"],
        )
        new_entry_id = max_id + 1

        new_entry_record = {
            "entry_id": new_entry_id,
            "meal_plan_id": meal_plan_id,
            "plan_date": plan_date,
            "meal_type": meal_type,
            "recipe_id": recipe_id,
            "servings_adult": servings_adult,
            "servings_child": servings_child,
            "notes": notes,
        }
        entries_table.append(new_entry_record)

        #4. Auditing
        _log_audit_event(
            data=data,
            household_id=meal_plan_record.get("household_id"),
            user_id=user_id,
            entity_type="meal_plan_entries",
            entity_id=new_entry_id,
            action_enum="create",
            payload_json={"recipe_id": recipe_id, "plan_date": plan_date},
        )

        #5. Response
        return _build_success_response(new_entry_record)
class GetMealPlanForWeekTool(Tool):
    """
    A tool to retrieve the full details of a meal plan, including all its entries.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetMealPlanForWeek",
                "description": (
                    "Retrieves a full meal plan and its daily entries by its unique ID. "
                    "The entries are enriched with recipe titles for clarity."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_plan_id": {
                            "type": "integer",
                            "description": "The unique identifier for the meal plan to retrieve.",
                        }
                    },
                    "required": ["meal_plan_id"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], meal_plan_id: int) -> dict[str, Any]:
        """
        Executes the logic to fetch and enrich a full meal plan.

        Args:
            data: The main in-memory dictionary containing all datasets.
            meal_plan_id: The ID of the meal plan to fetch.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the fully detailed and hydrated meal plan object.
        """
        #1. Validate Inputs
        param_definitions = {"meal_plan_id": {"type": int, "required": True}}
        validation_error = _validate_inputs({"meal_plan_id": meal_plan_id}, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Data Retrieval: Find the base meal plan object
        meal_plan_record = next(
            (
                p
                for p in data.get("meal_plans", [])
                if p.get("meal_plan_id") == meal_plan_id
            ),
            None,
        )

        if not meal_plan_record:
            return _build_error_response(
                "NOT_FOUND", {"entity": "MealPlan", "entity_id": meal_plan_id}
            )

        #3. Data Enrichment (Hydration): Fetch and enrich plan entries
        plan_entries = [
            e
            for e in data.get("meal_plan_entries", [])
            if e.get("meal_plan_id") == meal_plan_id
        ]

        enriched_entries = []
        all_recipes = data.get("recipes", [])
        for entry in plan_entries:
            recipe_info = next(
                (
                    r
                    for r in all_recipes
                    if r.get("recipe_id") == entry.get("recipe_id")
                ),
                None,
            )
            enriched_entry = entry.copy()
            enriched_entry["recipe_title"] = (
                recipe_info.get("recipe_title") if recipe_info else "Unknown Recipe"
            )
            enriched_entries.append(enriched_entry)

        #Sort entries by date for a logical view
        enriched_entries.sort(key=lambda x: x.get("plan_date", ""))

        #4. Build the final response object
        detailed_plan = meal_plan_record.copy()
        detailed_plan["entries"] = enriched_entries

        #5. Return the standardized success response
        return _build_success_response(detailed_plan)
class UpdateMealPlanEntryTool(Tool):
    """
    A tool to update a single entry within an existing meal plan.
    """

    #Defines which fields of a meal plan entry are safely updatable.
    UPDATABLE_FIELDS = {"recipe_id", "servings_adult", "servings_child", "notes"}

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "UpdateMealPlanEntry",
                "description": "Updates a single entry within a meal plan. Allows changing the recipe, serving sizes, or notes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "entry_id": {
                            "type": "integer",
                            "description": "The unique ID for the meal plan entry to update.",
                        },
                        "updates": {
                            "type": "object",
                            "description": "A dictionary of fields and their new values to apply.",
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user performing the action, for auditing.",
                        },
                    },
                    "required": ["entry_id", "updates"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], entry_id: int, updates: dict, user_id: int = None) -> dict[str, Any]:
        """
        Executes the logic to find and modify a meal plan entry.

        Args:
            data: The main in-memory dictionary containing all datasets.
            entry_id: The ID of the meal plan entry to update.
            updates: A dictionary containing the fields to update.
            user_id: The ID of the user making the update, if applicable.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the updated meal plan entry object.
        """
        #1. Validate Inputs
        param_definitions = {
            "entry_id": {"type": int, "required": True},
            "updates": {"type": dict, "required": True},
            "user_id": {"type": int, "required": False},
        }
        validation_error = _validate_inputs({"entry_id": entry_id, "updates": updates, "user_id": user_id}, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Pre-condition Check: If updating recipe_id, ensure it exists
        if "recipe_id" in updates:
            new_recipe_id = updates["recipe_id"]
            if not any(
                r.get("recipe_id") == new_recipe_id for r in data.get("recipes", [])
            ):
                return _build_error_response(
                    "NOT_FOUND", {"entity": "Recipe", "entity_id": new_recipe_id}
                )

        #3. Find and Update the Record
        entry_record = next(
            (
                e
                for e in data.get("meal_plan_entries", [])
                if e.get("entry_id") == entry_id
            ),
            None,
        )

        if not entry_record:
            return _build_error_response(
                "NOT_FOUND", {"entity": "MealPlanEntry", "entity_id": entry_id}
            )

        for key, value in updates.items():
            if key in UpdateMealPlanEntryTool.UPDATABLE_FIELDS:
                entry_record[key] = value

        #4. Auditing
        meal_plan = next(
            (
                p
                for p in data.get("meal_plans", [])
                if p.get("meal_plan_id") == entry_record["meal_plan_id"]
            ),
            None,
        )
        household_id = meal_plan.get("household_id") if meal_plan else None

        _log_audit_event(
            data=data,
            household_id=household_id,
            user_id=user_id,
            entity_type="meal_plan_entries",
            entity_id=entry_id,
            action_enum="update",
            payload_json=updates,
        )

        #5. Response
        return _build_success_response(entry_record)
class RemoveRecipeFromMealPlanTool(Tool):
    """
    A tool to remove a single recipe entry from a meal plan.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "RemoveRecipeFromMealPlan",
                "description": "Removes a single recipe entry from a meal plan using its unique entry ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "entry_id": {
                            "type": "integer",
                            "description": "The unique ID for the meal plan entry to remove.",
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user performing the action, for auditing.",
                        },
                    },
                    "required": ["entry_id"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], entry_id: int, user_id: int = None) -> dict[str, Any]:
        """
        Executes the logic to find and remove a meal plan entry.

        Args:
            data: The main in-memory dictionary containing all datasets.
            entry_id: The ID of the entry to be removed.
            user_id: The ID of the user performing the action, optional.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains a confirmation of the deletion.
        """
        #1. Validate Inputs
        param_definitions = {
            "entry_id": {"type": int, "required": True},
            "user_id": {"type": int, "required": False},
        }
        validation_error = _validate_inputs({"entry_id": entry_id, "user_id": user_id}, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        entries_table = data.get("meal_plan_entries", [])

        #2. Find the entry to remove
        entry_to_remove = next(
            (e for e in entries_table if e.get("entry_id") == entry_id), None
        )

        if not entry_to_remove:
            return _build_error_response(
                "NOT_FOUND", {"entity": "MealPlanEntry", "entity_id": entry_id}
            )

        #3. Auditing (must be done before the data is removed)
        meal_plan = next(
            (
                p
                for p in data.get("meal_plans", [])
                if p.get("meal_plan_id") == entry_to_remove["meal_plan_id"]
            ),
            None,
        )
        household_id = meal_plan.get("household_id") if meal_plan else None

        _log_audit_event(
            data=data,
            household_id=household_id,
            user_id=user_id,
            entity_type="meal_plan_entries",
            entity_id=entry_id,
            action_enum="delete",
            payload_json=entry_to_remove,  #Log the data that was deleted
        )

        #4. Perform the removal
        data["meal_plan_entries"] = [
            e for e in entries_table if e.get("entry_id") != entry_id
        ]

        #5. Response
        return _build_success_response(
            {"status": "success", "deleted_entry": entry_to_remove}
        )
class GetHouseholdInventoryTool(Tool):
    """
    A tool to retrieve all inventory items for a specific household.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetHouseholdInventory",
                "description": "Retrieves a list of all inventory items for a given household, enriched with ingredient names.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {
                            "type": "integer",
                            "description": "The unique identifier for the household.",
                        }
                    },
                    "required": ["household_id"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], household_id: int) -> dict[str, Any]:
        """
        Executes the logic to find and return a household's inventory.

        Args:
            data: The main in-memory dictionary containing all datasets.
            household_id: The ID of the household to retrieve inventory for.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains a list of enriched inventory items.
        """
        #1. Validate Inputs
        param_definitions = {"household_id": {"type": int, "required": True}}
        validation_error = _validate_inputs({"household_id": household_id}, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Pre-condition Check: Ensure the household exists
        if not any(
            h.get("household_id") == household_id for h in data.get("households", [])
        ):
            return _build_error_response(
                "NOT_FOUND", {"entity": "Household", "entity_id": household_id}
            )

        #3. Data Retrieval and Enrichment (Hydration)
        inventory_items = [
            i
            for i in data.get("inventory_items", [])
            if i.get("household_id") == household_id
        ]

        enriched_items = []
        all_ingredients_meta = data.get("ingredients", [])
        for item in inventory_items:
            ingredient_meta = next(
                (
                    i
                    for i in all_ingredients_meta
                    if i.get("ingredient_id") == item.get("ingredient_id")
                ),
                None,
            )
            enriched_item = item.copy()
            enriched_item["ingredient_name"] = (
                ingredient_meta.get("ingredient_name")
                if ingredient_meta
                else "Unknown Ingredient"
            )
            enriched_items.append(enriched_item)

        #4. Sort results alphabetically for consistency
        enriched_items.sort(key=lambda x: x.get("ingredient_name", ""))

        #5. Return the standardized success response
        return _build_success_response(enriched_items)
class AddItemToInventoryTool(Tool):
    """
    A tool to add an item to a household's inventory or update its quantity.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "AddItemToInventory",
                "description": (
                    "Adds an item to a household's inventory. If the ingredient already exists, "
                    "it updates the quantity. Otherwise, it creates a new inventory entry."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {
                            "type": "integer",
                            "description": "The unique ID for the household.",
                        },
                        "ingredient_id": {
                            "type": "integer",
                            "description": "The unique ID of the ingredient to add.",
                        },
                        "quantity": {
                            "type": "number",
                            "description": "The quantity of the ingredient to add.",
                        },
                        "unit": {
                            "type": "string",
                            "description": "The unit of measurement for the quantity.",
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user performing the action, for auditing.",
                        },
                    },
                    "required": ["household_id", "ingredient_id", "quantity", "unit"],
                },
            },
        }

    @staticmethod
    def invoke(
        data: dict[str, Any],
        household_id: int,
        ingredient_id: int,
        quantity: float,
        unit: str,
        user_id: int = None
    ) -> dict[str, Any]:
        """
        Executes the logic to add or update an inventory item.

        Args:
            data: The main in-memory dictionary containing all datasets.
            household_id: The ID of the household.
            ingredient_id: The ID of the ingredient.
            quantity: The quantity of the ingredient.
            unit: The unit of measurement for the quantity.
            user_id: The ID of the user (optional).

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the final state of the inventory item.
        """
        #1. Validate Inputs
        param_definitions = {
            "household_id": {"type": int, "required": True},
            "ingredient_id": {"type": int, "required": True},
            "quantity": {"type": (int, float), "required": True},
            "unit": {"type": str, "required": True},
            "user_id": {"type": int, "required": False},
        }
        validation_error = _validate_inputs(
            {
                "household_id": household_id,
                "ingredient_id": ingredient_id,
                "quantity": quantity,
                "unit": unit,
                "user_id": user_id,
            },
            param_definitions
        )
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Pre-condition Checks
        if not any(
            h.get("household_id") == household_id for h in data.get("households", [])
        ):
            return _build_error_response(
                "NOT_FOUND", {"entity": "Household", "entity_id": household_id}
            )
        if not any(
            i.get("ingredient_id") == ingredient_id for i in data.get("ingredients", [])
        ):
            return _build_error_response(
                "NOT_FOUND", {"entity": "Ingredient", "entity_id": ingredient_id}
            )

        #3. Logic: Find existing item or prepare for creation
        inventory_table = data.setdefault("inventory_items", [])
        existing_item = next(
            (
                item
                for item in inventory_table
                if item.get("household_id") == household_id
                and item.get("ingredient_id") == ingredient_id
            ),
            None,
        )

        context = {"ingredients": data.get("ingredients", [])}

        if existing_item:
            action = "update"
            normalized_addition = _normalize_domain_data(
                "unit_measurement",
                {"ingredient_id": ingredient_id, "quantity": quantity, "unit": unit},
                context,
            )

            normalized_existing = _normalize_domain_data(
                "unit_measurement", existing_item, context
            )

            #Now that both are in the standard unit, we can safely add them
            new_total_quantity = (
                normalized_existing["quantity"] + normalized_addition["quantity"]
            )

            existing_item["quantity"] = round(new_total_quantity, 2)
            existing_item["unit"] = normalized_existing[
                "unit"
            ]  #Store in the standard unit

            final_record = existing_item
            entity_id = existing_item["inv_item_id"]
        else:
            #Create new item (normalize the input for consistency)
            action = "create"
            normalized_input = _normalize_domain_data(
                "unit_measurement",
                {"ingredient_id": ingredient_id, "quantity": quantity, "unit": unit},
                context,
            )

            max_id = max(
                (i.get("inv_item_id", 0) for i in inventory_table), default=7000
            )
            new_item_id = max_id + 1

            new_record = {
                "inv_item_id": new_item_id,
                "household_id": household_id,
                "ingredient_id": ingredient_id,
                "quantity": normalized_input["quantity"],
                "unit": normalized_input["unit"],
                "location_enum": "pantry",  #Default location
                "best_by_date": None,
            }
            inventory_table.append(new_record)
            final_record = new_record
            entity_id = new_item_id

        #4. Auditing
        _log_audit_event(
            data=data,
            household_id=household_id,
            user_id=user_id,
            entity_type="inventory_items",
            entity_id=entity_id,
            action_enum=action,
            payload_json={
                "ingredient_id": ingredient_id,
                "quantity_added": quantity,
                "unit": unit,
            },
        )

        #5. Response
        return _build_success_response(final_record)
class UseItemFromInventoryTool(Tool):
    """
    A tool to decrease the quantity of an item in a household's inventory.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "UseItemFromInventory",
                "description": (
                    "Decreases the quantity of a specific ingredient in a household's inventory. "
                    "If the used quantity is greater than or equal to the available quantity, the item is removed."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {
                            "type": "integer",
                            "description": "The unique ID for the household.",
                        },
                        "ingredient_id": {
                            "type": "integer",
                            "description": "The unique ID of the ingredient to use.",
                        },
                        "quantity": {
                            "type": "number",
                            "description": "The quantity of the ingredient that was used.",
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user performing the action, for auditing.",
                        },
                    },
                    "required": ["household_id", "ingredient_id", "quantity"],
                },
            },
        }

    @staticmethod
    def invoke(
        data: dict[str, Any],
        household_id: int,
        ingredient_id: int,
        quantity: float,
        user_id: int = None
    ) -> dict[str, Any]:
        """
        Executes the logic to consume an inventory item.

        Args:
            data: The main in-memory dictionary containing all datasets.
            household_id: The ID of the household.
            ingredient_id: The ID of the ingredient.
            quantity: The quantity to be used.
            user_id: The ID of the user (optional).

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the updated item or a removal confirmation.
        """
        #1. Validate Inputs
        param_definitions = {
            "household_id": {"type": int, "required": True},
            "ingredient_id": {"type": int, "required": True},
            "quantity": {"type": (int, float), "required": True},
            "user_id": {"type": int, "required": False},
        }
        validation_error = _validate_inputs(
            {
                "household_id": household_id,
                "ingredient_id": ingredient_id,
                "quantity": quantity,
                "user_id": user_id,
            },
            param_definitions
        )
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        inventory_table = data.get("inventory_items", [])

        #2. Find the item in inventory
        item_to_use = next(
            (
                item
                for item in inventory_table
                if item.get("household_id") == household_id
                and item.get("ingredient_id") == ingredient_id
            ),
            None,
        )

        if not item_to_use:
            return _build_error_response(
                "NOT_FOUND",
                {
                    "entity": "Inventory Item",
                    "entity_id": f"for ingredient {ingredient_id}",
                },
            )

        #3. Logic: Decrement quantity or remove item
        current_quantity = item_to_use.get("quantity", 0)
        item_id = item_to_use.get("inv_item_id")

        payload = {"ingredient_id": ingredient_id, "quantity_used": quantity}

        if quantity >= current_quantity:
            #Item is fully consumed
            action = "delete"
            #Log a copy of the item before it's deleted
            _log_audit_event(
                data=data,
                household_id=household_id,
                user_id=user_id,
                entity_type="inventory_items",
                entity_id=item_id,
                action_enum=action,
                payload_json=payload,
            )
            #Rebuild the list without the removed item
            data["inventory_items"] = [
                item for item in inventory_table if item.get("inv_item_id") != item_id
            ]
            response_data = {"status": "item_removed", "removed_item": item_to_use}
        else:
            #Item is partially consumed
            action = "update"
            item_to_use["quantity"] -= quantity
            _log_audit_event(
                data=data,
                household_id=household_id,
                user_id=user_id,
                entity_type="inventory_items",
                entity_id=item_id,
                action_enum=action,
                payload_json=payload,
            )
            response_data = item_to_use

        #4. Response
        return _build_success_response(response_data)
class RemoveItemFromInventoryTool(Tool):
    """
    A tool to explicitly remove an item from a household's inventory.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "RemoveItemFromInventory",
                "description": (
                    "Explicitly removes an entire item from inventory. Useful for scenarios "
                    "like discarding expired food. Identify the item either by its unique 'inv_item_id' "
                    "or by the combination of 'household_id' and 'ingredient_id'."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inv_item_id": {
                            "type": "integer",
                            "description": "The unique ID of the inventory item to remove.",
                        },
                        "household_id": {
                            "type": "integer",
                            "description": "The household ID, used with ingredient_id if inv_item_id is absent.",
                        },
                        "ingredient_id": {
                            "type": "integer",
                            "description": "The ingredient ID, used with household_id if inv_item_id is absent.",
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user performing the action, for auditing.",
                        },
                    },
                    "required": [],
                },
            },
        }

    @staticmethod
    def invoke(
        data: dict[str, Any],
        inv_item_id: int = None,
        household_id: int = None,
        ingredient_id: int = None,
        user_id: int = None
    ) -> dict[str, Any]:
        """
        Executes the logic to find and explicitly remove an inventory item.

        Args:
            data: The main in-memory dictionary containing all datasets.
            inv_item_id: The inventory item ID.
            household_id: The household ID.
            ingredient_id: The ingredient ID.
            user_id: The user ID.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the item that was removed.
        """
        #1. Validate Input Types
        param_definitions = {
            "inv_item_id": {"type": int, "required": False},
            "household_id": {"type": int, "required": False},
            "ingredient_id": {"type": int, "required": False},
            "user_id": {"type": int, "required": False},
        }
        validation_error = _validate_inputs(
            {
                "inv_item_id": inv_item_id,
                "household_id": household_id,
                "ingredient_id": ingredient_id,
                "user_id": user_id
            },
            param_definitions
        )
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Specific Validation: Ensure at least one identification method is provided
        if not inv_item_id and not (household_id and ingredient_id):
            return _build_error_response(
                "REQUIRED_PARAMETER",
                {"param": "'inv_item_id' or both 'household_id' and 'ingredient_id'"},
            )

        #3. Find the item to remove
        inventory_table = data.get("inventory_items", [])
        item_to_remove = None
        if inv_item_id:
            item_to_remove = next(
                (
                    item
                    for item in inventory_table
                    if item.get("inv_item_id") == inv_item_id
                ),
                None,
            )
        else:
            item_to_remove = next(
                (
                    item
                    for item in inventory_table
                    if item.get("household_id") == household_id
                    and item.get("ingredient_id") == ingredient_id
                ),
                None,
            )

        if not item_to_remove:
            return _build_error_response(
                "NOT_FOUND",
                {
                    "entity": "Inventory Item",
                    "entity_id": inv_item_id or f"for ingredient {ingredient_id}",
                },
            )

        #4. Auditing (before the data is removed)
        item_id_to_remove = item_to_remove["inv_item_id"]
        _log_audit_event(
            data=data,
            household_id=item_to_remove.get("household_id"),
            user_id=user_id,
            entity_type="inventory_items",
            entity_id=item_id_to_remove,
            action_enum="delete",
            payload_json=item_to_remove,  #Log the full record being deleted
        )

        #5. Perform the removal
        data["inventory_items"] = [
            item
            for item in inventory_table
            if item.get("inv_item_id") != item_id_to_remove
        ]

        #6. Response
        return _build_success_response(
            {"status": "success", "removed_item": item_to_remove}
        )
class GenerateGroceryListFromMealPlanTool(Tool):
    """
    A tool to create an optimized grocery list from a meal plan and inventory.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "GenerateGroceryListFromMealPlan",
                "description": (
                    "Creates a new grocery list by calculating ingredients needed for a meal plan, "
                    "subtracting items already in the household's inventory."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_plan_id": {
                            "type": "integer",
                            "description": "The unique ID for the meal plan.",
                        },
                        "household_id": {
                            "type": "integer",
                            "description": "The unique ID for the household the plan belongs to.",
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user creating the list, for auditing.",
                        },
                    },
                    "required": ["meal_plan_id", "household_id", "user_id"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], meal_plan_id: int, household_id: int, user_id: int) -> dict[str, Any]:
        """
        Executes the logic to generate an optimized grocery list.

        Args:
            data: The main in-memory dictionary containing all datasets.
            meal_plan_id: The ID of the meal plan.
            household_id: The ID of the household.
            user_id: The ID of the user.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the ID of the new list and its item IDs.
        """
        pass
        #1. Validate Inputs
        param_definitions = {
            "meal_plan_id": {"type": int, "required": True},
            "household_id": {"type": int, "required": True},
            "user_id": {"type": int, "required": True},
        }
        validation_error = _validate_inputs({"meal_plan_id": meal_plan_id, "household_id": household_id, "user_id": user_id}, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Pre-condition Checks
        meal_plan = next(
            (
                p
                for p in data.get("meal_plans", [])
                if p.get("meal_plan_id") == meal_plan_id
            ),
            None,
        )
        if not meal_plan:
            return _build_error_response(
                "NOT_FOUND", {"entity": "MealPlan", "entity_id": meal_plan_id}
            )
        if meal_plan.get("household_id") != household_id:
            return _build_error_response(
                "UNSUPPORTED_OPERATION",
                {
                    "operation": "Generate List",
                    "entity": "MealPlan does not belong to the specified household.",
                },
            )

        #3. Core Logic: Calculate Net Needs
        all_ingredients_meta = data.get("ingredients", [])
        context = {"ingredients": all_ingredients_meta}

        #3a. Aggregate all required ingredients for the plan, normalizing units
        plan_entries = [
            e
            for e in data.get("meal_plan_entries", [])
            if e.get("meal_plan_id") == meal_plan_id
        ]
        recipe_ids = {e["recipe_id"] for e in plan_entries}
        required_ingredients_list = [
            ri
            for ri in data.get("recipe_ingredients", [])
            if ri["recipe_id"] in recipe_ids
        ]

        required_totals = collections.defaultdict(float)
        for req in required_ingredients_list:
            normalized_req = _normalize_domain_data("unit_measurement", req, context)
            required_totals[normalized_req["ingredient_id"]] += normalized_req[
                "quantity"
            ]

        #3b. Get available inventory, normalizing units
        inventory_items = [
            i
            for i in data.get("inventory_items", [])
            if i.get("household_id") == household_id
        ]
        available_totals = collections.defaultdict(float)
        for item in inventory_items:
            normalized_item = _normalize_domain_data("unit_measurement", item, context)
            available_totals[normalized_item["ingredient_id"]] += normalized_item[
                "quantity"
            ]

        #3c. Calculate what needs to be bought
        net_needed_items = []
        for ingredient_id, required_qty in required_totals.items():
            needed_qty = required_qty - available_totals.get(ingredient_id, 0)
            if needed_qty > 0:
                ingredient_meta = next(
                    (
                        i
                        for i in all_ingredients_meta
                        if i["ingredient_id"] == ingredient_id
                    ),
                    {},
                )
                net_needed_items.append(
                    {
                        "ingredient_id": ingredient_id,
                        "quantity": round(needed_qty, 2),
                        "unit": ingredient_meta.get("default_unit", "units"),
                        "grocery_section": ingredient_meta.get(
                            "grocery_section", "Misc"
                        ),
                        "pantry_staple_flag": ingredient_meta.get(
                            "pantry_staple_flag", False
                        ),
                    }
                )

        #4. Create Grocery List and Items
        gl_table = data.setdefault("grocery_lists", [])
        max_list_id = max(
            (g.get("list_id", 0) for g in gl_table),
            default=DEFAULT_BUSINESS_RULES["INITIAL_ID_DEFAULTS"]["grocery_lists"],
        )
        new_list_id = max_list_id + 1

        timestamp = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
        new_list_record = {
            "list_id": new_list_id,
            "household_id": household_id,
            "source_meal_plan_id": meal_plan_id,
            "created_by_user_id": user_id,
            "created_at": timestamp,
            "status_enum": "initialized",
        }
        gl_table.append(new_list_record)

        gli_table = data.setdefault("grocery_list_items", [])
        max_item_id = max(
            (i.get("item_id", 0) for i in gli_table),
            default=DEFAULT_BUSINESS_RULES["INITIAL_ID_DEFAULTS"]["grocery_list_items"],
        )
        created_item_ids = []

        for item in net_needed_items:
            max_item_id += 1
            new_item_record = {
                "item_id": max_item_id,
                "list_id": new_list_id,
                "overlap_last_month_flag": False,
                **item,
            }
            gli_table.append(new_item_record)
            created_item_ids.append(max_item_id)

        #5. Auditing
        _log_audit_event(
            data,
            household_id=household_id,
            user_id=user_id,
            entity_type="grocery_lists",
            entity_id=new_list_id,
            action_enum="create",
            payload_json={"source_meal_plan_id": meal_plan_id},
        )

        #6. Response
        return _build_success_response(
            {
                "list_id": new_list_id,
                "items_added_count": len(created_item_ids),
                "created_item_ids": created_item_ids,
            }
        )
class GetGroceryListDetailsTool(Tool):
    """
    A tool to retrieve the full details of a grocery list, including its items.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetGroceryListDetails",
                "description": "Retrieves a grocery list and all its items, enriched with ingredient names, by its unique ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "integer",
                            "description": "The unique identifier for the grocery list to retrieve.",
                        }
                    },
                    "required": ["list_id"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], list_id: int) -> dict[str, Any]:
        """
        Executes the logic to fetch and enrich a full grocery list.

        Args:
            data: The main in-memory dictionary containing all datasets.
            list_id: The ID of the grocery list to fetch.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the fully detailed grocery list object.
        """
        #1. Validate Inputs
        param_definitions = {"list_id": {"type": int, "required": True}}
        validation_error = _validate_inputs({"list_id": list_id}, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Data Retrieval: Find the base grocery list object
        list_record = next(
            (g for g in data.get("grocery_lists", []) if g.get("list_id") == list_id),
            None,
        )

        if not list_record:
            return _build_error_response(
                "NOT_FOUND", {"entity": "GroceryList", "entity_id": list_id}
            )

        #3. Data Enrichment (Hydration): Fetch and enrich list items
        list_items = [
            item
            for item in data.get("grocery_list_items", [])
            if item.get("list_id") == list_id
        ]

        enriched_items = []
        all_ingredients_meta = data.get("ingredients", [])
        for item in list_items:
            ingredient_meta = next(
                (
                    i
                    for i in all_ingredients_meta
                    if i.get("ingredient_id") == item.get("ingredient_id")
                ),
                None,
            )
            enriched_item = item.copy()
            enriched_item["ingredient_name"] = (
                ingredient_meta.get("ingredient_name")
                if ingredient_meta
                else "Unknown Ingredient"
            )
            enriched_items.append(enriched_item)

        #Sort items by grocery section for a more organized list
        enriched_items.sort(
            key=lambda x: (x.get("grocery_section", ""), x.get("ingredient_name", ""))
        )

        #4. Build the final response object
        detailed_list = list_record.copy()
        detailed_list["items"] = enriched_items

        #5. Return the standardized success response
        return _build_success_response(detailed_list)
class AddItemToGroceryListTool(Tool):
    """
    A tool to add a single item to an existing grocery list.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "AddItemToGroceryList",
                "description": (
                    "Adds a single ingredient to a grocery list. If the ingredient already "
                    "exists on the list, its quantity is updated. Otherwise, a new item is created."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "integer",
                            "description": "The unique ID for the grocery list to modify.",
                        },
                        "ingredient_id": {
                            "type": "integer",
                            "description": "The unique ID of the ingredient to add.",
                        },
                        "quantity": {
                            "type": "number",
                            "description": "The quantity of the ingredient to add.",
                        },
                        "unit": {
                            "type": "string",
                            "description": "The unit of measurement for the quantity.",
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user performing the action, for auditing.",
                        },
                    },
                    "required": ["list_id", "ingredient_id", "quantity", "unit"],
                },
            },
        }

    @staticmethod
    def invoke(
        data: dict[str, Any],
        list_id: int,
        ingredient_id: int,
        quantity: float,
        unit: str,
        user_id: int = None
    ) -> dict[str, Any]:
        """
        Executes the logic to add or update a grocery list item.

        Args:
            data: The main in-memory dictionary containing all datasets.
            list_id: The ID of the grocery list.
            ingredient_id: The ID of the ingredient.
            quantity: The quantity of the ingredient.
            unit: The unit of the ingredient.
            user_id: The ID of the user (optional).

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the final state of the grocery list item.
        """
        pass
        #1. Validate Inputs
        param_definitions = {
            "list_id": {"type": int, "required": True},
            "ingredient_id": {"type": int, "required": True},
            "quantity": {"type": (int, float), "required": True},
            "unit": {"type": str, "required": True},
            "user_id": {"type": int, "required": False},
        }
        validation_error = _validate_inputs(
            {
                "list_id": list_id,
                "ingredient_id": ingredient_id,
                "quantity": quantity,
                "unit": unit,
                "user_id": user_id
            },
            param_definitions
        )
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Pre-condition Checks
        if not any(g.get("list_id") == list_id for g in data.get("grocery_lists", [])):
            return _build_error_response(
                "NOT_FOUND", {"entity": "GroceryList", "entity_id": list_id}
            )
        ingredient_meta = next(
            (
                i
                for i in data.get("ingredients", [])
                if i.get("ingredient_id") == ingredient_id
            ),
            None,
        )
        if not ingredient_meta:
            return _build_error_response(
                "NOT_FOUND", {"entity": "Ingredient", "entity_id": ingredient_id}
            )

        #3. Logic: Find existing item or prepare for creation
        gli_table = data.setdefault("grocery_list_items", [])
        existing_item = next(
            (
                item
                for item in gli_table
                if item.get("list_id") == list_id
                and item.get("ingredient_id") == ingredient_id
            ),
            None,
        )

        list_record = next(
            g for g in data.get("grocery_lists", []) if g.get("list_id") == list_id
        )
        household_id = list_record.get("household_id")

        if existing_item:
            #Update existing item
            action = "update"
            #For simplicity, we assume units are compatible and just add quantity.
            #A more advanced normalizer could handle unit conversions.
            existing_item["quantity"] += quantity
            final_record = existing_item
            entity_id = existing_item["item_id"]
        else:
            #Create new item
            action = "create"
            max_id = max(
                (i.get("item_id", 0) for i in gli_table),
                default=DEFAULT_BUSINESS_RULES["INITIAL_ID_DEFAULTS"][
                    "grocery_list_items"
                ],
            )
            new_item_id = max_id + 1

            new_record = {
                "item_id": new_item_id,
                "list_id": list_id,
                "ingredient_id": ingredient_id,
                "quantity": quantity,
                "unit": unit,
                "grocery_section": ingredient_meta.get("grocery_section", "Misc"),
                "pantry_staple_flag": ingredient_meta.get("pantry_staple_flag", False),
                "overlap_last_month_flag": False,  #Cannot be determined here
            }
            gli_table.append(new_record)
            final_record = new_record
            entity_id = new_item_id

        #4. Auditing
        _log_audit_event(
            data=data,
            household_id=household_id,
            user_id=user_id,
            entity_type="grocery_list_items",
            entity_id=entity_id,
            action_enum=action,
            payload_json={
                "ingredient_id": ingredient_id,
                "quantity_added": quantity,
                "unit": unit,
            },
        )

        #5. Response
        return _build_success_response(final_record)
class CheckProductAvailabilityAtStoreTool(Tool):
    """
    A tool to check product availability for a grocery list at a specific store.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "CheckProductAvailabilityAtStore",
                "description": (
                    "Checks the stock status for each item on a grocery list at a specific store. "
                    "Returns a list of items that are low in stock or out of stock."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "integer",
                            "description": "The unique ID for the grocery list to check.",
                        },
                        "store_id": {
                            "type": "integer",
                            "description": "The unique ID of the store to check against.",
                        },
                    },
                    "required": ["list_id", "store_id"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], list_id: int, store_id: int) -> dict[str, Any]:
        """
        Executes the logic to check store inventory against a grocery list.

        Args:
            data: The main in-memory dictionary containing all datasets.
            list_id: The ID of the grocery list to check.
            store_id: The ID of the store to check against.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains a list of items with potential stock issues.
        """
        #1. Validate Inputs
        param_definitions = {
            "list_id": {"type": int, "required": True},
            "store_id": {"type": int, "required": True},
        }
        validation_error = _validate_inputs({"list_id": list_id, "store_id": store_id}, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Pre-condition Checks
        if not any(g.get("list_id") == list_id for g in data.get("grocery_lists", [])):
            return _build_error_response(
                "NOT_FOUND", {"entity": "GroceryList", "entity_id": list_id}
            )
        if not any(s.get("store_id") == store_id for s in data.get("stores", [])):
            return _build_error_response(
                "NOT_FOUND", {"entity": "Store", "entity_id": store_id}
            )

        #3. Core Logic
        list_items = [
            item
            for item in data.get("grocery_list_items", [])
            if item.get("list_id") == list_id
        ]
        all_store_products = data.get("store_products", [])
        all_ingredients_meta = data.get("ingredients", [])

        problem_items = []
        for item in list_items:
            ingredient_id = item["ingredient_id"]

            #Find all products at the store for this ingredient
            candidate_products = [
                p
                for p in all_store_products
                if p.get("store_id") == store_id
                and p.get("ingredient_id") == ingredient_id
            ]

            #Find the best available product (in stock or low, and cheapest)
            in_stock_products = [
                p
                for p in candidate_products
                if p.get("stock_status_enum") in ("in_stock", "low")
            ]

            best_product = None
            if in_stock_products:
                best_product = min(
                    in_stock_products, key=lambda p: p.get("price_cents", float("inf"))
                )

            status = ""
            if not best_product:
                status = "out_of_stock"
            elif best_product.get("stock_status_enum") == "low":
                status = "low_stock"

            if status:
                ingredient_meta = next(
                    (
                        i
                        for i in all_ingredients_meta
                        if i["ingredient_id"] == ingredient_id
                    ),
                    {},
                )
                problem_items.append(
                    {
                        "ingredient_id": ingredient_id,
                        "ingredient_name": ingredient_meta.get(
                            "ingredient_name", "Unknown"
                        ),
                        "status": status,
                    }
                )

        #4. Response
        return _build_success_response(problem_items)
class FindSubstituteProductsTool(Tool):
    """
    A tool to find available in-stock substitutes for out-of-stock items.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "FindSubstituteProducts",
                "description": (
                    "For a given list of out-of-stock or low-stock ingredients at a specific store, "
                    "suggests available in-stock products as substitutes based on a predefined knowledge base."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {
                            "type": "integer",
                            "description": "The unique ID of the store where the check is being performed.",
                        },
                        "problem_items": {
                            "type": "array",
                            "items": {"type": "object"},
                            "description": "The list of items with stock issues, from the 'check_product_availability_at_store' tool.",
                        },
                    },
                    "required": ["store_id", "problem_items"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], store_id: int, problem_items: list) -> dict[str, Any]:
        """
        Executes the logic to find viable, in-stock substitute products.

        Args:
            data: The main in-memory dictionary containing all datasets.
            store_id: The ID of the store.
            problem_items: A list of problem items.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains a list of substitution suggestions.
        """
        #1. Validate Inputs
        param_definitions = {
            "store_id": {"type": int, "required": True},
            "problem_items": {"type": list, "required": True},
        }
        validation_error = _validate_inputs({"store_id": store_id, "problem_items": problem_items}, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Pre-condition Check
        if not any(s.get("store_id") == store_id for s in data.get("stores", [])):
            return _build_error_response(
                "NOT_FOUND", {"entity": "Store", "entity_id": store_id}
            )

        #3. Core Logic
        suggestions = []
        all_store_products = data.get("store_products", [])

        for item in problem_items:
            original_ingredient_id = item.get("ingredient_id")

            #Find substitution rules for the problematic ingredient
            substitute_options = INGREDIENT_SUBSTITUTE_MAP.get(
                original_ingredient_id, []
            )

            for sub_ingredient_id in substitute_options:
                #Find all products for the substitute ingredient at the store
                candidate_products = [
                    p
                    for p in all_store_products
                    if p.get("store_id") == store_id
                    and p.get("ingredient_id") == sub_ingredient_id
                ]

                #Find the best available option (in stock and cheapest)
                in_stock_products = [
                    p
                    for p in candidate_products
                    if p.get("stock_status_enum") in ("in_stock", "low")
                ]

                if in_stock_products:
                    best_sub_product = min(
                        in_stock_products,
                        key=lambda p: p.get("price_cents", float("inf")),
                    )

                    suggestions.append(
                        {
                            "original_ingredient_id": original_ingredient_id,
                            "substitute_ingredient_id": sub_ingredient_id,
                            "substitute_product_id": best_sub_product["product_id"],
                            "substitute_product_name": best_sub_product.get(
                                "product_name"
                            ),
                            "price_cents": best_sub_product.get("price_cents"),
                        }
                    )
                    #Found a valid substitute, stop searching for this item
                    break

        #4. Response
        return _build_success_response(suggestions)
class PlaceGroceryOrderTool(Tool):
    """
    A tool to create a formal order from a grocery list for a specific store.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "PlaceGroceryOrder",
                "description": "Places a grocery order from a list for a store, creating order and order_item records.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {
                            "type": "integer",
                            "description": "The unique ID for the household placing the order.",
                        },
                        "store_id": {
                            "type": "integer",
                            "description": "The unique ID of the store to order from.",
                        },
                        "list_id": {
                            "type": "integer",
                            "description": "The unique ID of the grocery list to use.",
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "The ID of the user placing the order.",
                        },
                        "substitutions": {
                            "type": "array",
                            "description": "Optional list of substitutions for out-of-stock items.",
                        },
                    },
                    "required": ["household_id", "store_id", "list_id", "user_id"],
                },
            },
        }

    @staticmethod
    def invoke(
        data: dict[str, Any],
        household_id: int,
        store_id: int,
        list_id: int,
        user_id: int,
        substitutions: list = None
    ) -> dict[str, Any]:
        """
        Executes the logic to create order and order_item records.

        Args:
            data: The main in-memory dictionary containing all datasets.
            household_id: The ID of the household placing the order.
            store_id: The ID of the store where the order is placed.
            list_id: The ID of the grocery list being ordered.
            user_id: The ID of the user placing the order.
            substitutions: A list of substitutions for the order.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the newly created and calculated order object.
        """
        pass
        #1. Validate Inputs
        param_definitions = {
            "household_id": {"type": int, "required": True},
            "store_id": {"type": int, "required": True},
            "list_id": {"type": int, "required": True},
            "user_id": {"type": int, "required": True},
            "substitutions": {"type": list, "required": False},
        }
        validation_error = _validate_inputs(
            {
                "household_id": household_id,
                "store_id": store_id,
                "list_id": list_id,
                "user_id": user_id,
                "substitutions": substitutions,
            },
            param_definitions
        )
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Pre-condition Checks
        list_record = next(
            (g for g in data.get("grocery_lists", []) if g.get("list_id") == list_id),
            None,
        )
        if not list_record:
            return _build_error_response(
                "NOT_FOUND", {"entity": "GroceryList", "entity_id": list_id}
            )
        if list_record.get("status_enum") == "ordered":
            return _build_error_response(
                "UNSUPPORTED_OPERATION",
                {
                    "operation": "Place Order",
                    "entity": f"GroceryList {list_id} has already been ordered.",
                },
            )

        #3. Core Logic
        #3a. Create the main Order record
        orders_table = data.setdefault("orders", [])
        max_order_id = max(
            (o.get("order_id", 0) for o in orders_table),
            default=DEFAULT_BUSINESS_RULES["INITIAL_ID_DEFAULTS"]["orders"],
        )
        new_order_id = max_order_id + 1

        timestamp = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
        #Simplification for scheduling: next day between 6-8 PM
        delivery_start = (
            (datetime.now(timezone.utc) + timedelta(days=1))
            .replace(hour=18, minute=0, second=0, microsecond=0)
            .isoformat()
            .replace("+00:00", "Z")
        )
        delivery_end = (
            (datetime.now(timezone.utc) + timedelta(days=1))
            .replace(hour=20, minute=0, second=0, microsecond=0)
            .isoformat()
            .replace("+00:00", "Z")
        )

        new_order_record = {
            "order_id": new_order_id,
            "household_id": household_id,
            "store_id": store_id,
            "list_id": list_id,
            "status_enum": "placed",
            "subtotal_cents": 0,
            "total_cents": 0,
            "placed_ts": timestamp,
            "scheduled_slot_start_ts": delivery_start,
            "scheduled_slot_end_ts": delivery_end,
        }

        #3b. Create Order Items and calculate subtotal
        sub_map = {
            s["original_ingredient_id"]: s["substitute_product_id"]
            for s in (substitutions or [])
        }
        list_items = [
            item
            for item in data.get("grocery_list_items", [])
            if item.get("list_id") == list_id
        ]
        oi_table = data.setdefault("order_items", [])
        max_oi_id = max(
            (oi.get("order_item_id", 0) for oi in oi_table),
            default=DEFAULT_BUSINESS_RULES["INITIAL_ID_DEFAULTS"]["order_items"],
        )

        subtotal_cents = 0
        for item in list_items:
            ingredient_id = item["ingredient_id"]
            product_id_to_add = sub_map.get(ingredient_id)
            substitute_product_id_for_log = None

            if product_id_to_add:
                substitute_product_id_for_log = product_id_to_add
            else:
                #Find the best in-stock product if no substitution was provided
                candidate_products = [
                    p
                    for p in data.get("store_products", [])
                    if p.get("store_id") == store_id
                    and p.get("ingredient_id") == ingredient_id
                    and p.get("stock_status_enum") in ("in_stock", "low")
                ]
                if not candidate_products:
                    continue  #Skip item if not available and not substituted
                product_id_to_add = min(
                    candidate_products, key=lambda p: p.get("price_cents", float("inf"))
                )["product_id"]

            product_record = next(
                (
                    p
                    for p in data.get("store_products", [])
                    if p.get("product_id") == product_id_to_add
                ),
                None,
            )
            if not product_record:
                continue

            max_oi_id += 1
            oi_table.append(
                {
                    "order_item_id": max_oi_id,
                    "order_id": new_order_id,
                    "product_id": product_id_to_add,
                    "requested_qty": 1,
                    "fulfilled_qty": 1,
                    "substitute_product_id": substitute_product_id_for_log,
                }
            )
            subtotal_cents += product_record.get("price_cents", 0)

        #3c. Finalize totals and update statuses
        new_order_record["subtotal_cents"] = subtotal_cents
        new_order_record["total_cents"] = (
            subtotal_cents + DEFAULT_BUSINESS_RULES["DEFAULT_ORDER_FEE_CENTS"]
        )
        orders_table.append(new_order_record)
        list_record["status_enum"] = "ordered"

        #4. Auditing
        _log_audit_event(
            data,
            household_id=household_id,
            user_id=user_id,
            entity_type="orders",
            entity_id=new_order_id,
            action_enum="create",
            payload_json={"list_id": list_id, "store_id": store_id},
        )

        #5. Response
        return _build_success_response(new_order_record)
class GetOrderStatusTool(Tool):
    """
    A tool to retrieve the status and details of a grocery order.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetOrderStatus",
                "description": "Retrieves the full details of a grocery order, including its status and all line items enriched with product names.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "integer",
                            "description": "The unique identifier for the order to retrieve.",
                        }
                    },
                    "required": ["order_id"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], order_id: int) -> dict[str, Any]:
        """
        Executes the logic to find and return the details of an order.

        Args:
            data: The main in-memory dictionary containing all datasets.
            order_id: The ID of the order to retrieve.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the fully detailed and hydrated order object.
        """
        #1. Validate Inputs
        param_definitions = {"order_id": {"type": int, "required": True}}
        validation_error = _validate_inputs({"order_id": order_id}, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Data Retrieval
        order_record = next(
            (o for o in data.get("orders", []) if o.get("order_id") == order_id), None
        )

        if not order_record:
            return _build_error_response(
                "NOT_FOUND", {"entity": "Order", "entity_id": order_id}
            )

        #3. Data Enrichment (Hydration)
        order_items = [
            item
            for item in data.get("order_items", [])
            if item.get("order_id") == order_id
        ]
        all_products = data.get("store_products", [])

        enriched_items = []
        for item in order_items:
            enriched_item = item.copy()

            #Enrich with the main product name
            product_info = next(
                (
                    p
                    for p in all_products
                    if p.get("product_id") == item.get("product_id")
                ),
                None,
            )
            enriched_item["product_name"] = (
                product_info.get("product_name") if product_info else "Unknown Product"
            )

            #Enrich with the substitute product name, if applicable
            sub_id = item.get("substitute_product_id")
            if sub_id:
                sub_info = next(
                    (p for p in all_products if p.get("product_id") == sub_id), None
                )
                enriched_item["substitute_product_name"] = (
                    sub_info.get("product_name") if sub_info else "Unknown Substitute"
                )

            enriched_items.append(enriched_item)

        #4. Build the final response object
        detailed_order = order_record.copy()
        detailed_order["items"] = enriched_items

        #5. Return the standardized success response
        return _build_success_response(detailed_order)
#==============================================================================
#4. Tool Manifest
#==============================================================================


TOOLS = [
    #Household & User Management
    GetHouseholdProfileTool(),
    ListHouseholdMembersTool(),
    GetMemberDetailsTool(),
    UpdateMemberPreferencesTool(),
    AddHouseholdMemberTool(),
    #Recipe & Ingredient Management
    SearchRecipesTool(),
    GetRecipeDetailsTool(),
    FindRecipesByIngredientsTool(),
    GetIngredientInfoTool(),
    GetRecipeSubstitutionsTool(),
    AddNewRecipeTool(),
    #Meal Planning
    GetMealHistoryTool(),
    LogMealAsPreparedTool(),
    CreateMealPlanTool(),
    AddRecipeToMealPlanTool(),
    GetMealPlanForWeekTool(),
    UpdateMealPlanEntryTool(),
    RemoveRecipeFromMealPlanTool(),
    #Inventory Management
    GetHouseholdInventoryTool(),
    AddItemToInventoryTool(),
    UseItemFromInventoryTool(),
    RemoveItemFromInventoryTool(),
    #Grocery & Ordering
    GenerateGroceryListFromMealPlanTool(),
    GetGroceryListDetailsTool(),
    AddItemToGroceryListTool(),
    CheckProductAvailabilityAtStoreTool(),
    FindSubstituteProductsTool(),
    PlaceGroceryOrderTool(),
    GetOrderStatusTool(),
]
