# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetInventoryBySku(Tool):
    """Tool to get inventory levels for a SKU across all warehouses."""

    @staticmethod
    def invoke(data: Dict[str, Any], sku: str) -> str:
        """Execute the tool with given parameters."""
        inventory = list(data.get("inventory", {}).values())
        results = [item for item in inventory if item.get("sku") == sku]
        if not results:
            return json.dumps({"error": f"No inventory found for SKU {sku}"}, indent=2)
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "get_inventory_by_sku",
                "description": "Retrieves inventory levels for a specific product SKU across all warehouses.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product to check inventory for.",
                        }
                    },
                    "required": ["sku"],
                },
            },
        }
