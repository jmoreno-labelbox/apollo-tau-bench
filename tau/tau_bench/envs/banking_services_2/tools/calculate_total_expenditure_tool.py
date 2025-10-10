# Sierra copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateTotalExpenditureTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id, end_date, start_date, transaction_type = 'Purchase') -> str:

        transactions = list(data.get('transactions', {}).values())
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
            "total_expenditure": total,
            "transaction_count": len(matching)
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_total_expenditure",
                "description": "Calculate total expenditure for purchases or other transaction types in a date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account identifier"},
                        "start_date": {"type": "string", "description": "Start date (ISO format)"},
                        "end_date": {"type": "string", "description": "End date (ISO format)"},
                        "transaction_type": {"type": "string", "description": "Type of transaction (e.g. Purchase, Withdrawal)"}
                    },
                    "required": ["account_id", "start_date", "end_date", "transaction_type"]
                }
            }
        }
