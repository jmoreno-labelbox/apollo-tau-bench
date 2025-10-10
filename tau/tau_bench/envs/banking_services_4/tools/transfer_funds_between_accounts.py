# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class TransferFundsBetweenAccounts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        from_account_id = kwargs.get("from_account_id")
        to_account_id = kwargs.get("to_account_id")
        amount = kwargs.get("amount")
        reason = kwargs.get("reason", "Fund transfer")

        if not from_account_id or not to_account_id or amount is None:
            return json.dumps({"error": "from_account_id, to_account_id, and amount are required"})

        accounts = load_json("accounts.json")

        from_account = next((acc for acc in accounts if acc["account_id"] == from_account_id), None)
        to_account = next((acc for acc in accounts if acc["account_id"] == to_account_id), None)

        if from_account is None:
            return json.dumps({"error": f"from_account_id {from_account_id} not found"})
        if to_account is None:
            return json.dumps({"error": f"to_account_id {to_account_id} not found"})
        if from_account["balance"] < amount:
            return json.dumps({"error": "Insufficient funds in source account"})

        from_account["balance"] -= amount
        to_account["balance"] += amount

        return json.dumps({
            "success": True,
            "from_account_id": from_account_id,
            "to_account_id": to_account_id,
            "transferred_amount": amount,
            "reason": reason,
            "from_account_balance": from_account["balance"],
            "to_account_balance": to_account["balance"],
            "note": "Changes are in-memory only; not persisted to file."
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "transfer_funds_between_accounts",
                "description": "Transfers a specified amount from one account to another.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "from_account_id": {
                            "type": "string",
                            "description": "The source account ID to debit funds from."
                        },
                        "to_account_id": {
                            "type": "string",
                            "description": "The destination account ID to credit funds to."
                        },
                        "amount": {
                            "type": "number",
                            "description": "The amount to transfer."
                        },
                        "reason": {
                            "type": "string",
                            "description": "Optional reason for the transfer."
                        }
                    },
                    "required": ["from_account_id", "to_account_id", "amount"]
                }
            }
        }
