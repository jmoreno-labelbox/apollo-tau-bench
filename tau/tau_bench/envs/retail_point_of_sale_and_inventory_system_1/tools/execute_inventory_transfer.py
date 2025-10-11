# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ExecuteInventoryTransfer(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], from_store_id, quantity, sku, to_store_id) -> str:

        inventory = list(data.get("inventory", {}).values())  # Ajustado para lista
        from_item = None
        to_item = None

        for item in inventory:
            if item['store_id'] == from_store_id and item['sku'] == sku:
                from_item = item
            if item['store_id'] == to_store_id and item['sku'] == sku:
                to_item = item

        if from_item and to_item:
            from_item['quantity'] -= quantity
            to_item['quantity'] += quantity
            return json.dumps({
                "status": "success",
                "sku": sku,
                "quantity": quantity,
                "from_store": from_store_id,
                "to_store": to_store_id
            })

        return json.dumps({"status": "failed", "reason": "Inventory item not found in one or both stores."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "execute_inventory_transfer",
                "description": "Executes a stock transfer of a specific SKU from one store to another.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {"type": "string", "description": "The SKU of the product to transfer."},
                        "quantity": {"type": "integer", "description": "The quantity of stock to transfer."},
                        "from_store_id": {"type": "string", "description": "The ID of the origin store."},
                        "to_store_id": {"type": "string", "description": "The ID of the destination store."},
                    },
                    "required": ["sku", "quantity", "from_store_id", "to_store_id"],
                },
            },
        }
