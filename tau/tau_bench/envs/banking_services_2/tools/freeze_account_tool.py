from tau_bench.envs.tool import Tool
from typing import Any, Dict
import json

class FreezeAccountTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str, reason: str = 'Customer request') -> str:
        accounts = data.get('accounts', [])

        for account in accounts:
            if account['account_id'] == account_id:
                old_status = account['status']
                account['status'] = 'Frozen'
                account['freeze_reason'] = reason
                account['freeze_date'] = get_current_timestamp()

                return json.dumps({
                    "account_id": account_id,
                    "old_status": old_status,
                    "new_status": "Frozen",
                    "reason": reason,
                    "freeze_date": account['freeze_date']
                }, indent=2)

        return json.dumps({"error": f"Account {account_id} not found"}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FreezeAccount",
                "description": "Freeze an account to prevent transactions",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account identifier"},
                        "reason": {"type": "string", "description": "Reason for freezing"}
                    },
                    "required": ["account_id"]
                }
            }
        }
