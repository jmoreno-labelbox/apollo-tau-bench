# Copyright Sierra

import re
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateInventoryRecord(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], location, sku, store_id) -> str:

        inventory_list = list(data.get("inventory", {}).values())  # Ajustado para lista

        for item in inventory_list:
            if item.get("sku") == sku and item.get("store_id") == store_id:
                return json.dumps({"status": "exists", "inventory_id": item.get("id")})

        max_inv_id_num = 0
        for item in inventory_list:
            inv_id = item.get("id")
            if isinstance(inv_id, str):
                match = re.match(r"INV-(\d+)", inv_id)
                if match:
                    num = int(match.group(1))
                    if num > max_inv_id_num:
                        max_inv_id_num = num

        next_inv_id_num = max_inv_id_num + 1
        new_inv_id = f"INV-{next_inv_id_num:04d}"

        new_record = {
            "id": new_inv_id,
            "sku": sku,
            "store_id": store_id,
            "quantity": 0,
            "reserved_quantity": 0,
            "reorder_level": 10,
            "safety_stock": 5,
            "location": location,
            "status": "out_of_stock",
            "last_stock_count": "2025-07-28"
        }

        inventory_list.append(new_record)  # Ajustado para adicionar.
        data["inventory"] = inventory_list

        return json.dumps({"status": "created", "inventory_id": new_inv_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_inventory_record",
                "description": "Creates a new inventory record for a product at a specific store, if one does not already exist.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {"type": "string", "description": "The SKU of the product."},
                        "store_id": {"type": "string", "description": "The ID of the store."},
                        "location": {"type": "string", "description": "A placeholder location for the new inventory record."},
                    },
                    "required": ["sku", "store_id", "location"],
                },
            },
        }
