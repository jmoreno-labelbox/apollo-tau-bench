# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTransactionDetailsByAccountIdForTimeDuration(Tool):
    """Returns a list of transactions for a given account ID within a specified time range."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        account_id = kwargs.get("account_id", "").strip()
        start_date_str = kwargs.get("start_date", "").strip()
        end_date_str = kwargs.get("end_date", "").strip()
        customer_id = kwargs.get("customer_id", "").strip()
        if not account_id or not start_date_str or not end_date_str:
            return json.dumps({
                "error": "account_id, start_date, and end_date are required."
            }, indent=2)

        try:
            start_date = datetime.fromisoformat(start_date_str)
            end_date = datetime.fromisoformat(end_date_str)
        except ValueError:
            return json.dumps({
                "error": "Invalid date format. Use ISO format (YYYY-MM-DD)."
            }, indent=2)

        transactions = list(data.get("transactions", {}).values())
        filtered_transactions = [
            txn for txn in transactions
            if txn.get("account_id") == account_id and
               start_date <= datetime.fromisoformat(txn.get("transaction_date", "")) <= end_date
        ]

        return json.dumps(filtered_transactions, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_transaction_details_by_account_id_for_time_duration",
                "description": (
                    "Returns all transactions for a specific account ID between the provided start and end dates."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {
                            "type": "string",
                            "description": "Account ID for which to fetch transactions"
                        },
                        "start_date": {
                            "type": "string",
                            "description": "Start date in ISO format (YYYY-MM-DD)"
                        },
                        "end_date": {
                            "type": "string",
                            "description": "End date in ISO format (YYYY-MM-DD)"
                        }
                    },
                    "required": ["customer_id", "account_id", "start_date", "end_date"]
                }
            }
        }
