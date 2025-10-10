# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateCreditUtilizationTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id) -> str:
        accounts = list(data.get('accounts', {}).values())

        credit_accounts = []
        total_balance = 0
        total_limit = 0

        for account in accounts:
            if (account['customer_id'] == customer_id and
                account['account_type'] == 'Credit Card'):
                credit_limit = account.get('credit_limit', 5000)
                current_balance = abs(account['balance'])

                utilization = (current_balance / credit_limit) * 100 if credit_limit > 0 else 0

                credit_accounts.append({
                    'account_id': account['account_id'],
                    'balance': current_balance,
                    'credit_limit': credit_limit,
                    'utilization_percent': round(utilization, 2)
                })

                total_balance += current_balance
                total_limit += credit_limit

        overall_utilization = (total_balance / total_limit) * 100 if total_limit > 0 else 0

        return json.dumps({
            "customer_id": customer_id,
            "credit_accounts": credit_accounts,
            "total_balance": total_balance,
            "total_limit": total_limit,
            "overall_utilization_percent": round(overall_utilization, 2)
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_credit_utilization",
                "description": "Calculate credit utilization for all customer credit cards",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer identifier"}
                    },
                    "required": ["customer_id"]
                }
            }
        }
