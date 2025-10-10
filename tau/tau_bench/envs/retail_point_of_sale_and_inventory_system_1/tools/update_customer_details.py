# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateCustomerDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get('customer_id')
        customers = list(data.get("customers", {}).values())  # Array []
        updated_customer = None
        for customer in customers:
            if customer.get("customer_id") == customer_id:
                for key, value in kwargs.items():
                    if key != 'customer_id':
                        customer[key] = value
                customer["updated_at"] = "2025-07-28T16:38:15Z"  # System time
                updated_customer = customer
                break
        return json.dumps({"updated_customer": updated_customer})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_customer_details",
                "description": "Updates various details of an existing customer record by ID. Can update 'membership_level', 'email', 'phone_number', 'address', etc.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "The ID of the customer to update.",
                        },
                        "name": {"type": "string", "description": "The new full name of the customer."},
                        "phone_number": {"type": "string", "description": "The new contact phone number."},
                        "email": {"type": "string", "description": "The new company email address."},
                        "address": {"type": "string", "description": "The new physical address."},
                        "membership_level": {"type": "string", "description": "The new membership level (e.g., 'basic', 'silver', 'gold', 'platinum', 'diamond')."},
                        "birthdate": {"type": "string", "format": "date", "description": "The new birthdate (YYYY-MM-DD)."},
                        "opt_in_marketing": {"type": "boolean", "description": "New marketing opt-in status."},
                        "status": {"type": "string", "description": "The new employment status (e.g. 'active', 'inactive', 'terminated')."},
                    },
                    "required": ["customer_id"],
                },
            },
        }
