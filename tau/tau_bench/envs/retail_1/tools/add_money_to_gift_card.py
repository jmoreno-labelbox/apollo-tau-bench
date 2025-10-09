from tau_bench.envs.tool import Tool
import json
from typing import Any

class AddMoneyToGiftCard(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str,
        gift_card_id: str,
        payment_method_id: str,
        amount: float,
    ) -> str:
        pass
        users = data["users"]
        #Verify if the user is present
        user = [row for row in users.values() if row["user_id"] == user_id]
        if len(user) > 1:
            payload = {"error": "Multiple users found"}
            out = json.dumps(payload)
            return out
        if len(user) == 0:
            payload = {"error": "User not found"}
            out = json.dumps(payload)
            return out
        user = user[0]
        #Verify if the gift card is present
        if gift_card_id not in user["payment_methods"]:
            payload = {"error": "gift card not found"}
            out = json.dumps(payload)
            return out

        #Verify if the payment method is available
        if payment_method_id not in user["payment_methods"]:
            payload = {"error": "payment method not found"}
            out = json.dumps(payload)
            return out

        #Deposit funds into the gift card
        user["payment_methods"][gift_card_id]["balance"] += amount
        user["payment_methods"][gift_card_id]["balance"] = round(
            user["payment_methods"][gift_card_id]["balance"], 2
        )
        payload = user
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddMoneyToGiftCard",
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
