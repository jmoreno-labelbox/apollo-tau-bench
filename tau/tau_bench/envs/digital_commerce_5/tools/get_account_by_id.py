# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAccountById(Tool):
    """Fetch an account record by its account_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str) -> str:
        account_id = str(account_id)
        if not account_id:
            return json.dumps({"error": "Missing required field: account_id"}, indent=2)
        accounts = list(list(list(data.get("accounts", {}).values())) if isinstance(data.get("accounts"), dict) else data.get("accounts", []))
        for account in accounts:
            if account.get("account_id") == account_id:
                return json.dumps(account, indent=2)
        return json.dumps({"error": f"No account found with ID {account_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_account_by_id",
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
