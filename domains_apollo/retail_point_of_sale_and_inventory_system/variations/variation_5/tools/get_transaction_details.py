from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any

class GetTransactionDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], transaction_id: str = None) -> str:
        transactions = data.get("transactions", [])
        result = [
            item for item in transactions if item["transaction_id"] == transaction_id
        ]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTransactionDetails",
                "parameters": {"transaction_id": {"type": "string"}},
                "required": ["transaction_id"],
            },
        }
