# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RemoveUserFromGroups(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        account_id = kwargs.get("account_id")
        group_ids = kwargs.get("group_ids")
        audit_log = data.setdefault("group_membership_audit", [])
        removed_groups = []
        for group_id in group_ids:
            audit_id = _get_next_id(audit_log, "audit_id", "gma")
            audit_log.append({"audit_id": audit_id, "account_id": account_id, "group_id": group_id, "action": "remove", "actor": "SYSTEM", "timestamp": FIXED_NOW})
            removed_groups.append(group_id)
        return json.dumps({"status": "success", "account_id": account_id, "groups_removed": removed_groups}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "remove_user_from_groups", "description": "Remove a user from a list of access groups and log the changes.", "parameters": {"type": "object", "properties": {"account_id": {"type": "string"}, "group_ids": {"type": "array", "items": {"type": "string"}}}, "required": ["account_id", "group_ids"]}}}
