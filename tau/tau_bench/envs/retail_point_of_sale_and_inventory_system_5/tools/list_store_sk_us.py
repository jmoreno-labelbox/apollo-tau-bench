# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListStoreSKUs(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        store_id = kwargs.get("store_id")
        inventory = list(data.get("inventory", {}).values())
        result = [item["sku"] for item in inventory if item["store_id"] == store_id]
        return json.dumps(result, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "list_store_skus", "parameters": {"store_id": {"type": "string"}}, "required": ["store_id"]}}
