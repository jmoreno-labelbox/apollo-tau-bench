# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddCustomerPhoneNumber(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        phone_type = kwargs.get("phone_type")
        phone_number = kwargs.get("phone_number")
        is_primary = kwargs.get("is_primary", False)

        customer = next((c for c in list(data.get('customers', {}).values()) if c['customer_id'] == customer_id), None)
        if not customer:
            return json.dumps({"error": "Customer not found."})

        if "contact_info" not in customer:
            customer["contact_info"] = {}
        if "phone_numbers" not in customer["contact_info"]:
            customer["contact_info"]["phone_numbers"] = []

        if is_primary:
            for phone in customer["contact_info"]["phone_numbers"]:
                phone["is_primary"] = False

        customer["contact_info"]["phone_numbers"].append({
                "type": phone_type,
                "number": phone_number,
                "is_primary": is_primary
        })

        return json.dumps(customer["contact_info"]["phone_numbers"])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "add_customer_phone_number",
                        "description": "Adds a new phone number to a customer's profile.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string"},
                                        "phone_type": {"type": "string", "description": "Type of phone number (e.g., 'Work', 'Home')."},
                                        "phone_number": {"type": "string"},
                                        "is_primary": {"type": "boolean", "description": "Set to true if this should be the new primary number."}
                                },
                                "required": ["customer_id", "phone_type", "phone_number"]
                        }
                }
        }
