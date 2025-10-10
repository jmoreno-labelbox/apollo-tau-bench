# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCustomerDetailsByName(Tool):
    """Returns the full customer object using first name and last name."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        first_name = kwargs.get("first_name", "").strip().lower()
        last_name = kwargs.get("last_name", "").strip().lower()

        if not first_name or not last_name:
            return json.dumps({
                "error": "first_name and last_name are required."
            }, indent=2)

        customers = list(data.get("customers", {}).values())
        for customer in customers:
            pi = customer.get("personal_info", {})
            if (
                pi.get("first_name", "").strip().lower() == first_name and
                pi.get("last_name", "").strip().lower() == last_name
            ):
                return json.dumps(customer, indent=2)

        return json.dumps({"error": "Customer not found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_customer_details_by_name",
                "description": "Returns the full customer object based on first name and last name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {
                            "type": "string",
                            "description": "Customer's first name"
                        },
                        "last_name": {
                            "type": "string",
                            "description": "Customer's last name"
                        }
                    },
                    "required": ["first_name", "last_name"]
                }
            }
        }
