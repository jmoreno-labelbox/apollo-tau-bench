from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class GetCustomerIdByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], customer_name: str = None) -> str:
        customers = data.get("customers", [])
        for customer in customers:
            if customer.get("name") == customer_name:
                payload = {"customer_id": customer.get("customer_id")}
                out = json.dumps(payload)
                return out
        payload = {"customer_id": None}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCustomerIdByName",
                "description": "Retrieves the customer ID for a given customer name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_name": {
                            "type": "string",
                            "description": "The full name of the customer.",
                        },
                    },
                    "required": ["customer_name"],
                },
            },
        }
