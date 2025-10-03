from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetCustomersAboveXSpend(Tool):  #VIEW
    @staticmethod
    def invoke(data: dict[str, Any], transactions: list[dict[str, Any]] = None, amount: float = None) -> str:
        spend_by_customer = {}
        # Use transactions from data if not provided
        txn_list = transactions if transactions is not None else data.get("transactions", [])
        for txn in txn_list:
            customer_id = txn.get("customer_id")
            total_amount = txn.get("total_amount", 0.0)
            if customer_id:
                spend_by_customer[customer_id] = (
                    spend_by_customer.get(customer_id, 0.0) + total_amount
                )
        result = [cid for cid, spend in spend_by_customer.items() if spend > amount]
        payload = result
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCustomersAboveXSpend",
                "description": "Return a list of customer IDs who have spent more than the specified amount across all transactions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "amount": {
                            "type": "int",
                            "description": "The minimum total spend threshold.",
                        }
                    },
                    "required": ["amount"],
                },
            },
        }
