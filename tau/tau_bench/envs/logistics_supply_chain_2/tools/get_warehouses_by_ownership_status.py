from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetWarehousesByOwnershipStatus(Tool):
    """Utility for fetching warehouses based on their ownership status."""

    @staticmethod
    def invoke(data: dict[str, Any], ownership_status: str, list_of_ids: list = None) -> str:
        if list_of_ids is None:
            list_of_ids = []
        warehouses = data.get("warehouses", [])
        result = []
        for warehouse in warehouses:
            if warehouse["ownership_status"].lower() == ownership_status.lower():
                result.append(warehouse["warehouse_id"])
        if list_of_ids:
            result = [r for r in result if r in list_of_ids]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetWarehousesByOwnershipStatus",
                "description": "Retrieve full warehouse details using warehouse ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ownership_status": {
                            "type": "string",
                            "description": "Owned, Leased",
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of suppliers to choose from.",
                        },
                    },
                    "required": ["ownership_status"],
                },
            },
        }
