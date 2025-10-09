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

class GetTransactionDetailsByAccountIdForTimeDuration(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = "", start_date: str = "", end_date: str = "", customer_id: str = "") -> str:
        account_id = account_id.strip()
        start_date_str = start_date.strip()
        end_date_str = end_date.strip()
        customer_id = customer_id.strip()
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

        transactions = data.get("transactions", {}).values()
        filtered_transactions = [
            txn for txn in transactions.values() if txn.get("account_id") == account_id and
               start_date <= datetime.fromisoformat(txn.get("transaction_date", "")) <= end_date
        ]

        return json.dumps(filtered_transactions, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getTransactionDetailsByAccountIdForTimeDuration",
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
