# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateCustomerPreferences(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        paperless_billing = kwargs.get("paperless_billing")
        communication_channel = kwargs.get("communication_channel")

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
                        "name": "update_customer_preferences",
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
