# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateCustomerLoyaltyPoints(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str, points_to_add: int) -> str:
        customers = list(data.get("customers", {}).values())
        for i, customer in enumerate(customers):
            if customer.get("customer_id") == customer_id:
                current_points = customer.get("loyalty_points", 0)
                customers[i]["loyalty_points"] = current_points + points_to_add
        return json.dumps(customers[i], indent=2)
        return json.dumps({"error": f"Customer with ID {customer_id} not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_customer_loyalty_points",
                "description": "Update loyalty points for a specific customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Unique identifier of the customer."},
                        "points_to_add": {"type": "integer", "description": "Number of points to add."}
                    },
                    "required": ["customer_id", "points_to_add"]
                }
            }
        }
