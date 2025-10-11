# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RemoveAccountGroups(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str, group_ids: List[str], actor: str, timestamp: str) -> str:
        acct = _find_one(data["directory_accounts"], account_id=account_id)
        if not acct:
            return json.dumps({"status": "error", "reason": "account_not_found"})
        current = set(acct.get("group_ids", []))
        for gid in group_ids:
            if gid in current:
                current.remove(gid)
                _append_row(
                    data["group_membership_audit"],
                    {
                        "audit_id": f"gma_{account_id}_{gid}_remove",
                        "account_id": account_id,
                        "group_id": gid,
                        "action": "remove",
                        "actor": actor,
                        "timestamp": timestamp,
                    },
                )
        acct["group_ids"] = sorted(current)
        return json.dumps({"status": "ok", "account": acct})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_account_groups",
                "description": "Remove groups from an account and append audit entries.",
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
