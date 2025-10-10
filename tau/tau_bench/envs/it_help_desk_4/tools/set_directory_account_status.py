# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetDirectoryAccountStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        account_id = kwargs.get("account_id")
        status = kwargs.get("status")
        accounts = data.get("directory_accounts", [])
        account = next((a for a in accounts if a.get("account_id") == account_id), None)
        if not account:
            return json.dumps({"error": f"Account {account_id} not found."}, indent=2)
        if status not in ["enabled", "disabled", "inactive"]:
            return json.dumps({"error": "Status must be 'enabled', 'disabled', or 'inactive'."}, indent=2)
        account["status"] = status
        account["disabled_at"] = FIXED_NOW if status in ["disabled", "inactive"] else None
        return json.dumps(account, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "set_directory_account_status", "description": "Enable or disable a user's directory account.", "parameters": {"type": "object", "properties": {"account_id": {"type": "string"}, "status": {"type": "string"}}, "required": ["account_id", "status"]}}}
