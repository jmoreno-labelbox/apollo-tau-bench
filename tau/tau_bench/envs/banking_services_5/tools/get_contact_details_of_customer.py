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
        return list(db.values())
    return db

class GetContactDetailsOfCustomer(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        if not customer_id:
            return json.dumps({"error": "customer_id is required."}, indent=2)

        customers = data.get("customers", [])
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
                "name": "getContactDetailsOfCustomer",
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
