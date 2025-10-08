from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any

class LogTransfer(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], from_store: str, to_store: str, sku: str, quantity: int) -> str:
        entry = {
            "from_store": from_store,
            "to_store": to_store,
            "sku": sku,
            "quantity": quantity,
        }
        data.setdefault("transfer_logs", []).append(entry)
        payload = {"message": "Transfer logged.", "entry": entry}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogTransfer",
                "parameters": {
                    "from_store": {"type": "string"},
                    "to_store": {"type": "string"},
                    "sku": {"type": "string"},
                    "quantity": {"type": "number"},
                },
                "required": ["from_store", "to_store", "sku", "quantity"],
            },
        }
