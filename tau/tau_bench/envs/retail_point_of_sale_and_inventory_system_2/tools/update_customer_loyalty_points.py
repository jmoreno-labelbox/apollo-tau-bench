from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateCustomerLoyaltyPoints(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], customer_id: str, points_to_add: int) -> str:
        customers = data.get("customers", [])
        for i, customer in enumerate(customers):
            if customer.get("customer_id") == customer_id:
                current_points = customer.get("loyalty_points", 0)
                customers[i]["loyalty_points"] = current_points + points_to_add
                data["customers"] = customers
                payload = customers[i]
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
                "name": "UpdateCustomerLoyaltyPoints",
                "description": "Update loyalty points for a specific customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique identifier of the customer.",
                        },
                        "points_to_add": {
                            "type": "integer",
                            "description": "Number of points to add.",
                        },
                    },
                    "required": ["customer_id", "points_to_add"],
                },
            },
        }
