from tau_bench.envs.tool import Tool
import json
from typing import Any

class SetVariantAvailability(Tool):
    """Adjust a variant's 'available' status."""

    @staticmethod
    def invoke(data, item_id=None, available=None) -> str:
        if item_id is None or available is None:
            payload = {"error": "item_id and available are required"}
            out = json.dumps(payload, indent=2)
            return out
        prod, variant = _find_product_by_item(data, item_id)
        if not prod:
            payload = {"error": f"item_id {item_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        prod["variants"][item_id]["available"] = bool(available)
        payload = {"success": True, "item_id": item_id, "available": bool(available)}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "setVariantAvailability",
                "description": "Set the boolean 'available' flag for a variant.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_id": {"type": "string"},
                        "available": {"type": "boolean"},
                    },
                    "required": ["item_id", "available"],
                },
            },
        }
