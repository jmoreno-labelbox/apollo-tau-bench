from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateDirectoryAccount(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, status: str = None) -> str:
        if employee_id is None:
            payload = {
                    "status": "error",
                    "description": "The employee_id field is required.",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        if all([param is None for param in [status]]):
            payload = {
                    "status": "error",
                    "description": "At least one parameter to be changed is required.",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        directory_accounts = data.get("directory_accounts")

        for account in directory_accounts:
            if account["employee_id"] == employee_id:
                if status is not None:
                    account["status"] = status
                    if status == "disabled":
                        account["disabled_at"] = FIXED_NOW
        payload = {
                "status": "ok",
                "description": f"Successfully updated account for {employee_id}.",
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateDirectoryAccount",
                "description": "Allows updates for directory accounts, including disabling accounts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The id of the employee to update.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The status to set.",
                        },
                    },
                    "required": ["employee_id"],
                },
            },
        }
