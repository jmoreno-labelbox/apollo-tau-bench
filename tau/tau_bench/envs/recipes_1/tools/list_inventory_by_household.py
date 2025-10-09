from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ListInventoryByHousehold(Tool):
    """Retrieve all inventory_items for a household (can be filtered by location if desired)."""

    @staticmethod
    def invoke(data: dict[str, Any], household_id: int = None, location_enum: str = None) -> str:
        if household_id is None:
            return _json_dump({"error": "household_id is required"})
        rows = [
            i
            for i in data.get("inventory_items", {}).values()
            if int(i.get("household_id")) == int(household_id)
        ]
        if location_enum:
            rows = [
                r for r in rows if str(r.get("location_enum")) == str(location_enum)
            ]
        return _json_dump({"household_id": household_id, "inventory_items": rows})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListInventoryByHousehold",
                "description": "List inventory items for a household; optional location filter.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "location_enum": {"type": "string"},
                    },
                    "required": ["household_id"],
                },
            },
        }
