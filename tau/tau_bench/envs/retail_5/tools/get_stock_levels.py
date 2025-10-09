from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class GetStockLevels(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str = None, item_id: str = None, low_stock_threshold: int = 50) -> str:
        suppliers = data["suppliers"]

        if supplier_id:
            supplier = next(
                (s for s in suppliers.values() if s["supplier_id"] == supplier_id), None
            )
            if not supplier:
                payload = {"error": "Supplier not found"}
                out = json.dumps(payload)
                return out

            if item_id:
                stock_level = supplier["item_stock"].get(item_id, "not_found")
                payload = {
                        "supplier_id": supplier_id,
                        "item_id": item_id,
                        "stock_level": stock_level,
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out

            low_stock_items = []
            for item, stock in supplier["item_stock"].items():
                if (isinstance(stock, int) and stock < low_stock_threshold) or (
                    isinstance(stock, str) and stock == "out_of_stock"
                ):
                    low_stock_items.append({"item_id": item, "stock_level": stock})
            payload = {
                    "supplier_id": supplier_id,
                    "low_stock_items": low_stock_items,
                    "threshold": low_stock_threshold,
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #Retrieve low stock information from all suppliers
        all_low_stock = []
        for supplier in suppliers.values():
            for item, stock in supplier["item_stock"].items():
                if (isinstance(stock, int) and stock < low_stock_threshold) or (
                    isinstance(stock, str) and stock == "out_of_stock"
                ):
                    all_low_stock.append(
                        {
                            "supplier_id": supplier["supplier_id"],
                            "supplier_name": supplier["name"],
                            "item_id": item,
                            "stock_level": stock,
                        }
                    )
        payload = all_low_stock
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getStockLevels",
                "description": "Get stock levels for items, with options to filter by supplier or check low stock items.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Supplier ID to check stock for",
                        },
                        "item_id": {
                            "type": "string",
                            "description": "Specific item ID to check stock for",
                        },
                        "low_stock_threshold": {
                            "type": "integer",
                            "description": "Threshold below which items are considered low stock",
                            "default": 50,
                        },
                    },
                },
            },
        }
