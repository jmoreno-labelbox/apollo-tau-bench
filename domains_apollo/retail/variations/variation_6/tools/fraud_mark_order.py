from tau_bench.envs.tool import Tool
import json
from typing import Any

class FraudMarkOrder(Tool):
    """Link a fraud_check dictionary to an order."""

    @staticmethod
    def invoke(data, order_id: str = None, risk_level: str = None, reason_code: str = None) -> str:
        if not order_id or not risk_level or not reason_code:
            payload = {"error": "order_id, risk_level, reason_code are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        o = _find_order(data, order_id)
        if not o:
            payload = {"error": f"order_id {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        o["fraud_check"] = {"risk_level": risk_level, "reason_code": reason_code}
        payload = {"success": True, "order_id": order_id, "risk_level": risk_level}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "fraudMarkOrder",
                "description": "Mark an order with fraud_check metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "risk_level": {"type": "string"},
                        "reason_code": {"type": "string"},
                    },
                    "required": ["order_id", "risk_level", "reason_code"],
                },
            },
        }
