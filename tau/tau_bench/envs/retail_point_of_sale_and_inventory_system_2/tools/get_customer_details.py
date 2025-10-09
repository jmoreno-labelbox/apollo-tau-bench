from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetCustomerDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], customer_id: str) -> str:
        customers = data.get("customers", [])
        for customer in customers:
            if customer.get("customer_id") == customer_id:
                payload = customer
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
                "name": "GetCustomerDetails",
                "description": "Get detailed information about a specific customer.",
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
