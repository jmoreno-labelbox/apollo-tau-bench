# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTransactionDetailsTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        transaction_id = kwargs.get('transaction_id')
        transactions = list(data.get('transactions', {}).values())

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
                "name": "get_transaction_details",
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
