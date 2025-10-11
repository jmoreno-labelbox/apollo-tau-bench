# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateCustomerPersonalInfo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id, field, value) -> str:
        field_to_update = field
        new_value = value

        customer = next((c for c in data['customers'] if c['customer_id'] == customer_id), None)
        if not customer:
            return json.dumps({"error": "Customer not found"})

        if "personal_info" in customer and field_to_update in customer["personal_info"]:
            customer["personal_info"][field_to_update] = new_value
            return json.dumps(customer["personal_info"])

        return json.dumps({"error": f"Field {field_to_update} not found in personal info."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "update_customer_personal_info",
                        "description": "Updates a specific field in a customer's personal information.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string"},
                                        "field": {"type": "string", "description": "The field to update (e.g., 'marital_status')."},
                                        "value": {"type": "string", "description": "The new value for the field."}
                                },
                                "required": ["customer_id", "field", "value"]
                        }
                }
        }
