from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any

class ListStoreTransactions(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], store_id: str = None) -> str:
        transactions = data.get("transactions", [])
        result = [item for item in transactions if item["store_id"] == store_id]
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
