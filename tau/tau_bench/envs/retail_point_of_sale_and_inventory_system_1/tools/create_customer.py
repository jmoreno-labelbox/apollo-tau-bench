# Sierra Copyright

import re
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateCustomer(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], loyalty_points, membership_level, name, opt_in_marketing) -> str:

        customers = list(data.get("customers", {}).values())

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
            "status": "active"
        }

        customers.append(new_customer)
        data["customers"] = customers

        return json.dumps({"customer_id": new_customer_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_customer",
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
                        }
                    },
                    "required": ["name", "membership_level", "opt_in_marketing", "loyalty_points"],
                },
            },
        }
