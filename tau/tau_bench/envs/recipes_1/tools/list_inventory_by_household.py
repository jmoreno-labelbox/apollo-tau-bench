# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump


class ListInventoryByHousehold(Tool):
    """Return all inventory_items for a household (optionally filtered by location)."""
    @staticmethod
    def invoke(data: Dict[str, Any], household_id, location_enum) -> str:
        if household_id is None:
            return _json_dump({"error": "household_id is required"})
        rows = [i for i in list(data.get("inventory_items", {}).values()) if int(i.get("household_id")) == int(household_id)]
        if location_enum:
            rows = [r for r in rows if str(r.get("location_enum")) == str(location_enum)]
        return _json_dump({"household_id": household_id, "inventory_items": rows})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "list_inventory_by_household",
            "description": "List inventory items for a household; optional location filter.",
            "parameters": {"type": "object", "properties": {
                "household_id": {"type": "integer"},
                "location_enum": {"type": "string"}
            }, "required": ["household_id"]}
        }}
