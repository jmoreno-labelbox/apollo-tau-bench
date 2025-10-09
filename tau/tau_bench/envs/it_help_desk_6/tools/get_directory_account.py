from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetDirectoryAccount(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        employee_id: str | None = None,
        account_id: str | None = None,
    ) -> str:
        pass
        acct = None
        if account_id:
            acct = _find_one(data["directory_accounts"], account_id=account_id)
        elif employee_id:
            acct = _find_one(data["directory_accounts"], employee_id=employee_id)
        payload = {"status": "ok", "account": acct}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDirectoryAccount",
                "description": "Get a directory account by employee_id or account_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "account_id": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
