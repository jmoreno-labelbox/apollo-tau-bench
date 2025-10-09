from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class AssignAppAccount(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, app_id: str = None) -> str:
        if employee_id is None or app_id is None:
            payload = {
                    "status": "error",
                    "description": "The employee_id and app_id fields are required.",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        accounts = data.get("app_accounts")

        new_account = {
            "app_account_id": "appacc_000000",
            "employee_id": employee_id,
            "app_id": app_id,
            "status": "active",
            "created_at": FIXED_NOW,
        }

        accounts.append(new_account)
        payload = {
                "status": "ok",
                "description": f"Added {app_id} account for {employee_id}",
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assignAppAccount",
                "description": "Assigns an app to a user by appending to the app_accounts database.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The id of the employee to assign licenses to.",
                        },
                        "app_id": {
                            "type": "string",
                            "description": "The id of the app to assign.",
                        },
                    },
                    "required": ["employee_id", "app_id"],
                },
            },
        }
