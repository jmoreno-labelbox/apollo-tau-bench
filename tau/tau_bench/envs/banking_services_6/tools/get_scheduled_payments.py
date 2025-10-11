# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetScheduledPayments(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id) -> str:
        scheduled_payments = data.get("scheduled_payments", [])
        customer_payments = [pay for pay in scheduled_payments if pay.get("customer_id") == customer_id]
        return json.dumps(customer_payments)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_scheduled_payments",
                        "description": "Get all scheduled payments for a given customer.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string", "description": "The unique ID of the customer."}
                                },
                                "required": ["customer_id"],
                        },
                },
        }
