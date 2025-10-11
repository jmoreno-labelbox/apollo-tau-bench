# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListOrdersForContact(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], contact_id: str) -> str:
        if not contact_id:
            return json.dumps({"error": "contact_id is required."}, indent=2)
        contact_id = _as_id(contact_id)
        rows = [o for o in list(data.get("orders", {}).values()) if _as_id(o.get("contact_id")) == contact_id]
        rows = sorted(rows, key=lambda o: str(o.get("order_date", "")), reverse=True)  # ISO description
        return json.dumps({"orders": rows}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_orders_for_contact",
                "description": "List orders for a contact_id, newest first.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "contact_id": {"type": "string", "description": "Target contact_id."},
                    },
                    "required": ["contact_id"],
                },
            },
        }
