# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCustomerPurchaseCountsBySku(Tool): # READ_DATA
    @staticmethod
    def invoke(data: Dict[str, Any], sku: str) -> str:
        transactions = data["transactions"]
        purchase_counts = {}

        for transaction in transactions:
            customer_id = transaction.get("customer_id")
            for item in transaction.get("line_items", []):
                if item["sku"] == sku:
                    if customer_id:
                        purchase_counts[customer_id] = purchase_counts.get(customer_id, 0) + item["quantity"]

        return json.dumps(purchase_counts)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_customer_purchase_counts_by_sku",
                "description": "Get a list of customer IDs and how many times they purchased a specific product SKU.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product to count purchases for."
                        }
                    },
                    "required": ["sku"]
                }
            }
        }
