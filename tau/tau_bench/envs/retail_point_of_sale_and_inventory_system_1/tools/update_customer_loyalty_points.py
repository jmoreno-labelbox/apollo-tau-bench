# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateCustomerLoyaltyPoints(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id, points_to_add) -> str:
        customers = list(data.get("customers", {}).values())
        updated_customer = None
        for customer in customers:
            if customer.get("customer_id") == customer_id:
                customer["loyalty_points"] = customer.get("loyalty_points", 0) + points_to_add
                updated_customer = customer
                break
        return json.dumps({"updated_customer": updated_customer})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_customer_loyalty_points",
                "description": "Adds loyalty points to a customer's record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "The ID of the customer to update.",
                        },
                        "points_to_add": {
                            "type": "integer",
                            "description": "The number of loyalty points to add.",
                        },
                    },
                    "required": ["customer_id", "points_to_add"],
                },
            },
        }
