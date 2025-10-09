from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any

class ApplyBulkDiscount(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], store_id: str = None, sku: str = None, discount_percent: int = None, min_quantity: int = None) -> str:
        payload = {"bulk_discount_applied": True}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {"name": "ApplyBulkDiscount", "parameters": {}, "required": []},
        }
