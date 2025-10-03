from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpsertAppAccount(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        app_account_id: str,
        employee_id: str,
        app_id: str,
        status: str,
        created_at: str,
    ) -> str:
        row = _find_one(data["app_accounts"], app_account_id=app_account_id)
        if row:
            _update_row(row, {"status": status})
        else:
            row = {
                "app_account_id": app_account_id,
                "employee_id": employee_id,
                "app_id": app_id,
                "status": status,
                "created_at": created_at,
            }
            _append_row(data["app_accounts"], row)
        payload = {"status": "ok", "app_account": row}
        out = json.dumps(payload)
        return out
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsertAppAccount",
                "description": "Create or update an app account for an employee.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "app_account_id": {"type": "string"},
                        "employee_id": {"type": "string"},
                        "app_id": {"type": "string"},
                        "status": {"type": "string"},
                        "created_at": {"type": "string"},
                    },
                    "required": [
                        "app_account_id",
                        "employee_id",
                        "app_id",
                        "status",
                        "created_at",
                    ],
                },
            },
        }
