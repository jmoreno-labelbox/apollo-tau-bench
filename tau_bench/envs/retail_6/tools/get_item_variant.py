from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetItemVariant(Tool):
    """Retrieve product and variant using item_id."""

    @staticmethod
    def invoke(data, item_id: str = None) -> str:
        if not item_id:
            payload = {"error": "item_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        prod, variant = _find_product_by_item(data, item_id)
        if not prod:
            payload = {"error": f"item_id {item_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"product_id": prod["product_id"], "variant": variant}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "getItemVariant",
                "description": "Return the variant record and product_id for a given item_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"item_id": {"type": "string"}},
                    "required": ["item_id"],
                },
            },
        }
