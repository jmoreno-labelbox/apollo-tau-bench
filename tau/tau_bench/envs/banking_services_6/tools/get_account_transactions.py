from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List

class GetAccountTransactions(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str, days_history: int = 30, current_date: str = None) -> str:
        current_dt = NOW if not current_date else datetime.combine(date=date.fromisoformat(current_date), time=time(hour=0, minute=0, second=0, tzinfo=timezone.utc))

        transactions = data.get('transactions', [])
        account_transactions = [t for t in transactions if t['account_id'] == account_id]
        cutoff_date = current_dt - timedelta(days=days_history)

        recent_transactions = [
                t for t in account_transactions
                if datetime.fromisoformat(t['transaction_date'].replace('Z', '')).astimezone(timezone.utc) > cutoff_date
        ]

        return json.dumps(recent_transactions)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "GetAccountTransactions",
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
