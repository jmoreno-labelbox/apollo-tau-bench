from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List

class GetScheduledPayments(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        scheduled_payments = data.get("scheduled_payments", [])
        customer_payments = [pay for pay in scheduled_payments if pay.get("customer_id") == customer_id]
        return json.dumps(customer_payments)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "GetScheduledPayments",
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
