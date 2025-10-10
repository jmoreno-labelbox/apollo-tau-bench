# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateCustomerAddress(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str, new_address: str) -> str:
        customers = list(data.get("customers", {}).values())

        for i, customer in enumerate(customers):
            if customer.get("customer_id") == customer_id:
                customers[i]["address"] = new_address
                data["customers"] = customers
                return json.dumps(customers[i], indent=2)

        return json.dumps({"error": f"Customer with ID {customer_id} not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_customer_address",
                "description": "Update the address of an existing customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Unique identifier of the customer."},
                        "new_address": {"type": "string", "description": "New address for the customer."}
                    },
                    "required": ["customer_id", "new_address"]
                }
            }
        }
