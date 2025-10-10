# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GenerateAccountStatementTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        account_id = kwargs.get('account_id')
        start_date = kwargs.get('start_date')
        end_date = kwargs.get('end_date')

        accounts = list(data.get('accounts', {}).values())
        transactions = list(data.get('transactions', {}).values())

        account = None
        for a in accounts:
            if a['account_id'] == account_id:
                account = a
                break

        if not account:
            return json.dumps({"error": f"Account {account_id} not found"}, indent=2)

        statement_transactions = []
        total_credits = 0
        total_debits = 0

        for transaction in transactions:
            if (transaction['account_id'] == account_id and
                start_date <= transaction['transaction_date'] <= end_date):

                statement_transactions.append({
                    'date': transaction['transaction_date'],
                    'description': transaction['description'],
                    'amount': transaction['amount'],
                    'type': transaction['transaction_type']
                })

                if transaction['amount'] > 0:
                    total_credits += transaction['amount']
                else:
                    total_debits += abs(transaction['amount'])

        return json.dumps({
            "account_id": account_id,
            "account_type": account['account_type'],
            "statement_period": f"{start_date} to {end_date}",
            "opening_balance": account['balance'] + total_debits - total_credits,
            "closing_balance": account['balance'],
            "total_credits": total_credits,
            "total_debits": total_debits,
            "transaction_count": len(statement_transactions),
            "transactions": statement_transactions
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_account_statement",
                "description": "Generate account statement for a date range",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account identifier"},
                        "start_date": {"type": "string", "description": "Statement start date (ISO format)"},
                        "end_date": {"type": "string", "description": "Statement end date (ISO format)"}
                    },
                    "required": ["account_id", "start_date", "end_date"]
                }
            }
        }
