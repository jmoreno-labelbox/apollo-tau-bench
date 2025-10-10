# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetExpiredInventory(Tool):
    """Tool to retrieve inventory items that are expired as of today."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        today = datetime.strptime(kwargs.get('today'), "%Y-%m-%d").date()
        inventories = list(data.get("inventory", {}).values())
        list_of_inventories = kwargs.get("list_of_ids", None)
        expired = []
        for item in inventories:
            exp_date = item.get("expiration_date")
            if exp_date:
                try:
                    if datetime.strptime(exp_date, "%Y-%m-%d").date() < today:
                        expired.append(item['inventory_id'])
                except Exception:
                    continue
        if list_of_inventories:
            expired = [e for e in expired if e in list_of_inventories]
        return json.dumps(expired, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_expired_inventory",
                "description": "Retrieve inventory items that are expired.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "today": {"type": "string", "description": "Reference date"},
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of inventories to choose from."
                        }
                    },
                    "required": ["today"]
                }
            }
        }
