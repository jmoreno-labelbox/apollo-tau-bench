# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAccountById(Tool):
    """Read an account by its account_id."""

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_account_by_id",
                "description": "Return a single account record for the given account_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "The account_id to fetch."}
                    },
                    "required": ["account_id"],
                    "additionalProperties": False,
                },
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], account_id: Any) -> str:
        accounts = data.get("accounts") or []
        target_id = str(account_id)
        result = {}
        for acc in accounts:
            if str(acc.get("account_id")) == target_id:
                result = acc
                break
        return json.dumps(result, indent=2)
