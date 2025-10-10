# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTransactionDetailsByAccountIdAndMerchantName(Tool):
    """Retrieves transactions for a specific account and merchant name."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        account_id = (kwargs.get("account_id") or "").strip()
        raw_name = kwargs.get("merchant_name")
        merchant_name = (raw_name or "").strip().lower()

        if not account_id or not merchant_name:
            return json.dumps(
                {"error": "account_id and merchant_name are required."},
                indent=2
            )

        transactions = list(data.get("transactions", {}).values())
        matched = [
            txn for txn in transactions
            if txn.get("account_id") == account_id
            and (txn.get("merchant_name") or "").strip().lower() == merchant_name
        ]

        if not matched:
            return json.dumps({"message": "No matching transactions found."}, indent=2)

        return json.dumps({"transactions": matched}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_transaction_details_by_account_id_and_merchant_name",
                "description": (
                    "Fetches transaction records using the account ID and merchant name."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {
                            "type": "string",
                            "description": "Account ID used for the transactions"
                        },
                        "merchant_name": {
                            "type": "string",
                            "description": "Merchant name to filter transactions (case-insensitive)"
                        }
                    },
                    "required": ["account_id", "merchant_name"]
                }
            }
        }
