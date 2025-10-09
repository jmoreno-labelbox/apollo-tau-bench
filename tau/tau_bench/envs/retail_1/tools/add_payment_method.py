from tau_bench.envs.tool import Tool
import json
from typing import Any

class AddPaymentMethod(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str,
        payment_method_source: str,
        last_four: str = None,
        brand: str = None,
        balance: int = None,
    ) -> str:
        pass
        users = data["users"]
        #Verify if the user is present
        user = [row for row in users if row["user_id"] == user_id]
        if len(user) > 1:
            payload = {"error": "Multiple users found"}
            out = json.dumps(payload)
            return out
        if len(user) == 0:
            payload = {"error": "User not found"}
            out = json.dumps(payload)
            return out
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
                payload = {"error": "brand is required for credit card"}
                out = json.dumps(payload)
                return out
            if last_four is not None:
                payment_method["last_four"] = last_four
            else:
                payload = {"error": "last four digits are required for credit card"}
                out = json.dumps(
                    payload)
                return out
            payment_method["id"] = f"credit_card_{user_id[-4:]}"
        elif payment_method_source == "paypal":
            payment_method["id"] = f"paypal_{user_id[-4:]}"
        else:
            payload = {"error": "unsupported payment method source"}
            out = json.dumps(payload)
            return out

        #Insert the new payment method
        user["payment_methods"][payment_method["id"]] = payment_method
        payload = user
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddPaymentMethod",
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
                            "description": "The payment method to be added, including id, source (e.g., gift_card or credit_card), and balance if applicable.",
                        },
                        "last_four": {
                            "type": "string",
                            "description": "The last four digits of the credit card (required if source is credit card).",
                        },
                        "brand": {
                            "type": "string",
                            "description": "The brand of the credit card, such as visa or mastercard (required if source is credit card).",
                        },
                        "balance": {
                            "type": "integer",
                            "description": "The balance of the gift card, if not present the balance is set to 0.",
                        },
                    },
                    "required": ["user_id", "payment_method_source"],
                },
            },
        }
