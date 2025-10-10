# Sierra copyright.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetContactByEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], email: Any) -> str:
        contacts = data.get("contacts", [])
        match = next((c for c in contacts if c.get("email") == email), None)
        return json.dumps(match or {}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_contact_by_email",
                "description": "Return a contact by exact email (includes contact_id and account_id).",
                "parameters": {
                    "type": "object",
                    "properties": {"email": {"type": "string"}},
                    "required": ["email"],
                },
            },
        }
