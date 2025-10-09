from tau_bench.envs.tool import Tool
import json
from typing import Any

class CheckLowStock(Tool):  #CREATE
    @staticmethod
    def invoke(data: dict[str, Any], store_id: str, current_time: str) -> str:
        db = data.get("inventory", [])
        low_stock_skus = []
        for row in db:
            if row.get("store_id") == store_id:
                quantity = row.get("quantity", 0)
                reorder_level = row.get("reorder_level", 0)
                safety_stock = row.get("safety_stock", 0)
                if quantity <= reorder_level or row["status"] in [
                    "low_stock",
                    "critical",
                ]:
                    row["quantity"] += safety_stock
                    row["safety_stock"] = 0
                    row["updated_at"] = current_time
                    if row["status"] not in ["low_stock", "critical"]:
                        row["status"] = "low_stock"
                    low_stock_skus.append(row.get("sku"))
        payload = {"low_stock_skus": low_stock_skus}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckLowStock",
                "description": "Checks all inventory items for a given store_id. If quantity is below reorder_level, adds safety_stock to quantity, sets safety_stock to 0, and marks status as 'low_stock'. Returns a list of SKUs for items with 'low_stock' or 'critical' status for that store.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {
                            "type": "string",
                            "description": "Store ID to check inventory for.",
                        },
                        "current_time": {
                            "type": "string",
                            "description": "Timestamp for updated_at.",
                        },
                    },
                    "required": ["store_id", "current_time"],
                },
            },
        }
