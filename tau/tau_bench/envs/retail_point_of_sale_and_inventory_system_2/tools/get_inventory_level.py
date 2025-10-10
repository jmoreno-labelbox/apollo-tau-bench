# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetInventoryLevel(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], sku: str) -> str:
        inventory = list(data.get("inventory", {}).values())
        products = list(data.get("products", {}).values())

        product = next((p for p in products if p.get("sku") == sku), None)
        if not product:
            return json.dumps({"error": f"Product with SKU {sku} not found."})

        inventory_records = [inv for inv in inventory if inv.get("sku") == sku]

        if not inventory_records:
            return json.dumps({"error": f"No inventory records found for SKU {sku}"})

        total_quantity = sum(inv.get("quantity", 0) for inv in inventory_records)
        total_reserved = sum(inv.get("reserved_quantity", 0) for inv in inventory_records)
        total_available = total_quantity - total_reserved

        inventory_info = {
            "sku": sku,
            "name": product.get('name'),
            "total_quantity": total_quantity,
            "total_reserved_quantity": total_reserved,
            "total_available_quantity": total_available,
            "inventory_records": inventory_records
        }
        return json.dumps(inventory_info, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_inventory_level",
                "description": "Get current inventory level for a specific product SKU.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {"type": "string", "description": "Stock Keeping Unit (SKU) of the product."}
                    },
                    "required": ["sku"]
                }
            }
        }
