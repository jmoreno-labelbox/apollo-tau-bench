from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone, date, timedelta
import calendar
from typing import Any, Dict
import random

class BlockAccountForCustomerId(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, account_id: str = None) -> str:
        if not customer_id or not account_id:
            return json.dumps(
                {"error": "Both customer_id and account_id are required."},
                indent=2
            )

        # Find the account and verify ownership
        accounts = data.get("accounts", [])
        account = next((a for a in accounts
                        if a["account_id"] == account_id
                        and a["customer_id"] == customer_id), None)
        if not account:
            return json.dumps(
                {"error": "Account not found or does not belong to the customer."},
                indent=2
            )

        # Block it
        account["status"] = "Blocked"
        return json.dumps(account, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "BlockAccountForCustomerId",
                "description": "Sets the status of a given customer’s account to 'Blocked'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "ID of the customer who owns the account"
                        },
                        "account_id": {
                            "type": "string",
                            "description": "ID of the account to block"
                        }
                    },
                    "required": ["customer_id", "account_id"]
                }
            }
        }
