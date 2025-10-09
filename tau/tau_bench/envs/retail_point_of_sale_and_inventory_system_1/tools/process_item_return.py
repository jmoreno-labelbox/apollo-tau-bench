from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ProcessItemReturn(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], transaction_id: str = None, sku: str = None, quantity_returned: int = None, unit_price: float = None) -> str:
        transactions = data.get("transactions", {}).values()
        inventory = data.get("inventory", {}).values()

        for txn in transactions.values():
            if txn.get("transaction_id") == transaction_id:
                txn["status"] = "returned"
                break

        for item in inventory.values():
            if item.get("sku") == sku:
                item["quantity"] += quantity_returned
                break

        credit_amount = unit_price * quantity_returned
        payload = {"status": "success", "credit_amount": credit_amount}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ProcessItemReturn",
                "description": "Processes an item return and calculates the credit amount based on the original unit price.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "transaction_id": {
                            "type": "string",
                            "description": "The ID of the transaction for the return.",
                        },
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the item being returned.",
                        },
                        "quantity_returned": {
                            "type": "integer",
                            "description": "The quantity of the item being returned.",
                        },
                        "unit_price": {
                            "type": "number",
                            "description": "The original unit price of the item for credit calculation.",
                        },
                    },
                    "required": [
                        "transaction_id",
                        "sku",
                        "quantity_returned",
                        "unit_price",
                    ],
                },
            },
        }
