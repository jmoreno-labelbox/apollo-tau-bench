# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddMoneyToGiftCard(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, gift_card_id: str, payment_method_id: str, amount: float) -> str:
        users = data["users"]
        # Verify the existence of the user.
        user = [row for row in users if row["user_id"] == user_id]
        if len(user) > 1:
            return json.dumps({"error": "Multiple users found"})
        if len(user) == 0:
            return json.dumps({"error": "User not found"})
        user = user[0]
        # Verify the existence of the gift card.
        if gift_card_id not in user["payment_methods"]:
            return json.dumps({"error": "gift card not found"})

        # Verify the existence of the payment method.
        if payment_method_id not in user["payment_methods"]:
            return json.dumps({"error": "payment method not found"})

        # Load funds onto the gift card.
        user["payment_methods"][gift_card_id]["balance"] += amount
        user["payment_methods"][gift_card_id]["balance"] = round(user["payment_methods"][gift_card_id]["balance"], 2)

        return json.dumps(user)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_money_to_gift_card",
                "description": "Add money to a user's gift card.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user id, such as 'sara_doe_496'.",
                        },
                        "gift_card_id": {
                            "type": "string",
                            "description": "The gift card id, such as 'gift_card_0000'.",
                        },
                        "payment_method_id": {
                            "type": "string",
                            "description": "The payment method id to pay for the gift card, such as 'credit_card_0000'.",
                        },
                        "amount": {
                            "type": "number",
                            "description": "The amount of money to add to the gift card.",
                        },
                    },
                    "required": ["user_id", "amount"],
                },
            },
        }
