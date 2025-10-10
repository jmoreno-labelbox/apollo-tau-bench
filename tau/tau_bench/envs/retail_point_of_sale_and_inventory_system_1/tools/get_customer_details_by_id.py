# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCustomerDetailsById(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get('customer_id')
        customers = list(data.get("customers", {}).values())  # Lista []
        for customer in customers:
            if customer.get("customer_id") == customer_id:
                return json.dumps(customer)
        return json.dumps({})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_customer_details_by_id",
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
