# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCustomerIdByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_name) -> str:
        customers = list(data.get("customers", {}).values())
        for customer in customers:
            if customer.get("name") == customer_name:
                return json.dumps({"customer_id": customer.get("customer_id")})
        return json.dumps({"customer_id": None})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_customer_id_by_name",
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
