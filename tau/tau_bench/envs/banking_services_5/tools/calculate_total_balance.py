from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone, date, timedelta
import calendar
from typing import Any, Dict
import random



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CalculateTotalBalance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, account_ids: list = None) -> str:
        if account_ids is None:
            account_ids = []
        if not customer_id or not isinstance(account_ids, list) or not account_ids:
            return json.dumps(
                {"error": "customer_id and a non-empty list of account_ids are required."},
                indent=2
            )

        customers = data.get("customers", {}).values()
        if not any(c.get("customer_id") == customer_id for c in customers.values()):
            return json.dumps({"error": "Customer not found."}, indent=2)

        accounts = data.get("accounts", {}).values()
        total = 0.0
        for acc in accounts.values():
            if acc.get("account_id") in account_ids and acc.get("customer_id") == customer_id:
                total += acc.get("balance", 0.0)

        return json.dumps({"total_balance": total}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateTotalBalance",
                "description": "Calculates the sum of balances for the specified accounts of a given customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "ID of the customer whose accounts are to be summed"
                        },
                        "account_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of account IDs to include in the total"
                        }
                    },
                    "required": ["customer_id", "account_ids"]
                }
            }
        }
