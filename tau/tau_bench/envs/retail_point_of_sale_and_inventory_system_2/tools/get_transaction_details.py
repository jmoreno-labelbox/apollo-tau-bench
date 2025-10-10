# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTransactionDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], transaction_id: str) -> str:
        transactions = list(data.get("transactions", {}).values())
        for transaction in transactions:
            if transaction.get("transaction_id") == transaction_id:
                return json.dumps(transaction, indent=2)
        return json.dumps({"error": f"Transaction with ID {transaction_id} not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_transaction_details",
                "description": "Get detailed information about a specific transaction.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "transaction_id": {"type": "string", "description": "Unique identifier of the transaction."}
                    },
                    "required": ["transaction_id"]
                }
            }
        }
