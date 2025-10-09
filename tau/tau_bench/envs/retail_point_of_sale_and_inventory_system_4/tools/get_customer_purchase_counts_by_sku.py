from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetCustomerPurchaseCountsBySku(Tool):  #VIEW
    @staticmethod
    def invoke(data: dict[str, Any], sku: str) -> str:
        transactions = data["transactions"]
        purchase_counts = {}

        for transaction in transactions.values():
            customer_id = transaction.get("customer_id")
            for item in transaction.get("line_items", []):
                if item["sku"] == sku:
                    if customer_id:
                        purchase_counts[customer_id] = (
                            purchase_counts.get(customer_id, 0) + item["quantity"]
                        )
        payload = purchase_counts
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCustomerPurchaseCountsBySku",
                "description": "Get a list of customer IDs and how many times they purchased a specific product SKU.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product to count purchases for.",
                        }
                    },
                    "required": ["sku"],
                },
            },
        }
