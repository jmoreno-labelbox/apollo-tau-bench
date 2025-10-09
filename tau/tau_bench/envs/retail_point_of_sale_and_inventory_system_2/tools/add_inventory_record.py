from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class AddInventoryRecord(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        sku: str,
        store_id: str,
        quantity: int,
        location: str,
        reorder_level: int,
        safety_stock: int
    ) -> str:
        inventory = data.get("inventory", [])
        products = data.get("products", [])

        # Verify the existence of the product
        product = next((p for p in products if p.get("sku") == sku), None)
        if not product:
            payload = {"error": f"Product with SKU {sku} not found."}
            out = json.dumps(payload)
            return out

        # Determine if an inventory entry is present for this SKU and location
        existing_record = next(
            (
                inv
                for inv in inventory
                if inv.get("sku") == sku and inv.get("store_id") == store_id
            ),
            None,
        )
        if existing_record:
            payload = {
                "error": f"Inventory record for SKU {sku} in store {store_id} already exists."
            }
            out = json.dumps(payload)
            return out

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
            "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        inventory.append(new_inventory_record)
        data["inventory"] = inventory
        payload = new_inventory_record
        out = json.dumps(payload, indent=2)
        return out
        pass
        inventory = data.get("inventory", [])
        products = data.get("products", [])

        #Verify the existence of the product
        product = next((p for p in products if p.get("sku") == sku), None)
        if not product:
            payload = {"error": f"Product with SKU {sku} not found."}
            out = json.dumps(payload)
            return out

        #Determine if an inventory entry is present for this SKU and location
        existing_record = next(
            (
                inv
                for inv in inventory
                if inv.get("sku") == sku and inv.get("store_id") == store_id
            ),
            None,
        )
        if existing_record:
            payload = {
                    "error": f"Inventory record for SKU {sku} in store {store_id} already exists."
                }
            out = json.dumps(
                payload)
            return out

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
            "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        inventory.append(new_inventory_record)
        data["inventory"] = inventory
        payload = new_inventory_record
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addInventoryRecord",
                "description": "Add a new inventory record for a product in a store.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {"type": "string", "description": "SKU of the product."},
                        "store_id": {
                            "type": "string",
                            "description": "Store ID where the inventory is located.",
                        },
                        "quantity": {
                            "type": "integer",
                            "description": "Initial quantity in stock.",
                        },
                        "location": {
                            "type": "string",
                            "description": "Physical location within the store.",
                        },
                        "reorder_level": {
                            "type": "integer",
                            "description": "Reorder level threshold.",
                        },
                        "safety_stock": {
                            "type": "integer",
                            "description": "Safety stock level.",
                        },
                    },
                    "required": [
                        "sku",
                        "store_id",
                        "quantity",
                        "location",
                        "reorder_level",
                        "safety_stock",
                    ],
                },
            },
        }
