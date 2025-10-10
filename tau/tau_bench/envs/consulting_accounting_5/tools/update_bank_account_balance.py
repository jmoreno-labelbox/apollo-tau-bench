# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateBankAccountBalance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Updates or inserts balance for a given bank account.
        """
        account_id = kwargs["account_id"]
        new_balance = kwargs["balance"]
        account = next((b for b in data["bank_accounts"] if b["account_id"] == account_id), None)

        if account:
            account["balance"] = new_balance
        else:
            account = {
                "account_id": account_id,
                "account_type": kwargs.get("account_type", ""),
                "balance": new_balance
            }
            data["bank_accounts"].append(account)

        return json.dumps(account["account_id"])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateBankAccountBalance",
                "description": "Update or insert a bank account balance in bank_accounts.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string"},
                        "balance": {"type": "number"},
                        "account_type": {"type": "string"}
                    },
                    "required": ["account_id", "balance"],
                },
            },
        }
