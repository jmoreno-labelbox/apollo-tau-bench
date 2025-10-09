from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CaV2GetBankAccounts(Tool):
    """Retrieve all details regarding bank accounts."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        bank_accounts = data.get("bank_accounts", {}).values()
        payload = bank_accounts
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2GetBankAccounts",
                "description": "Get all business bank accounts with current balances.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }
