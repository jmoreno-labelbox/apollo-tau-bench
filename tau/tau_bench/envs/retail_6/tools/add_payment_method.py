# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddPaymentMethod(Tool):
    """Attach a payment method record to a user. Must include a stable id in payload."""
    @staticmethod
    def invoke(data, payment_method, user_id) -> str:
        payment = payment_method
        if not user_id or not isinstance(payment, dict) or 'id' not in payment:
            return json.dumps({"error":"user_id and payment_method object with 'id' are required"}, indent=2)
        user = _find_user(data, user_id)
        if not user:
            return json.dumps({"error":f"user_id {user_id} not found"}, indent=2)
        pm = user.setdefault('payment_methods', {})
        pm[payment['id']] = payment
        return json.dumps({"success": True, "user_id": user_id, "payment_method_id": payment['id']}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"add_payment_method","description":"Add/update a payment method on a user. The payload must include a 'id'.","parameters":{"type":"object","properties":{"user_id":{"type":"string"},"payment_method":{"type":"object"}},"required":["user_id","payment_method"]}}}
