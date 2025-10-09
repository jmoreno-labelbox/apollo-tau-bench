from tau_bench.envs.tool import Tool
from typing import Any, Dict
import json

class GenerateFinancialReportTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, start_date: str = None, end_date: str = None) -> str:
        transactions = data.get('transactions', [])
        scheduled_payments = data.get('scheduled_payments', [])
        support_tickets = data.get('support_tickets', [])
        loans = data.get('loans', [])

        total_deposits = 0
        total_withdrawals = 0
        total_purchases = 0
        total_payments = 0
        total_bill_payments = 0
        total_atm_withdrawals = 0
        deposit_count = 0
        withdrawal_count = 0
        purchase_count = 0
        payment_count = 0
        bill_payment_count = 0
        atm_withdrawal_count = 0

        for txn in transactions:
            if txn.get('account_id') != account_id:
                continue
            txn_date = txn.get('transaction_date', '')

            if start_date and txn_date and txn_date < start_date:
                continue
            if end_date and txn_date and txn_date > end_date:
                continue

            txn_type = txn.get('transaction_type', '').lower()
            amount = txn.get('amount', 0)

            if txn_type == 'deposit':
                total_deposits += amount
                deposit_count += 1
            elif txn_type == 'withdrawal':
                total_withdrawals += abs(amount)
                withdrawal_count += 1
            elif txn_type == 'purchase':
                total_purchases += abs(amount)
                purchase_count += 1
            elif txn_type == 'payment':
                total_payments += abs(amount)
                payment_count += 1
            elif txn_type == 'bill payment':
                total_bill_payments += abs(amount)
                bill_payment_count += 1
            elif txn_type == 'atm withdrawal':
                total_atm_withdrawals += abs(amount)
                atm_withdrawal_count += 1

        scheduled_count = 0
        for payment in scheduled_payments:
            if payment.get('from_account_id', None) != account_id:
                continue
            payment_date = payment.get('next_payment_date', '')

            if start_date and payment_date and payment_date < start_date:
                continue
            if end_date and payment_date and payment_date > end_date:
                continue
            scheduled_count += 1

        support_ticket_count = 0
        for ticket in support_tickets:
            if ticket.get('account_id', '') != account_id:
                continue
            ticket_date = ticket.get('created_date', '')

            if start_date and ticket_date and ticket_date < start_date:
                continue
            if end_date and ticket_date and ticket_date > end_date:
                continue
            support_ticket_count += 1

        loans_for_account = []
        for loan in loans:
            if loan.get('account_id', '') != account_id:
                continue
            loan_date = loan.get('issue_date', '')

            if start_date and loan_date and loan_date < start_date:
                continue
            if end_date and loan_date and loan_date > end_date:
                continue
            loans_for_account.append(loan)

        report = {
            "account_id": account_id,
            "start_date": start_date,
            "end_date": end_date,
            "totals": {
                "deposits": total_deposits,
                "withdrawals": total_withdrawals,
                "purchases": total_purchases,
                "payments": total_payments,
                "bill_payments": total_bill_payments,
                "atm_withdrawals": total_atm_withdrawals
            },
            "counts": {
                "deposits": deposit_count,
                "withdrawals": withdrawal_count,
                "purchases": purchase_count,
                "payments": payment_count,
                "bill_payments": bill_payment_count,
                "atm_withdrawals": atm_withdrawal_count,
                "scheduled_payments": scheduled_count,
                "support_tickets": support_ticket_count,
                "loans": len(loans_for_account)
            },
            "loans": loans_for_account
        }
        return json.dumps(report, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateFinancialReport",
                "description": "Generate a comprehensive financial report for an account, including totals and counts for deposits, withdrawals, purchases, payments, bill payments, ATM withdrawals, scheduled payments, support tickets, and loans over a given period.",
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
