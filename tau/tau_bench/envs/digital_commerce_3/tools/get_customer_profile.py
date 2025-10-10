# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCustomerProfile(Tool):
    """Retrieve detailed customer profile including account and contact information."""

    @staticmethod
    def invoke(data: Dict[str, Any], email: Any = None, contact_id: Any = None) -> str:
        email = f"{email}" if email is not None else None
        contact_id = _idstr(contact_id) if contact_id is not None else None
        if not email and not contact_id:
            return _error("email or contact_id is required.")

        contacts = data.get("contacts", [])
        contact = (
            _find_one(contacts, "email", email)
            if email
            else _find_one(contacts, "contact_id", contact_id)
        )
        if not contact:
            return _error("Contact not found.")

        accounts = list(data.get("accounts", {}).values())
        account = _find_one(accounts, "account_id", contact.get("account_id"))

        return json.dumps({"contact": contact, "account": account}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_customer_profile",
                "description": "Retrieve detailed customer profile including account and contact information by email.",
                "parameters": {
                    "type": "object",
                    "properties": {"email": {"type": "string"}, "contact_id": {"type": "string"}},
                    "required": [],
                },
            },
        }
