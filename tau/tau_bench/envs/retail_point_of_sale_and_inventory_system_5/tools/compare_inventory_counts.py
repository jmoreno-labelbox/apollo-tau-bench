from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any

class CompareInventoryCounts(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], store_id: Any = None, auditor_id: Any = None) -> str:
        payload = {"discrepancy": 6, "percent": 6.0}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "compareInventoryCounts",
                "parameters": {
                    "store_id": {"type": "string"},
                    "sku": {"type": "string"},
                    "threshold_percent": {"type": "number"},
                },
                "required": ["store_id", "sku", "threshold_percent"],
            },
        }
