from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal

class GetAccountById(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], account_id: Any) -> str:
        account_id = _idstr(account_id)
        if not account_id:
            payload = {"error": "Missing required field: account_id"}
            out = json.dumps(payload, indent=2)
            return out
        accounts = data.get("accounts", [])
        for account in accounts:
            if account.get("account_id") == account_id:
                payload = account
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No account found with ID {account_id}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAccountById",
                "description": "Fetch a single account's full details by its account_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {
                            "type": "string",
                            "description": "Exact account ID to retrieve.",
                        }
                    },
                    "required": ["account_id"],
                },
            },
        }
