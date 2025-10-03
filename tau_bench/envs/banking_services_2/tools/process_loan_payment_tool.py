from tau_bench.envs.tool import Tool
from typing import Any, Dict
import json

class ProcessLoanPaymentTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], loan_id: str = None, payment_amount: float = None, from_account_id: str = None) -> str:
        loans = data.get('loans', [])
        accounts = data.get('accounts', [])
        transactions = data.get('transactions', [])

        loan = None
        for l in loans:
            if l['loan_id'] == loan_id:
                loan = l
                break

        if not loan:
            return json.dumps({"error": f"Loan {loan_id} not found"}, indent=2)

        account = None
        for a in accounts:
            if a['account_id'] == from_account_id:
                account = a
                break

        if not account or account['balance'] < payment_amount:
            return json.dumps({"error": "Insufficient funds"}, indent=2)

        account['balance'] -= payment_amount
        loan['current_balance'] -= payment_amount

        transaction = {
            "transaction_id": f"txn_{generate_unique_id()}",
            "account_id": from_account_id,
            "transaction_date": get_current_timestamp(),
            "amount": -payment_amount,
            "currency": "USD",
            "transaction_type": "Loan Payment",
            "description": f"Loan payment for {loan_id}",
            "status": "Completed",
            "channel": "Online"
        }

        transactions.append(transaction)

        return json.dumps({
            "loan_id": loan_id,
            "payment_amount": payment_amount,
            "new_loan_balance": loan['current_balance'],
            "new_account_balance": account['balance'],
            "transaction_id": transaction['transaction_id']
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ProcessLoanPayment",
                "description": "Make a payment towards a loan",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "loan_id": {"type": "string", "description": "Loan identifier"},
                        "payment_amount": {"type": "number", "description": "Payment amount"},
                        "from_account_id": {"type": "string", "description": "Source account for payment"}
                    },
                    "required": ["loan_id", "payment_amount", "from_account_id"]
                }
            }
        }
