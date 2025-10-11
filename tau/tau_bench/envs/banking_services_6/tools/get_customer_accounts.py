# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCustomerAccounts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id) -> str:
        accounts = list(data.get("accounts", {}).values())
        customer_accounts = [acc for acc in accounts if acc.get("customer_id") == customer_id]
        return json.dumps(customer_accounts)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_customer_accounts",
                        "description": "Retrieves all accounts associated with a given customer ID.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string", "description": "The unique identifier for the customer."}
                                },
                                "required": ["customer_id"],
                        },
                },
        }
