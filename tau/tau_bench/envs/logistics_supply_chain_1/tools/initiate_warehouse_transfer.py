from tau_bench.envs.tool import Tool
import json
import random
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class InitiateWarehouseTransfer(Tool):
    """Facilitates a stock transfer between two warehouses, modifying inventory levels."""

    @staticmethod
    def invoke(data: dict[str, Any], sku: str = None, quantity: int = None, from_warehouse_id: str = None, to_warehouse_id: str = None) -> str:
        if not all([sku, quantity, from_warehouse_id, to_warehouse_id]):
            payload = {
                    "error": "sku, quantity, from_warehouse_id, and to_warehouse_id are required."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        inventory = data.get("inventory", [])
        source_inv = next(
            (
                i
                for i in inventory
                if i.get("sku") == sku and i.get("warehouse_id") == from_warehouse_id
            ),
            None,
        )
        dest_inv = next(
            (
                i
                for i in inventory
                if i.get("sku") == sku and i.get("warehouse_id") == to_warehouse_id
            ),
            None,
        )
        if not source_inv:
            payload = {
                    "error": f"SKU {sku} not found in source warehouse {from_warehouse_id}."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        if source_inv["quantity_available"] < quantity:
            payload = {"error": f"Insufficient available stock in {from_warehouse_id}."}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        source_inv["quantity_available"] -= quantity
        source_inv["quantity_allocated"] += quantity
        if dest_inv:
            dest_inv["quantity_inbound"] += quantity
        else:
            product_details = next(
                (p for p in data.get("product_master", []) if p.get("sku") == sku), {}
            )
            new_inv_record = {
                "inventory_id": f"INV-{random.randint(10000, 99999)}",
                "sku": sku,
                "product_name": product_details.get("product_name"),
                "warehouse_id": to_warehouse_id,
                "quantity_on_hand": 0,
                "quantity_available": 0,
                "quantity_allocated": 0,
                "quantity_inbound": quantity,
                "quantity_damaged": 0,
            }
            inventory.append(new_inv_record)
        payload = {
                "status": "success",
                "transfer_id": f"T-{from_warehouse_id}-{to_warehouse_id}-{random.randint(1000, 9999)}",
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InitiateWarehouseTransfer",
                "description": "Initiates a stock transfer of a specific SKU from a source warehouse to a destination warehouse.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {"type": "string"},
                        "quantity": {"type": "integer"},
                        "from_warehouse_id": {"type": "string"},
                        "to_warehouse_id": {"type": "string"},
                    },
                    "required": [
                        "sku",
                        "quantity",
                        "from_warehouse_id",
                        "to_warehouse_id",
                    ],
                },
            },
        }
