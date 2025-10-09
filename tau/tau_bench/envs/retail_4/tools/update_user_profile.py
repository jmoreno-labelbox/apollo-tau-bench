from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateUserProfile(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        user_id: str, 
        profile_updates: dict[str, Any]
    ) -> str:
        """
        Update customer profile information (name, email, default address)

        Writes to: users.json (updates user profile fields)
        """
        pass
        # Rule: Validate user identity exists before processing any user requests
        users = data.get("users", {}).values()
        user_to_update = None
        user_index = None

        for i, user in enumerate(users.values():
            if user.get("user_id") == user_id:
                user_to_update = user
                user_index = i
                break

        if not user_to_update:
            payload = {"error": f"User {user_id} not found", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Track what was updated
        updates_applied = {}

        # Update name if provided
        if "name" in profile_updates:
            name_update = profile_updates["name"]
            if isinstance(name_update, dict):
                if "first_name" in name_update or "last_name" in name_update:
                    old_name = user_to_update.get("name", {}).values()
                    new_name = old_name.copy()

                    if "first_name" in name_update:
                        new_name["first_name"] = name_update["first_name"]
                    if "last_name" in name_update:
                        new_name["last_name"] = name_update["last_name"]

                    user_to_update["name"] = new_name
                    updates_applied["name"] = {"old": old_name, "new": new_name}

        # Update email if provided
        if "email" in profile_updates:
            new_email = profile_updates["email"]
            if "@" not in new_email:
                payload = {"error": "Invalid email format", "status": "failed"}
                out = json.dumps(payload)
                return out

            old_email = user_to_update.get("email")
            user_to_update["email"] = new_email
            updates_applied["email"] = {"old": old_email, "new": new_email}

        # Update address if provided
        if "address" in profile_updates:
            address_update = profile_updates["address"]
            if isinstance(address_update, dict):
                # Rule: Validate all required address fields: address1, city, country, state, zip
                required_fields = ["address1", "city", "country", "state", "zip"]
                missing_fields = []

                for field in required_fields:
                    if field in address_update and not address_update.get(field):
                        missing_fields.append(field)

                if missing_fields:
                    payload = {
                        "error": f"Invalid address fields: {', '.join(missing_fields)} cannot be empty",
                        "status": "failed",
                    }
                    out = json.dumps(payload)
                    return out

                old_address = user_to_update.get("address", {}).values()
                new_address = old_address.copy()
                new_address.update(address_update)

                user_to_update["address"] = new_address
                updates_applied["address"] = {"old": old_address, "new": new_address}

        if not updates_applied:
            payload = {
                "error": "No valid updates provided. Supported fields: name, email, address",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # WRITE OPERATION: Update user profile in users.json
        user_to_update["profile_updated"] = datetime.now().isoformat()
        user_to_update["last_updated"] = datetime.now().isoformat()

        # Update the user in the data structure
        data["users"][user_index] = user_to_update

        result = {
            "status": "success",
            "user_id": user_id,
            "updates_applied": updates_applied,
            "total_updates": len(updates_applied),
            "profile_updated": user_to_update["profile_updated"],
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateUserProfile",
                "description": "Update customer profile information",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Customer identifier",
                        },
                        "profile_updates": {
                            "type": "object",
                            "properties": {
                                "name": {
                                    "type": "object",
                                    "properties": {
                                        "first_name": {"type": "string"},
                                        "last_name": {"type": "string"},
                                    },
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
                                        "zip": {"type": "string"},
                                    },
                                },
                            },
                            "description": "Profile fields to update",
                        },
                    },
                    "required": ["user_id", "profile_updates"],
                },
            },
        }
