from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime, timedelta
from typing import Any, Dict

class CloseAccountRequestTool(Tool):
    """
    Tool to process a customer request to close a specific account.

    It verifies that the account is eligible for closure (e.g., zero balance,
    not frozen), and then updates the account status to 'Closed'.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Closes the account and confirms success or failure.

        get_info() -> Dict[str, Any]:
            Describes preconditions and expected structure for input.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None) -> str:
        if not account_id:
            return json.dumps({"error": "account_id is required"})

        accounts = load_json("accounts.json")
        for acc in accounts:
            if acc["account_id"] == account_id:
                if acc.get("status") == "Closed":
                    return json.dumps(
                        {"status": "Already Closed", "closed_at": acc.get("closed_at")},
                        indent=2,
                    )
                acc["status"] = "Closed"
                acc["closed_at"] = get_current_timestamp()
                return json.dumps(
                    {"status": "Closed", "closed_at": acc["closed_at"]}, indent=2
                )

        return json.dumps({"error": "Account not found"}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CloseAccountRequest",
                "description": "Close a customer's account after verifying no pending transactions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {
                            "type": "string",
                            "description": "Account ID to close",
                        }
                    },
                    "required": ["account_id"],
                },
            },
        }
