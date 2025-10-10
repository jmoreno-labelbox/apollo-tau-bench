# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTransactionDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], transaction_id) -> str:
        transaction = next((t for t in list(data.get('transactions', {}).values()) if t['transaction_id'] == transaction_id), None)
        if transaction:
            return json.dumps(transaction)
        return json.dumps({"error": "Transaction not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_transaction_details",
                        "description": "Retrieves the full details of a single transaction.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "transaction_id": {"type": "string", "description": "The unique ID of the transaction."}
                                },
                                "required": ["transaction_id"]
                        }
                }
        }
