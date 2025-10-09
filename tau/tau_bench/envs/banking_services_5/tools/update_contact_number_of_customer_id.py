from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone, date, timedelta
import calendar
from typing import Any, Dict
import random



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateContactNumberOfCustomerId(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, new_phone_number: str = None, set_as_primary: bool = False) -> str:
        if not customer_id or not new_phone_number:
            return json.dumps({
                "error": "Both customer_id and new_phone_number are required."
            }, indent=2)

        customers = data.get("customers", {}).values()
        for customer in customers.values():
            if customer.get("customer_id") == customer_id:
                contact_info = customer.setdefault("contact_info", {}).values()
                phone_numbers = contact_info.setdefault("phone_numbers", [])

                if set_as_primary:
                    for phone in phone_numbers:
                        phone["is_primary"] = False

                phone_entry = {
                    "type": "Mobile",
                    "number": new_phone_number,
                    "is_primary": set_as_primary
                }
                phone_numbers.append(phone_entry)

                return json.dumps({"status": "Phone number updated successfully."}, indent=2)

        return json.dumps({"error": "Customer not found."}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateContactNumberOfCustomerId",
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
