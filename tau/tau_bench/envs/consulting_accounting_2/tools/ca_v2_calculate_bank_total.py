from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CaV2CalculateBankTotal(Tool):
    """Compute the overall balance across all bank accounts."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        bank_accounts = data.get("bank_accounts", [])

        total_balance = 0.0
        account_details = []

        # Compute only liquid assets (checking and savings accounts)
        liquid_account_types = ["checking", "savings"]

        for account in bank_accounts:
            account_type = account.get("account_type", "")
            balance = float(account.get("current_balance", 0.0))

            account_details.append(
                {
                    "account_id": account.get("account_id"),
                    "account_type": account_type,
                    "balance": balance,
                }
            )

            # Include only liquid accounts in total
            if account_type in liquid_account_types:
                total_balance += balance
        payload = {
            "status": "success",
            "total_balance": total_balance,
            "account_count": len(bank_accounts),
            "account_details": account_details,
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2CalculateBankTotal",
                "description": "Calculate total balance across all bank accounts.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                },
            },
        }
