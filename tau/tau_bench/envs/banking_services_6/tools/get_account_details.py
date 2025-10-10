# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAccountDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        account_id = kwargs.get("account_id")
        account = next((a for a in data['accounts'] if a['account_id'] == account_id), None)
        if account:
            return json.dumps(account)
        return json.dumps({"error": "Account not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_account_details",
                        "description": "Retrieves full details for a specific account.",
                        "parameters": {
                                "type": "object",
                                "properties": {"account_id": {"type": "string"}},
                                "required": ["account_id"]
                        }
                }
        }
