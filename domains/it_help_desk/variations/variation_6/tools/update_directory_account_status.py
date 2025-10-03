from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateDirectoryAccountStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        account_id: str,
        status: str,
        disabled_at: str | None = None,
    ) -> str:
        pass
        acct = _find_one(data["directory_accounts"], account_id=account_id)
        if not acct:
            payload = {"status": "error", "reason": "account_not_found"}
            out = json.dumps(payload)
            return out
        if status not in {"enabled", "disabled"}:
            payload = {"status": "error", "reason": "invalid_status"}
            out = json.dumps(payload)
            return out
        acct["status"] = status
        acct["disabled_at"] = disabled_at
        payload = {"status": "ok", "account": acct}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateDirectoryAccountStatus",
                "description": "Set a directory account status to 'enabled' or 'disabled'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string"},
                        "status": {"type": "string"},
                        "disabled_at": {"type": "string"},
                    },
                    "required": ["account_id", "status"],
                },
            },
        }
