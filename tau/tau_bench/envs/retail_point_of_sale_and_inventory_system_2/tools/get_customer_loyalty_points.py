from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetCustomerLoyaltyPoints(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], customer_id: str) -> str:
        customers = data.get("customers", {}).values()
        for customer in customers.values():
            if customer.get("customer_id") == customer_id:
                loyalty_info = {
                    "customer_id": customer_id,
                    "name": customer.get("name"),
                    "loyalty_points": customer.get("loyalty_points", 0),
                    "membership_level": customer.get("membership_level", "bronze"),
                }
                payload = loyalty_info
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Customer with ID {customer_id} not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCustomerLoyaltyPoints",
                "description": "Get loyalty points balance for a specific customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique identifier of the customer.",
                        }
                    },
                    "required": ["customer_id"],
                },
            },
        }
