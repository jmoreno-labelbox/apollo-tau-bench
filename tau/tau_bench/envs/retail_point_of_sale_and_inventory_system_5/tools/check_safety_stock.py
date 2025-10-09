from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any

class CheckSafetyStock(Tool):
    @staticmethod
    def invoke(data: dict[str, Any],
        store_id: Any = None,
        sku: Any = None,
        min_percent: int = None
    ) -> str:
        payload = {"safety_stock_ok": True}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckSafetyStock",
                "parameters": {
                    "store_id": {"type": "string"},
                    "sku": {"type": "string"},
                    "min_percent": {"type": "number"},
                },
                "required": ["store_id", "sku", "min_percent"],
            },
        }
