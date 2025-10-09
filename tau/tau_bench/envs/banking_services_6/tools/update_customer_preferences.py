from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List

class UpdateCustomerPreferences(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, paperless_billing: bool = None, communication_channel: str = None) -> str:
        customer = next((c for c in data['customers'] if c['customer_id'] == customer_id), None)
        if not customer:
            return json.dumps({"error": "Customer not found"})

        if "preferences" not in customer:
            customer["preferences"] = {}

        if paperless_billing is not None:
            customer["preferences"]["paperless_billing"] = paperless_billing
        if communication_channel is not None:
            customer["preferences"]["communication_channel"] = communication_channel

        return json.dumps(customer["preferences"])
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "UpdateCustomerPreferences",
                        "description": "Updates a customer's communication preferences.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string"},
                                        "paperless_billing": {"type": "boolean"},
                                        "communication_channel": {"type": "string"}
                                },
                                "required": ["customer_id"]
                        }
                }
        }
