# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetWarehouseCapacity(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], warehouse_id: str) -> str:
        warehouses = list(data.get("warehouses", {}).values())
        warehouse = next((w for w in warehouses if w.get("warehouse_id") == warehouse_id), None)

        if not warehouse:
            return json.dumps({"error": f"Warehouse {warehouse_id} not found"})

        total_capacity = warehouse.get("total_storage_capacity_cbm", 0)
        utilization = warehouse.get("current_utilization_percentage", 0)

        return json.dumps({
            "warehouse_id": warehouse_id,
            "total_capacity_cbm": total_capacity,
            "current_utilization_percentage": utilization,
            "used_capacity_cbm": total_capacity * (utilization / 100),
            "remaining_capacity_cbm": total_capacity * ((100 - utilization) / 100)
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_warehouse_capacity",
                "description": "Get warehouse capacity and utilization information",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {"type": "string", "description": "Warehouse identifier"}
                    },
                    "required": ["warehouse_id"]
                }
            }
        }
