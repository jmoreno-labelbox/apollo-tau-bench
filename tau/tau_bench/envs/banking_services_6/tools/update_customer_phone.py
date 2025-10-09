from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateCustomerPhone(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, new_phone_number: str = None) -> str:
        for customer in data.get("customers", []):
            if customer.get("customer_id") == customer_id:
                for phone in customer.get("contact_info", {}).get("phone_numbers", []):
                    if phone.get("is_primary"):
                        phone["number"] = new_phone_number
                        return json.dumps(customer)
                customer["contact_info"]["phone_numbers"].append({"type": "Mobile", "number": new_phone_number, "is_primary": True})
                return json.dumps(customer)
        return json.dumps({"error": "Customer not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "UpdateCustomerPhone",
                        "description": "Updates the primary phone number for a customer.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string", "description": "The customer's unique ID."},
                                        "new_phone_number": {"type": "string", "description": "The new primary phone number."}
                                },
                                "required": ["customer_id", "new_phone_number"],
                        },
                },
        }
