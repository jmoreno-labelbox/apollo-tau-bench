# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCustomersAboveXSpend(Tool): # READ
    @staticmethod
    def invoke(data: Dict[str, Any], amount: float) -> str:
        transactions = list(data.get("transactions", {}).values())
        spend_by_customer = {}
        for txn in transactions:
            customer_id = txn.get("customer_id")
            total_amount = txn.get("total_amount", 0.0)
            if customer_id:
                spend_by_customer[customer_id] = spend_by_customer.get(customer_id, 0.0) + total_amount
        result = [cid for cid, spend in spend_by_customer.items() if spend > amount]
        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_customers_above_x_spend",
                "description": "Return a list of customer IDs who have spent more than the specified amount across all transactions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "amount": {
                            "type": "integer",
                            "description": "The minimum total spend threshold."
                        }
                    },
                    "required": ["amount"]
                }
            }
        }
