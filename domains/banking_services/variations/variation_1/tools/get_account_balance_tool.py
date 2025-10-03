from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime, timedelta
from typing import Any, Dict

class GetAccountBalanceTool(Tool):
    """
    Tool to retrieve the current balance and currency of a specified account.

    This tool searches through account records and returns the balance information
    for a valid account ID, or an error message if the account is not found.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Returns the balance and currency for the given account ID.

        get_info() -> Dict[str, Any]:
            Provides metadata and schema for function invocation.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None) -> str:
        if not account_id:
            return json.dumps({"error": "account_id is required"}, indent=2)

        accounts = load_json("accounts.json")
        for acc in accounts:
            if acc["account_id"] == account_id:
                return json.dumps(
                    {
                        "account_id": account_id,
                        "balance": acc["balance"],
                        "currency": acc.get("currency", "USD"),
                    },
                    indent=2,
                )

        return json.dumps({"error": "Account not found"}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAccountBalance",
                "description": "Return the current balance of a customer's account.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account ID"}
                    },
                    "required": ["account_id"],
                },
            },
        }
