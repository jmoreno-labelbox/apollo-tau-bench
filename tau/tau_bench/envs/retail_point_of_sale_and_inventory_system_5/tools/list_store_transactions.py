from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ListStoreTransactions(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], store_id: str = None) -> str:
        transactions = data.get("transactions", {}).values()
        result = [item for item in transactions.values() if item["store_id"] == store_id]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListStoreTransactions",
                "parameters": {"store_id": {"type": "string"}},
                "required": ["store_id"],
            },
        }
