from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetAccount(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], account_id: str) -> str:
        account_id = _sid(account_id)
        accs = data.get("accounts", [])
        a = next((x for x in accs if x.get("account_id") == account_id), None)
        payload = a or {"error": f"account {account_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAccount",
                "description": "Retrieve account by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"account_id": {"type": "string"}},
                    "required": ["account_id"],
                },
            },
        }
