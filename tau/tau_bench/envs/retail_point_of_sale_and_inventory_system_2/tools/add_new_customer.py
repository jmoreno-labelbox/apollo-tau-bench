from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class AddNewCustomer(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], name: str, email: str, phone_number: str, address: str
    ) -> str:
        customers = data.get("customers", [])

        if any(c.get("email") == email for c in customers):
            payload = {"error": f"Customer with email {email} already exists."}
            out = json.dumps(payload)
            return out

        customer_id = f"CUST-{len(customers) + 5001:04d}"

        new_customer = {
            "customer_id": customer_id,
            "name": name,
            "email": email,
            "phone_number": phone_number,
            "address": address,
            "loyalty_points": 0,
            "membership_level": "bronze",
        }

        customers.append(new_customer)
        data["customers"] = customers
        payload = new_customer
        out = json.dumps(payload, indent=2)
        return out
        pass
        customers = data.get("customers", [])

        if any(c.get("email") == email for c in customers):
            payload = {"error": f"Customer with email {email} already exists."}
            out = json.dumps(payload)
            return out

        customer_id = f"CUST-{len(customers) + 5001:04d}"

        new_customer = {
            "customer_id": customer_id,
            "name": name,
            "email": email,
            "phone_number": phone_number,
            "address": address,
            "loyalty_points": 0,
            "membership_level": "bronze",
        }

        customers.append(new_customer)
        data["customers"] = customers
        payload = new_customer
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddNewCustomer",
                "description": "Add a new customer to the system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Customer's full name.",
                        },
                        "email": {
                            "type": "string",
                            "description": "Customer's email address.",
                        },
                        "phone_number": {
                            "type": "string",
                            "description": "Customer's phone number.",
                        },
                        "address": {
                            "type": "string",
                            "description": "Customer's address.",
                        },
                    },
                    "required": ["name", "email", "phone_number", "address"],
                },
            },
        }
