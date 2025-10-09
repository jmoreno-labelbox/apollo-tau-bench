from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any, Dict



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetWarehouseCapacity(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], warehouse_id: str, total_storage_capacity_cbm: float = 0, current_utilization_percentage: float = 0) -> str:
        warehouses = data.get("warehouses", {}).values()
        warehouse = next((w for w in warehouses.values() if w.get("warehouse_id") == warehouse_id), None)

        if not warehouse:
            return json.dumps({"error": f"Warehouse {warehouse_id} not found"})

        total_capacity = warehouse.get("total_storage_capacity_cbm", total_storage_capacity_cbm)
        utilization = warehouse.get("current_utilization_percentage", current_utilization_percentage)

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
                "name": "GetWarehouseCapacity",
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
