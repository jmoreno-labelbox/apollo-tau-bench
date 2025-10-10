# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateUtilizationPercentage(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], warehouse_id: str) -> str:
        warehouses = data.get("warehouses", [])
        warehouse = next((w for w in warehouses if w.get("warehouse_id") == warehouse_id), None)

        if not warehouse:
            return json.dumps({"error": f"Warehouse {warehouse_id} not found"})

        utilization = warehouse.get("current_utilization_percentage", 85.0)

        return json.dumps({
            "warehouse_id": warehouse_id,
            "utilization_percentage": utilization,
            "status": "under_capacity" if utilization < 90 else "approaching_capacity"
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_utilization_percentage",
                "description": "Calculate current warehouse utilization percentage",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {"type": "string", "description": "Warehouse identifier"}
                    },
                    "required": ["warehouse_id"]
                }
            }
        }
