from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetInventoryBySku(Tool):
    """Utility for obtaining inventory quantities for a SKU in all warehouses."""

    @staticmethod
    def invoke(data: dict[str, Any], sku: str) -> str:
        """Run the tool using the specified parameters."""
        inventory = data.get("inventory", {}).values()
        results = [item for item in inventory.values() if item.get("sku") == sku]
        if not results:
            payload = {"error": f"No inventory found for SKU {sku}"}
            out = json.dumps(payload, indent=2)
            return out
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide the tool's specifications for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetInventoryBySku",
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
