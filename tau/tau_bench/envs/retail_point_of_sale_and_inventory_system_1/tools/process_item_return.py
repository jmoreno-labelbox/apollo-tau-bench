# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ProcessItemReturn(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        transaction_id = kwargs.get('transaction_id')
        sku = kwargs.get('sku')
        quantity_returned = kwargs.get('quantity_returned')
        unit_price = kwargs.get('unit_price')

        transactions = list(data.get("transactions", {}).values())  # Array []
        inventory = list(data.get("inventory", {}).values())  # Array []

        for txn in transactions:
            if txn.get("transaction_id") == transaction_id:
                txn['status'] = 'returned'
                break

        for item in inventory:
            if item.get("sku") == sku:
                item["quantity"] += quantity_returned
                break

        credit_amount = unit_price * quantity_returned
        return json.dumps({"status": "success", "credit_amount": credit_amount})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "process_item_return",
                "description": "Processes an item return and calculates the credit amount based on the original unit price.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "transaction_id": {"type": "string", "description": "The ID of the transaction for the return."},
                        "sku": {"type": "string", "description": "The SKU of the item being returned."},
                        "quantity_returned": {"type": "integer", "description": "The quantity of the item being returned."},
                        "unit_price": {"type": "number", "description": "The original unit price of the item for credit calculation."},
                    },
                    "required": ["transaction_id", "sku", "quantity_returned", "unit_price"],
                },
            },
        }
