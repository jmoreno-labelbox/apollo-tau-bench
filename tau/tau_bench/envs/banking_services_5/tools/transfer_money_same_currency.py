from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone, date, timedelta
import calendar
from typing import Any, Dict
import random



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class TransferMoneySameCurrency(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, source_account_id: str = None, 
               target_account_id: str = None, currency: str = None, amount: float = None) -> str:
        if not all([customer_id, source_account_id, target_account_id, currency, amount]):
            return json.dumps(
                {"error": "customer_id, source_account_id, target_account_id, currency, and amount are required."},
                indent=2
            )

        accounts = data.get("accounts", {}).values()
        src = next((a for a in accounts.values() if a["account_id"] == source_account_id and a.get("customer_id") == customer_id), None)
        tgt = next((a for a in accounts.values() if a["account_id"] == target_account_id), None)

        if not src:
            return json.dumps({"error": f"Source account '{source_account_id}' not found for customer '{customer_id}'."}, indent=2)
        if not tgt:
            return json.dumps({"error": f"Target account '{target_account_id}' not found for customer '{customer_id}'."}, indent=2)

        if src.get("currency") != currency or tgt.get("currency") != currency:
            return json.dumps({"error": "Currency mismatch for same‑currency transfer."}, indent=2)

        if src.get("balance", 0.0) < amount:
            return json.dumps({"error": "Insufficient balance in source account."}, indent=2)

        src["balance"] -= amount
        tgt["balance"] += amount

        return json.dumps({
            "message": "Transfer successful (same currency).",
            "customer_id": customer_id,
            "source_account_id": source_account_id,
            "target_account_id": target_account_id,
            "amount_transferred": amount,
            "currency": currency,
            "source_balance": src["balance"],
            "target_balance": tgt["balance"]
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "TransferMoneySameCurrency",
                "description": "Transfers funds between two accounts of the same customer in the same currency.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "ID of the customer performing the transfer"},
                        "source_account_id": {"type": "string", "description": "Account ID to debit"},
                        "target_account_id": {"type": "string", "description": "Account ID to credit"},
                        "currency": {"type": "string", "description": "Currency of the transfer"},
                        "amount": {"type": "number", "description": "Amount to transfer"}
                    },
                    "required": ["customer_id", "source_account_id", "target_account_id", "currency", "amount"]
                }
            }
        }
