from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateTransactionStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], transaction_id: str, new_status: str) -> str:
        transactions = data.get("transactions", {}).values()
        valid_statuses = ["pending", "completed", "cancelled", "refunded"]

        if new_status not in valid_statuses:
            payload = {
                "error": f"Invalid status. Valid statuses are: {', '.join(valid_statuses)}"
            }
            out = json.dumps(payload)
            return out

        for i, transaction in enumerate(transactions):
            if transaction.get("transaction_id") == transaction_id:
                transactions[i]["status"] = new_status
                data["transactions"] = transactions
                payload = transactions[i]
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
                "name": "UpdateTransactionStatus",
                "description": "Update the status of an existing transaction.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "transaction_id": {
                            "type": "string",
                            "description": "Unique identifier of the transaction.",
                        },
                        "new_status": {"type": "string", "description": "New status."},
                    },
                    "required": ["transaction_id", "new_status"],
                },
            },
        }
