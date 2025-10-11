# Sierra copyright.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ValidateUserIdentity(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str = None, first_name: str = None, last_name: str = None, ) -> str:
        """
        Simple validation to check if user exists in the system with optional name verification
        Can search by user_id OR by first_name and last_name combination
        Always includes comprehensive user location details in the response

        Data Sources: users.json (user_id, name, address)
        """
        # Check the validity of input parameters.
        if not user_id and (not first_name or not last_name):
            return json.dumps({
                "error": "Either user_id must be provided, or both first_name and last_name must be provided",
                "status": "failed"
            })

        users = list(data.get("users", {}).values())
        target_user = None
        search_method = "user_id" if user_id else "name_search"

        if user_id:
            # Requirement: Confirm the existence of user identity prior to handling any user requests.
            target_user = next((u for u in users if u.get("user_id") == user_id), None)

            if not target_user:
                return json.dumps({
                    "error": f"User {user_id} not found",
                    "status": "failed",
                    "user_exists": False,
                    "search_method": search_method
                })
        else:
            # Query based on first_name and last_name.
            matching_users = []

            for user in users:
                user_name = user.get("name", {})
                stored_first_name = user_name.get("first_name", "").lower().strip()
                stored_last_name = user_name.get("last_name", "").lower().strip()

                provided_first_name = first_name.lower().strip()
                provided_last_name = last_name.lower().strip()

                if stored_first_name == provided_first_name and stored_last_name == provided_last_name:
                    matching_users.append(user)

            if not matching_users:
                return json.dumps({
                    "error": f"No user found with name '{first_name} {last_name}'",
                    "status": "failed",
                    "user_exists": False,
                    "search_method": search_method,
                    "search_criteria": {
                        "first_name": first_name,
                        "last_name": last_name
                    }
                })

            if len(matching_users) > 1:
                # Duplicate users detected with identical names.
                user_ids = [user.get("user_id") for user in matching_users]
                return json.dumps({
                    "error": f"Multiple users found with name '{first_name} {last_name}'. Please specify user_id.",
                    "status": "multiple_matches",
                    "matching_user_ids": user_ids,
                    "total_matches": len(matching_users),
                    "search_method": search_method,
                    "search_criteria": {
                        "first_name": first_name,
                        "last_name": last_name
                    }
                })

            # One user detected
            target_user = matching_users[0]
            user_id = target_user.get("user_id")  # Assign user_id to the response.

        # Extra checks for first_name and last_name when searching using user_id, if they are supplied.
        validation_details = {"user_id_valid": True}
        user_name = target_user.get("name", {})
        stored_first_name = user_name.get("first_name", "")
        stored_last_name = user_name.get("last_name", "")
        stored_email = target_user.get("email", "")

        # Validate names only if both user_id and names are supplied for further confirmation.
        if search_method == "user_id":
            if first_name is not None:
                if stored_first_name.lower() != first_name.lower():
                    return json.dumps({
                        "error": f"First name mismatch for user {user_id}",
                        "status": "failed",
                        "user_exists": True,
                        "first_name_valid": False,
                        "search_method": search_method
                    })
                validation_details["first_name_valid"] = True

            if last_name is not None:
                if stored_last_name.lower() != last_name.lower():
                    return json.dumps({
                        "error": f"Last name mismatch for user {user_id}",
                        "status": "failed",
                        "user_exists": True,
                        "last_name_valid": False,
                        "search_method": search_method
                    })
                validation_details["last_name_valid"] = True
        else:
            # Names are considered valid for search since the user was located using their name.
            validation_details["first_name_valid"] = True
            validation_details["last_name_valid"] = True

        # Ensure to provide complete user location information in the response.
        user_address = target_user.get("address", {})

        user_location_details = {
            "address1": user_address.get("address1", ""),
            "address2": user_address.get("address2", ""),
            "city": user_address.get("city", ""),
            "state": user_address.get("state", ""),
            "zip": user_address.get("zip", ""),
            "country": user_address.get("country", "")
        }

        # Verify if the address is fully specified.
        required_address_fields = ["address1", "city", "state", "zip", "country"]
        address_complete = all(user_address.get(field) for field in required_address_fields)
        missing_fields = [field for field in required_address_fields if not user_address.get(field)]

        # Assess the status of address quality and completeness.
        address_status = "complete" if address_complete else "incomplete"
        if len(missing_fields) >= 4:
            address_status = "minimal"
        elif len(missing_fields) >= 2:
            address_status = "partial"

        # Verify if the location is eligible for delivery based on the couriers available.
        couriers = data.get("couriers", [])
        supported_countries = set()
        for courier in couriers:
            supported_countries.update(courier.get("coverage_area", []))

        destination_country = user_address.get("country", "")
        delivery_available = destination_country in supported_countries if destination_country else False

        return json.dumps({
            "status": "success",
            "user_exists": True,
            "user_id": user_id,
            "search_method": search_method,
            "validation_details": validation_details,
            "user_name": {
                "first_name": stored_first_name,
                "last_name": stored_last_name,
                "full_name": f"{stored_first_name} {stored_last_name}".strip()
            },
            "user_email": {
                "email": stored_email
            },
            "user_location": {
                "address_details": user_location_details,
                "address_status": address_status,
                "address_complete": address_complete,
                "missing_fields": missing_fields,
                "delivery_available": delivery_available,
                "supported_country": destination_country in supported_countries if destination_country else None
            }
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "validate_user_identity",
                "description": "Check if user exists in the system with optional name verification. Can search by user_id OR by first_name and last_name combination. Always returns comprehensive user details including complete location information and delivery availability.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "Customer identifier to validate (optional if first_name and last_name are provided)"},
                        "first_name": {"type": "string", "description": "First name for user search or additional validation (required if user_id not provided)"},
                        "last_name": {"type": "string", "description": "Last name for user search or additional validation (required if user_id not provided)"}
                    },
                    "anyOf": [
                        {"required": ["user_id"]},
                        {"required": ["first_name", "last_name"]}
                    ]
                }
            }
        }
