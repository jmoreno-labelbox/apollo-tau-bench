from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateCustomerEmail(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], customer_id: str, new_email: str) -> str:
        customers = data.get("customers", [])

        for customer in customers:
            if (
                customer.get("email") == new_email
                and customer.get("customer_id") != customer_id
            ):
                payload = {
                    "error": f"Email {new_email} is already in use by another customer."
                }
                out = json.dumps(payload)
                return out

        for i, customer in enumerate(customers):
            if customer.get("customer_id") == customer_id:
                customers[i]["email"] = new_email
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
                "name": "UpdateCustomerEmail",
                "description": "Update the email address for a specific customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique identifier of the customer.",
                        },
                        "new_email": {
                            "type": "string",
                            "description": "New email address for the customer.",
                        },
                    },
                    "required": ["customer_id", "new_email"],
                },
            },
        }
