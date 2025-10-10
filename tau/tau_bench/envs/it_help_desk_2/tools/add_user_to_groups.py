# Copyright Sierra Corporation

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddUserToGroups(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        account_id = kwargs.get("account_id")
        group_ids = kwargs.get("group_ids")
        audit_log = data.setdefault("group_membership_audit", [])
        added_groups = []
        for group_id in group_ids:
            audit_id = _get_next_id(audit_log, "audit_id", "gma")
            audit_log.append({"audit_id": audit_id, "account_id": account_id, "group_id": group_id, "action": "add", "actor": "SYSTEM", "timestamp": FIXED_NOW})
            added_groups.append(group_id)
        return json.dumps({"status": "success", "account_id": account_id, "groups_added": added_groups}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "add_user_to_groups", "description": "Add a user to a list of access groups and log the changes.", "parameters": {"type": "object", "properties": {"account_id": {"type": "string"}, "group_ids": {"type": "array", "items": {"type": "string"}}}, "required": ["account_id", "group_ids"]}}}
