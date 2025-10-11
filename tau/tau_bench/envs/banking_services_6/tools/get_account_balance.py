# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAccountBalance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id) -> str:
        accounts = list(data.get("accounts", {}).values())
        for account in accounts:
            if account.get("account_id") == account_id:
                return json.dumps({"account_id": account_id, "balance": account.get("balance"), "currency": account.get("currency")})
        return json.dumps({"error": "Account not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_account_balance",
                        "description": "Gets the current balance for a specific account.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "account_id": {"type": "string", "description": "The unique identifier for the account."}
                                },
                                "required": ["account_id"],
                        },
                },
        }
