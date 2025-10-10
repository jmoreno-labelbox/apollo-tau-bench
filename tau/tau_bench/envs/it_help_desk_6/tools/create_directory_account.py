# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateDirectoryAccount(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        account_id: str,
        employee_id: str,
        username: str,
        created_at: str,
        status: str = "enabled",
        group_ids: Optional[List[str]] = None,
    ) -> str:
        # Validate employee exists
        if not _find_one(data["employees"], employee_id=employee_id):
            _append_row(
                data["validation_issues"],
                {
                    "issue_id": f"vi_{account_id}",
                    "entity": "directory_accounts",
                    "entity_id": account_id,
                    "field": "employee_id",
                    "rule": "employee_must_exist",
                    "details": employee_id,
                    "created_at": created_at,
                },
            )
            return json.dumps({"status": "error", "reason": "employee_not_found"})

        row = {
            "account_id": account_id,
            "employee_id": employee_id,
            "username": username,
            "status": status,
            "group_ids": group_ids or [],
            "created_at": created_at,
            "disabled_at": None,
        }
        _append_row(data["directory_accounts"], row)
        return json.dumps({"status": "ok", "account": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_directory_account",
                "description": "Create a new directory account for an employee (deterministic IDs/timestamps provided by caller).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string"},
                        "employee_id": {"type": "string"},
                        "username": {"type": "string"},
                        "created_at": {"type": "string"},
                        "status": {"type": "string"},
                        "group_ids": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["account_id", "employee_id", "username", "created_at"],
                },
            },
        }
