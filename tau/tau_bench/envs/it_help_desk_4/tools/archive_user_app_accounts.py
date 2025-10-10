# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ArchiveUserAppAccounts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id) -> str:
        app_accounts = list(data.get("app_accounts", {}).values())
        archived_count = 0
        for acc in app_accounts:
            if acc.get("employee_id") == employee_id:
                acc["status"] = "archived"
                archived_count += 1
        return json.dumps({"employee_id": employee_id, "app_accounts_archived": archived_count}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "archive_user_app_accounts", "description": "Archives a user's accounts in integrated applications like Slack or GitHub.", "parameters": {"type": "object", "properties": {"employee_id": {"type": "string"}}, "required": ["employee_id"]}}}
