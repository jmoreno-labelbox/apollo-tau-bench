# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddInventoryRecord(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], sku: str, store_id: str, quantity: int, location: str, reorder_level: int, safety_stock: int) -> str:
        inventory = list(data.get("inventory", {}).values())
        products = list(data.get("products", {}).values())

        # Check if product exists
        product = next((p for p in products if p.get("sku") == sku), None)
        if not product:
                return json.dumps({"error": f"Product with SKU {sku} not found."})

        # Check if inventory record already exists for this SKU and store
        existing_record = next((inv for inv in inventory if inv.get("sku") == sku and inv.get("store_id") == store_id), None)
        if existing_record:
                return json.dumps({"error": f"Inventory record for SKU {sku} in store {store_id} already exists."})

        inventory_id = _get_next_inventory_id(inventory)

        new_inventory_record = {
            "id": inventory_id,
            "sku": sku,
            "store_id": store_id,
            "quantity": quantity,
            "location": location,
            "reorder_level": reorder_level,
            "safety_stock": safety_stock,
            "reserved_quantity": 0,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        inventory.append(new_inventory_record)
                return json.dumps(new_inventory_record, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_inventory_record",
                "description": "Add a new inventory record for a product in a store.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {"type": "string", "description": "SKU of the product."},
                        "store_id": {"type": "string", "description": "Store ID where the inventory is located."},
                        "quantity": {"type": "integer", "description": "Initial quantity in stock."},
                        "location": {"type": "string", "description": "Physical location within the store."},
                        "reorder_level": {"type": "integer", "description": "Reorder level threshold."},
                        "safety_stock": {"type": "integer", "description": "Safety stock level."}
                    },
                    "required": ["sku", "store_id", "quantity", "location", "reorder_level", "safety_stock"]
                }
            }
        }
