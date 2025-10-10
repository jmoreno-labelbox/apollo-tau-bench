# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateAccount(Tool):
    """
    Create a new account and primary contact, setting the account's default pricebook_id.
    - If a contact with the given email already exists, return its account/contact ids (no new records).
    - Otherwise, generate the next sequential string ids for both account and contact.
    - Default pricebook_id is "1" (Retail) unless explicitly provided.
    Return shape: {"account_id": "...", "contact_id": "...", "pricebook_id": "..."}
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_account",
                "description": "Create a new account + primary contact and set the account's default pricebook_id (defaults to '1').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email": {
                            "type": "string",
                            "description": "Primary contact email (unique).",
                        },
                        "first_name": {"type": "string", "description": "Primary first name."},
                        "last_name": {"type": "string", "description": "Primary last name."},
                        "pricebook_id": {
                            "type": "string",
                            "description": "Default pricebook for the new account. Defaults to '1' (Retail).",
                            "default": "1",
                        },
                    },
                    "required": ["email", "first_name", "last_name"],
                },
            },
        }

    @staticmethod
    def invoke(
        data: Dict[str, Any], email: str, first_name: str, last_name: str, pricebook_id: str = "1"
    ) -> dict:
        contacts = data.setdefault("contacts", [])
        accounts = data.setdefault("accounts", [])

        account = {
            "account_id": "114",
            "account_name": f"{first_name} {last_name}",
            "default_pricebook_id": "1",
            "type": "B2C Customer",
            "billing_street": "789 Home St",
            "shipping_street": "789 Home St",
        }
        contact = {
            "contact_id": "216",
            "account_id": "114",
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": "111-222-3333",
        }
        accounts.append(account)
        contacts.append(contact)

        return {"account": account, "contact": contact, "pricebook_id": pricebook_id}
