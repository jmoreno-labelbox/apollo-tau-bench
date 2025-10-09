from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetAllWarehouses(Tool):
    """Fetches all warehouse records from the dataset, allowing for filtering."""

    @staticmethod
    def invoke(data: dict[str, Any], filters: dict[str, Any] = None) -> str:
        warehouses = data.get("warehouses", [])

        if not warehouses:
            payload = {"message": "No warehouses found."}
            out = json.dumps(payload)
            return out

        if not filters:
            payload = warehouses
            out = json.dumps(payload)
            return out

        filtered_warehouses = []
        for warehouse in warehouses:
            match = True
            for key, value in filters.items():
                warehouse_value = warehouse.get(key)

                if isinstance(warehouse_value, list):
                    if value not in warehouse_value:
                        match = False
                        break
                elif isinstance(warehouse_value, str) and isinstance(value, str):
                    if warehouse_value.lower() != value.lower():
                        match = False
                        break
                elif warehouse_value != value:
                    match = False
                    break
            if match:
                filtered_warehouses.append(warehouse)

        if filtered_warehouses:
            payload = filtered_warehouses
            out = json.dumps(payload)
            return out
        else:
            payload = {"message": "No warehouses found matching the specified filters."}
            out = json.dumps(payload)
            return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAllWarehouses",
                "description": "Retrieves a list of all warehouses, with an option to filter by specific criteria like warehouse_type or certifications.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filters": {
                            "type": "object",
                            "description": "Optional. A dictionary of key-value pairs to filter warehouses. Example: {'warehouse_type': 'Cold Storage', 'certifications': 'FDA Registered'}",
                        }
                    },
                    "required": [],
                },
            },
        }
