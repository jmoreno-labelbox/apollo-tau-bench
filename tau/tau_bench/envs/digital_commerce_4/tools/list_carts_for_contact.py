# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListCartsForContact(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], contact_id: Any) -> str:
        if not contact_id:
            return json.dumps({"error": "contact_id is required."}, indent=2)
        contact_id = _as_id(contact_id)
        carts = [c for c in data.get("carts", []) if _as_id(c.get("contact_id")) == contact_id]

        def _idnum(s):
            try:
                return int(str(s))
            except Exception:
                return 10**9

        carts.sort(
            key=lambda c: (str(c.get("last_updated_at", "")), -_idnum(c.get("cart_id"))),
            reverse=True,
        )
        return json.dumps({"contact_id": contact_id, "carts": carts}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_carts_for_contact",
                "description": "List carts for a contact, newest first.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "contact_id": {"type": "string", "description": "Target contact_id."}
                    },
                    "required": ["contact_id"],
                },
            },
        }
