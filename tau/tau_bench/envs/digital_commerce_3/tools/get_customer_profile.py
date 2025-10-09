from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetCustomerProfile(Tool):
    """Obtain comprehensive customer profile with account and contact details."""

    @staticmethod
    def invoke(data: dict[str, Any], email: Any = None, contact_id: Any = None) -> str:
        email = f"{email}" if email is not None else None
        contact_id = _idstr(contact_id) if contact_id is not None else None
        if not email and not contact_id:
            return _error("email or contact_id is required.")

        contacts = data.get("contacts", {}).values()
        contact = (
            _find_one(list(contacts.values()), "email", email)
            if email
            else _find_one(list(contacts.values()), "contact_id", contact_id)
        )
        if not contact:
            return _error("Contact not found.")

        accounts = data.get("accounts", {}).values()
        account = _find_one(list(accounts.values()), "account_id", contact.get("account_id"))
        payload = {"contact": contact, "account": account}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCustomerProfile",
                "description": "Retrieve detailed customer profile including account and contact information by email.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email": {"type": "string"},
                        "contact_id": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
