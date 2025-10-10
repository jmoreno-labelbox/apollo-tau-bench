# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListTransactionsByCustomer(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str) -> str:
        transactions = list(data.get("transactions", {}).values())
        customer_transactions = [t for t in transactions if t.get("customer_id") == customer_id]
        return json.dumps({"transactions": customer_transactions, "count": len(customer_transactions), "customer_id": customer_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_transactions_by_customer",
                "description": "List all transactions for a specific customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Unique identifier of the customer."}
                    },
                    "required": ["customer_id"]
                }
            }
        }
