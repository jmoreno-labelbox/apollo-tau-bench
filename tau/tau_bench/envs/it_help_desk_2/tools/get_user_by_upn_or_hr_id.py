# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserByUpnOrHrId(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_lookup) -> str:
        accounts = data.get("directory_accounts", [])
        for acc in accounts:
            if acc.get("hr_id") == user_lookup or acc.get("upn") == user_lookup or acc.get("employee_id") == user_lookup:
                return json.dumps(acc, indent=2)
        return json.dumps({"user_lookup": user_lookup, "account": None}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_user_by_upn_or_hr_id", "description": "Retrieve a user's directory account using their UPN, HR ID, or Employee ID.", "parameters": {"type": "object", "properties": {"user_lookup": {"type": "string"}}, "required": ["user_lookup"]}}}
