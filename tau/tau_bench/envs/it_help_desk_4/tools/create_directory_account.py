# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateDirectoryAccount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], hr_id, legal_name) -> str:
        accounts = list(data.get("directory_accounts", {}).values())
        username = legal_name.lower().replace(" ", ".")
        upn = f"{username}@company.com"
        name_part = "".join(filter(str.isalnum, legal_name.split()[0])).lower()
        last_initial = legal_name.split()[-1][0].lower()
        hr_num = hr_id.split('-')[-1]
        account_id = f"acc_{name_part}{last_initial}{hr_num}"
        new_account = {"account_id": account_id, "employee_id": f"emp_{hr_num}", "hr_id": hr_id, "username": username, "upn": upn, "status": "enabled", "created_at": FIXED_NOW, "disabled_at": None}
        accounts.append(new_account)
        return json.dumps(new_account, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_directory_account", "description": "Create a new user account in the directory.", "parameters": {"type": "object", "properties": {"legal_name": {"type": "string"}, "hr_id": {"type": "string"}, "department": {"type": "string"}, "job_title": {"type": "string"}}, "required": ["legal_name", "hr_id", "department", "job_title"]}}}
