from tau_bench.envs.tool import Tool
import json
from datetime import date, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ListInventoryByHousehold(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], household_id: str = None) -> str:
        if household_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
        rows = [
            i
            for i in data.get("inventory_items", [])
            if i.get("household_id") == household_id
        ]
        return _json_dump({"household_id": household_id, "inventory_items": rows})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListInventoryByHousehold",
                "description": "Get inventory items for a household; defaults to primary household.",
                "parameters": {
                    "type": "object",
                    "properties": {"household_id": {"type": "integer"}},
                    "required": [],
                },
            },
        }
