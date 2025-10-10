# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCustomerLoans(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        loans = list(data.get("loans", {}).values())
        customer_loans = [loan for loan in loans if loan.get("customer_id") == customer_id]
        return json.dumps(customer_loans)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_customer_loans",
                        "description": "Retrieves all loans associated with a given customer ID.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string", "description": "The unique identifier for the customer."}
                                },
                                "required": ["customer_id"],
                        },
                },
        }
