from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List

class UpdateAccountStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, new_status: str = None) -> str:
        account = next((acc for acc in data["accounts"].values() if acc["account_id"] == account_id), None)
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
                        "name": "UpdateAccountStatus",
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
