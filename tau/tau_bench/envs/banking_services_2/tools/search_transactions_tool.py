from tau_bench.envs.tool import Tool
from typing import Any, Dict
import json



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SearchTransactionsTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, start_date: str = None, 
               end_date: str = None, min_amount: float = None, max_amount: float = None, description_keywords: str = None, 
               transaction_type: str = None) -> str:
        transactions = data.get('transactions', [])
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
                "name": "SearchTransactions",
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
