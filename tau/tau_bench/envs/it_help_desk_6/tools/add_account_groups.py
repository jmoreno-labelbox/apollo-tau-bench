from tau_bench.envs.tool import Tool
import json
from typing import Any

class AddAccountGroups(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        account_id: str,
        group_ids: list[str],
        actor: str,
        timestamp: str,
    ) -> str:
        pass
        acct = _find_one(data["directory_accounts"], account_id=account_id)
        if not acct:
            payload = {"status": "error", "reason": "account_not_found"}
            out = json.dumps(payload)
            return out
        current = set(acct.get("group_ids", []))
        for gid in group_ids:
            if gid not in current:
                current.add(gid)
                _append_row(
                    data["group_membership_audit"],
                    {
                        "audit_id": f"gma_{account_id}_{gid}_add",
                        "account_id": account_id,
                        "group_id": gid,
                        "action": "add",
                        "actor": actor,
                        "timestamp": timestamp,
                    },
                )
        acct["group_ids"] = sorted(current)
        payload = {"status": "ok", "account": acct}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addAccountGroups",
                "description": "Add groups to an account and append audit entries.",
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
