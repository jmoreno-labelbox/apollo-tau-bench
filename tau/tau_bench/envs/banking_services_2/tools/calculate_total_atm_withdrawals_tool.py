# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateTotalATMWithdrawalsTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id, end_date, start_date) -> str:

        transactions = list(data.get('transactions', {}).values())
        total_atm_withdrawals = 0
        withdrawal_count = 0

        for txn in transactions:
            if txn.get('account_id') != account_id:
                continue
            txn_date = txn.get('transaction_date', '')
            if start_date and txn_date < start_date:
                continue
            if end_date and txn_date > end_date:
                continue
            if txn.get('transaction_type', '').lower() == 'atm withdrawal':
                total_atm_withdrawals += abs(txn.get('amount', 0))
                withdrawal_count += 1

        return json.dumps({
            "account_id": account_id,
            "start_date": start_date,
            "end_date": end_date,
            "total_atm_withdrawals": total_atm_withdrawals,
            "atm_withdrawal_count": withdrawal_count
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_total_atm_withdrawals",
                "description": "Calculate total ATM withdrawals for an account in a given date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account identifier"},
                        "start_date": {"type": "string", "description": "Start date (ISO format)"},
                        "end_date": {"type": "string", "description": "End date (ISO format)"}
                    },
                    "required": ["account_id", "start_date", "end_date"]
                }
            }
        }
