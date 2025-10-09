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

class GetTransactionDetailsByAccountIdAndMerchantName(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, merchant_name: str = None) -> str:
        account_id = (account_id or "").strip()
        merchant_name = (merchant_name or "").strip().lower()

        if not account_id or not merchant_name:
            return json.dumps(
                {"error": "account_id and merchant_name are required."},
                indent=2
            )

        transactions = data.get("transactions", {}).values()
        matched = [
            txn for txn in transactions.values() if txn.get("account_id") == account_id
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
                "name": "getTransactionDetailsByAccountIdAndMerchantName",
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
