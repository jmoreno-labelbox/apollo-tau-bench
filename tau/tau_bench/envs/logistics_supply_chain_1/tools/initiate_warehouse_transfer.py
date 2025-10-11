# Copyright Sierra

import random
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class InitiateWarehouseTransfer(Tool):
    """Creates a stock transfer between two warehouses, adjusting inventory levels."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sku, quantity, from_warehouse_id, to_warehouse_id = map(kwargs.get, ["sku", "quantity", "from_warehouse_id", "to_warehouse_id"])
        if not all([sku, quantity, from_warehouse_id, to_warehouse_id]):
            return json.dumps({"error": "sku, quantity, from_warehouse_id, and to_warehouse_id are required."}, indent=2)
        inventory = list(data.get('inventory', {}).values())
        source_inv = next((i for i in inventory if i.get('sku') == sku and i.get('warehouse_id') == from_warehouse_id), None)
        dest_inv = next((i for i in inventory if i.get('sku') == sku and i.get('warehouse_id') == to_warehouse_id), None)
        if not source_inv:
            return json.dumps({"error": f"SKU {sku} not found in source warehouse {from_warehouse_id}."}, indent=2)
        if source_inv['quantity_available'] < quantity:
            return json.dumps({"error": f"Insufficient available stock in {from_warehouse_id}."}, indent=2)
        source_inv['quantity_available'] -= quantity
        source_inv['quantity_allocated'] += quantity
        if dest_inv:
            dest_inv['quantity_inbound'] += quantity
        else:
            product_details = next((p for p in data.get('product_master', []) if p.get('sku') == sku), {})
            new_inv_record = {"inventory_id": f"INV-{random.randint(10000, 99999)}", "sku": sku, "product_name": product_details.get("product_name"), "warehouse_id": to_warehouse_id, "quantity_on_hand": 0, "quantity_available": 0, "quantity_allocated": 0, "quantity_inbound": quantity, "quantity_damaged": 0}
            inventory.append(new_inv_record)
        return json.dumps({"status": "success", "transfer_id": f"T-{from_warehouse_id}-{to_warehouse_id}-{random.randint(1000, 9999)}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "initiate_warehouse_transfer", "description": "Initiates a stock transfer of a specific SKU from a source warehouse to a destination warehouse.", "parameters": {"type": "object", "properties": {"sku": {"type": "string"}, "quantity": {"type": "integer"}, "from_warehouse_id": {"type": "string"}, "to_warehouse_id": {"type": "string"}}, "required": ["sku", "quantity", "from_warehouse_id", "to_warehouse_id"]}}}
