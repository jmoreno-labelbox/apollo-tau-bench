from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetPolicyExceptionByUserId(Tool):
    """Identifies all policy exceptions for a specific user, with the option to include inactive exceptions."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, include_inactive: bool = False) -> str:
        terminal_statuses = {"REVOKED", "REJECTED", "EXPIRED"}
        try:
            policy_exceptions = data.get("policy_exceptions", [])
        except:
            policy_exceptions = []

        user_exceptions = []
        for exc in policy_exceptions:
            if exc.get("user_id") == user_id:
                if include_inactive:
                    user_exceptions.append(exc)
                elif exc.get("status") not in terminal_statuses:
                    user_exceptions.append(exc)
        payload = user_exceptions
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPolicyExceptionByUserId",
                "description": "Retrieves a list of policy exceptions for a given user ID. By default, it only returns active exceptions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user to find exceptions for.",
                        },
                        "include_inactive": {
                            "type": "boolean",
                            "description": "Set to true to include expired, revoked, or rejected exceptions. Defaults to false.",
                        },
                    },
                    "required": ["user_id"],
                },
            },
        }
