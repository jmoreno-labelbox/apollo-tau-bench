from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetUserByUpnOrHrId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_lookup: str = None) -> str:
        accounts = data.get("directory_accounts", {}).values()
        for acc in accounts.values():
            if (
                acc.get("hr_id") == user_lookup
                or acc.get("upn") == user_lookup
                or acc.get("employee_id") == user_lookup
            ):
                payload = acc
                out = json.dumps(payload, indent=2)
                return out
        payload = {"user_lookup": user_lookup, "account": None}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserByUpnOrHrId",
                "description": "Retrieve a user's directory account using their UPN, HR ID, or Employee ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_lookup": {"type": "string"}},
                    "required": ["user_lookup"],
                },
            },
        }
