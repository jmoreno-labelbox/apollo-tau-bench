from tau_bench.envs.tool import Tool
from typing import Any, Dict
import json

class GenerateDetailedMonthlySummaryTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, month: str = None) -> str:
        transactions = data.get('transactions', [])
        scheduled_payments = data.get('scheduled_payments', [])
        support_tickets = data.get('support_tickets', [])

        start_date = f"{month}-01T00:00:00Z"
        end_date = f"{month}-31T23:59:59Z"

        purchases = []
        deposits = []
        total_purchases = 0
        total_deposits = 0

        for txn in transactions:
            if txn.get('account_id') != account_id:
                continue
            if txn.get('transaction_date', '') < start_date or txn.get('transaction_date', '') > end_date:
                continue
            if txn.get('transaction_type') == 'Purchase':
                purchases.append(txn)
                total_purchases += abs(txn.get('amount', 0))
            if txn.get('transaction_type') == 'Deposit':
                deposits.append(txn)
                total_deposits += txn.get('amount', 0)

        scheduled = []
        recurring = []
        for payment in scheduled_payments:
            if payment.get('from_account_id', None) == account_id and payment.get('next_payment_date', '')[:7] == month:
                scheduled.append(payment)
                if payment.get('frequency') in ['Monthly', 'Weekly']:
                    recurring.append(payment)

        tickets = []
        for ticket in support_tickets:
            if ticket.get('account_id', '') == account_id and ticket.get('created_date', '')[:7] == month:
                tickets.append(ticket)

        summary = {
            "account_id": account_id,
            "month": month,
            "total_purchases": total_purchases,
            "total_deposits": total_deposits,
            "scheduled_payments": scheduled,
            "recurring_payments": recurring,
            "support_tickets": tickets
        }
        return json.dumps(summary, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateDetailedMonthlySummary",
                "description": "Generate a detailed monthly summary for an account including purchases, deposits, scheduled payments, and support tickets.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account identifier"},
                        "month": {"type": "string", "description": "Month in YYYY-MM format"}
                    },
                    "required": ["account_id", "month"]
                }
            }
        }
