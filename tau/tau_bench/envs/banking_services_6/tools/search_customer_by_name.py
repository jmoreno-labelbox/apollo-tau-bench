# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchCustomerByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        first_name = kwargs.get("first_name")
        last_name = kwargs.get("last_name")
        customers = list(data.get("customers", {}).values())
        results = []
        for customer in customers:
            pi = customer.get("personal_info", {})
            if pi.get("first_name", "").lower().strip() == first_name.lower().strip() and \
                    pi.get("last_name", "").lower().strip() == last_name.lower().strip():
                results.append(customer)
        return json.dumps(results)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "search_customer_by_name",
                        "description": "Searches for a customer by their first and last name.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "first_name": {"type": "string", "description": "The customer's first name."},
                                        "last_name": {"type": "string", "description": "The customer's last name."}
                                },
                                "required": ["first_name", "last_name"],
                        },
                },
        }
