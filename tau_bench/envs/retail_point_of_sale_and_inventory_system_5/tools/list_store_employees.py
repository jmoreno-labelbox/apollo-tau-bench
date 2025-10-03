from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any

class ListStoreEmployees(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], store_id: str = None) -> str:
        employees = data.get("employees", [])
        result = [item for item in employees if item["store_id"] == store_id]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListStoreEmployees",
                "parameters": {"store_id": {"type": "string"}},
                "required": ["store_id"],
            },
        }
