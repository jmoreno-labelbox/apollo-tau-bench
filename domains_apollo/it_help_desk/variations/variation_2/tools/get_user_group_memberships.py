from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetUserGroupMemberships(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], account_id: str = None) -> str:
        account = next(
            (
                a
                for a in data.get("directory_accounts", [])
                if a.get("account_id") == account_id
            ),
            None,
        )
        if account and "group_ids" in account:
            payload = {"account_id": account_id, "group_ids": account["group_ids"]}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"account_id": account_id, "group_ids": []}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserGroupMemberships",
                "description": "Takes a snapshot of a user's current access groups for auditing.",
                "parameters": {
                    "type": "object",
                    "properties": {"account_id": {"type": "string"}},
                    "required": ["account_id"],
                },
            },
        }
