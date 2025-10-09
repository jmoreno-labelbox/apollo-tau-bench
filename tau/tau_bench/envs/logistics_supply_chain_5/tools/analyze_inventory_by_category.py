from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any, Dict



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AnalyzeInventoryByCategory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], warehouse_id: str, inventory: list = None, product_master: list = None) -> str:
        inventory = inventory if inventory is not None else data.get("inventory", {}).values()
        product_master = product_master if product_master is not None else data.get("product_master", {}).values()

        warehouse_inventory = [item for item in inventory.values() if item.get("warehouse_id") == warehouse_id]

        category_analysis = {}
        for item in warehouse_inventory:
            sku = item.get("sku")
            product = next((p for p in product_master if p.get("sku") == sku), None)
            if product:
                category = product.get("category", "Unknown")
                if category not in category_analysis:
                    category_analysis[category] = {"items": 0, "total_value": 0}
                category_analysis[category]["items"] += 1
                category_analysis[category]["total_value"] += item.get("total_value", 0)

        return json.dumps({
            "warehouse_id": warehouse_id,
            "category_breakdown": category_analysis,
            "analysis_date": get_current_timestamp()
        })
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AnalyzeInventoryByCategory",
                "description": "Analyze inventory breakdown by product category",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {"type": "string", "description": "Warehouse identifier"}
                    },
                    "required": ["warehouse_id"]
                }
            }
        }
