from tau_bench.envs.tool import Tool
from typing import Any, Dict
import json

class CalculateTotalWithdrawalTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, start_date: str = None, end_date: str = None) -> str:
        transaction_type = 'Withdrawal'

        transactions = data.get('transactions', [])
        total = 0
        matching = []

        for transaction in transactions:
            if transaction.get('account_id') != account_id:
                continue
            if transaction.get('transaction_type') != transaction_type:
                continue
            if start_date and transaction.get('transaction_date', '') < start_date:
                continue
            if end_date and transaction.get('transaction_date', '') > end_date:
                continue
            total += abs(transaction.get('amount', 0))
            matching.append(transaction)

        return json.dumps({
            "account_id": account_id,
            "transaction_type": transaction_type,
            "start_date": start_date,
            "end_date": end_date,
            "total_withdrawal": total,
            "transaction_count": len(matching)
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateTotalWithdrawal",
                "description": "Calculate total withdrawals for an account in a date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account identifier"},
                        "start_date": {"type": "string", "description": "Start date (ISO format)"},
                        "end_date": {"type": "string", "description": "End date (ISO format)"}
                    },
                    "required": ["account_id", "start_date", "end_date"]
                }
            }
        }
