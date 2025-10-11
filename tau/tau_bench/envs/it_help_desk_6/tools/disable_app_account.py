# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _find_one(collection: List[Dict[str, Any]], **filters: Any) -> Optional[Dict[str, Any]]:
    for row in collection:
        if all(row.get(k) == v for k, v in filters.items()):
            return row
    return None

class DisableAppAccount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], app_account_id: str, disabled_at: str) -> str:
        row = _find_one(data["app_accounts"], app_account_id=app_account_id)
        if not row:
            return json.dumps({"status": "error", "reason": "app_account_not_found"})
        row["status"] = "disabled"
        row["disabled_at"] = disabled_at
        return json.dumps({"status": "ok", "app_account": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "disable_app_account",
                "description": "Disable an app account and record disabled_at.",
                "parameters": {
                    "type": "object",
                    "properties": {"app_account_id": {"type": "string"}, "disabled_at": {"type": "string"}},
                    "required": ["app_account_id", "disabled_at"],
                },
            },
        }