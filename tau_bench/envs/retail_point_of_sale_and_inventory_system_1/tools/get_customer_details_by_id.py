from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class GetCustomerDetailsById(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], customer_id: str = None) -> str:
        customers = data.get("customers", [])
        for customer in customers:
            if customer.get("customer_id") == customer_id:
                payload = customer
                out = json.dumps(payload)
                return out
        payload = {}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCustomerDetailsById",
                "description": "Retrieves all details for a customer given their ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "The ID of the customer.",
                        },
                    },
                    "required": ["customer_id"],
                },
            },
        }
