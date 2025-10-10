# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCustomerAccountDetailsByCustomerId(Tool):
    """Returns the full account details of a customer using customer_id and last 4 digits of the account number."""

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id) -> str:

        if not customer_id :
            return json.dumps({
                "error": "customer_id is required."
            }, indent=2)

        accounts = list(data.get("accounts", {}).values())
        for account in accounts:
            if (account.get("customer_id") == customer_id ):
                return json.dumps(account, indent=2)

        return json.dumps({"error": "Account not found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_customer_account_details_by_customer_id",
                "description": (
                    "Returns the full account record for a customer using their customer_id "
                    "and the last 4 digits of their account number."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique ID of the customer"
                        }
                    },
                    "required": ["customer_id"]
                }
            }
        }
