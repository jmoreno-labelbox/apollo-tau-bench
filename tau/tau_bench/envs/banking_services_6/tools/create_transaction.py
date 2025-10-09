from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List

class CreateTransaction(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], source_account_id: str = None, destination_account_id: str = None, amount: float = 0.0, description: str = "") -> str:
        transaction_id = _get_next_transaction_id(data)

        source_account = next((acc for acc in data["accounts"] if acc["account_id"] == source_account_id), None)
        if not source_account:
            return json.dumps({"error": "Source account not found."})

        source_account["balance"] -= amount

        if destination_account_id:
            dest_account = next((acc for acc in data["accounts"] if acc["account_id"] == destination_account_id), None)
            if dest_account:
                dest_account["balance"] += amount

        new_transaction = {
                "transaction_id": transaction_id,
                "account_id": source_account_id,
                "transaction_date": NOW.strftime(DT_STR_FORMAT),
                "amount": -amount,
                "currency": source_account['currency'],
                "transaction_type": "Transfer" if destination_account_id else "Payment",
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
                        "name": "CreateTransaction",
                        "description": "Creates a new transaction between accounts.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "source_account_id": {"type": "string", "description": "The ID of the account to transfer from."},
                                        "destination_account_id": {"type": "string", "description": "The ID of the account to transfer to (optional for external)."},
                                        "amount": {"type": "number", "description": "The amount to transfer."},
                                        "description": {"type": "string", "description": "A description for the transaction."}
                                },
                                "required": ["source_account_id", "amount", "description"],
                        },
                },
        }
