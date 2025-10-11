# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchTransactionsTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id, end_date, max_amount, min_amount, start_date, transaction_type) -> str:

        transactions = list(data.get('transactions', {}).values())
        filtered_transactions = []

        for transaction in transactions:
            if transaction['account_id'] != account_id:
                continue

            if start_date and transaction['transaction_date'] < start_date:
                continue
            if end_date and transaction['transaction_date'] > end_date:
                continue
            if min_amount is not None and abs(transaction['amount']) < min_amount:
                continue
            if max_amount is not None and abs(transaction['amount']) > max_amount:
                continue
            if transaction_type and transaction['transaction_type'] != transaction_type:
                continue

            filtered_transactions.append({
                'transaction_id': transaction['transaction_id'],
                'date': transaction['transaction_date'],
                'amount': transaction['amount'],
                'type': transaction['transaction_type'],
                'description': transaction['description'],
                'merchant': transaction.get('merchant_name', 'N/A')
            })

        return json.dumps(filtered_transactions, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_transactions",
                "description": "Search transactions with filters",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account identifier"},
                        "start_date": {"type": "string", "description": "Start date (ISO format)"},
                        "end_date": {"type": "string", "description": "End date (ISO format)"},
                        "min_amount": {"type": "number", "description": "Minimum transaction amount"},
                        "max_amount": {"type": "number", "description": "Maximum transaction amount"},
                        "transaction_type": {"type": "string", "description": "Transaction type filter"}
                    },
                    "required": ["account_id"]
                }
            }
        }
