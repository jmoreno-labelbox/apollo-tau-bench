# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CaV2GetBankAccounts(Tool):
    """Get all bank account information."""

    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        bank_accounts = data.get("bank_accounts", [])
        return json.dumps(bank_accounts)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_get_bank_accounts",
                "description": "Get all business bank accounts with current balances.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }
