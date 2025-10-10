# Copyright Sierra Technologies

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAccountTransactionsTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id, limit = 10) -> str:
        transactions = list(data.get('transactions', {}).values())

        account_transactions = []
        for transaction in transactions:
            if transaction['account_id'] == account_id:
                account_transactions.append({
                    'transaction_id': transaction['transaction_id'],
                    'date': transaction['transaction_date'],
                    'amount': transaction['amount'],
                    'description': transaction['description'],
                    'status': transaction['status']
                })

        account_transactions.sort(key=lambda x: x['date'], reverse=True)
        return json.dumps(account_transactions[:limit], indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_account_transactions",
                "description": "Get recent transactions for a specific account",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account identifier"},
                        "limit": {"type": "integer", "description": "Maximum number of transactions to return", "default": 10}
                    },
                    "required": ["account_id"]
                }
            }
        }
