from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class UpdateUserMembership(Tool):
    """
    Basic API tool for updating user membership levels.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any], user_email: str = None, new_membership: str = None
    ) -> str:
        # Check the necessary parameters for validity
        if not user_email or not new_membership:
            payload = {
                "status": "Missing required parameters",
                "required": ["user_email", "new_membership"],
            }
            out = json.dumps(payload)
            return out

        # Check the membership level for validity
        valid_memberships = ["basic", "silver", "gold", "platinum"]
        if new_membership not in valid_memberships:
            payload = {
                "status": "Invalid membership level",
                "valid_memberships": valid_memberships,
                "received": new_membership,
            }
            out = json.dumps(payload)
            return out

        # Locate the user
        users = data.get("users", [])
        target_user = None
        user_index = None

        for i, user in enumerate(users):
            if user.get("email") == user_email:
                target_user = user
                user_index = i
                break

        if not target_user:
            payload = {"status": "User not found", "email": user_email}
            out = json.dumps(payload)
            return out

        # Revise membership
        old_membership = target_user.get("membership", "basic")
        data["users"][user_index]["membership"] = new_membership

        response = {
            "user_email": user_email,
            "user_name": target_user.get("name"),
            "old_membership": old_membership,
            "new_membership": new_membership,
            "status": "success",
            "message": f"Membership updated from {old_membership} to {new_membership}",
        }
        payload = response
        out = json.dumps(payload, indent=2)
        return out
    

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateUserMembership",
                "description": "Update user membership level to unlock additional benefits and services. Each membership tier offers progressively more amenities including priority check-in, baggage allowances, lounge access, and customer service levels.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_email": {
                            "type": "string",
                            "description": "User email address to update membership for",
                        },
                        "new_membership": {
                            "type": "string",
                            "description": "New membership level: 'basic', 'silver', 'gold', or 'platinum'. Each level provides different benefits and service tiers.",
                        },
                    },
                    "required": ["user_email", "new_membership"],
                },
            },
        }
