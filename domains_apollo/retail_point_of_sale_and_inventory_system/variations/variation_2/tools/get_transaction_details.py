from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetTransactionDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], transaction_id: str) -> str:
        transactions = data.get("transactions", [])
        for transaction in transactions:
            if transaction.get("transaction_id") == transaction_id:
                payload = transaction
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Transaction with ID {transaction_id} not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTransactionDetails",
                "description": "Get detailed information about a specific transaction.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "transaction_id": {
                            "type": "string",
                            "description": "Unique identifier of the transaction.",
                        }
                    },
                    "required": ["transaction_id"],
                },
            },
        }
