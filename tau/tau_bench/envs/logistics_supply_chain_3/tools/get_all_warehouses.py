# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAllWarehouses(Tool):
    """Retrieves all warehouse records from the dataset, with an option to filter."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        warehouses = data.get("warehouses", [])
        filters = kwargs.get("filters")

        if not warehouses:
            return json.dumps({"message": "No warehouses found."})

        if not filters:
            return json.dumps(warehouses)

        filtered_warehouses = []
        for warehouse in warehouses:
            match = True
            for key, value in filters.items():
                warehouse_value = warehouse.get(key)

                # If the warehouse field is a list (e.g., certifications, special_capabilities)
                # This checks if the required value is present in the list.
                if isinstance(warehouse_value, list):
                    if value not in warehouse_value:
                        match = False
                        break
                # Handle case-insensitivity for string comparisons
                elif isinstance(warehouse_value, str) and isinstance(value, str):
                    if warehouse_value.lower() != value.lower():
                        match = False
                        break
                # Direct comparison for other types
                elif warehouse_value != value:
                    match = False
                    break
            if match:
                filtered_warehouses.append(warehouse)

        if filtered_warehouses:
            return json.dumps(filtered_warehouses)
        else:
            return json.dumps(
                {"message": "No warehouses found matching the specified filters."}
            )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_all_warehouses",
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
