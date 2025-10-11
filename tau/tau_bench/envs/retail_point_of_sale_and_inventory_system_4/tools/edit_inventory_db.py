# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _find_by_id(db, id_field, id_value):
    for i, row in enumerate(db):
        if row.get(id_field) == id_value:
            return i, row
    return None, None

class EditInventoryDb(Tool): # GENERATE
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        id: str = None,
        sku: str = None,
        store_id: str = None,
        quantity: int = None,
        reserved_quantity: int = None,
        reorder_level: int = None,
        safety_stock: int = None,
        location: str = None,
        status: str = None,
        last_stock_count: str = None,
        current_time: str = None,
        delete: bool = False
    ) -> str:
        db = list(data.get("inventory", {}).values())
        if id:
            idx, row = _find_by_id(db, "id", id)
            if row:
                if delete:
                    # --- REMOVE ---
                    del db[idx]
                    return json.dumps({"result": "deleted"})
                else:
                    # --- MODIFICATION ---
                    if sku is not None: row["sku"] = sku
                    if store_id is not None: row["store_id"] = store_id
                    if quantity is not None: row["quantity"] = quantity
                    if reserved_quantity is not None: row["reserved_quantity"] = reserved_quantity
                    if reorder_level is not None: row["reorder_level"] = reorder_level
                    if safety_stock is not None: row["safety_stock"] = safety_stock
                    if location is not None: row["location"] = location
                    if status is not None: row["status"] = status
                    if last_stock_count is not None: row["last_stock_count"] = last_stock_count
                    if current_time is not None: row["updated_at"] = current_time
                    return json.dumps({"result": row})
            else:
                return json.dumps({"error": f"Inventory {id} not found"})
        else:
            # --- INITIALIZE ---
            if sku is None or store_id is None or quantity is None or current_time is None:
                return json.dumps({"error": "Missing required field for creation (sku, store_id, quantity, current_time)"})
            new_row = {
                "id": id if id is not None else f"INV-{1000 + len(db) + 5}",
                "sku": sku,
                "store_id": store_id,
                "quantity": quantity,
                "reserved_quantity": reserved_quantity if reserved_quantity is not None else 0,
                "reorder_level": reorder_level if reorder_level is not None else 0,
                "safety_stock": safety_stock if safety_stock is not None else 0,
                "location": location if location is not None else "Unknown",
                "status": status if status is not None else "in_stock",
                "last_stock_count": last_stock_count if last_stock_count is not None else "Unknown",
                "created_at": current_time,
                "updated_at": current_time
            }
            db.append(new_row)
            return json.dumps({"result": new_row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "edit_inventory_db",
                "description": "Create, update, or delete an inventory row by id. If delete is True, deletes the row. If id is given it will edit the row with the given information. If no id is given, it will create a new row with the given info, as long as sku, store_id, quantity, location, and current_time are given.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string", "default": None, "description": "The inventory id to edit or delete. If not provided, a new id will be generated."},
                        "delete": {"type": "boolean", "default": False, "description": "Whether to delete the specified inventory record."},
                        "sku": {"type": "string", "default": None, "description": "SKU of the product."},
                        "store_id": {"type": "string", "default": None, "description": "Store ID."},
                        "quantity": {"type": "integer", "default": None, "description": "Quantity in stock."},
                        "reserved_quantity": {"type": "integer", "default": None, "description": "Reserved quantity."},
                        "reorder_level": {"type": "integer", "default": None, "description": "Reorder level."},
                        "safety_stock": {"type": "integer", "default": None, "description": "Safety stock."},
                        "location": {"type": "string", "default": None, "description": "Location in store."},
                        "status": {"type": "string", "default": None, "description": "Status of inventory."},
                        "last_stock_count": {"type": "string", "default": None, "description": "Last stock count date."},
                        "current_time": {"type": "string", "default": None, "description": "Current timestamp for created_at/updated_at."}
                    },
                    "required": []
                }
            }
        }