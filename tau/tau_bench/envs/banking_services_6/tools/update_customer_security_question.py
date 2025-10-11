# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateCustomerSecurityQuestion(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id, security_question) -> str:

        customer = next((c for c in data['customers'] if c['customer_id'] == customer_id), None)
        if not customer:
            return json.dumps({"error": "Customer not found"})

        if "security" not in customer:
            customer["security"] = {}

        if security_question is not None:
            customer["security"]["security_question"] = security_question

        return json.dumps(customer["security"])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "update_customer_security_question",
                        "description": "Updates a customer's security question.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string"},
                                        "security_question": {"type": "string"}
                                },
                                "required": ["customer_id", "security_question"]
                        }
                }
        }
