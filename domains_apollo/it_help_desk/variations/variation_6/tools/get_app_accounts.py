from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetAppAccounts(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], employee_id: str, app_id: str | None = None
    ) -> str:
        pass
        results = []
        for a in data["app_accounts"]:
            if a["employee_id"] != employee_id:
                continue
            if app_id and a["app_id"] != app_id:
                continue
            results.append(a)
        payload = {"status": "ok", "app_accounts": results}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAppAccounts",
                "description": "Get app accounts for an employee, optionally filtered by app_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "app_id": {"type": "string"},
                    },
                    "required": ["employee_id"],
                },
            },
        }
