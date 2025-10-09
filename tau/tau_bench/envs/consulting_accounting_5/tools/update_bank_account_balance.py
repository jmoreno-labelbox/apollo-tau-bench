from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any, Dict
from datetime import timedelta

class UpdateBankAccountBalance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str, balance: float, account_type: str = "") -> str:
        """
        Updates or inserts balance for a given bank account.
        """
        account = next((b for b in data["bank_accounts"].values() if b["account_id"] == account_id), None)

        if account:
            account["balance"] = balance
        else:
            account = {
                "account_id": account_id,
                "account_type": account_type,
                "balance": balance
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
