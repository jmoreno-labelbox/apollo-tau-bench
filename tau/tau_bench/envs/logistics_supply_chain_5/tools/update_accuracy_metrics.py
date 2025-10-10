# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAccuracyMetrics(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], warehouse_id: str) -> str:
        warehouses = data.get("warehouses", [])
        inventory = list(data.get("inventory", {}).values())
        cycle_counts = data.get("cycle_counts", [])

        warehouse = next((w for w in warehouses if w.get("warehouse_id") == warehouse_id), None)
        if not warehouse:
            return json.dumps({"error": f"Warehouse {warehouse_id} not found"})

        # Calculate accuracy metrics
        warehouse_inventory = [item for item in inventory if item.get("warehouse_id") == warehouse_id]
        warehouse_counts = [count for count in cycle_counts if count.get("warehouse_id") == warehouse_id]

        total_items = len(warehouse_inventory)
        accurate_counts = len([count for count in warehouse_counts if abs(count.get("variance", 0)) <= count.get("system_count", 1) * 0.02])

        accuracy_percentage = (accurate_counts / max(len(warehouse_counts), 1)) * 100 if warehouse_counts else 99.5

        metrics = {
            "warehouse_id": warehouse_id,
            "inventory_accuracy_percentage": round(accuracy_percentage, 2),
            "total_items_counted": len(warehouse_counts),
            "accurate_counts": accurate_counts,
            "last_updated": get_current_timestamp()
        }

        return json.dumps(metrics)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_accuracy_metrics",
                "description": "Update inventory accuracy metrics for a warehouse",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {"type": "string", "description": "Warehouse identifier"}
                    },
                    "required": ["warehouse_id"]
                }
            }
        }
