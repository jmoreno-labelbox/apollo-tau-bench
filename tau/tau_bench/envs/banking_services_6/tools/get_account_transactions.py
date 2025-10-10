# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAccountTransactions(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        account_id = kwargs.get("account_id")
        days_history = kwargs.get("days_history", 30)
        current_date = kwargs.get("current_date")
        current_dt = NOW if not current_date else datetime.combine(date=date.fromisoformat(current_date), time=time(hour=0, minute=0, second=0, tzinfo=UTC))

        transactions = list(data.get('transactions', {}).values())
        account_transactions = [t for t in transactions if t['account_id'] == account_id]
        cutoff_date = current_dt - timedelta(days=days_history)

        recent_transactions = [
                t for t in account_transactions
                if datetime.fromisoformat(t['transaction_date'].replace('Z', '')).astimezone(UTC) > cutoff_date
        ]

        return json.dumps(recent_transactions)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_account_transactions",
                        "description": "Retrieves transaction history for a specific account for a given period.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "account_id": {"type": "string"},
                                        "days_history": {"type": "integer", "description": "Number of past days to fetch transactions for. Defaults to 30."},
                                        "current_date": {"type": "string", "description": "The current date in ISO format. Defaults to today."}
                                },
                                "required": ["account_id"]
                        }
                }
        }
