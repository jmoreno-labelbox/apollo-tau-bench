# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class VerifyGiftCardBalance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], first_name: str, last_name: str, user_id: str) -> str:
        """
        Verify gift card balance using customer name and user ID authentication

        Data Sources: users.json (user verification and gift card balances)
        """
        if not first_name or not last_name or not user_id:
            return json.dumps({
                "error": "First name, last name, and user ID are required",
                "status": "failed"
            })

        # Requirement: Confirm the existence of user identity prior to handling any user requests.
        users = list(data.get("users", {}).values())
        user = next((u for u in users if u.get("user_id") == user_id), None)

        if not user:
            return json.dumps({
                "error": f"User {user_id} not found",
                "status": "failed"
            })

        # Check if the name corresponds to the user record.
        user_name = user.get("name", {})
        stored_first_name = user_name.get("first_name", "").lower().strip()
        stored_last_name = user_name.get("last_name", "").lower().strip()

        provided_first_name = first_name.lower().strip()
        provided_last_name = last_name.lower().strip()

        if stored_first_name != provided_first_name or stored_last_name != provided_last_name:
            return json.dumps({
                "error": "Name verification failed. Please check your first and last name.",
                "status": "authentication_failed"
            })

        # Condition: Accepted payment methods include credit card, PayPal, or gift card.
        payment_methods = user.get("payment_methods", {})
        gift_cards = []

        for method_id, method_details in payment_methods.items():
            if method_details.get("source") == "gift_card":
                balance = method_details.get("balance", 0)
                gift_cards.append({
                    "gift_card_id": method_id,
                    "balance": balance,
                    "last_updated": method_details.get("last_updated", "N/A")
                })

        if not gift_cards:
            return json.dumps({
                "status": "success",
                "user_id": user_id,
                "customer_name": f"{first_name} {last_name}",
                "gift_cards_found": 0,
                "message": "No gift cards found for this account"
            })

        # Determine the overall balance of gift cards.
        total_balance = sum(card["balance"] for card in gift_cards)

        result = {
            "status": "success",
            "user_id": user_id,
            "customer_name": f"{first_name} {last_name}",
            "gift_cards_found": len(gift_cards),
            "total_balance": round(total_balance, 2),
            "gift_cards": gift_cards,
            "verification_timestamp": datetime.now().isoformat()
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "verify_gift_card_balance",
                "description": "Verify gift card balance using customer name and user ID authentication",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {"type": "string", "description": "Customer's first name"},
                        "last_name": {"type": "string", "description": "Customer's last name"},
                        "user_id": {"type": "string", "description": "Customer identifier"}
                    },
                    "required": ["first_name", "last_name", "user_id"]
                }
            }
        }
