from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any, Dict, List
import os

class ApplyTransactionAdjustment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, amount: float = None, reason: str = None) -> str:
        if account_id is None or amount is None or reason is None:
            return json.dumps({"error": "account_id, amount, and reason are required"})

        accounts = load_json("accounts.json")
        accounts = _convert_db_to_list(accounts)
        for account in accounts:
            if account["account_id"] == account_id:
                account["balance"] += amount

                return json.dumps({
                    "success": True,
                    "account_id": account_id,
                    "adjusted_amount": amount,
                    "new_balance": account["balance"],
                    "reason": reason
                })

        return json.dumps({
            "success": False,
            "error": f"Account with ID {account_id} not found."
        })
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ApplyTransactionAdjustment",
                "description": "Applies a manual credit or debit adjustment to a specified account, typically for dispute resolutions or corrections.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {
                            "type": "string",
                            "description": "The ID of the account to apply the adjustment to."
                        },
                        "amount": {
                            "type": "number",
                            "description": "The amount to adjust. Positive for credit, negative for debit."
                        },
                        "reason": {
                            "type": "string",
                            "description": "The reason for the adjustment (e.g., 'Dispute credit reversal')."
                        }
                    },
                    "required": ["account_id", "amount", "reason"]
                }
            }
        }
