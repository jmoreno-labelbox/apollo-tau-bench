from tau_bench.envs.tool import Tool
from typing import Any, Dict
import json

class GetCustomerAccountsTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        accounts = data.get('accounts', [])

        customer_accounts = []
        for account in accounts:
            if account['customer_id'] == customer_id:
                customer_accounts.append({
                    'account_id': account['account_id'],
                    'account_type': account['account_type'],
                    'balance': account['balance'],
                    'status': account['status'],
                    'last_4': account['account_number_last_4']
                })

        return json.dumps(customer_accounts, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCustomerAccounts",
                "description": "Get all accounts for a specific customer",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Unique customer identifier"}
                    },
                    "required": ["customer_id"]
                }
            }
        }
