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

class UpdateEmailForOfCustomerId(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, new_email: str = None) -> str:
        if not customer_id or not new_email:
            return json.dumps({
                "error": "Both customer_id and new_email are required."
            }, indent=2)

        customers = data.get("customers", [])
        for customer in customers:
            if customer.get("customer_id") == customer_id:
                contact_info = customer.setdefault("contact_info", {})
                contact_info["email_address"] = new_email
                return json.dumps({"status": "Email updated successfully."}, indent=2)

        return json.dumps({"error": "Customer not found."}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateEmailForOfCustomerId",
                "description": "Updates the email address for the specified customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique identifier of the customer"
                        },
                        "new_email": {
                            "type": "string",
                            "description": "New email address to set for the customer"
                        }
                    },
                    "required": ["customer_id", "new_email"]
                }
            }
        }
