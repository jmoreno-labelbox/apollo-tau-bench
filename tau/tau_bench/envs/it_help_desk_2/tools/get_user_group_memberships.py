# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserGroupMemberships(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        account_id = kwargs.get("account_id")
        account = next((a for a in data.get("directory_accounts", []) if a.get("account_id") == account_id), None)
        if account and "group_ids" in account:
            return json.dumps({"account_id": account_id, "group_ids": account["group_ids"]}, indent=2)
        return json.dumps({"account_id": account_id, "group_ids": []}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_user_group_memberships", "description": "Takes a snapshot of a user's current access groups for auditing.", "parameters": {"type": "object", "properties": {"account_id": {"type": "string"}}, "required": ["account_id"]}}}
