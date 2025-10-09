from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ListTransactionsByCustomer(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], customer_id: str) -> str:
        transactions = data.get("transactions", {}).values()
        customer_transactions = [
            t for t in transactions.values() if t.get("customer_id") == customer_id
        ]
        payload = {
            "transactions": customer_transactions,
            "count": len(customer_transactions),
            "customer_id": customer_id,
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListTransactionsByCustomer",
                "description": "List all transactions for a specific customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique identifier of the customer.",
                        }
                    },
                    "required": ["customer_id"],
                },
            },
        }
