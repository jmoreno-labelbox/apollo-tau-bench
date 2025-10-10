# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCustomerDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id) -> str:
        customer = next((c for c in list(data.get('customers', {}).values()) if c['customer_id'] == customer_id), None)
        if customer:
            return json.dumps(customer)
        return json.dumps({"error": "Customer not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_customer_details",
                        "description": "Retrieves the full profile details for a single customer.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string", "description": "The unique ID of the customer."}
                                },
                                "required": ["customer_id"]
                        }
                }
        }
