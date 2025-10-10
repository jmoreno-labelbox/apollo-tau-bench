# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateUserMembership(Tool):
    """
    Simple API tool to update user membership level.
    """

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        user_email: str = None,
        new_membership: str = None,
        membership_level: str = None
    ) -> str:
        
        # Validate required parameters
        # Use membership_level if new_membership is not provided
        if not new_membership and membership_level:
            new_membership = membership_level
            
        if not user_email or not new_membership:
            return json.dumps({
                "status": "Missing required parameters",
                "required": ["user_email", "new_membership or membership_level"]
            })

        # Validate membership level
        valid_memberships = ["basic", "silver", "gold", "platinum"]
        if new_membership not in valid_memberships:
            return json.dumps({
                "status": "Invalid membership level",
                "valid_memberships": valid_memberships,
                "received": new_membership
            })

        # Find user
        users = list(data.get("users", {}).values())
        target_user = None
        user_index = None

        for i, user in enumerate(users):
            if user.get("email") == user_email:
                target_user = user
                user_index = i
                break

        if not target_user:
            return json.dumps({
                "status": "User not found",
                "email": user_email
            })

        # Update membership
        old_membership = target_user.get("membership", "basic")
        data["users"][user_index]["membership"] = new_membership

        response = {
            "user_email": user_email,
            "user_name": target_user.get("name"),
            "old_membership": old_membership,
            "new_membership": new_membership,
            "status": "success",
            "message": f"Membership updated from {old_membership} to {new_membership}"
        }

        return json.dumps(response, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_user_membership",
                "description": "Update user membership level to unlock additional benefits and services. Each membership tier offers progressively more amenities including priority check-in, baggage allowances, lounge access, and customer service levels.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_email": {
                            "type": "string",
                            "description": "User email address to update membership for"
                        },
                        "new_membership": {
                            "type": "string",
                            "description": "New membership level: 'basic', 'silver', 'gold', or 'platinum'. Each level provides different benefits and service tiers."
                        },
                        "membership_level": {
                            "type": "string",
                            "description": "Alternative parameter name for new_membership. New membership level: 'basic', 'silver', 'gold', or 'platinum'. Each level provides different benefits and service tiers."
                        }
                    },
                    "required": ["user_email"],
                    "oneOf": [
                        {
                            "required": ["user_email", "new_membership"]
                        },
                        {
                            "required": ["user_email", "membership_level"]
                        }
                    ]
                }
            }
        }
