# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool








def _update_row(row: Dict[str, Any], updates: Dict[str, Any]) -> None:
    for k, v in updates.items():
        row[k] = v

def _find_one(collection: List[Dict[str, Any]], ) -> Optional[Dict[str, Any]]:
    for row in collection:
        if all(row.get(k) == v for k, v in filters.items()):
            return row
    return None

def _append_row(table: List[Dict[str, Any]], row: Dict[str, Any]) -> None:
    table.append(row)

class UpsertAppAccount(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], app_account_id: str, employee_id: str, app_id: str, status: str, created_at: str
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
        return json.dumps({"status": "ok", "app_account": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsert_app_account",
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
                    "required": ["app_account_id", "employee_id", "app_id", "status", "created_at"],
                },
            },
        }