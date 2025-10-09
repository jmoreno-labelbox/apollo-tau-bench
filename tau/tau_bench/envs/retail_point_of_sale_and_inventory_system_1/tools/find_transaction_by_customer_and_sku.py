from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FindTransactionByCustomerAndSku(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], customer_id: str = None, sku: str = None) -> str:
        transactions = data.get("transactions", [])
        for txn in transactions:
            if txn.get("customer_id") == customer_id:
                for item in txn.get("line_items", []):
                    if item.get("sku") == sku:
                        payload = {
                            "transaction_id": txn.get("transaction_id"),
                            "unit_price": item.get("unit_price"),
                        }
                        out = json.dumps(payload)
                        return out
        payload = {}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindTransactionByCustomerAndSku",
                "description": "Finds a past transaction for a customer containing a specific SKU and returns its ID and the item's unit price.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "The customer's unique ID.",
                        },
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product to find.",
                        },
                    },
                    "required": ["customer_id", "sku"],
                },
            },
        }
