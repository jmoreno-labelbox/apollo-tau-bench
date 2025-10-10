# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateContactNumberOfCustomerId(Tool):
    """Adds a new contact number for a customer and optionally sets it as the primary number."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        new_number = kwargs.get("new_phone_number")
        is_primary = kwargs.get("set_as_primary", False)


        if not customer_id or not new_number:
            return json.dumps({
                "error": "Both customer_id and new_phone_number are required."
            }, indent=2)

        customers = list(data.get("customers", {}).values())
        for customer in customers:
            if customer.get("customer_id") == customer_id:
                contact_info = customer.setdefault("contact_info", {})
                phone_numbers = contact_info.setdefault("phone_numbers", [])

                if is_primary:
                    for phone in phone_numbers:
                        phone["is_primary"] = False


                phone_entry = {
                    "type": "Mobile",
                    "number": new_number,
                    "is_primary": is_primary
                }
                phone_numbers.append(phone_entry)

                return json.dumps({"status": "Phone number updated successfully."}, indent=2)

        return json.dumps({"error": "Customer not found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_contact_number_of_customer_id",
                "description": "Adds a new phone number for a customer and sets it as primary if specified.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique identifier of the customer"
                        },
                        "new_phone_number": {
                            "type": "string",
                            "description": "New phone number to be added"
                        },
                        "set_as_primary": {
                            "type": "boolean",
                            "description": "Flag to mark the new number as the primary number"
                        }
                    },
                    "required": ["customer_id", "new_phone_number"]
                }
            }
        }
