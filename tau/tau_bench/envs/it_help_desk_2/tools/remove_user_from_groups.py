# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _get_next_id(table: List[Dict[str, Any]], key: str, prefix: str) -> str:
    if not table:
        return f"{prefix}_00001"
    max_id = 0
    for item in table:
        try:
            num = int(item[key].split('_')[-1])
            if num > max_id:
                max_id = num
        except (ValueError, IndexError):
            continue
    return f"{prefix}_{max_id + 1:05d}"

class RemoveUserFromGroups(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id, group_ids) -> str:
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