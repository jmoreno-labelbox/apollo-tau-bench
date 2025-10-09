from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetInventoryItems(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], household_id: int) -> str:
        inv = _get_table(data, "inventory_items")
        items = [x for x in inv.values() if x.get("household_id") == household_id]
        payload = {"inventory_items": items}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetInventoryItems",
                "description": "Returns inventory_items rows for a household.",
                "parameters": {
                    "type": "object",
                    "properties": {"household_id": {"type": "integer"}},
                    "required": ["household_id"],
                },
            },
        }
