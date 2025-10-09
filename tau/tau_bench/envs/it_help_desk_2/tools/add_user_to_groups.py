from tau_bench.envs.tool import Tool
import json
from typing import Any

class AddUserToGroups(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], account_id: str = None, group_ids: list = None) -> str:
        audit_log = data.setdefault("group_membership_audit", [])
        added_groups = []
        for group_id in group_ids:
            audit_id = _get_next_id(audit_log, "audit_id", "gma")
            audit_log.append(
                {
                    "audit_id": audit_id,
                    "account_id": account_id,
                    "group_id": group_id,
                    "action": "add",
                    "actor": "SYSTEM",
                    "timestamp": FIXED_NOW,
                }
            )
            added_groups.append(group_id)
        payload = {
            "status": "success",
            "account_id": account_id,
            "groups_added": added_groups,
        }
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddUserToGroups",
                "description": "Add a user to a list of access groups and log the changes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string"},
                        "group_ids": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["account_id", "group_ids"],
                },
            },
        }
