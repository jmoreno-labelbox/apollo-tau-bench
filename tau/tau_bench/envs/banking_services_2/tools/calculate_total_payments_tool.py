# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateTotalPaymentsTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        account_id = kwargs.get('account_id')
        start_date = kwargs.get('start_date')
        end_date = kwargs.get('end_date')

        transactions = list(data.get('transactions', {}).values())
        total_payments = 0
        payment_count = 0

        for txn in transactions:
            if txn.get('account_id') != account_id:
                continue
            txn_date = txn.get('transaction_date', '')
            if start_date and txn_date < start_date:
                continue
            if end_date and txn_date > end_date:
                continue
            if txn.get('transaction_type', '').lower() == 'payment':
                total_payments += abs(txn.get('amount', 0))
                payment_count += 1

        return json.dumps({
            "account_id": account_id,
            "start_date": start_date,
            "end_date": end_date,
            "total_payments": total_payments,
            "payment_count": payment_count
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_total_payments",
                "description": "Calculate total payments for an account in a given date range.",
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
