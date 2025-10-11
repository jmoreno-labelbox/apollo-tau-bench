# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateInterestEarnedTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id, days = 30) -> str:
        accounts = list(data.get('accounts', {}).values())

        for account in accounts:
            if account['account_id'] == account_id:
                if account['account_type'] != 'Savings':
                    return json.dumps({"error": "Interest calculation only available for savings accounts"}, indent=2)

                balance = account['balance']
                annual_rate = account.get('interest_rate', 0.02)
                daily_rate = annual_rate / 365

                interest_earned = balance * daily_rate * days

                return json.dumps({
                    "account_id": account_id,
                    "current_balance": balance,
                    "annual_interest_rate": annual_rate,
                    "days_calculated": days,
                    "interest_earned": round(interest_earned, 2),
                    "projected_balance": round(balance + interest_earned, 2)
                }, indent=2)

        return json.dumps({"error": f"Account {account_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_interest_earned",
                "description": "Calculate interest earned for a savings account",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Savings account identifier"},
                        "days": {"type": "integer", "description": "Number of days to calculate", "default": 30}
                    },
                    "required": ["account_id"]
                }
            }
        }
