# Copyright Sierra Technologies.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateTotalDepositsAndPurchasesTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id, end_date, start_date) -> str:

        transactions = list(data.get('transactions', {}).values())
        total_deposits = 0
        total_purchases = 0
        deposit_count = 0
        purchase_count = 0

        for txn in transactions:
            if txn.get('account_id') != account_id:
                continue
            txn_date = txn.get('transaction_date', '')
            if start_date and txn_date < start_date:
                continue
            if end_date and txn_date > end_date:
                continue
            txn_type = txn.get('transaction_type', '')
            amount = txn.get('amount', 0)
            if txn_type == 'Deposit':
                total_deposits += amount
                deposit_count += 1
            elif txn_type == 'Purchase':
                total_purchases += abs(amount)
                purchase_count += 1

        return json.dumps({
            "account_id": account_id,
            "start_date": start_date,
            "end_date": end_date,
            "total_deposits": total_deposits,
            "total_purchases": total_purchases,
            "deposit_count": deposit_count,
            "purchase_count": purchase_count
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_total_deposits_and_purchases",
                "description": "Calculate total deposits and purchases for an account in a given date range.",
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
