from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreateInventoryRecord(Tool):
    """Generates a new, blank inventory record for a product in a designated warehouse."""

    @staticmethod
    def invoke(data: dict[str, Any], sku: str = None, warehouse_id: str = None) -> str:
        if not sku or not warehouse_id:
            payload = {"error": "SKU and warehouse_id are required."}
            out = json.dumps(payload)
            return out

        inventory_items = data.get("inventory", [])
        for item in inventory_items:
            if item.get("sku") == sku and item.get("warehouse_id") == warehouse_id:
                payload = {
                    "error": f"Inventory record for SKU {sku} at warehouse {warehouse_id} already exists."
                }
                out = json.dumps(payload)
                return out

        product_details = {}
        products = data.get("product_master", [])
        for p in products:
            if p.get("sku") == sku:
                product_details = p
                break

        warehouse_details = {}
        warehouses = data.get("warehouses", [])
        warehouse_details = next(
            (wh for wh in warehouses if wh.get("warehouse_id") == warehouse_id), {}
        )

        if not product_details or not warehouse_details:
            payload = {
                "error": "Could not find product or warehouse details to create the record."
            }
            out = json.dumps(payload)
            return out

        max_inv_num = 0
        for item in inventory_items:
            inv_id = item.get("inventory_id", "INV-0000")
            inv_num_str = inv_id.split("-")[-1]
            if inv_num_str.isdigit():
                max_inv_num = max(max_inv_num, int(inv_num_str))
        new_inventory_id = f"INV-{max_inv_num + 1:04d}"

        new_record = {
            "inventory_id": new_inventory_id,
            "sku": sku,
            "product_name": product_details.get("product_name"),
            "product_description": product_details.get("product_description"),
            "warehouse_id": warehouse_id,
            "warehouse_name": warehouse_details.get("warehouse_name"),
            "location_in_warehouse": None,
            "quantity_on_hand": 0,
            "quantity_available": 0,
            "quantity_allocated": 0,
            "quantity_inbound": 0,
            "quantity_damaged": 0,
            "unit_cost": product_details.get("unit_price"),
            "total_value": 0.00,
            "currency": product_details.get("currency"),
            "unit_weight_kg": product_details.get("weight_kg"),
            "unit_dimensions_cm": product_details.get("dimensions_cm"),
            "lot_number": None,
            "expiration_date": None,
            "received_date": None,
            "last_counted_date": None,
            "reorder_point": 0,
            "stock_status": "Out of Stock",
            "storage_requirements": product_details.get("storage_requirements"),
        }

        inventory_items.append(new_record)
        payload = {
            "status": "success",
            "inventory_id": new_inventory_id,
            "message": "New inventory record created.",
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateInventoryRecord",
                "description": "Creates a new, empty inventory record for a given SKU at a specific warehouse. Fails if a record already exists.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product.",
                        },
                        "warehouse_id": {
                            "type": "string",
                            "description": "The ID of the warehouse to create the record in.",
                        },
                    },
                    "required": ["sku", "warehouse_id"],
                },
            },
        }
