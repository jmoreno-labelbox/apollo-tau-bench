# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAccountDetailsByCustomerIdAndAccountId(Tool):
    """
    Retrieves a single account’s details by matching both customer_id and account_id.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], account_id, customer_id) -> str:

        if not customer_id or not account_id:
            return json.dumps({
                "error": "customer_id and account_id are both required."
            }, indent=2)

        # Retrieve the account information.
        acct = next(
            (a for a in list(data.get("accounts", {}).values())
             if a.get("customer_id") == customer_id and a.get("account_id") == account_id),
            None
        )

        if not acct:
            return json.dumps({
                "error": f"No account found for customer_id '{customer_id}' with account_id '{account_id}'."
            }, indent=2)

        # Provide the account information.
        return json.dumps({
            "account_id":            acct["account_id"],
            "customer_id":           acct["customer_id"],
            "account_type":          acct["account_type"],
            "balance":               acct.get("balance"),
            "currency":              acct.get("currency"),
            "status":                acct.get("status"),
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
        "function": {
            "name": "get_account_details_by_customer_id_and_account_id",
            "description": "Fetches the full details of an account matching the given customer_id and account_id.",
            "parameters": {
                "type": "object",
                "properties": {
                    "customer_id": {
                        "type": "string",
                        "description": "ID of the customer who owns the account."
                    },
                    "account_id": {
                        "type": "string",
                        "description": "ID of the account to retrieve."
                    }
                },
                "required": ["customer_id", "account_id"]
            }
        }
    }
