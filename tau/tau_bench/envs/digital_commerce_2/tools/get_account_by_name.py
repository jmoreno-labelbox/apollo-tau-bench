from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetAccountByName(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], name: Any) -> str:
        account_name = name
        if not account_name:
            payload = {"error": "Missing required field: name"}
            out = json.dumps(payload, indent=2)
            return out
        accounts = data.get("accounts", [])
        for account in accounts:
            if account.get("account_name") == account_name:
                payload = account
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No account found with name '{account_name}'"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAccountByName",
                "description": "Fetch a single account's full details by its account_name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Exact account name to retrieve.",
                        }
                    },
                    "required": ["name"],
                },
            },
        }
