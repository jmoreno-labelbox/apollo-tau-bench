from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SetDirectoryAccountStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], account_id: str = None, status: str = None, department: Any = None) -> str:
        accounts = data.get("directory_accounts", [])
        account = next((a for a in accounts if a.get("account_id") == account_id), None)
        if not account:
            payload = {"error": f"Account {account_id} not found."}
            out = json.dumps(payload, indent=2)
            return out
        if status not in ["enabled", "disabled", "inactive"]:
            payload = {"error": "Status must be 'enabled', 'disabled', or 'inactive'."}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        account["status"] = status
        account["disabled_at"] = (
            FIXED_NOW if status in ["disabled", "inactive"] else None
        )
        payload = account
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetDirectoryAccountStatus",
                "description": "Enable or disable a user's directory account.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["account_id", "status"],
                },
            },
        }
