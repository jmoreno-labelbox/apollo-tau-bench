# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateCustomerPhoneNumber(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str, new_phone_number: str) -> str:
        customers = list(data.get("customers", {}).values())

        for i, customer in enumerate(customers):
            if customer.get("customer_id") == customer_id:
                customers[i]["phone_number"] = new_phone_number
        return json.dumps(customers[i], indent=2)
        return json.dumps({"error": f"Customer with ID {customer_id} not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_customer_phone_number",
                "description": "Update the phone number of an existing customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Unique identifier of the customer."},
                        "new_phone_number": {"type": "string", "description": "New phone number for the customer."}
                    },
                    "required": ["customer_id", "new_phone_number"]
                }
            }
        }
