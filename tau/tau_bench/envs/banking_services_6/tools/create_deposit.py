# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateDeposit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        transaction_id = _get_next_transaction_id(data)
        account_id = kwargs.get("account_id")
        amount = kwargs.get("amount")
        description = kwargs.get("description")

        account = next((acc for acc in data["accounts"] if acc["account_id"] == account_id), None)
        if not account:
            return json.dumps({"error": "Account not found."})

        account["balance"] += amount

        new_transaction = {
                "transaction_id": transaction_id,
                "account_id": account_id,
                "transaction_date": NOW.strftime(DT_STR_FORMAT),
                "amount": amount,
                "currency": account['currency'],
                "transaction_type": "Deposit",
                "description": description,
                "status": "Completed",
                "channel": "Online"
        }
        data["transactions"].append(new_transaction)

        return json.dumps(new_transaction)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "create_deposit",
                        "description": "Records an external deposit into an account.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "account_id": {"type": "string"},
                                        "amount": {"type": "number"},
                                        "description": {"type": "string"}
                                },
                                "required": ["account_id", "amount", "description"]
                        }
                }
        }
