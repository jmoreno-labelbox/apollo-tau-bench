# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class TransferMoneyWithConversion(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id, source_account_id, source_amount, source_currency, target_account_id, target_amount, target_currency) -> str:
        src_id          = source_account_id
        tgt_id          = target_account_id

        if not all([customer_id, src_id, tgt_id, source_amount, target_amount, source_currency, target_currency]):
            return json.dumps(
                {"error": "customer_id, source_account_id, target_account_id, source_amount, target_amount, source_currency, and target_currency are required."},
                indent=2
            )

        accounts = list(data.get("accounts", {}).values())
        src = next(
            (a for a in accounts if a.get("account_id") == src_id and a.get("customer_id") == customer_id),
            None
        )
        tgt = next(
            (a for a in accounts if a.get("account_id") == tgt_id),
            None
        )

        if not src:
            return json.dumps({"error": f"Source account '{src_id}' not found for customer '{customer_id}'."}, indent=2)
        if not tgt:
            return json.dumps({"error": f"Target account '{tgt_id}' not found for customer '{customer_id}'."}, indent=2)

        if src.get("currency") != source_currency or tgt.get("currency") != target_currency:
            return json.dumps({"error": "Currency mismatch for one or both accounts."}, indent=2)

        if src.get("balance", 0.0) < source_amount:
            return json.dumps({"error": "Insufficient balance in source account."}, indent=2)

        # execute the transfer
        src["balance"] -= source_amount
        tgt["balance"] = tgt.get("balance", 0.0) + target_amount

        return json.dumps({
            "message": "Cross‑currency transfer successful.",
            "customer_id": customer_id,
            "source_account_id": src_id,
            "target_account_id": tgt_id,
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
                "name": "transfer_money_with_conversion",
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
