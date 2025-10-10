# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAppAccounts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str, app_id: Optional[str] = None) -> str:
        results = []
        for a in data["app_accounts"]:
            if a["employee_id"] != employee_id:
                continue
            if app_id and a["app_id"] != app_id:
                continue
            results.append(a)
        return json.dumps({"status": "ok", "app_accounts": results})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_app_accounts",
                "description": "Get app accounts for an employee, optionally filtered by app_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}, "app_id": {"type": "string"}},
                    "required": ["employee_id"],
                },
            },
        }
