# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateDirectoryAccountStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str, status: str, disabled_at: Optional[str] = None) -> str:
        acct = _find_one(data["directory_accounts"], account_id=account_id)
        if not acct:
            return json.dumps({"status": "error", "reason": "account_not_found"})
        if status not in {"enabled", "disabled"}:
            return json.dumps({"status": "error", "reason": "invalid_status"})
        acct["status"] = status
        acct["disabled_at"] = disabled_at
        return json.dumps({"status": "ok", "account": acct})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_directory_account_status",
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
