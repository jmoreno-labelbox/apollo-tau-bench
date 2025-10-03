from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any

class TriggerRecountIfNeeded(Tool):
    @staticmethod
    def invoke(data: dict[str, Any],
        store_id: Any = None,
        sku: Any = None,
        discrepancy_threshold: float = None
    ) -> str:
        payload = {"recount_triggered": True}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "TriggerRecountIfNeeded",
                "parameters": {
                    "store_id": {"type": "string"},
                    "sku": {"type": "string"},
                    "discrepancy_threshold": {"type": "number"},
                },
                "required": ["store_id", "sku", "discrepancy_threshold"],
            },
        }
