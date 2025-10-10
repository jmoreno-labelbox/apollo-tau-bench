# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AnalyzeInventoryByCategory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], warehouse_id: str) -> str:
        inventory = list(data.get("inventory", {}).values())
        product_master = data.get("product_master", [])

        warehouse_inventory = [item for item in inventory if item.get("warehouse_id") == warehouse_id]

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
                "name": "analyze_inventory_by_category",
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
