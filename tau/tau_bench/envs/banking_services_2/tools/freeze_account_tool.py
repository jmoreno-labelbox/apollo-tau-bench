# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import get_current_timestamp


class FreezeAccountTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        account_id = kwargs.get('account_id')
        reason = kwargs.get('reason', 'Customer request')
        accounts = list(data.get('accounts', {}).values())

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
                "name": "freeze_account",
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
