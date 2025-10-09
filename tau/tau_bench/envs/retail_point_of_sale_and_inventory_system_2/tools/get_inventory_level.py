from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetInventoryLevel(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sku: str) -> str:
        inventory = data.get("inventory", [])
        products = data.get("products", [])

        product = next((p for p in products if p.get("sku") == sku), None)
        if not product:
            payload = {"error": f"Product with SKU {sku} not found."}
            out = json.dumps(payload)
            return out

        inventory_records = [inv for inv in inventory if inv.get("sku") == sku]

        if not inventory_records:
            payload = {"error": f"No inventory records found for SKU {sku}"}
            out = json.dumps(payload)
            return out

        total_quantity = sum(inv.get("quantity", 0) for inv in inventory_records)
        total_reserved = sum(
            inv.get("reserved_quantity", 0) for inv in inventory_records
        )
        total_available = total_quantity - total_reserved

        inventory_info = {
            "sku": sku,
            "name": product.get("name"),
            "total_quantity": total_quantity,
            "total_reserved_quantity": total_reserved,
            "total_available_quantity": total_available,
            "inventory_records": inventory_records,
        }
        payload = inventory_info
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetInventoryLevel",
                "description": "Get current inventory level for a specific product SKU.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "Stock Keeping Unit (SKU) of the product.",
                        }
                    },
                    "required": ["sku"],
                },
            },
        }
