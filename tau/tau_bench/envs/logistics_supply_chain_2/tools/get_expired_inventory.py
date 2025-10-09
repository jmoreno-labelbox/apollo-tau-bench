from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetExpiredInventory(Tool):
    """Utility for fetching inventory items that have expired as of the current date."""

    @staticmethod
    def invoke(data: dict[str, Any], today: str, list_of_ids: list[str] = None) -> str:
        today_date = datetime.strptime(today, "%Y-%m-%d").date()
        inventories = data.get("inventory", [])
        expired = []
        for item in inventories:
            exp_date = item.get("expiration_date")
            if exp_date:
                try:
                    if datetime.strptime(exp_date, "%Y-%m-%d").date() < today_date:
                        expired.append(item["inventory_id"])
                except Exception:
                    continue
        if list_of_ids:
            expired = [e for e in expired if e in list_of_ids]
        payload = expired
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetExpiredInventory",
                "description": "Retrieve inventory items that are expired.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "today": {"type": "string", "description": "Reference date"},
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of inventories to choose from.",
                        },
                    },
                    "required": ["today"],
                },
            },
        }
