# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAccountByName(Tool):
    """Fetch a company account record by its account_name."""

    @staticmethod
    def invoke(data: Dict[str, Any], name: Any) -> str:
        account_name = name
        if not account_name:
            return json.dumps({"error": "Missing required field: name"}, indent=2)
        accounts = list(data.get("accounts", {}).values())
        for account in accounts:
            if account.get("account_name") == account_name:
                return json.dumps(account, indent=2)

        return json.dumps({"error": f"No account found with name '{account_name}'"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_account_by_name",
                "description": "Fetch a single company account's full details by its account_name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Exact company account name to retrieve.",
                        }
                    },
                    "required": ["name"],
                },
            },
        }
