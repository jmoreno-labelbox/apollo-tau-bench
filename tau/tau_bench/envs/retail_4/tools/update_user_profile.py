# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateUserProfile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, profile_updates: Dict[str, Any]) -> str:
        """
        Update customer profile information (name, email, default address)

        Writes to: users.json (updates user profile fields)
        """
        # Requirement: Confirm user identity before handling any requests.
        users = list(data.get("users", {}).values())
        user_to_update = None
        user_index = None

        for i, user in enumerate(users):
            if user.get("user_id") == user_id:
                user_to_update = user
                user_index = i
                break

        if not user_to_update:
            return json.dumps({"error": f"User {user_id} not found", "status": "failed"})

        # Monitor the changes made.
        updates_applied = {}

        # Modify the name if it is supplied.
        if "name" in profile_updates:
            name_update = profile_updates["name"]
            if isinstance(name_update, dict):
                if "first_name" in name_update or "last_name" in name_update:
                    old_name = user_to_update.get("name", {})
                    new_name = old_name.copy()

                    if "first_name" in name_update:
                        new_name["first_name"] = name_update["first_name"]
                    if "last_name" in name_update:
                        new_name["last_name"] = name_update["last_name"]

                    user_to_update["name"] = new_name
                    updates_applied["name"] = {"old": old_name, "new": new_name}

        # Modify email if supplied.
        if "email" in profile_updates:
            new_email = profile_updates["email"]
            if "@" not in new_email:
                return json.dumps({"error": "Invalid email format", "status": "failed"})

            old_email = user_to_update.get("email")
            user_to_update["email"] = new_email
            updates_applied["email"] = {"old": old_email, "new": new_email}

        # Modify the address if available.
        if "address" in profile_updates:
            address_update = profile_updates["address"]
            if isinstance(address_update, dict):
                # Requirement: Ensure all mandatory address fields are validated: address1, city, country, state, zip.
                required_fields = ["address1", "city", "country", "state", "zip"]
                missing_fields = []

                for field in required_fields:
                    if field in address_update and not address_update.get(field):
                        missing_fields.append(field)

                if missing_fields:
                    return json.dumps({
                        "error": f"Invalid address fields: {', '.join(missing_fields)} cannot be empty",
                        "status": "failed"
                    })

                old_address = user_to_update.get("address", {})
                new_address = old_address.copy()
                new_address.update(address_update)

                user_to_update["address"] = new_address
                updates_applied["address"] = {"old": old_address, "new": new_address}

        if not updates_applied:
            return json.dumps({
                "error": "No valid updates provided. Supported fields: name, email, address",
                "status": "failed"
            })

        # UPDATE OPERATION: Modify user profile in users.json
        user_to_update["profile_updated"] = datetime.now().isoformat()
        user_to_update["last_updated"] = datetime.now().isoformat()

        # Modify the user information in the data structure.
        data["users"][user_index] = user_to_update

        result = {
            "status": "success",
            "user_id": user_id,
            "updates_applied": updates_applied,
            "total_updates": len(updates_applied),
            "profile_updated": user_to_update["profile_updated"]
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_user_profile",
                "description": "Update customer profile information",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "Customer identifier"},
                        "profile_updates": {
                            "type": "object",
                            "properties": {
                                "name": {
                                    "type": "object",
                                    "properties": {
                                        "first_name": {"type": "string"},
                                        "last_name": {"type": "string"}
                                    }
                                },
                                "email": {"type": "string"},
                                "address": {
                                    "type": "object",
                                    "properties": {
                                        "address1": {"type": "string"},
                                        "address2": {"type": "string"},
                                        "city": {"type": "string"},
                                        "country": {"type": "string"},
                                        "state": {"type": "string"},
                                        "zip": {"type": "string"}
                                    }
                                }
                            },
                            "description": "Profile fields to update"
                        }
                    },
                    "required": ["user_id", "profile_updates"]
                }
            }
        }
