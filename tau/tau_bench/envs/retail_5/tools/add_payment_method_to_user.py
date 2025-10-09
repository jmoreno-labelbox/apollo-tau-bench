from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class AddPaymentMethodToUser(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, payment_method: dict = None) -> str:
        if not user_id or not payment_method:
            payload = {"error": "user_id and payment_method are required"}
            out = json.dumps(payload)
            return out

        user = next((u for u in data["users"].values() if u["user_id"] == user_id), None)
        if not user:
            payload = {"error": "User not found"}
            out = json.dumps(payload)
            return out

        method_id = f"{payment_method.get('source', 'card')}_{generate_unique_id()}"
        payment_method["id"] = method_id
        user["payment_methods"][method_id] = payment_method
        payload = {"success": True, "payment_method_id": method_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addPaymentMethodToUser",
                "description": "Add a new payment method to a user's profile.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user.",
                        },
                        "payment_method": {
                            "type": "object",
                            "description": "Object containing payment details like source, brand, last_four.",
                        },
                    },
                    "required": ["user_id", "payment_method"],
                },
            },
        }
