from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List

class GetAccountBalance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None) -> str:
        accounts = data.get("accounts", [])
        for account in accounts:
            if account.get("account_id") == account_id:
                return json.dumps({"account_id": account_id, "balance": account.get("balance"), "currency": account.get("currency")})
        return json.dumps({"error": "Account not found"})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "GetAccountBalance",
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
