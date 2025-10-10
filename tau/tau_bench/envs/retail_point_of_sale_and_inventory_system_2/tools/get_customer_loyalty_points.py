# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCustomerLoyaltyPoints(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str) -> str:
        customers = list(data.get("customers", {}).values())
        for customer in customers:
            if customer.get("customer_id") == customer_id:
                loyalty_info = {
                    "customer_id": customer_id,
                    "name": customer.get("name"),
                    "loyalty_points": customer.get("loyalty_points", 0),
                    "membership_level": customer.get("membership_level", "bronze")
                }
                return json.dumps(loyalty_info, indent=2)
        return json.dumps({"error": f"Customer with ID {customer_id} not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_customer_loyalty_points",
                "description": "Get loyalty points balance for a specific customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Unique identifier of the customer."}
                    },
                    "required": ["customer_id"]
                }
            }
        }
