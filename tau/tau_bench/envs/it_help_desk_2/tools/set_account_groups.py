from tau_bench.envs.tool import Tool
import json
from typing import Any

class SetAccountGroups(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        account_id: str,
        group_ids: list[str],
        actor: str,
        timestamp: str
    ) -> str:
        acct = _find_one(data["directory_accounts"], account_id=account_id)
        if not acct:
            payload = {"status": "error", "reason": "account_not_found"}
            out = json.dumps(payload)
            return out
        old = set(acct.get("group_ids", []))
        new = set(group_ids)
        to_add = sorted(list(new - old))
        to_remove = sorted(list(old - new))
        acct["group_ids"] = sorted(group_ids)
        if not to_add and not to_remove:
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
        payload = {"status": "ok", "account": acct, "added": to_add, "removed": to_remove}
        out = json.dumps(payload)
        return out
        pass
        acct = _find_one(data["directory_accounts"], account_id=account_id)
        if not acct:
            payload = {"status": "error", "reason": "account_not_found"}
            out = json.dumps(payload)
            return out
        old = set(acct.get("group_ids", []))
        new = set(group_ids)
        to_add = sorted(list(new - old))
        to_remove = sorted(list(old - new))
        acct["group_ids"] = sorted(group_ids)
        if not to_add and not to_remove:
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
        payload = {"status": "ok", "account": acct, "added": to_add, "removed": to_remove}
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setAccountGroups",
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
