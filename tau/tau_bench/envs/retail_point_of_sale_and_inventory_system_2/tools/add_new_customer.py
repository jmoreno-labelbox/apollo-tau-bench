# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddNewCustomer(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], name: str, email: str, phone_number: str, address: str) -> str:
        customers = list(data.get("customers", {}).values())

        if any(c.get("email") == email for c in customers):
            return json.dumps({"error": f"Customer with email {email} already exists."})

        customer_id = f"CUST-{len(customers) + 5001:04d}"

        new_customer = {
            "customer_id": customer_id,
            "name": name,
            "email": email,
            "phone_number": phone_number,
            "address": address,
            "loyalty_points": 0,
            "membership_level": "bronze"
        }

        customers.append(new_customer)
        data["customers"][customer_id] = new_customer
        return json.dumps(new_customer, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_new_customer",
                "description": "Add a new customer to the system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Customer's full name."},
                        "email": {"type": "string", "description": "Customer's email address."},
                        "phone_number": {"type": "string", "description": "Customer's phone number."},
                        "address": {"type": "string", "description": "Customer's address."}
                    },
                    "required": ["name", "email", "phone_number", "address"]
                }
            }
        }
