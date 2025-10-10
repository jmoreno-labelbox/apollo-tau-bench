# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateCustomerAddress(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        for customer in list(data.get("customers", {}).values()):
            if customer.get("customer_id") == customer_id:
                new_address = {
                        "street_address": kwargs.get("street_address"),
                        "city": kwargs.get("city"),
                        "state": kwargs.get("state"),
                        "postal_code": kwargs.get("postal_code"),
                        "country": kwargs.get("country")
                }
                customer["contact_info"]["mailing_address"] = new_address
                customer["contact_info"]["residential_address"] = new_address
                return json.dumps(customer)
        return json.dumps({"error": "Customer not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "update_customer_address",
                        "description": "Updates the mailing and residential address for a customer.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string", "description": "The customer's unique ID."},
                                        "street_address": {"type": "string", "description": "The new street address."},
                                        "city": {"type": "string", "description": "The new city."},
                                        "state": {"type": "string", "description": "The new state or province."},
                                        "postal_code": {"type": "string", "description": "The new postal code."},
                                        "country": {"type": "string", "description": "The new country."}
                                },
                                "required": ["customer_id", "street_address", "city", "state", "postal_code", "country"],
                        },
                },
        }
