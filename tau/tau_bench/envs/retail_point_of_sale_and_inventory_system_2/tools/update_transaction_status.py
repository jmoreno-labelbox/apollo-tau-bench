# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateTransactionStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], transaction_id: str, new_status: str) -> str:
        transactions = list(data.get("transactions", {}).values())
        valid_statuses = ["pending", "completed", "cancelled", "refunded"]

        if new_status not in valid_statuses:
            return json.dumps({"error": f"Invalid status. Valid statuses are: {', '.join(valid_statuses)}"})

        for i, transaction in enumerate(transactions):
            if transaction.get("transaction_id") == transaction_id:
                transactions[i]["status"] = new_status
                data["transactions"] = transactions
                return json.dumps(transactions[i], indent=2)
        return json.dumps({"error": f"Transaction with ID {transaction_id} not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_transaction_status",
                "description": "Update the status of an existing transaction.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "transaction_id": {"type": "string", "description": "Unique identifier of the transaction."},
                        "new_status": {"type": "string", "description": "New status."}
                    },
                    "required": ["transaction_id", "new_status"]
                }
            }
        }
