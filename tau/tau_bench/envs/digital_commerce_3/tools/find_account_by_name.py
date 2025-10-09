from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FindAccountByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], account_name: Any) -> str:
        match = next(
            (
                a
                for a in data.get("accounts", {}).values()
                if a.get("account_name") == account_name
            ),
            {},
        )
        payload = match
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "findAccountByName",
                "description": "Returns account record by exact name.",
                "parameters": {
                    "type": "object",
                    "properties": {"account_name": {"type": "string"}},
                    "required": ["account_name"],
                },
            },
        }
