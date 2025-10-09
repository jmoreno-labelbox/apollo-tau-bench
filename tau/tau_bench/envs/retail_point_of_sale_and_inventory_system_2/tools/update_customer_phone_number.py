from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateCustomerPhoneNumber(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], customer_id: str, new_phone_number: str) -> str:
        customers = data.get("customers", {}).values()

        for i, customer in enumerate(customers):
            if customer.get("customer_id") == customer_id:
                customers[i]["phone_number"] = new_phone_number
                data["customers"] = customers
                payload = customers[i]
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Customer with ID {customer_id} not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCustomerPhoneNumber",
                "description": "Update the phone number of an existing customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique identifier of the customer.",
                        },
                        "new_phone_number": {
                            "type": "string",
                            "description": "New phone number for the customer.",
                        },
                    },
                    "required": ["customer_id", "new_phone_number"],
                },
            },
        }
