# Copyright by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetDirectoryAccount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: Optional[str] = None, account_id: Optional[str] = None) -> str:
        acct = None
        if account_id:
            acct = _find_one(data["directory_accounts"], account_id=account_id)
        elif employee_id:
            acct = _find_one(data["directory_accounts"], employee_id=employee_id)
        return json.dumps({"status": "ok", "account": acct})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_directory_account",
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
