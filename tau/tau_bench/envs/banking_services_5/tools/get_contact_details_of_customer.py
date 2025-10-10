# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetContactDetailsOfCustomer(Tool):
    """Returns the email and primary phone number of a customer by customer ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        if not customer_id:
            return json.dumps({"error": "customer_id is required."}, indent=2)

        customers = list(data.get("customers", {}).values())
        for customer in customers:
            if customer.get("customer_id") == customer_id:
                contact_info = customer.get("contact_info", {})
                email = contact_info.get("email_address")
                phone_list = contact_info.get("phone_numbers", [])
                primary_phone = next((p["number"] for p in phone_list if p.get("is_primary")), None)

                return json.dumps({
                    "email": email,
                    "primary_phone_number": primary_phone
                }, indent=2)

        return json.dumps({"error": "Customer not found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_contact_details_of_customer",
                "description": "Returns the email and primary phone number of a customer given their customer ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique ID of the customer"
                        }
                    },
                    "required": ["customer_id"]
                }
            }
        }
