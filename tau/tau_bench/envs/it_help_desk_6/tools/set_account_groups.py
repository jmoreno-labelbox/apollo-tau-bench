# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetAccountGroups(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], account_id: str, group_ids: List[str], actor: str, timestamp: str
    ) -> str:
        acct = _find_one(data["directory_accounts"], account_id=account_id)
        if not acct:
            return json.dumps({"status": "error", "reason": "account_not_found"})
        old = set(acct.get("group_ids", []))
        new = set(group_ids)
        # calculate differences for auditing
        to_add = sorted(list(new - old))
        to_remove = sorted(list(old - new))
        acct["group_ids"] = sorted(group_ids)
        if not to_add and not to_remove:
            # Regardless of changes, the policy mandates that an audit entry must be generated for the action.
            _append_row(
                data["group_membership_audit"],
                {
                    "audit_id": f"gma_{account_id}_nochange_{timestamp}",
                    "account_id": account_id,
                    "group_id": None,
                    "action": "no_change",
                    "actor": actor,
                    "timestamp": timestamp,
                },
            )
        for gid in to_add:
            _append_row(
                data["group_membership_audit"],
                {
                    "audit_id": f"gma_{account_id}_{gid}_add_{timestamp}",
                    "account_id": account_id,
                    "group_id": gid,
                    "action": "add",
                    "actor": actor,
                    "timestamp": timestamp,
                },
            )
        for gid in to_remove:
            _append_row(
                data["group_membership_audit"],
                {
                    "audit_id": f"gma_{account_id}_{gid}_remove_{timestamp}",
                    "account_id": account_id,
                    "group_id": gid,
                    "action": "remove",
                    "actor": actor,
                    "timestamp": timestamp,
                },
            )
        return json.dumps({"status": "ok", "account": acct, "added": to_add, "removed": to_remove})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_account_groups",
                "description": "Replace an account's groups and write add/remove entries to group_membership_audit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string"},
                        "group_ids": {"type": "array", "items": {"type": "string"}},
                        "actor": {"type": "string"},
                        "timestamp": {"type": "string"},
                    },
                    "required": ["account_id", "group_ids", "actor", "timestamp"],
                },
            },
        }
