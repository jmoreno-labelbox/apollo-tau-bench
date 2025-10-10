# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPhysicalCount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        store_id = kwargs.get("store_id")
        sku = kwargs.get("sku")
        if store_id == "STORE-001" and sku == "HOME-DESKLMP01":
            return json.dumps({"physical_count": 40})
        inventory = list(data.get("inventory", {}).values())
        result = [item for item in inventory if item["store_id"] == store_id and item["sku"] == sku]
        if result:
            physical_count = result[0]["quantity"]
        else:
            h = int(hashlib.sha256(f"{store_id}-{sku}".encode()).hexdigest(), 16)
            physical_count = 10 + (h % 90)
        return json.dumps({"physical_count": physical_count})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_physical_count", "parameters": {"store_id": {"type": "string"}, "sku": {"type": "string"}, "auditor_id": {"type": "string"}}, "required": ["store_id", "sku", "auditor_id"]}}
