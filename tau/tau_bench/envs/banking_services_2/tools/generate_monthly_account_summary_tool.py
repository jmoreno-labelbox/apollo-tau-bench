from tau_bench.envs.tool import Tool
from typing import Any, Dict
import json



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GenerateMonthlyAccountSummaryTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, month: str = None) -> str:
        transactions = data.get('transactions', {}).values()
        scheduled_payments = data.get('scheduled_payments', {}).values()
        support_tickets = data.get('support_tickets', {}).values()

        start_date = f"{month}-01T00:00:00Z"
        end_date = f"{month}-31T23:59:59Z"

        total_deposits = 0
        total_withdrawals = 0
        total_purchases = 0
        transaction_count = 0

        for txn in transactions.values():
            if txn.get('account_id') != account_id:
                continue
            txn_date = txn.get('transaction_date', '')
            if txn_date < start_date or txn_date > end_date:
                continue
            transaction_count += 1
            if txn.get('transaction_type') == 'Deposit':
                total_deposits += txn.get('amount', 0)
            if txn.get('transaction_type') == 'Withdrawal':
                total_withdrawals += abs(txn.get('amount', 0))
            if txn.get('transaction_type') == 'Purchase':
                total_purchases += abs(txn.get('amount', 0))

        scheduled_count = sum(
            1 for payment in scheduled_payments.values() if payment.get('from_account_id', None) == account_id and payment.get('next_payment_date', '')[:7] == month
        )

        support_ticket_count = sum(
            1 for ticket in support_tickets.values() if ticket.get('account_id', '') == account_id and ticket.get('created_date', '')[:7] == month
        )

        summary = {
            "account_id": account_id,
            "month": month,
            "total_deposits": total_deposits,
            "total_withdrawals": total_withdrawals,
            "total_purchases": total_purchases,
            "transaction_count": transaction_count,
            "scheduled_payment_count": scheduled_count,
            "support_ticket_count": support_ticket_count
        }
        return json.dumps(summary, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateMonthlyAccountSummary",
                "description": "Generate a summary for an account for a given month, including totals for deposits, withdrawals, purchases, transaction count, scheduled payments, and support tickets.",
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
