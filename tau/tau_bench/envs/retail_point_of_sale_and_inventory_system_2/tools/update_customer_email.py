# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateCustomerEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str, new_email: str) -> str:
        customers = list(data.get("customers", {}).values())

        for customer in customers:
            if customer.get("email") == new_email and customer.get("customer_id") != customer_id:
                return json.dumps({"error": f"Email {new_email} is already in use by another customer."})

        for i, customer in enumerate(customers):
            if customer.get("customer_id") == customer_id:
                customers[i]["email"] = new_email
        return json.dumps(customers[i], indent=2)
        return json.dumps({"error": f"Customer with ID {customer_id} not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_customer_email",
                "description": "Update the email address for a specific customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Unique identifier of the customer."},
                        "new_email": {"type": "string", "description": "New email address for the customer."}
                    },
                    "required": ["customer_id", "new_email"]
                }
            }
        }
