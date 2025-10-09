from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateCustomerDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], customer_id: str, name: str = None, email: str = None, phone: str = None,
        address: Any = None,
        opt_in_marketing: Any = None,
        membership_level: Any = None,
        status: Any = None,
        phone_number: Any = None,
    ) -> str:
        customers = data.get("customers", [])
        updated_customer = None
        for customer in customers:
            if customer.get("customer_id") == customer_id:
                if name is not None:
                    customer["name"] = name
                if email is not None:
                    customer["email"] = email
                if phone is not None:
                    customer["phone"] = phone
                customer["updated_at"] = "2025-07-28T16:38:15Z"
                updated_customer = customer
                break
        payload = {"updated_customer": updated_customer}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCustomerDetails",
                "description": "Updates various details of an existing customer record by ID. Can update 'membership_level', 'email', 'phone_number', 'address', etc.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "The ID of the customer to update.",
                        },
                        "name": {
                            "type": "string",
                            "description": "The new full name of the customer.",
                        },
                        "phone_number": {
                            "type": "string",
                            "description": "The new contact phone number.",
                        },
                        "email": {
                            "type": "string",
                            "description": "The new company email address.",
                        },
                        "address": {
                            "type": "string",
                            "description": "The new physical address.",
                        },
                        "membership_level": {
                            "type": "string",
                            "description": "The new membership level (e.g., 'basic', 'silver', 'gold', 'platinum', 'diamond').",
                        },
                        "birthdate": {
                            "type": "string",
                            "format": "date",
                            "description": "The new birthdate (YYYY-MM-DD).",
                        },
                        "opt_in_marketing": {
                            "type": "boolean",
                            "description": "New marketing opt-in status.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The new employment status (e.g. 'active', 'inactive', 'terminated').",
                        },
                    },
                    "required": ["customer_id"],
                },
            },
        }
