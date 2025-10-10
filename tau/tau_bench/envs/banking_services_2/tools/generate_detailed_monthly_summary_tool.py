# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GenerateDetailedMonthlySummaryTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        account_id = kwargs.get('account_id')
        month_str = kwargs.get('month')

        transactions = list(data.get('transactions', {}).values())
        scheduled_payments = data.get('scheduled_payments', [])
        support_tickets = list(data.get('support_tickets', {}).values())

        start_date = f"{month_str}-01T00:00:00Z"
        end_date = f"{month_str}-31T23:59:59Z"

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
            if payment.get('from_account_id', None) == account_id and payment.get('next_payment_date', '')[:7] == month_str:
                scheduled.append(payment)
                if payment.get('frequency') in ['Monthly', 'Weekly']:
                    recurring.append(payment)

        tickets = []
        for ticket in support_tickets:
            if ticket.get('account_id', '') == account_id and ticket.get('created_date', '')[:7] == month_str:
                tickets.append(ticket)

        summary = {
            "account_id": account_id,
            "month": month_str,
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
                "name": "generate_detailed_monthly_summary",
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
