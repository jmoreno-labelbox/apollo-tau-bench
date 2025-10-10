# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RestockLowInventory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"restock_triggered": True}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "restock_low_inventory", "parameters": {"store_id": {"type": "string"}, "sku": {"type": "string"}, "quantity": {"type": "number"}}, "required": ["store_id", "sku", "quantity"]}}
