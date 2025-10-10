# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddPaymentMethod(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, payment_method_source: str, last_four: str = None, brand: str = None, balance: int = None) -> str:
        users = data["users"]
        # Check if the user exists
        user = [row for row in users if row["user_id"] == user_id]
        if len(user) > 1:
            return json.dumps({"error": "Multiple users found"})
        if len(user) == 0:
            return json.dumps({"error": "User not found"})
        user = user[0]

        payment_method = {}
        payment_method["source"] = payment_method_source
        if payment_method_source == "gift_card":
            payment_method["balance"] = balance if balance is not None else 0
            payment_method["id"] = f"gift_card_{user_id[-4:]}"
        elif payment_method_source == "credit_card":
            if brand is not None:
                payment_method["brand"] = brand
            else:
                return json.dumps({"error": "brand is required for credit card"})
            if last_four is not None:
                payment_method["last_four"] = last_four
            else:
                return json.dumps({"error": "last four digits are required for credit card"})
            payment_method["id"] = f"credit_card_{user_id[-4:]}"
        elif payment_method_source == "paypal":
            payment_method["id"] = f"paypal_{user_id[-4:]}"
        else:
            return json.dumps({"error": "unsupported payment method source"})

        # Add the new payment method
        user["payment_methods"][payment_method["id"]] = payment_method
        return json.dumps(user)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_payment_method",
                "description": "Add a new payment method for a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user id, such as 'sara_doe_496'.",
                        },
                        "payment_method_source": {
                            "type": "string",
                            "description": "The payment method to be added, including id, source (e.g., gift_card or credit_card), and balance if applicable."
                        },
                        "last_four": {
                            "type": "string",
                            "description": "The last four digits of the credit card (required if source is credit card)."
                        },
                        "brand": {
                            "type": "string",
                            "description": "The brand of the credit card, such as visa or mastercard (required if source is credit card)."
                        },
                        "balance": {
                            "type": "integer",
                            "description": "The balance of the gift card, if not present the balance is set to 0."
                        },

                    },
                    "required": ["user_id", "payment_method_source"],
                },
            },
        }
