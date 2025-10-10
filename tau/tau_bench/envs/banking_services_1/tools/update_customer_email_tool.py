# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateCustomerEmailTool(Tool):
    """
    Tool to update a customer's email and phone number.

    The tool validates the input data, updates the corresponding account(s),
    and marks the operation as successful. It simulates basic fraud checks via format control.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Updates email and phone for the given customer if found.

        get_info() -> Dict[str, Any]:
            Returns input schema and tool description for external use.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        new_email = kwargs.get("new_email")
        new_phone = kwargs.get("new_phone")

        if not customer_id or not new_email or not new_phone:
            return json.dumps(
                {
                    "status": "error",
                    "message": "Missing required parameters: 'customer_id', 'new_email', and/or 'new_phone'.",
                    "required": ["customer_id", "new_email", "new_phone"],
                },
                indent=2,
            )

        accounts = load_json("accounts.json")
        updated = False
        for acc in accounts:
            if acc["customer_id"] == customer_id:
                acc.setdefault("contact_info", {})["email_address"] = new_email
                acc["contact_info"]["phone_numbers"] = [
                    {"number": new_phone, "is_primary": True}
                ]
                updated = True

        if not updated:
            return json.dumps(
                {
                    "status": "fail",
                    "message": "Customer account not found",
                    "customer_id": customer_id,
                },
                indent=2,
            )

        return json.dumps(
            {
                "status": "success",
                "validated": True,
                "updated_fields": {
                    "email_address": new_email,
                    "primary_phone": new_phone,
                },
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_customer_email",
                "description": "Update a customer's email and phone number with format validation and fraud checks.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Customer ID to identify the account to update.",
                        },
                        "new_email": {
                            "type": "string",
                            "description": "New email address (e.g., user@example.com).",
                        },
                        "new_phone": {
                            "type": "string",
                            "description": "New phone number (e.g., +1-202-555-0183).",
                        },
                    },
                    "required": ["customer_id", "new_email", "new_phone"],
                },
            },
        }
