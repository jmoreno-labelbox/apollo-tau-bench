# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindTransactionByCustomerAndSku(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id, sku) -> str:
        transactions = list(data.get("transactions", {}).values())  # Array []
        for txn in transactions:
            if txn.get("customer_id") == customer_id:
                for item in txn.get("line_items", []):
                    if item.get("sku") == sku:
                        return json.dumps({
                            "transaction_id": txn.get("transaction_id"),  # Assumindo que o id está presente no objeto.
                            "unit_price": item.get("unit_price")
                        })
        return json.dumps({})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_transaction_by_customer_and_sku",
                "description": "Finds a past transaction for a customer containing a specific SKU and returns its ID and the item's unit price.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "The customer's unique ID."},
                        "sku": {"type": "string", "description": "The SKU of the product to find."},
                    },
                    "required": ["customer_id", "sku"],
                },
            },
        }
