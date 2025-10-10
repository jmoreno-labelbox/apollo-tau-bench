# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCustomerDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str) -> str:
        customers = list(data.get("customers", {}).values())
        for customer in customers:
            if customer.get("customer_id") == customer_id:
                return json.dumps(customer, indent=2)
        return json.dumps({"error": f"Customer with ID {customer_id} not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_customer_details",
                "description": "Get detailed information about a specific customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Unique identifier of the customer."}
                    },
                    "required": ["customer_id"]
                }
            }
        }
