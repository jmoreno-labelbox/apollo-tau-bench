from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetInventoryAnalytics(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], store_id: str | None = None) -> str:
        inventory = data.get("inventory", [])
        products = data.get("products", [])

        if store_id:
            inventory = [inv for inv in inventory if inv.get("store_id") == store_id]

        total_items = len(inventory)
        total_quantity = sum(inv.get("quantity", 0) for inv in inventory)
        total_value = 0.0

        for inv_record in inventory:
            product = next(
                (p for p in products if p.get("sku") == inv_record.get("sku")), None
            )
            if product:
                total_value += inv_record.get("quantity", 0) * product.get("price", 0)

        low_stock_items = len(
            [inv for inv in inventory if inv.get("quantity", 0) <= 10]
        )

        analytics = {
            "store_id": store_id,
            "total_items": total_items,
            "total_quantity": total_quantity,
            "total_value": round(total_value, 2),
            "low_stock_items": low_stock_items,
            "average_quantity": (
                round(total_quantity / total_items, 2) if total_items > 0 else 0
            ),
        }
        payload = analytics
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getInventoryAnalytics",
                "description": "Get inventory analytics for a store or all stores.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {
                            "type": "string",
                            "description": "Optional: Store ID to filter analytics.",
                        }
                    },
                    "required": [],
                },
            },
        }
