# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateInventoryRecord(Tool):
    """Creates a new, empty inventory record for a product in a specific warehouse."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sku = kwargs.get("sku")
        warehouse_id = kwargs.get("warehouse_id")

        if not sku or not warehouse_id:
            return json.dumps({"error": "SKU and warehouse_id are required."})

        # Verify if the record is already present.
        inventory_items = list(data.get("inventory", {}).values())
        for item in inventory_items:
            if item.get("sku") == sku and item.get("warehouse_id") == warehouse_id:
                return json.dumps(
                    {
                        "error": f"Inventory record for SKU {sku} at warehouse {warehouse_id} already exists."
                    }
                )

        # Retrieve product and warehouse information to fill in the new entry.
        product_details = {}
        products = list(data.get("product_master", {}).values())
        for p in products:
            if p.get("sku") == sku:
                product_details = p
                break

        warehouse_details = {}
        warehouses = list(data.get("warehouses", {}).values())
        warehouse_details = next(
            (wh for wh in warehouses if wh.get("warehouse_id") == warehouse_id), {}
        )

        if not product_details or not warehouse_details:
            return json.dumps(
                {
                    "error": "Could not find product or warehouse details to create the record."
                }
            )

        # Automatically increment inventory identifier
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
            "unit_cost": product_details.get(
                "unit_price"
            ),  # Utilizing unit_price as a substitute for cost.
            "total_value": 0.00,
            "currency": product_details.get("currency"),
            "unit_weight_kg": product_details.get("weight_kg"),
            "unit_dimensions_cm": product_details.get("dimensions_cm"),
            "lot_number": None,
            "expiration_date": None,
            "received_date": None,
            "last_counted_date": None,
            "reorder_point": 0,  # Standard reorder threshold
            "stock_status": "Out of Stock",
            "storage_requirements": product_details.get("storage_requirements"),
        }

        inventory_items.append(new_record)

        return json.dumps(
            {
                "status": "success",
                "inventory_id": new_inventory_id,
                "message": "New inventory record created.",
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_inventory_record",
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
