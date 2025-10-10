# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAddressForCustomerId(Tool):
    """Updates mailing and/or residential address for a given customer ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        mailing_address = kwargs.get("mailing_address")
        residential_address = kwargs.get("residential_address")

        if not customer_id:
            return json.dumps({"error": "customer_id is required."}, indent=2)

        if not mailing_address and not residential_address:
            return json.dumps({
                "error": "At least one of mailing_address or residential_address must be provided."
            }, indent=2)

        customers = list(data.get("customers", {}).values())
        for customer in customers:
            if customer.get("customer_id") == customer_id:
                contact_info = customer.setdefault("contact_info", {})
                if mailing_address:
                    contact_info["mailing_address"] = mailing_address
                if residential_address:
                    contact_info["residential_address"] = residential_address
                return json.dumps({"status": "Address updated successfully."}, indent=2)

        return json.dumps({"error": "Customer not found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_address_for_customer_id",
                "description": "Updates mailing and/or residential address for a given customer ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique identifier of the customer"
                        },
                        "mailing_address": {
                            "type": "object",
                            "description": "New mailing address object"
                        },
                        "residential_address": {
                            "type": "object",
                            "description": "New residential address object"
                        }
                    },
                    "required": ["customer_id"]
                }
            }
        }
