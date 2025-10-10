# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CheckUserPaymentMethods(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        """
        List user's available payment methods
        Data Sources: users.json (payment_methods)
        """
        users = list(data.get("users", {}).values())
        user = next((u for u in users if u.get("user_id") == user_id), None)

        if not user:
            return json.dumps({"error": f"User {user_id} not found", "status": "failed"})

        payment_methods = user.get("payment_methods", {})
        method_list = []

        for method_id, method_info in payment_methods.items():
            method_data = {
                "payment_method_id": method_id,
                "source": method_info.get("source"),
            }
            if method_info.get("source") == "credit_card":
                method_data["brand"] = method_info.get("brand")
                method_data["last_four"] = method_info.get("last_four")
            elif method_info.get("source") == "gift_card":
                method_data["balance"] = method_info.get("balance")

            method_list.append(method_data)

        return json.dumps({
            "status": "success",
            "user_id": user_id,
            "payment_methods": method_list,
            "total_methods": len(method_list)
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_user_payment_methods",
                "description": "List user's available payment methods",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "User identifier (e.g., 'lucas_brown_6720')"}
                    },
                    "required": ["user_id"]
                }
            }
        }
