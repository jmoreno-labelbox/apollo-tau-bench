from tau_bench.envs.tool import Tool
import json
import random
from typing import Any

class GetInventoryDetails(Tool):
    """Obtains a single inventory record for a SKU located at a specific warehouse."""

    @staticmethod
    def invoke(data: dict[str, Any], sku: str = None, warehouse_id: str = None) -> str:
        if not all([sku, warehouse_id]):
            payload = {"error": "sku and warehouse_id are required."}
            out = json.dumps(payload, indent=2)
            return out
        inventory_record = next(
            (
                i
                for i in data.get("inventory", [])
                if i.get("sku") == sku and i.get("warehouse_id") == warehouse_id
            ),
            None,
        )
        if not inventory_record:
            payload = {
                    "error": f"Inventory for SKU '{sku}' not found at warehouse '{warehouse_id}'."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = inventory_record
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetInventoryDetails",
                "description": "Retrieves a single inventory record for a SKU at a specific warehouse.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {"type": "string"},
                        "warehouse_id": {"type": "string"},
                    },
                    "required": ["sku", "warehouse_id"],
                },
            },
        }
