from tau_bench.envs.tool import Tool
import json
from typing import Any

class ListStores(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], stores: list = None) -> str:
        stores = _get_table(data, "stores")
        payload = {"stores": stores}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listStores",
                "description": "Returns all stores.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }
