# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCustomerProfileTool(Tool):
    """
    Tool to fetch the profile information of a customer based on customer ID.

    It returns the customer's full name, email address, and primary phone number
    as a summarized contact profile.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Retrieves customer details like name, email, and phone.

        get_info() -> Dict[str, Any]:
            Supplies metadata for integration with external tools.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        if not customer_id:
            return json.dumps({"error": "customer_id is required"}, indent=2)

        customers = load_json("customers.json")
        for c in customers:
            if c["customer_id"] == customer_id:
                profile = {
                    "name": f"{c['personal_info']['first_name']} {c['personal_info']['last_name']}",
                    "email": c["contact_info"]["email_address"],
                    "phone": c["contact_info"]["phone_numbers"][0]["number"],
                }
                return json.dumps(profile, indent=2)

        return json.dumps({"error": "Customer not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_customer_profile",
                "description": "Retrieve personal and contact details from the customer profile.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer ID"}
                    },
                    "required": ["customer_id"],
                },
            },
        }
