from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CheckUserPaymentMethods(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str) -> str:
        """
        List user's available payment methods
        Data Sources: users.json (payment_methods)
        """
        users = data.get("users", [])
        user = next((u for u in users if u.get("user_id") == user_id), None)

        if not user:
            payload = {"error": f"User {user_id} not found", "status": "failed"}
            out = json.dumps(payload)
            return out

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
        payload = {
            "status": "success",
            "user_id": user_id,
            "payment_methods": method_list,
            "total_methods": len(method_list),
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckUserPaymentMethods",
                "description": "List user's available payment methods",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "User identifier (e.g., 'liam_wilson_6720')",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }
