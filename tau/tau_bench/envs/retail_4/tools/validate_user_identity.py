from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ValidateUserIdentity(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str = None,
        first_name: str = None,
        last_name: str = None,
    ) -> str:
        """
        Simple validation to check if user exists in the system with optional name verification
        Can search by user_id OR by first_name and last_name combination
        Always includes comprehensive user location details in the response

        Data Sources: users.json (user_id, name, address)
        """
        _first_nameL = first_name or ''.lower()
        _last_nameL = last_name or ''.lower()
        pass
        #Validate input parameters
        if not user_id and (not first_name or not last_name):
            payload = {
                    "error": "Either user_id must be provided, or both first_name and last_name must be provided",
                    "status": "failed",
                }
            out = json.dumps(
                payload)
            return out

        users = data.get("users", {}).values()
        target_user = None
        search_method = "user_id" if user_id else "name_search"

        if user_id:
            #Rule: Validate user identity exists before processing any user requests
            target_user = next((u for u in users.values() if u.get("user_id") == user_id), None)

            if not target_user:
                payload = {
                        "error": f"User {user_id} not found",
                        "status": "failed",
                        "user_exists": False,
                        "search_method": search_method,
                    }
                out = json.dumps(
                    payload)
                return out
        else:
            #Search by first_name and last_name
            matching_users = []

            for user in users.values():
                user_name = user.get("name", {}).values()
                stored_first_name = user_name.get("first_name", "").lower().strip()
                stored_last_name = user_name.get("last_name", "").lower().strip()

                provided_first_name = first_name.lower().strip()
                provided_last_name = last_name.lower().strip()

                if (
                    stored_first_name == provided_first_name
                    and stored_last_name == provided_last_name
                ):
                    matching_data["users"][user_id] = user

            if not matching_users:
                payload = {
                        "error": f"No user found with name '{first_name} {last_name}'",
                        "status": "failed",
                        "user_exists": False,
                        "search_method": search_method,
                        "search_criteria": {
                            "first_name": first_name,
                            "last_name": last_name,
                        },
                    }
                out = json.dumps(
                    payload)
                return out

            if len(matching_users) > 1:
                #Multiple users found with same name
                user_ids = [user.get("user_id") for user in matching_users]
                payload = {
                        "error": f"Multiple users found with name '{first_name} {last_name}'. Please specify user_id.",
                        "status": "multiple_matches",
                        "matching_user_ids": user_ids,
                        "total_matches": len(matching_users),
                        "search_method": search_method,
                        "search_criteria": {
                            "first_name": first_name,
                            "last_name": last_name,
                        },
                    }
                out = json.dumps(
                    payload)
                return out

            #Single user found
            target_user = matching_users[0]
            user_id = target_user.get("user_id")  #Set user_id for response

        #Additional validation for first_name and last_name if provided when searching by user_id
        validation_details = {"user_id_valid": True}
        user_name = target_user.get("name", {}).values()
        stored_first_name = user_name.get("first_name", "")
        stored_last_name = user_name.get("last_name", "")
        stored_email = target_user.get("email", "")

        #Only validate names if user_id was provided and names were also provided (for additional verification)
        if search_method == "user_id":
            if first_name is not None:
                if stored_first_name.lower() != first_name.lower():
                    payload = {
                            "error": f"First name mismatch for user {user_id}",
                            "status": "failed",
                            "user_exists": True,
                            "first_name_valid": False,
                            "search_method": search_method,
                        }
                    out = json.dumps(
                        payload)
                    return out
                validation_details["first_name_valid"] = True

            if last_name is not None:
                if stored_last_name.lower() != last_name.lower():
                    payload = {
                            "error": f"Last name mismatch for user {user_id}",
                            "status": "failed",
                            "user_exists": True,
                            "last_name_valid": False,
                            "search_method": search_method,
                        }
                    out = json.dumps(
                        payload)
                    return out
                validation_details["last_name_valid"] = True
        else:
            #For name search, names are automatically valid since we found the user by name
            validation_details["first_name_valid"] = True
            validation_details["last_name_valid"] = True

        #Always include comprehensive user location details in the response
        user_address = target_user.get("address", {}).values()

        user_location_details = {
            "address1": user_address.get("address1", ""),
            "address2": user_address.get("address2", ""),
            "city": user_address.get("city", ""),
            "state": user_address.get("state", ""),
            "zip": user_address.get("zip", ""),
            "country": user_address.get("country", ""),
        }

        #Check if address is complete
        required_address_fields = ["address1", "city", "state", "zip", "country"]
        address_complete = all(
            user_address.get(field) for field in required_address_fields
        )
        missing_fields = [
            field for field in required_address_fields if not user_address.get(field)
        ]

        #Determine address quality/completeness status
        address_status = "complete" if address_complete else "incomplete"
        if len(missing_fields) >= 4:
            address_status = "minimal"
        elif len(missing_fields) >= 2:
            address_status = "partial"

        #Check if location supports delivery (based on available couriers)
        couriers = data.get("couriers", {}).values()
        supported_countries = set()
        for courier in couriers.values():
            supported_countries.update(courier.get("coverage_area", []))

        destination_country = user_address.get("country", "")
        delivery_available = (
            destination_country in supported_countries if destination_country else False
        )
        payload = {
                "status": "success",
                "user_exists": True,
                "user_id": user_id,
                "search_method": search_method,
                "validation_details": validation_details,
                "user_name": {
                    "first_name": stored_first_name,
                    "last_name": stored_last_name,
                    "full_name": f"{stored_first_name} {stored_last_name}".strip(),
                },
                "user_email": {"email": stored_email},
                "user_location": {
                    "address_details": user_location_details,
                    "address_status": address_status,
                    "address_complete": address_complete,
                    "missing_fields": missing_fields,
                    "delivery_available": delivery_available,
                    "supported_country": (
                        destination_country in supported_countries
                        if destination_country
                        else None
                    ),
                },
            }
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ValidateUserIdentity",
                "description": "Check if user exists in the system with optional name verification. Can search by user_id OR by first_name and last_name combination. Always returns comprehensive user details including complete location information and delivery availability.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Customer identifier to validate (optional if first_name and last_name are provided)",
                        },
                        "first_name": {
                            "type": "string",
                            "description": "First name for user search or additional validation (required if user_id not provided)",
                        },
                        "last_name": {
                            "type": "string",
                            "description": "Last name for user search or additional validation (required if user_id not provided)",
                        },
                    },
},
            },
        }
