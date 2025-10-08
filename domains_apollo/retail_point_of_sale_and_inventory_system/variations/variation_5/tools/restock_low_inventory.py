from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any

class RestockLowInventory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any],
        store_id: Any = None,
        sku: Any = None,
        quantity: int = None
    ) -> str:
        payload = {"restock_triggered": True}
        out = json.dumps(payload, indent=2)
        return out
        
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RestockLowInventory",
                "parameters": {
                    "store_id": {"type": "string"},
                    "sku": {"type": "string"},
                    "quantity": {"type": "number"},
                },
                "required": ["store_id", "sku", "quantity"],
            },
        }
