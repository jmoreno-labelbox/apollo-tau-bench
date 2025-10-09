from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal

class UpdateStreetAddress(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        account_id: Any,
        new_shipping_street: Any,
        new_billing_street: Any = None,
    ) -> str:
        account_id = _idstr(account_id)
        new_shipping_street = new_shipping_street
        new_billing_street = new_billing_street
        if not account_id or not new_shipping_street:
            payload = {
                "error": "Missing required field: account_id and/or new_shipping_street"
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        accounts = data.get("accounts", [])
        for account in accounts:
            if account.get("account_id") == account_id:
                account["shipping_street"] = new_shipping_street
                if new_billing_street:
                    account["billing_street"] = new_billing_street
                payload = account
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No account found with ID {account_id}"}
        out = json.dumps(payload, indent=2)
        return out


    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateStreetAddress",
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
