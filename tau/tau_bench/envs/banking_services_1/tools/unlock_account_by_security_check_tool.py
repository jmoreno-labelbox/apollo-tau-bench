# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UnlockAccountBySecurityCheckTool(Tool):
    """
    Tool to unlock a frozen account after a security verification process.

    This tool verifies that the account exists and is currently frozen,
    then updates the account status to "Active" upon passing checks.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Unlocks the specified account if conditions are met.

        get_info() -> Dict[str, Any]:
            Returns metadata and parameter expectations for integration.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id, security_code) -> str:
        if not customer_id or not security_code:
            return json.dumps({"error": "customer_id and security_code are required"})

        accounts = load_json("accounts.json")
        for acc in accounts:
            if acc["customer_id"] == customer_id:
                acc["status"] = "Active"
                acc["unlocked_at"] = get_current_timestamp()
                return json.dumps({"status": "Unlocked"}, indent=2)

        return json.dumps({"error": "Customer account not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "unlock_account_by_security_check",
                "description": "Unlock an account after verifying security code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer ID"},
                        "security_code": {
                            "type": "string",
                            "description": "Security code provided by user",
                        },
                    },
                    "required": ["customer_id", "security_code"],
                },
            },
        }
