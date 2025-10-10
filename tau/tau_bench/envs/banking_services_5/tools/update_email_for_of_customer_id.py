# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateEmailForOfCustomerId(Tool):
    """Updates the email address of a customer given their customer ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        new_email = kwargs.get("new_email")

        if not customer_id or not new_email:
            return json.dumps({
                "error": "Both customer_id and new_email are required."
            }, indent=2)

        customers = list(data.get("customers", {}).values())
        for customer in customers:
            if customer.get("customer_id") == customer_id:
                contact_info = customer.setdefault("contact_info", {})
                contact_info["email_address"] = new_email
                return json.dumps({"status": "Email updated successfully."}, indent=2)

        return json.dumps({"error": "Customer not found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_email_for_of_customer_id",
                "description": "Updates the email address for the specified customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique identifier of the customer"
                        },
                        "new_email": {
                            "type": "string",
                            "description": "New email address to set for the customer"
                        }
                    },
                    "required": ["customer_id", "new_email"]
                }
            }
        }
