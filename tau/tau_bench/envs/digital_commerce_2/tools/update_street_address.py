# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _idstr(v):
    return str(v) if isinstance(v, int) else v

class UpdateStreetAddress(Tool):
    """Update the shipping_street of an account by its account_id."""

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        account_id: Any,
        new_shipping_street: Any,
        new_billing_street: Any = None,
    ) -> str:
        account_id = _idstr(account_id)
        new_shipping_street = new_shipping_street
        new_billing_street = new_billing_street
        if not account_id or not new_shipping_street:
            return json.dumps(
                {"error": "Missing required field: account_id and/or new_shipping_street"}, indent=2
            )
        accounts = list(data.get("accounts", {}).values())
        for account in accounts:
            if account.get("account_id") == account_id:
                account["shipping_street"] = new_shipping_street
                if new_billing_street:
                    account["billing_street"] = new_billing_street
                return json.dumps(account, indent=2)

        return json.dumps({"error": f"No account found with ID {account_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_street_address",
                "description": "Update the shipping_street of an account by its account_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {
                            "type": "string",
                            "description": "Exact account ID whose shipping_street will be updated.",
                        },
                        "new_shipping_street": {
                            "type": "string",
                            "description": "New value for shipping_street.",
                        },
                        "new_billing_street": {
                            "type": "string",
                            "description": "New value for shipping_street.",
                        },
                    },
                    "required": ["account_id", "new_shipping_street"],
                },
            },
        }