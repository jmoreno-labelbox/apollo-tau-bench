# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class BlockAccountForCustomerId(Tool):
    """Blocks a customer's account by setting its status to 'Blocked'."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        account_id = kwargs.get("account_id")
        if not customer_id or not account_id:
            return json.dumps(
                {"error": "Both customer_id and account_id are required."},
                indent=2
            )

        # Locate the account and confirm ownership.
        accounts = list(data.get("accounts", {}).values())
        account = next((a for a in accounts
                        if a["account_id"] == account_id
                        and a["customer_id"] == customer_id), None)
        if not account:
            return json.dumps(
                {"error": "Account not found or does not belong to the customer."},
                indent=2
            )

        # Prevent it.
        account["status"] = "Blocked"
        return json.dumps(account, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "block_account_for_customer_id",
                "description": "Sets the status of a given customer’s account to 'Blocked'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "ID of the customer who owns the account"
                        },
                        "account_id": {
                            "type": "string",
                            "description": "ID of the account to block"
                        }
                    },
                    "required": ["customer_id", "account_id"]
                }
            }
        }
