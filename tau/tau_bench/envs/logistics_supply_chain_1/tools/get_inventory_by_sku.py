# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetInventoryBySku(Tool):
    """A tool to retrieve all inventory records for a given SKU across all warehouses."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sku = kwargs.get('sku')
        if not sku:
            return json.dumps({"error": "sku is a required argument."}, indent=2)
        inventory = list(data.get('inventory', {}).values())
        sku_inventory = [item for item in inventory if item.get('sku') == sku]
        return json.dumps(sku_inventory, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_inventory_by_sku", "description": "Retrieves all inventory records for a specific SKU across all warehouses.", "parameters": {"type": "object", "properties": {"sku": {"type": "string", "description": "The SKU to search for inventory records of."}}, "required": ["sku"]}}}
