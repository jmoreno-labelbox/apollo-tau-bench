# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CheckSafetyStock(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"safety_stock_ok": True}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "check_safety_stock", "parameters": {"store_id": {"type": "string"}, "sku": {"type": "string"}, "min_percent": {"type": "number"}}, "required": ["store_id", "sku", "min_percent"]}}
