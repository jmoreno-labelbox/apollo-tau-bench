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

class CreateCustomer(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], name: str = None, membership_level: str = None, 
               opt_in_marketing: bool = None, loyalty_points: int = None) -> str:
        customers = data.get("customers", [])

        max_customer_id_num = 0
        for customer in customers:
            if isinstance(customer.get("customer_id"), str):
                match = re.match(r"CUST-(\d+)", customer["customer_id"])
                if match:
                    num = int(match.group(1))
                    max_customer_id_num = max(max_customer_id_num, num)

        next_customer_id_num = max_customer_id_num + 1
        new_customer_id = f"CUST-{next_customer_id_num}"

        new_customer = {
            "customer_id": new_customer_id,
            "name": name,
            "phone_number": None,
            "loyalty_points": loyalty_points,
            "email": f"{str(name).replace(' ', '.').lower()}@example.com",
            "address": None,
            "membership_level": membership_level,
            "birthdate": None,
            "opt_in_marketing": opt_in_marketing,
            "status": "active",
        }

        customers.append(new_customer)
        data["customers"] = customers
        payload = {"customer_id": new_customer_id}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateCustomer",
                "description": "Creates a new customer record with specified details.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "The full name of the new customer.",
                        },
                        "membership_level": {
                            "type": "string",
                            "description": "The membership level for the new customer (e.g., 'basic', 'silver', 'gold', 'platinum').",
                        },
                        "opt_in_marketing": {
                            "type": "boolean",
                            "description": "Indicates if the customer has opted into marketing communications.",
                        },
                        "loyalty_points": {
                            "type": "integer",
                            "description": "The initial loyalty points for the customer.",
                        },
                    },
                    "required": [
                        "name",
                        "membership_level",
                        "opt_in_marketing",
                        "loyalty_points",
                    ],
                },
            },
        }
