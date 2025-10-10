# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetContactByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], first_name: Any, last_name: Any) -> str:
        if not first_name or not last_name:
            return json.dumps({"error": "first_name and last_name are required."}, indent=2)
        fn = str(first_name).strip().lower()
        ln = str(last_name).strip().lower()
        contacts = data.get("contacts", [])
        matches = [
            c
            for c in contacts
            if str(c.get("first_name", "")).strip().lower() == fn
            and str(c.get("last_name", "")).strip().lower() == ln
        ]
        if not matches:
            return json.dumps({}, indent=2)

        # deterministic: the smallest numeric contact_id is preferred in case of ties.
        def _key(c):
            s = str(c.get("contact_id", ""))
            try:
                return int(s)
            except Exception:
                return float("inf")

        return json.dumps(sorted(matches, key=_key)[0], indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_contact_by_name",
                "description": "Return a contact by exact first and last name (includes contact_id and account_id).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {
                            "type": "string",
                            "description": "Exact first name from contacts.",
                        },
                        "last_name": {
                            "type": "string",
                            "description": "Exact last name from contacts.",
                        },
                    },
                    "required": ["first_name", "last_name"],
                },
            },
        }
