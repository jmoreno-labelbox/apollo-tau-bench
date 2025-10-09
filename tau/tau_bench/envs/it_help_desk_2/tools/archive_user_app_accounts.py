from tau_bench.envs.tool import Tool
import json
from typing import Any

class ArchiveUserAppAccounts(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None) -> str:
        app_accounts = data.get("app_accounts", [])
        archived_count = 0
        for acc in app_accounts:
            if acc.get("employee_id") == employee_id:
                acc["status"] = "archived"
                archived_count += 1
        payload = {"employee_id": employee_id, "app_accounts_archived": archived_count}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "archiveUserAppAccounts",
                "description": "Archives a user's accounts in integrated applications like Slack or GitHub.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}},
                    "required": ["employee_id"],
                },
            },
        }
