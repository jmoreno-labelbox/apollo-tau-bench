# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CaV2CalculateBankTotal(Tool):
    """Calculate total balance across all bank accounts."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        bank_accounts = data.get("bank_accounts", [])

        total_balance = 0.0
        account_details = []

        # Compute solely the liquid assets (checking and savings accounts).
        liquid_account_types = ["checking", "savings"]

        for account in bank_accounts:
            account_type = account.get("account_type", "")
            balance = float(account.get("current_balance", 0.0))

            account_details.append({
                "account_id": account.get("account_id"),
                "account_type": account_type,
                "balance": balance
            })

            # Include only liquid accounts in the total.
            if account_type in liquid_account_types:
                total_balance += balance

        return json.dumps({
            "status": "success",
            "total_balance": total_balance,
            "account_count": len(bank_accounts),
            "account_details": account_details
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_calculate_bank_total",
                "description": "Calculate total balance across all bank accounts.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                },
            },
        }
