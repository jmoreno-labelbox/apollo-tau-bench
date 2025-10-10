# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetWarehousesByOwnershipStatus(Tool):
    """Tool to retrieve a warehouses by ownership status."""

    @staticmethod
    def invoke(data: Dict[str, Any], ownership_status, list_of_ids = []) -> str:
        warehouses = list(data.get("warehouses", {}).values())
        result = []
        for warehouse in warehouses:
            if warehouse["ownership_status"].lower() == ownership_status.lower():
                result.append(warehouse["warehouse_id"])
        if list_of_ids:
            result = [r for r in result if r in list_of_ids]
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_warehouses_by_ownership_status",
                "description": "Retrieve full warehouse details using warehouse ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ownership_status": {"type": "string", "description": "Owned, Leased"},
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of suppliers to choose from."
                        }
                    },
                    "required": ["ownership_status"]
                }
            }
        }
