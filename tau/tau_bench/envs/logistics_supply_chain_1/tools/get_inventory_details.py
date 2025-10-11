# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetInventoryDetails(Tool):
    """Retrieves a single inventory record for a SKU at a specific warehouse."""
    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        sku, warehouse_id = map(kwargs.get, ["sku", "warehouse_id"])
        if not all([sku, warehouse_id]):
            return json.dumps({"error": "sku and warehouse_id are required."}, indent=2)
        inventory_record = next((i for i in list(data.get('inventory', {}).values()) if i.get('sku') == sku and i.get('warehouse_id') == warehouse_id), None)
        if not inventory_record:
            return json.dumps({"error": f"Inventory for SKU '{sku}' not found at warehouse '{warehouse_id}'."}, indent=2)
        return json.dumps(inventory_record, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_inventory_details", "description": "Retrieves a single inventory record for a SKU at a specific warehouse.", "parameters": {"type": "object", "properties": {"sku": {"type": "string"}, "warehouse_id": {"type": "string"}}, "required": ["sku", "warehouse_id"]}}}
