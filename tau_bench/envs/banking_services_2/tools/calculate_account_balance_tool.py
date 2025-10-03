from tau_bench.envs.tool import Tool
from typing import Any, Dict
import json

class CalculateAccountBalanceTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None) -> str:
        accounts = data.get('accounts', [])

        for account in accounts:
            if account['account_id'] == account_id:
                return json.dumps({
                    "account_id": account_id,
                    "current_balance": account['balance'],
                    "account_type": account['account_type'],
                    "currency": account['currency']
                }, indent=2)

        return json.dumps({"error": f"Account {account_id} not found"}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateAccountBalance",
                "description": "Get current balance for a specific account",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account identifier"}
                    },
                    "required": ["account_id"]
                }
            }
        }
