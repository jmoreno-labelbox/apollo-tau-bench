# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCustomerDetailsByCustomerId(Tool):
    """Returns full customer record given a customer_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id = "") -> str:
        customer_id = customer_id.strip()
        if not customer_id:
            return json.dumps(
                {"error": "customer_id is required."},
                indent=2
            )

        customer = next(
            (c for c in list(data.get("customers", {}).values())
             if c.get("customer_id") == customer_id),
            None
        )
        if not customer:
            return json.dumps(
                {"error": f"Customer '{customer_id}' not found."},
                indent=2
            )

        return json.dumps(customer, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_customer_details_by_customer_id",
                "description": "Fetches the complete customer record for the given customer_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique identifier of the customer"
                        }
                    },
                    "required": ["customer_id"]
                }
            }
        }
