from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateDirectoryAccount(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        account_id: str,
        employee_id: str,
        username: str,
        created_at: str,
        status: str = "enabled",
        group_ids: list[str] | None = None,
        department: Any = None,
        job_title: Any = None,
    ) -> str:
        pass
        #Check if the employee is present
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
            payload = {"status": "error", "reason": "employee_not_found"}
            out = json.dumps(payload)
            return out

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
        payload = {"status": "ok", "account": row}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createDirectoryAccount",
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
