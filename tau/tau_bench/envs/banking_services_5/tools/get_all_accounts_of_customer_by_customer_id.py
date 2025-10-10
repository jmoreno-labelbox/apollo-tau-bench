# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAllAccountsOfCustomerByCustomerId(Tool):
    """Returns all account IDs associated with a given customer ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id) -> str:
        if not customer_id:
            return json.dumps({"error": "customer_id is required."}, indent=2)

        customers = list(data.get("customers", {}).values())
        for customer in customers:
            if customer.get("customer_id") == customer_id:
                return json.dumps({
                    "account_ids": customer.get("account_ids", [])
                }, indent=2)

        return json.dumps({"error": "Customer not found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_all_accounts_of_customer_by_customer_id",
                "description": "Returns all account IDs associated with a given customer ID.",
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
