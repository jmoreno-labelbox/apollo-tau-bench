from tau_bench.envs.tool import Tool
from typing import Any, Dict
import json

class CalculateTotalEventAndPurchaseSpendingTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, start_date: str = None, end_date: str = None) -> str:
        transactions = data.get('transactions', [])
        total_spending = 0
        event_spending = 0
        purchase_spending = 0
        event_count = 0
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
            amount = abs(txn.get('amount', 0))
            if txn_type == 'Event':
                event_spending += amount
                total_spending += amount
                event_count += 1
            elif txn_type == 'Purchase':
                purchase_spending += amount
                total_spending += amount
                purchase_count += 1

        return json.dumps({
            "account_id": account_id,
            "start_date": start_date,
            "end_date": end_date,
            "total_event_spending": event_spending,
            "total_purchase_spending": purchase_spending,
            "total_combined_spending": total_spending,
            "event_transaction_count": event_count,
            "purchase_transaction_count": purchase_count
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateTotalEventAndPurchaseSpending",
                "description": "Calculate total spending for 'Event' and 'Purchase' transactions for an account in a given date range.",
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
