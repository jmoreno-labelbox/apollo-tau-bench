from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class UpdateCustomerLoyaltyPoints(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], customer_id: str = None, points_to_add: int = None) -> str:
        customers = data.get("customers", [])
        updated_customer = None
        for customer in customers:
            if customer.get("customer_id") == customer_id:
                customer["loyalty_points"] = (
                    customer.get("loyalty_points", 0) + points_to_add
                )
                updated_customer = customer
                break
        payload = {"updated_customer": updated_customer}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCustomerLoyaltyPoints",
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
