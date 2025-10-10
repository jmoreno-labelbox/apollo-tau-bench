# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateWarehouse(Tool):
    """Tool to update warehouse details."""

    @staticmethod
    def invoke(data: Dict[str, Any], updates, warehouse_id) -> str:
        warehouses = list(data.get("warehouses", {}).values())

        for warehouse in warehouses:
            if warehouse["warehouse_id"] == warehouse_id:
                warehouse.update(updates)
                return json.dumps({"success": f"warehouse {warehouse_id} updated"}, indent=2)
        return json.dumps({"error": f"warehouse_id {warehouse_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_warehouse",
                "description": "Update warehouse by ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {"type": "string", "description": "The warehouse ID to update"},
                        "updates": {"type": "object", "description": "Fields and values to update"}
                    },
                    "required": ["warehouse_id", "updates"]
                }
            }
        }
