from tau_bench.envs.tool import Tool
import json
from typing import Any

class DisableAppAccount(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], app_account_id: str, disabled_at: str) -> str:
        pass
        row = _find_one(data["app_accounts"], app_account_id=app_account_id)
        if not row:
            payload = {"status": "error", "reason": "app_account_not_found"}
            out = json.dumps(payload)
            return out
        row["status"] = "disabled"
        row["disabled_at"] = disabled_at
        payload = {"status": "ok", "app_account": row}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DisableAppAccount",
                "description": "Disable an app account and record disabled_at.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "app_account_id": {"type": "string"},
                        "disabled_at": {"type": "string"},
                    },
                    "required": ["app_account_id", "disabled_at"],
                },
            },
        }
