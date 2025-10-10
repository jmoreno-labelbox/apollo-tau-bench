# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ApplyTransactionAdjustment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        account_id = kwargs.get("account_id")
        amount = kwargs.get("amount")
        reason = kwargs.get("reason")

        if account_id is None or amount is None or reason is None:
            return json.dumps({"error": "account_id, amount, and reason are required"})

        accounts = load_json("accounts.json")
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
                "name": "apply_transaction_adjustment",
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
