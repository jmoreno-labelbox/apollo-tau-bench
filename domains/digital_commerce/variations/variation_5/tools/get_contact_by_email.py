from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class GetContactByEmail(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], email: Any) -> str:
        contacts = data.get("contacts", [])
        match = next((c for c in contacts if c.get("email") == email), None)
        payload = match or {}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetContactByEmail",
                "description": "Return a contact by exact email (includes contact_id and account_id).",
                "parameters": {
                    "type": "object",
                    "properties": {"email": {"type": "string"}},
                    "required": ["email"],
                },
            },
        }
