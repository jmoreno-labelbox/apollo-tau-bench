from tau_bench.envs.tool import Tool
import json
from typing import Any

class AddPaymentMethod(Tool):
    """Link a payment method record to a user. A stable id must be included in the payload."""

    @staticmethod
    def invoke(data, user_id: str = None, payment_method: dict = None) -> str:
        if not user_id or not isinstance(payment_method, dict) or "id" not in payment_method:
            payload = {"error": "user_id and payment_method object with 'id' are required"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        user = _find_user(data, user_id)
        if not user:
            payload = {"error": f"user_id {user_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        pm = user.setdefault("payment_methods", {})
        pm[payment_method["id"]] = payment_method
        payload = {"success": True, "user_id": user_id, "payment_method_id": payment_method["id"]}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "addPaymentMethod",
                "description": "Add/update a payment method on a user. The payload must include a 'id'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "payment_method": {"type": "object"},
                    },
                    "required": ["user_id", "payment_method"],
                },
            },
        }
