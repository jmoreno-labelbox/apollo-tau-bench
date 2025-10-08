from tau_bench.envs.tool import Tool
from typing import Any, Dict
import json

class CalculateTotalPaymentsTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, start_date: str = None, end_date: str = None, transaction_type: str = None) -> str:
        transactions = data.get('transactions', [])
        total_payments = 0
        payment_count = 0
        
        # Use transaction_type parameter if provided, otherwise default to 'payment'
        filter_type = transaction_type.lower() if transaction_type else 'payment'

        for txn in transactions:
            if txn.get('account_id') != account_id:
                continue
            txn_date = txn.get('transaction_date', '')
            if start_date and txn_date < start_date:
                continue
            if end_date and txn_date > end_date:
                continue
            if txn.get('transaction_type', '').lower() == filter_type:
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
                "name": "CalculateTotalPayments",
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
