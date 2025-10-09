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
        return list(db.values())
    return db

class TransferMoneyWithConversion(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        customer_id: str = None,
        source_account_id: str = None,
        target_account_id: str = None,
        source_amount: float = None,
        target_amount: float = None,
        source_currency: str = None,
        target_currency: str = None
    ) -> str:
        if not all([customer_id, source_account_id, target_account_id, source_amount, target_amount, source_currency, target_currency]):
            return json.dumps(
                {"error": "customer_id, source_account_id, target_account_id, source_amount, target_amount, source_currency, and target_currency are required."},
                indent=2
            )

        accounts = data.get("accounts", [])
        src = next(
            (a for a in accounts if a.get("account_id") == source_account_id and a.get("customer_id") == customer_id),
            None
        )
        tgt = next(
            (a for a in accounts if a.get("account_id") == target_account_id),
            None
        )

        if not src:
            return json.dumps({"error": f"Source account '{source_account_id}' not found for customer '{customer_id}'."}, indent=2)
        if not tgt:
            return json.dumps({"error": f"Target account '{target_account_id}' not found for customer '{customer_id}'."}, indent=2)

        if src.get("currency") != source_currency or tgt.get("currency") != target_currency:
            return json.dumps({"error": "Currency mismatch for one or both accounts."}, indent=2)

        if src.get("balance", 0.0) < source_amount:
            return json.dumps({"error": "Insufficient balance in source account."}, indent=2)

        # perform the transfer
        src["balance"] -= source_amount
        tgt["balance"] = tgt.get("balance", 0.0) + target_amount

        return json.dumps({
            "message": "Cross‑currency transfer successful.",
            "customer_id": customer_id,
            "source_account_id": source_account_id,
            "target_account_id": target_account_id,
            "source_amount": source_amount,
            "target_amount": target_amount,
            "source_balance": src["balance"],
            "target_balance": tgt["balance"]
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "transferMoneyWithConversion",
                "description": (
                    "Transfers funds between two accounts of the same customer in different currencies when the source and target amounts are pre‑computed."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id":     {"type": "string", "description": "ID of the customer performing the transfer"},
                        "source_account_id": {"type": "string", "description": "Account ID to debit"},
                        "target_account_id": {"type": "string", "description": "Account ID to credit"},
                        "source_amount":     {"type": "number", "description": "Amount in source currency to debit"},
                        "target_amount":     {"type": "number", "description": "Amount in target currency to credit"},
                        "source_currency":   {"type": "string", "description": "Currency code of the source amount"},
                        "target_currency":   {"type": "string", "description": "Currency code of the target amount"}
                    },
                    "required": [
                        "customer_id",
                        "source_account_id",
                        "target_account_id",
                        "source_amount",
                        "target_amount",
                        "source_currency",
                        "target_currency"
                    ]
                }
            }
        }
