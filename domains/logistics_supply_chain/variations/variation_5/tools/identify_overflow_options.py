from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any, Dict

class IdentifyOverflowOptions(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], warehouse_id: str, required_capacity: int) -> str:
        warehouses = data.get("warehouses", [])
        current_warehouse = next((w for w in warehouses if w["warehouse_id"] == warehouse_id), None)

        if not current_warehouse:
            return json.dumps({"error": f"Warehouse {warehouse_id} not found"})

        # Locate nearby warehouses that have available space
        overflow_options = []
        for warehouse in warehouses:
            if warehouse["warehouse_id"] != warehouse_id:
                total_capacity = warehouse["total_storage_capacity_cbm"]
                utilization = warehouse["current_utilization_percentage"]
                available = total_capacity * ((100 - utilization) / 100)

                if available >= required_capacity:
                    overflow_options.append({
                        "warehouse_id": warehouse["warehouse_id"],
                        "warehouse_name": warehouse["warehouse_name"],
                        "available_capacity": available,
                        "city": warehouse["city"]
                    })

        return json.dumps({
            "overflow_options": overflow_options[:3],  # Three best choices
            "required_capacity": required_capacity
        })
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "IdentifyOverflowOptions",
                "description": "Identify warehouse overflow options for excess capacity",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {"type": "string", "description": "Current warehouse identifier"},
                        "required_capacity": {"type": "integer", "description": "Required overflow capacity"}
                    },
                    "required": ["warehouse_id", "required_capacity"]
                }
            }
        }
