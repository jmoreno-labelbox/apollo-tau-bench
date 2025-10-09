from tau_bench.envs.tool import Tool
from typing import Any, Dict
import json



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetTransactionDetailsTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], transaction_id: str = None) -> str:
        transactions = data.get('transactions', [])

        for transaction in transactions:
            if transaction['transaction_id'] == transaction_id:
                return json.dumps({
                    'transaction_id': transaction['transaction_id'],
                    'account_id': transaction['account_id'],
                    'date': transaction['transaction_date'],
                    'amount': transaction['amount'],
                    'type': transaction['transaction_type'],
                    'description': transaction['description'],
                    'merchant': transaction.get('merchant_name', 'N/A'),
                    'channel': transaction['channel'],
                    'status': transaction['status']
                }, indent=2)

        return json.dumps({"error": f"Transaction {transaction_id} not found"}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTransactionDetails",
                "description": "Get detailed information about a specific transaction",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "transaction_id": {"type": "string", "description": "Transaction identifier"}
                    },
                    "required": ["transaction_id"]
                }
            }
        }
