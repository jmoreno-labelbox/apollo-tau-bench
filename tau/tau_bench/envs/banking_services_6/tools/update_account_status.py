# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAccountStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        account_id = kwargs.get("account_id")
        new_status = kwargs.get("new_status")

        account = next((acc for acc in data["accounts"] if acc["account_id"] == account_id), None)
        if not account:
            return json.dumps({"error": "Account not found."})

        if new_status.lower() == "closed" and account["balance"] < 0:
            return json.dumps({"error": "Account has a negative balance and cannot be closed."})

        account["status"] = new_status
        return json.dumps(account)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "update_account_status",
                        "description": "Updates the status of an account (e.g., Active, Frozen, Closed).",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "account_id": {"type": "string", "description": "The unique identifier for the account."},
                                        "new_status": {"type": "string", "description": "The new status for the account."},
                                        "reason": {"type": "string", "description": "Optional reason for the status change."}
                                },
                                "required": ["account_id", "new_status"],
                        },
                },
        }
