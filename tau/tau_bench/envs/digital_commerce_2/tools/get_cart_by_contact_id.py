from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetCartByContactId(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], contact_id: Any, carts: list = None) -> str:
        contact_id = _idstr(contact_id)
        if not contact_id:
            payload = {"error": "Missing required field: contact_id"}
            out = json.dumps(payload, indent=2)
            return out
        carts = carts or data.get("carts", {}).values()
        for cart in carts:
            if cart.get("contact_id") == contact_id:
                payload = cart
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No cart found for contact_id '{contact_id}'"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCartByContactId",
                "description": "Fetch full cart details by contact_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "contact_id": {
                            "type": "string",
                            "description": "Exact contact ID to retrieve cart for.",
                        }
                    },
                    "required": ["contact_id"],
                },
            },
        }
